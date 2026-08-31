import numpy as np
try:
    from scipy.interpolate import make_interp_spline
except ImportError:
    warnings.warn("Scipy is not available in the current environment. " +
    "This is needed for spline interpolation of signal trace values. " +
    "If you do not wish to install scipy, note that Trace and TraceBatch " +
    "objects will be limited to order 0 and 1 interpolation capabilities.", ImportWarning)

class Trace(object):
    '''Representation of a single signal trace. This consists of a set of time points and corresponding
    signal values for all relevant variables.
    
    Instance Attributes
    ----------
    data (dict): mapping from variable names to callables that return the value at any time point.
    '''

    def __init__(self, variables, timePoints, data, kind='nearest'):
        '''Constructs callables for each variable in the trace to get values as a function of time.
        Requires scipy for spline interpolation modes
        
        Parameters:
        ----------
        variables (iterable of strings): names of the variables in the trace
        timePoints (iterable of number-like): time points at which the signal values are defined (only one set of
                                              time points is allowed for all variables collectively).
        data (iterable of iterables of number-like): signal values for each variable at each time point 
                                                     (must be in the same order as variables iter)
        kind (string): default='nearest' - type of interpolation to use for the callables. Accepts the following
                       values based on legacy call to scipy.interpolate.interp1d: 'linear', 'nearest', 'nearest-up',
                       'zero', 'slinear', 'quadratic', 'cubic', 'previous', 'next', or any integer for the order of 
                       spline interpolation. 
        '''
        def interp_func(times, values):
            if kind == 'linear':
                def interp(t):
                    self._clean(t, times)
                    return np.interp(t, times, values)
            elif kind == 'nearest':
                def interp(t):
                    self._clean(t, times)
                    idx = np.asarray(np.searchsorted(times, t, side='left'))
                    idx[idx == 0] = 1
                    prevs = times[idx - 1] - t <= t - times[idx]
                    return np.where(prevs, values[idx - 1], values[idx])
            elif kind == 'nearest-up':
                def interp(t):
                    self._clean(t, times)
                    idx = np.asarray(np.searchsorted(times, t, side='right'))
                    idx[idx == len(times)] = len(times) - 1
                    prevs = times[idx - 1] - t < t - times[idx]
                    return np.where(prevs, values[idx - 1], values[idx])
            elif kind == 'previous':
                def interp(t):
                    self._clean(t, times)
                    idx = np.asarray(np.searchsorted(times, t, side='left'))
                    idx[idx == 0] = 1
                    return values[idx - 1]
            elif kind == 'next':
                def interp(t):
                    self._clean(t, times)
                    idx = np.asarray(np.searchsorted(times, t, side='right'))
                    idx[idx == len(times)] = len(times) - 1
                    return values[idx]
            elif (isinstance(kind, int) and kind >= 0) or kind in ('zero', 'slinear', 'quadratic', 'cubic'):
                order = {'zero': 0, 'slinear': 1, 'quadratic': 2, 'cubic': 3}.get(kind, kind)
                b_spline = make_interp_spline(times, values, k=order)
                def interp(t):
                    self._clean(t, times)
                    return b_spline(t)
            else:
                raise ValueError(f'Invalid interpolation kind: {kind}')
            return interp
        self.data = {variable : interp_func(timePoints, var_data)
                            for variable, var_data in zip(variables, data)}

    def _clean(self, t, times):
        if np.any(t < times[0]) or np.any(t > times[-1]):
            raise ValueError(f'Cannot interpolate outside of time range [{times[0]}, {times[-1]}]')
        t = np.asarray(t)
        return t
    
    def value(self, variable, t):
        '''Returns value of the given signal component at time t.
        
        Parameters:
        ----------
        variable (str): identifier of the variable to fetch.
        t (number-like or array-like): time (or array of times) to check the variable value.
        
        Returns:
        ----------
        data (number-like or array-like): value (or array of values) of the signal at the indicated time(s).
        '''
        return self.data[variable](t)

    def values(self, variable, timepoints):
        '''Same as Trace.value, but converts timepoints into an ndarray for extra flexibility.
        
        Parameters:
        ----------
        variable (str): identifier of the variable to fetch.
        timepoints (number-like or array-like): time (or array of times) to check the variable value.
        
        Returns:
        ----------
        data (number-like or array-like): value (or array of values) of the signal at the indicated time(s).
        '''
        return self.data[variable](np.asarray(timepoints))

    def number_signals(self):
        return 1

    def __str__(self):
        raise NotImplementedError


