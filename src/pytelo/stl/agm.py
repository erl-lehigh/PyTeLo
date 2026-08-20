'''
 Copyright (c) 2019, Noushin Mehdipour <noushinm@bu.edu>,
 Copyright (c) 2015-2019 Cristian Ioan Vasile <cvasile@bu.edu,cvasile@lehigh.edu>,
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University

 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
 See license.txt file for license information.
'''
from __future__ import print_function

import numpy as np
from antlr4 import InputStream, CommonTokenStream

from pytelo._internal.stlLexer import stlLexer
from pytelo._internal.stlParser import stlParser

from .stl import Operation, RelOperation, STLAbstractSyntaxTreeExtractor, Trace


def powermean(vector, order, plus=0):
    '''Computes the power mean (generalized Holder mean) of a vector. 
    
    Parameters:
    ----------
    vector (array-like): Input vector whose mean is to be computed.
    order (float or str): The order of the power mean. Can be any real number or 'inf'/'-inf' 
                          for max/min.
    plus (int): default=0 - If truthy, the function computes a +1 shifted power mean.

    Returns:
    ----------
    mean (np.float64): The power mean of the input vector.
    '''
    alpha = 1. / len(vector)
    if order == 'inf':
        return np.max(vector)
    elif order == '-inf':
        return np.min(vector)
    if order != 0:
        if plus:
            return np.sum(alpha * (1+abs(vector))**order)**(1./order) - 1
        else:
            return np.sum(alpha * abs(vector)**order)**(1./order)
    else:
        if plus:
            return np.prod(1 + abs(vector)) ** alpha - 1
        else:
            return np.prod(abs(vector)) ** alpha

def conjunction_function(r_children, pos_order, neg_order, plus=0):
    '''Computes the conjuction robustness value from children values.
    
    Parameters:
    ----------
    r_children (array-like): Robustness values of the child nodes.
    pos_order (float or str): The order of the power mean for positive values.
    neg_order (float or str): The order of the power mean for negative values.
    plus (int): default=0 - If truthy, the function computes a +1 shifted power mean.

    Returns:
    ----------
    eta (np.float64): The conjuction robustness value.
    '''
    r_non_pos = r_children <= 0
    if np.any(r_non_pos):
        eta = -powermean(-r_children * r_non_pos, order=neg_order, plus=plus)
    else:
        eta = powermean(r_children, order=pos_order, plus=plus)
    return eta

def disjunction_function(r_children, pos_order, neg_order, plus=0):
    '''Computes the disjuction robustness value from children values. This is identical
    to -conjunction_function(-r_children, pos_order, neg_order, plus)

    Parameters:
    ----------
    r_children (array-like): Robustness values of the child nodes.
    pos_order (float or str): The order of the power mean for positive values.
    neg_order (float or str): The order of the power mean for negative values.
    plus (int): default=0 - If truthy, the function computes a +1 shifted power mean.

    Returns:
    ----------
    eta (np.float64): The disjuction robustness value.
    '''
    r_pos = r_children > 0
    if np.any(r_pos):
        eta = powermean(r_children * r_pos, order=neg_order, plus=plus)
    else:
        eta = -powermean(-r_children, order=pos_order, plus=plus)
    return eta

