'''
 Copyright (C) 2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''

import gurobipy as grb

from stl import Operation, RelOperation, STLFormula


class wstl2milp(object):
    '''Translate an WSTL formula to an MILP.'''

    def __init__(self, formula, ranges=None, vtypes=None, model=None):
        self.formula = formula

        self.ranges = ranges
        if ranges is None:
            self.ranges = {v: (0, 10) for v in self.formula.variables()}

        self.vtypes = vtypes
        if vtypes is None:
            self.vtypes = {v: grb.GRB.CONTINUOUS for v in self.ranges}

        self.model = model
        if model is None:
            self.model = grb.Model('WSTL formula: {}'.format(formula))

        self.M = 1000
        self.variables = dict()
        self.hat_variables = dict()

        self.__milp_call = {
            Operation.PRED : self.predicate,
            Operation.AND : self.conjunction,
            Operation.OR : self.disjunction,
            Operation.EVENT : self.eventually,
            Operation.ALWAYS : self.globally,
            Operation.UNTIL : self.until,
            # Operation.RELEASE : self.release #TODO:
        }

    def translate(self, satisfaction=True):
        '''Translates the STL formula to MILP from time 0.'''
        z, rho = self.to_milp(self.formula)
        if satisfaction:
            self.model.addConstr(z == 1, 'formula_satisfaction')
        return z, rho

    def to_milp(self, formula, t=0):
        '''Generates the MILP from the STL formula.'''
        (z, rho), added = self.add_formula_variables(formula, t)
        if added:
            self.__milp_call[formula.op](formula, z, rho, t)
        return z, rho

    def add_formula_variables(self, formula, t):
        '''Adds a variable for the `formula` at time `t`.'''
        if formula not in self.variables:
            self.variables[formula] = dict()
        if t not in self.variables[formula]:
            opname = Operation.getString(formula.op)
            identifier = formula.identifier()
            z_name = 'z_{}_{}_{}'.format(opname, identifier, t)
            if formula.op == Operation.PRED:
                z = self.model.addVar(vtype=grb.GRB.BINARY, name=z_name)
            else:
                z = self.model.addVar(vtype=grb.GRB.CONTINUOUS, name=z_name,
                                      lb=0, ub=1)
            rho_name = 'rho_{}_{}_{}'.format(opname, identifier, t)
            rho = self.model.addVar(vtype=grb.GRB.CONTINUOUS, name=rho_name,
                                    lb=-grb.GRB.INFINITY,ub=grb.GRB.INFINITY)
            self.variables[formula][t] = (z, rho)
            self.model.update()
            return self.variables[formula][t], True
        return self.variables[formula][t], False

    def add_hat_variable(self, formula, parent, t):
        '''Adds a hat variable for the `formula` at time `t`
        TODO:

        NOTE: Is caching correct, or does every disjunction, eventually,
        and until need their own version?
        '''
        if parent not in self.hat_variables:
            self.hat_variables[parent] = dict()
        if formula not in self.hat_variables[parent]:
            self.hat_variables[parent][formula] = dict()
        if t not in self.hat_variables[parent][formula]:
            opname = Operation.getString(formula.op)
            identifier = formula.identifier()
            parent_identifier = parent.identifier()
            z_name = 'zhat_{}_{}_{}_{}'.format(opname, identifier,
                                               parent_identifier, t)
            self.hat_variables[parent][formula][t] = self.model.addVar(
                            vtype=grb.GRB.CONTINUOUS, name=z_name, lb=0, ub=1)
            self.model.update()
            return self.hat_variables[parent][formula][t], True
        return self.hat_variables[parent][formula][t], False

    def add_state(self, state, t):
        '''Adds the `state` at time `t` as a variable.'''
        if state not in self.variables:
            self.variables[state] = dict()
        if t not in self.variables[state]:
            low, high = self.ranges[state]
            vtype = self.vtypes[state]
            name='{}_{}'.format(state, t)
            v = self.model.addVar(vtype=vtype, lb=low, ub=high, name=name)
            self.variables[state][t] = v
            print 'Added state:', state, 'time:', t
            self.model.update()
        return self.variables[state][t]

    def predicate(self, pred, z, rho, t):
        '''Adds a predicate to the model.'''
        assert pred.op == Operation.PRED
        v = self.add_state(pred.variable, t)
        if pred.relation in (RelOperation.GE, RelOperation.GT):
            self.model.addConstr(rho == v - pred.threshold)
            self.model.addConstr(rho >= self.M * (1 - z))
            self.model.addConstr(rho <= self.M * z)
        elif pred.relation in (RelOperation.LE, RelOperation.LT):
            raise NotImplementedError
            # self.model.addConstr(rho == pred.threshold - v)
        else:
            raise NotImplementedError

    def conjunction(self, formula, z, rho, t):
        '''Adds a conjunction to the model.'''
        assert formula.op == Operation.AND
        vars_children = [self.to_milp(f, t) for f in formula.children]
        z_sum = 0
        for k, (z_child, rho_child) in enumerate(vars_children):
            self.model.addConstr(z <= z_child)
            self.model.addConstr(rho <= (1 - formula.weight(k)) * rho_child
                                        + self.M * (1 - z))
            self.model.addConstr(rho <= formula.weight(k) * rho_child
                                        + self.M * z)

    def disjunction(self, formula, z, rho, t):
        '''Adds a disjunction to the model.'''
        assert formula.op == Operation.OR
        z_children, rho_children = zip(*[self.to_milp(f, t)
                                         for f in formula.children])
        z_hat_children,_ = zip(*[self.add_hat_variable(f, formula, t)
                                 for f in formula.children])
        vars_children = zip(z_children, z_hat_children, rho_children)
        for k, (z_child, z_hat_child, rho_child) in enumerate(vars_children):
            weight = formula.weight(k)
            self.model.addConstr(rho <= weight * rho_child
                                        + self.M * (2 - z_hat_child - z))
            self.model.addConstr(rho <= (1 - weight) * rho_child
                                        + self.M * (1 - z_hat_child + z))
        self.model.addConstr(z <= sum(z_children))
        self.model.addConstr(sum(z_hat_children) >= 1)

    def eventually(self, formula, z, rho, t):
        '''Adds an eventually to the model.'''
        assert formula.op == Operation.EVENT
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children, rho_children = zip(*[self.to_milp(child, t + tau)
                                         for tau in range(a, b+1)])
        z_hat_children, _ = zip(*[self.add_hat_variable(child, formula, t + tau)
                                  for tau in range(a, b+1)])
        vars_children = zip(range(a, b+1), z_children, z_hat_children,
                            rho_children)
        for tau, z_child, z_hat_child, rho_child in vars_children:
            weight = formula.weight(tau)
            self.model.addConstr(rho <= weight * rho_child
                                        + self.M * (2 - z_hat_child - z))
            self.model.addConstr(rho <= (1 - weight) * rho_child
                                        + self.M * (1 - z_hat_child + z))
        self.model.addConstr(z <= sum(z_children))
        self.model.addConstr(sum(z_hat_children) >= 1)

    def globally(self, formula, z, rho, t):
        '''Adds a globally to the model.'''
        assert formula.op == Operation.ALWAYS
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        vars_children = [self.to_milp(child, t + tau) for tau in range(a, b+1)]
        for tau, (z_child, rho_child) in zip(range(a, b+1), vars_children):
            self.model.addConstr(z <= z_child)
            self.model.addConstr(rho <= formula.weight(tau) * rho_child
                                        + self.M * (1 - z))
            self.model.addConstr(rho <= formula.weight(tau) * rho_child
                                        + self.M * z)

    def until(self, formula, z, rho, t):
        '''Adds an until to the model.'''
        assert formula.op == Operation.UNTIL

        raise NotImplementedError #TODO: under construction

        a, b = formula.low, formula.high
        z_children_left = [self.to_milp(formula.left, tau)
                                                 for tau in range(t, t+b+1)]
        z_children_right = [self.to_milp(formula.right, tau)
                                               for tau in range(t+a, t+b+1)]

        z_aux = []
        phi_alw = None
        if a > 0:
            phi_alw = STLFormula(Operation.ALWAYS, child=formula.left,
                                 low=t, high=t+a-1)
        for tau in range(t+a, t+b+1):
            if tau > t+a:
                phi_alw_u = STLFormula(Operation.ALWAYS, child=formula.left,
                                       low=t+a, high=tau)
            else:
                phi_alw_u = formula.left
            children = [formula.right, phi_alw_u]
            if phi_alw is not None:
                children.append(phi_alw)
            phi = STLFormula(Operation.AND, children=children)
            z_aux.append(self.add_formula_variables(phi, t))

        for k, z_right in enumerate(z_children_right):
            z_conj = z_aux[k]
            self.model.addConstr(z_conj <= z_right)
            for z_left in z_children_left[:t+a+k+1]:
                self.model.addConstr(z_conj <= z_left)
            m = 1 + (t + a + k)
            self.model.addConstr(z_conj >= 1-m + z_right
                                 + sum(z_children_left[:t+a+k+1]))

            self.model.addConstr(z >= z_conj)
        self.model.addConstr(z <= sum(z_aux))

    def release(self, formula, z, rho, t):
        '''Adds a release to the model.'''
        assert formula.op == Operation.RELEASE

        raise NotImplementedError #TODO: under construction

        a, b = formula.low, formula.high
        z_children_left = [self.to_milp(formula.left, tau)
                                                 for tau in range(t, t+b+1)]
        z_children_right = [self.to_milp(formula.right, tau)
                                               for tau in range(t+a, t+b+1)]

        z_aux = []
        phi_alw = None
        if a > 0:
            phi_alw = STLFormula(Operation.ALWAYS, child=formula.left,
                                 low=t, high=t+a-1)
        for tau in range(t+a, t+b+1):
            if tau > t+a:
                phi_alw_u = STLFormula(Operation.ALWAYS, child=formula.left,
                                       low=t+a, high=tau)
            else:
                phi_alw_u = formula.left
            children = [formula.right, phi_alw_u]
            if phi_alw is not None:
                children.append(phi_alw)
            phi = STLFormula(Operation.AND, children=children)
            z_aux.append(self.add_formula_variables(phi, t))

        for k, z_right in enumerate(z_children_right):
            z_conj = z_aux[k]
            self.model.addConstr(z_conj <= z_right)
            for z_left in z_children_left[:t+a+k+1]:
                self.model.addConstr(z_conj <= z_left)
            m = 1 + (t + a + k)
            self.model.addConstr(z_conj >= 1-m + z_right
                                 + sum(z_children_left[:t+a+k+1]))

            self.model.addConstr(z >= z_conj)
        self.model.addConstr(z <= sum(z_aux))