class TraceBatch(object):
    '''Representation of a batch of signal traces. This consists of a set of time points and corresponding
    signal values for all relevant variables across all batches.
    
    Instance Attributes
    ----------
    data (dict): mapping from variable names to callables that return the values at any time point for all
                 traces in an array-like object.
    no_signals (int): the number of traces in the batch.
    '''

    def __init__(self, variables, timePoints, data, kind='nearest'):
        '''Constructs callables for each variable in the trace to get values as a function of time.
        Requires scipy for spline interpolation modes
        
        Parameters:
        ----------
        variables (iterable of strings): names of the variables in the trace
        timePoints (iterable of number-like): time points at which the signal values are defined (only one set of
                                              time points is allowed for all variables collectively).
        data (array-like: num_traces X num_vars X t): signal values for each variable at each time point 
                                                      (must be in the same order as variables iter)
        kind (string): default='nearest' - type of interpolation to use for the callables. Accepts the following
                       values based on legacy call to scipy.interpolate.interp1d: 'linear', 'nearest', 'nearest-up',
                       'zero', 'slinear', 'quadratic', 'cubic', 'previous', 'next', or any integer for the order of 
                       spline interpolation. 
        '''
        def interp_func(times, values):
            if kind == 'linear':
                def interp(t):
                    self._clean(t, times)
                    idx = np.asarray(np.searchsorted(times, t, side='left'))
                    idx[idx == 0] = 1
                    times_low, times_high = times[idx - 1], times[idx]
                    vals_low, vals_high = values[:, idx -1], values[:, idx]
                    weights = (t - times_low) / (times_high - times_low)
                    return vals_low + weights * (vals_high - vals_low)
            elif kind == 'nearest':
                def interp(t):
                    self._clean(t, times)
                    idx = np.asarray(np.searchsorted(times, t, side='left'))
                    idx[idx == 0] = 1
                    prevs = times[idx - 1] - t <= t - times[idx]
                    return np.where(prevs, values[:, idx - 1], values[:, idx])
            elif kind == 'nearest-up':
                def interp(t):
                    self._clean(t, times)
                    idx = np.asarray(np.searchsorted(times, t, side='right'))
                    idx[idx == len(times)] = len(times) - 1
                    prevs = times[idx - 1] - t < t - times[idx]
                    return np.where(prevs, values[:, idx - 1], values[:, idx])
            elif kind == 'previous':
                def interp(t):
                    self._clean(t, times)
                    idx = np.asarray(np.searchsorted(times, t, side='left'))
                    idx[idx == 0] = 1
                    return values[:, idx - 1]
            elif kind == 'next':
                def interp(t):
                    self._clean(t, times)
                    idx = np.asarray(np.searchsorted(times, t, side='right'))
                    idx[idx == len(times)] = len(times) - 1
                    return values[:, idx]
            elif (isinstance(kind, int) and kind >= 0) or kind in ('zero', 'slinear', 'quadratic', 'cubic'):
                order = {'zero': 0, 'slinear': 1, 'quadratic': 2, 'cubic': 3}.get(kind, kind)
                b_splines = [make_interp_spline(times, trace, k=order) for trace in values]
                def interp(t):
                    self._clean(t, times)
                    return np.asarray([b_spline(t) for b_spline in b_splines])
            else:
                raise ValueError(f'Invalid interpolation kind: {kind}')
            return interp
        self.no_signals = len(data)
        var_dataset = np.swapaxes(np.asarray(data), 0, 1)
        self.data = {variable : interp_func(timePoints, var_data)
                            for variable, var_data in zip(variables, var_dataset)}

    def _clean(self, t, times):
        if np.any(t < times[0]) or np.any(t > times[-1]):
            raise ValueError(f'Cannot interpolate outside of time range [{times[0]}, {times[-1]}]')
        t = np.asarray(t)
        return t
        
    def value(self, variable, t):
        '''Returns values of the given signal component at time t across all traces.
        
        Parameters:
        ----------
        variable (str): identifier of the variable to fetch.
        t (number-like or array-like): time (or array of times) to check the variable values.
        
        Returns:
        ----------
        data (array-like): array of values of the indicated signal across all traces at the
                           indicated time(s).
        '''
        return self.data[variable](t)

    def values(self, variable, timepoints):
        '''Same as Trace.value, but converts timepoints into an ndarray for extra flexibility.
        
        Parameters:
        ----------
        variable (str): identifier of the variable to fetch.
        timepoints (number-like or array-like): time (or array of times) to check the variable
                                                values.
        
        Returns:
        ----------
        data (array-like): array of values of the indicated signals across all traces at the 
                           indicated time(s).
        '''
        return self.data[variable](np.asarray(timepoints))

    def number_signals(self):
        return self.no_signals

    def __str__(self):
        raise NotImplementedError