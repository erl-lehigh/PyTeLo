'''
 Copyright (C) 2022 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''

import gurobipy as grb

from stl import Operation, RelOperation, STLFormula
from stl2milp import stl2milp


class stl_dist_milp(stl2milp):
    '''Translate an STL formula to an MILP for distance computation.'''

    def __init__(self, formula, ranges, vtypes=None, model=None, robust=False,
                 prefix='', variables=None):
        stl2milp.__init__(self, formula, ranges, vtypes, model, robust)
        self.prefix = prefix

        if variables is not None:
            for var in ranges:
                if var in variables:
                    self.variables[var] = variables[var]

    def translate(self, satisfaction=1):
        '''Translates the STL formula to MILP from time 0.'''
        z = self.to_milp(self.formula)
        if satisfaction is not None:
            self.model.addConstr(z == satisfaction,
                                 self.prefix + 'formula_satisfaction')
        return z

    def add_formula_variable(self, formula, t, vtype=grb.GRB.BINARY):
        '''Adds a variable for the `formula` at time `t`.'''
        if formula not in self.variables:
            self.variables[formula] = dict()
        if t not in self.variables[formula]:
            opname = Operation.getName(formula.op)
            identifier = formula.identifier()
            name = '{}{}_{}_{}'.format(self.prefix, opname, identifier, t)
            self.variables[formula][t] = self.model.addVar(vtype=vtype,
                                                           name=name)
            self.model.update() #TODO: not sure if this is needed (NEEDED!)
            return self.variables[formula][t], True
        return self.variables[formula][t], False

    def predicate(self, pred, z, t):
        '''Adds a predicate to the model.'''
        assert pred.op == Operation.PRED
        v = self.add_state(pred.variable, t)
        if pred.relation in (RelOperation.GE, RelOperation.GT):
            self.model.addConstr(v - self.M * z <= pred.threshold - self.rho)
            self.model.addConstr(v + self.M * (1 - z) >= pred.threshold - self.rho)
        elif pred.relation in (RelOperation.LE, RelOperation.LT):
            self.model.addConstr(v + self.M * z >= pred.threshold + self.rho)
            self.model.addConstr(v - self.M * (1 - z) <= pred.threshold + self.rho)
        else:
            raise NotImplementedError


def stl_directed_distance(ast1, ast2, ranges):
    '''Computes the directed Pompeiu-Hausdorff distance between the languages
    of STL formula ast1 and the STL formula ast2.
    '''
    stl_milp1 = stl_dist_milp(ast1, ranges=ranges, robust=False)
    stl_milp1.translate(satisfaction=1)
    model = stl_milp1.model

    stl_milp2 = stl_dist_milp(ast2, ranges=ranges, robust=True,
                              prefix='ext_', model=model,
                              variables=stl_milp1.variables)
    z = stl_milp2.translate(satisfaction=0)
    model.addConstr(z == 0, 'formula2_violation')

    model.optimize()

    if model.status == grb.GRB.OPTIMAL:
        print('Vars')
        for var in model.getVars():
            print(var.VarName, ':', var.x)

        print('Constraints')
        for constr in model.getConstrs():
            print(':', str(constr))

        print('Objective')
        obj = model.getObjective()
        print(str(obj), ':', obj.getValue())

        return -obj.getValue()
    else:
        return 0


def stl_distance(ast1, ast2, ranges, return_directed=False):
    '''Computes the Pompeiu-Hausdorff distance between the languages of STL
    formulae ast1 and ast2.
    '''
    d1 = stl_directed_distance(ast1, ast2, ranges)
    d2 = stl_directed_distance(ast2, ast1, ranges)
    if return_directed:
        max(d1, d2), d1, d2
    return max(d1, d2)
