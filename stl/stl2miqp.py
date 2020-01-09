'''
 Copyright (C) 2018-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''

import gurobipy as grb

from stl import Operation, RelOperation
from stl2milp import stl2milp


class stl2miqp(stl2milp):
    '''Translate an STL formula to an MIQP.'''

    def predicate(self, pred, z, t):
        '''Adds a predicate to the model.'''
        assert pred.op == Operation.PRED
        variables = pred.expression.variables()
        variables = {var: self.add_state(var, t) for var in variables}
        expr = pred.expression.eval(variables)
        if pred.relation in (RelOperation.GE, RelOperation.GT):
            self.model.addConstr(expr - self.M * z <= pred.threshold + self.rho)
            self.model.addConstr(expr + self.M * (1 - z) >= pred.threshold + self.rho)
            # TODO: are the next two lines necessary?
            self.model.addConstr(v - self.M * z <= pred.threshold)
            self.model.addConstr(v + self.M * (1 - z) >= pred.threshold)
        elif pred.relation in (RelOperation.LE, RelOperation.LT):
            self.model.addConstr(expr + self.M * z >= pred.threshold - self.rho)
            self.model.addConstr(expr - self.M * (1 - z) <= pred.threshold - self.rho)
        else:
            raise NotImplementedError
