'''
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
'''

import gurobipy as grb

from stl import Operation, RelOperation

class wstl2milp(object):
    '''Translate an wSTL formula to an MILP.'''

    def __init__(self, formula, ranges=None, vtypes=None, model=None):
        self.formula = formula

        self.ranges = ranges
        if ranges is None:
            self.ranges = {v: (-9, 9) for v in self.formula.variables()}

        self.vtypes = vtypes
        if vtypes is None:
            self.vtypes = {v: grb.GRB.CONTINUOUS for v in self.ranges}

        self.model = model
        if model is None:
            self.model = grb.Model('wSTL formula: {}'.format(formula))

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
            Operation.RELEASE : self.release
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
                                    lb=-grb.GRB.INFINITY, ub=grb.GRB.INFINITY)
            self.variables[formula][t] = (z, rho)
            self.model.update()
            return self.variables[formula][t], True
        return self.variables[formula][t], False

    def add_hat_variable(self, formula, parent, t):
        '''Adds a hat variable for the `formula` at time `t`
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
                            vtype=grb.GRB.BINARY, name=z_name)
            # self.hat_variables[parent][formula][t] = self.model.addVar(
            #                 vtype=grb.GRB.CONTINUOUS, name=z_name, lb=0, ub=1)
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
            self.model.update()
        return self.variables[state][t]

    def predicate(self, pred, z, rho, t):
        '''Adds a predicate to the model.'''
        assert pred.op == Operation.PRED
        v = self.add_state(pred.variable, t)
        if pred.relation in (RelOperation.GE, RelOperation.GT):
            self.model.addConstr(v + self.M * (1 - z) >= pred.threshold + rho)
            self.model.addConstr(v - self.M * z <= pred.threshold + rho)

        elif pred.relation in (RelOperation.LE, RelOperation.LT):
            self.model.addConstr(v - self.M * (1 - z) <= pred.threshold - rho)
            self.model.addConstr(v + self.M * z >= pred.threshold - rho)
        else:
            raise NotImplementedError

    def conjunction(self, formula, z, rho, t):
        '''Adds a conjunction to the model.'''
        assert formula.op == Operation.AND
        vars_children = [self.to_milp(f, t) for f in formula.children]
    
        for k, (z_child, rho_child) in enumerate(vars_children):
            weight = formula.weight(k)
            self.model.addConstr(rho <= weight * rho_child)
            self.model.addConstr(z <= z_child)
        z_children, _ = zip(*vars_children)
        self.model.addConstr(z >= 1 - len(z_children) + sum(z_children))

    def disjunction(self, formula, z, rho, t):
        '''Adds a disjunction to the model.'''
        assert formula.op == Operation.OR
        z_children, rho_children = zip(*[self.to_milp(f, t)
                                         for f in formula.children])
        z_hat_children, _ = zip(*[self.add_hat_variable(f, formula, t)
                                 for f in formula.children])
        vars_children = zip(z_children, z_hat_children, rho_children)
        for k, (z_child, z_hat_child, rho_child) in enumerate(vars_children):
            weight = formula.weight(k)
            self.model.addConstr(
                rho <= weight * rho_child + self.M * (1 - z_hat_child))
            self.model.addConstr(z >= z_child)
            self.model.addConstr(z_hat_child <= z_child)
        self.model.addConstr(z <= sum(z_children))
        self.model.addConstr(sum(z_hat_children) >= z)

    def globally(self, formula, z, rho, t):
        '''Adds a globally to the model.'''
        assert formula.op == Operation.ALWAYS
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        vars_children = [self.to_milp(child, t + tau) for tau in range(a, b+1)]
        for tau, (z_child, rho_child) in zip(range(a, b+1), vars_children):
            weight = formula.weight(tau)
            self.model.addConstr(rho <= weight * rho_child)
            self.model.addConstr(z <= z_child)
        z_children, _ = zip(*vars_children)
        self.model.addConstr(z >= 1 - len(z_children) + sum(z_children))
    
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
            self.model.addConstr(
                rho <= weight * rho_child + self.M * (1 - z_hat_child))
            self.model.addConstr(z_hat_child <= z_child)
            self.model.addConstr(z >= z_child)
        self.model.addConstr(z <= sum(z_children))
        self.model.addConstr(sum(z_hat_children) >= z)

    def until(self, formula, z, rho, t):
        '''Adds an until to the model.'''
        assert formula.op == Operation.UNTIL

        raise NotImplementedError #TODO: under construction

    def release(self, formula, z, rho, t):
        '''Adds an release to the model.'''
        assert formula.op == Operation.release

        raise NotImplementedError #TODO: under construction
