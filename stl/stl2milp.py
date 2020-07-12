'''
 Copyright (C) 2018-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''

import numpy as np
import gurobipy as grb

from stl import Operation, RelOperation, STLFormula


class stl2milp(object):
    '''Translate an STL formula to an MILP.'''

    def __init__(self, formula, ranges, time_step=1, vtypes=None, model=None,
                 robust=False):
        '''
        Initializes the translation process of an STL formula to an MILP.

        Parameters
        ----------
        formula (STLFormula) - STL formila to translate
        ranges (dict) - the ranges of all variables that appear in the STL
            formula, and, optionally, the range of the robustness.
        time_step (float, default: 1) - the discretization time step.
        vtypes (dict, default: grb.GRB.CONTINUOUS) - the types of decision
            variables associates with the variables in the provided STL formula
            at all required times.
        model (guroby.Model, default: None) - a Guroby model to add variables
            and constraints to; if missing (i.e., None) a new model is created.
        robust (bool, default: False) - whether the encoding considers the
            robust or feasible problem.
        '''
        self.formula = formula
        self.time_step = float(self.time_step)

        self.M = 1000
        self.ranges = ranges
        assert set(self.formula.variables()) <= set(self.ranges)
        if robust and 'rho' not in self.ranges:
            self.ranges['rho'] = (-grb.GRB.INFINITY, self.M - 1)

        self.vtypes = vtypes
        if vtypes is None:
            self.vtypes = {v: grb.GRB.CONTINUOUS for v in self.ranges}

        self.model = model
        if model is None:
            self.model = grb.Model('STL formula: {}'.format(formula))

        self.variables = dict()

        if robust:
            rho_min, rho_max = self.ranges['rho']
            self.rho = self.model.addVar(vtype=self.vtypes['rho'], name='rho',
                                         lb=rho_min, ub=rho_max, obj=-1)
        else:
            self.rho = 0

        self.__milp_call = {
            Operation.PRED : self.predicate,
            Operation.AND : self.conjunction,
            Operation.OR : self.disjunction,
            Operation.EVENT : self.eventually,
            Operation.ALWAYS : self.globally,
            Operation.UNTIL : self.until
        }

    def translate(self, satisfaction=True):
        '''Translates the STL formula to MILP from time 0.'''
        z = self.to_milp(self.formula)
        if satisfaction:
            self.model.addConstr(z == 1, 'formula_satisfaction')
        return z

    def to_milp(self, formula, t=0):
        '''Generates the MILP from the STL formula.'''
        z, added = self.add_formula_variable(formula, t)
        if added:
            self.__milp_call[formula.op](formula, z, t)
        return z

    def add_formula_variable(self, formula, t, vtype=grb.GRB.BINARY):
        '''Adds a variable for the `formula` at time `t`.'''
        if formula not in self.variables:
            self.variables[formula] = dict()
        if t not in self.variables[formula]:
            opname = Operation.getString(formula.op)
            identifier = formula.identifier()
            time_index = round(t / float(self.time_step))
            name = '{}_{}_{}'.format(opname, identifier, time_index)
            self.variables[formula][t] = self.model.addVar(vtype=vtype,
                                                           name=name)
            self.model.update() #TODO: not sure if this is needed (NEEDED!)
            return self.variables[formula][t], True
        return self.variables[formula][t], False

    def add_state(self, state, t):
        '''Adds the `state` at time `t` as a variable.'''
        if state not in self.variables:
            self.variables[state] = dict()
        if t not in self.variables[state]:
            low, high = self.ranges[state]
            vtype = self.vtypes[state]
            time_index = round(t / float(self.time_step))
            name='{}_{}'.format(state, time_index)
            v = self.model.addVar(vtype=vtype, lb=low, ub=high, name=name)
            self.variables[state][t] = v
            self.model.update()
        return self.variables[state][t]

    def predicate(self, pred, z, t):
        '''Adds a predicate to the model.'''
        assert pred.op == Operation.PRED
        v = self.add_state(pred.variable, t)
        if pred.relation in (RelOperation.GE, RelOperation.GT):
            self.model.addConstr(v - self.M * z <= pred.threshold + self.rho)
            self.model.addConstr(v + self.M * (1 - z) >= pred.threshold + self.rho)
        elif pred.relation in (RelOperation.LE, RelOperation.LT):
            self.model.addConstr(v + self.M * z >= pred.threshold - self.rho)
            self.model.addConstr(v - self.M * (1 - z) <= pred.threshold - self.rho)
#            raise NotImplementedError
        else:
            raise NotImplementedError

    def conjunction(self, formula, z, t):
        '''Adds a conjunction to the model.'''
        assert formula.op == Operation.AND
        z_children = [self.to_milp(f, t) for f in formula.children]
        for z_child in z_children:
            self.model.addConstr(z <= z_child)
        self.model.addConstr(z >= 1 - len(z_children) + sum(z_children))

    def disjunction(self, formula, z, t):
        '''Adds a disjunction to the model.'''
        assert formula.op == Operation.OR
        z_children = [self.to_milp(f, t) for f in formula.children]
        for z_child in z_children:
            self.model.addConstr(z >= z_child)
        self.model.addConstr(z <= sum(z_children))

    def eventually(self, formula, z, t):
        '''Adds an eventually to the model.'''
        assert formula.op == Operation.EVENT
        dt = self.time_step
        a, b = formula.low, formula.high
        child = formula.child
        z_children = [self.to_milp(child, t + tau)
                      for tau in np.arange(a, b + dt, dt)]
        for z_child in z_children:
            self.model.addConstr(z >= z_child)
        self.model.addConstr(z <= sum(z_children))

    def globally(self, formula, z, t):
        '''Adds a globally to the model.'''
        assert formula.op == Operation.ALWAYS
        dt = self.time_step
        a, b = formula.low, formula.high
        child = formula.child
        z_children = [self.to_milp(child, t + tau)
                      for tau in np.arange(a, b + dt, dt)]
        for z_child in z_children:
            self.model.addConstr(z <= z_child)
        self.model.addConstr(z >= 1 - len(z_children) + sum(z_children))

    def until(self, formula, z, t):
        '''Adds an until to the model.'''
        assert formula.op == Operation.UNTIL

        raise NotImplementedError #TODO: under construction

        dt = self.time_step
        a, b = formula.low, formula.high
        z_children_left = [self.to_milp(formula.left, t + tau)
                           for tau in np.range(0, b + dt, dt)]
        z_children_right = [self.to_milp(formula.right, t + tau)
                            for tau in range(a, b + dt, dt)]

        z_aux = []
        phi_alw = None
        if a > 0:
            phi_alw = STLFormula(Operation.ALWAYS, child=formula.left,
                                 low=t, high=t + a - dt)
        for tau in np.arange(a, b + dt, dt):
            if tau > a:
                phi_alw_u = STLFormula(Operation.ALWAYS, child=formula.left,
                                       low=t + a, high=t + tau)
            else:
                phi_alw_u = formula.left
            children = [formula.right, phi_alw_u]
            if phi_alw is not None:
                children.append(phi_alw)
            phi = STLFormula(Operation.AND, children=children)
            z_aux.append(self.add_formula_variable(phi, t))

        start = rount((t + a) / dt)
        for k, z_right in enumerate(z_children_right):
            z_conj = z_aux[k]
            self.model.addConstr(z_conj <= z_right)
            for z_left in z_children_left[:start + k + 1]:
                self.model.addConstr(z_conj <= z_left)
            m = 1 + (start + k)
            self.model.addConstr(z_conj >= 1-m + z_right
                                 + sum(z_children_left[:start + k + 1]))

            self.model.addConstr(z >= z_conj)
        self.model.addConstr(z <= sum(z_aux))