def powermean_robustness(formula, trace, time, pos_order=0, neg_order=1,
                         maximum_robustness=1, plus=0):
    '''Computes the powermean robustness of a formula with respect to a trace at a given time.
    Recursively constructs robustness values over the formula tree as needed.

    Parameters:
    ----------
    formula (STLFormula): The STL formula with respect to which robustness is to be computed.
    trace (BoundedTrace): The signal trace whose robustness is to be evaluated.
    time (int): The time point at which robustness is to be evaluated.
    pos_order (int or float or str): default=0 - The order of the power mean for positive values.
                                                 Use 'inf'/'-inf' for max/min.
    neg_order (int or float or str): default=1 - The order of the power mean for negative values.
                                                 Use 'inf'/'-inf' for max/min.
    maximum_robustness (float): default=1 - The defined robustness of a boolean predicate. A True
                                            value in the trace returns maximum_robustness, False 
                                            returns -maximum_robustness.
    plus (int): default=0 - If truthy, the function computes a +1 shifted power mean.

    Returns:
    ----------
    eta (np.float64): The powermean robustness value.
    '''
    if formula.op == Operation.BOOL:
        if formula.value:
            return maximum_robustness
        else:
            return -maximum_robustness
    elif formula.op == Operation.PRED:
        value = trace.value(formula.variable, time)
        if formula.relation in (RelOperation.GE, RelOperation.GT):
            eta = value - formula.threshold
        elif formula.relation in (RelOperation.LE, RelOperation.LT):
            eta = formula.threshold - value
        elif formula.relation == RelOperation.EQ:
            eta = -abs(value - formula.threshold)
        elif formula.relation == RelOperation.NQ:
            eta = abs(value - formula.threshold)
        return eta / trace.range(formula.variable) # normalization

    if formula.op in (Operation.AND, Operation.OR):
        r_children = np.array([powermean_robustness(child, trace, time, pos_order, neg_order, maximum_robustness, plus)
                               for child in formula.children],
                              dtype=np.float64)
    elif formula.op in (Operation.ALWAYS, Operation.EVENT):
        r_children = np.array(
            [powermean_robustness(formula.child, trace, time + tau, pos_order, neg_order, maximum_robustness, plus)
             for tau in np.arange(formula.low, formula.high + 1)],
            dtype=np.float64)
    if formula.op in (Operation.AND, Operation.ALWAYS):
        eta = conjunction_function(r_children, pos_order, neg_order, plus=plus)
        return eta
    elif formula.op in (Operation.OR, Operation.EVENT):
        eta = disjunction_function(r_children, pos_order, neg_order, plus=plus)
        return eta

    if formula.op == Operation.NOT:
        return -powermean_robustness(formula.child, trace, time, pos_order, neg_order, maximum_robustness, plus=plus)
    elif formula.op in (Operation.IMPLIES, Operation.UNTIL):
        raise NotImplementedError
    else:
        raise ValueError('Unknown operation code {}!'.format(formula.op))


class BoundedTrace(Trace):
    '''Representation of a bounded system trace.
    
    Inherits from Trace and adds bounds for each variable to allow for normalization of robustness values.
    
    Instance Attributes:
    ----------
    bounds (dict): A dictionary mapping variable names to their respective (min, max) bounds.
    '''

    def __init__(self, variables, time_points, data, bounds, kind='nearest'):
        '''Construct a signal trace with bounds for each variable.'''
        Trace.__init__(self, variables, time_points, data, kind)
        self.bounds = bounds

    def range(self, variable):
        '''Return the size of the range of a specified variable.
        
        Parameters:
        ----------
        variable (str): The name of the variable for which to return the range.
        
        Returns:
        --------
        bound_len (float): The size of the range of the specified variable.
        '''
        var_bounds = self.bounds[variable]
        return var_bounds[1] - var_bounds[0]


if __name__ == '__main__':
    lexer = stlLexer(InputStream('!(x < 10) && F[0, 2] y > 2 || G[1, 3] z<=8'
                                 ' && G[4, 6] z>8'))
    #lexer = stlLexer(InputStream("G[4, 6] z>8"))
    tokens = CommonTokenStream(lexer)

    parser = stlParser(tokens)
    parse_tree = parser.stlProperty()
    print(parse_tree.toStringTree())

    ast = STLAbstractSyntaxTreeExtractor().visit(parse_tree)
    print('AST:', ast)

    var_names = ['x', 'y', 'z']
    var_values = [[8, 8, 11, 11, 11, 1, 1],
                  [1, 3, 2, 2, 2, 0, 0],
                  [3, 9, 8, 9, 9, 9, 9]]
    time_points = [0, 1, 2, 3, 4, 5, 6]
    data_bounds = {'x': (0, 20), 'y': (0, 10), 'z': (0, 10)}
    s = BoundedTrace(var_names, time_points, var_values, data_bounds)

    print('r:', powermean_robustness(ast, s, 0, plus=1))

    pnf = ast.pnf()
    print(pnf)
