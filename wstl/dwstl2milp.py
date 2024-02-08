'''
 Copyright (C) 2018-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 author: Gustavo A. Cardona
'''

import gurobipy as grb

from stl import Operation, RelOperation, STLFormula


class dwstl2milp(object):
    '''Translate an STL formula to an MILP.'''

    def __init__(self, formula, ranges=None, vtypes=None, model=None):
        self.formula = formula
        
        
        if ranges is None:
            self.ranges = {v: (-9, 9) for v in self.formula.variables()}
        else:
            self.ranges = ranges

        assert set(self.formula.variables()) <= set(self.ranges)

        # if robust and 'rho' not in self.ranges:
        #     self.ranges['rho'] = (-grb.GRB.INFINITY, self.M - 1)

        self.vtypes = vtypes
        if vtypes is None:
            self.vtypes = {v: grb.GRB.CONTINUOUS for v in self.ranges}

        self.model = model
        if model is None:
            self.model = grb.Model('STL formula: {}'.format(formula))
        
        self.M = 1000
        self.variables = dict()
        self.hat_variables = dict()
        
        # if robust:
        #     rho_min, rho_max = self.ranges['rho']
        #     self.rho = self.model.addVar(vtype=self.vtypes['rho'], name='rho',
        #                                  lb=rho_min, ub=rho_max, obj=-1)
        # else:
        #     self.rho = 0

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
        z, rho = self.to_milp(self.formula, self.formula, root=True)
        if satisfaction:
            self.model.addConstr(z == 1, 'formula_satisfaction')
        return z , rho

    def to_milp(self, formula, parent, t=0, root=False, t_parent=None):
        '''Generates the MILP from the STL formula.'''
        (z, rho), added = self.add_formula_variable(formula, parent, t, 
                                                    root, t_parent)
        if added:
            self.__milp_call[formula.op](formula, z, rho, t)
        return z, rho

    def add_formula_variable(self, formula, parent, t, root, t_parent):
        ''' Adds a variable for the `formula` at time `t`.'''
        if formula not in self.variables:
            self.variables[formula] = dict()
        if t not in self.variables[formula]:
            op_set={Operation.PRED, Operation.AND, Operation.ALWAYS}
            if parent.op in op_set and root==False:
                if parent.op == Operation.AND:
                    k = parent.children.index(formula)
                    weight = parent.weight(k)
                    temp = list(self.variables[parent][t_parent])
                    temp[1] *= weight
                    self.variables[parent][t_parent] = tuple(temp)
                elif parent.op == Operation.ALWAYS:
                    weight=parent.weight(t)
                    temp = list(self.variables[parent][t_parent])
                    temp[1] *= weight
                    self.variables[parent][t_parent] = tuple(temp)
                variable = self.variables[parent][t_parent]

            elif parent.op in {Operation.OR, Operation.EVENT} or root==True:
                opname = Operation.getString(formula.op)
                identifier = formula.identifier()
                name = '{}_{}_{}'.format(opname, identifier, t)
                z = self.model.addVar(vtype=grb.GRB.BINARY, name=name)

                rho_name = 'rho_{}_{}_{}'.format(opname, identifier, t)
                rho = self.model.addVar(vtype=grb.GRB.CONTINUOUS, name=rho_name,
                                    lb=-grb.GRB.INFINITY, ub=grb.GRB.INFINITY)                
                variable = (z, rho) 
            else:
                raise NotImplementedError
            self.variables[formula][t] = variable
            self.model.update()
            return variable, True
        return self.variables[formula][t], False
    
    def add_hat_variable(self, formula, parent, t):
        '''Adds a hat variable for the `formula` at time `t`
        TODO:
        TODO: check if we need the parent
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
            #TODO: we need to check if this will work for continuos interval [0.1]
            # and compare performance then proof in the paper this relaxation                                               
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
            self.model.addConstr(v - self.M * z <= pred.threshold + rho)
            self.model.addConstr(v + self.M * (1 - z) >= pred.threshold + rho)
        elif pred.relation in (RelOperation.LE, RelOperation.LT):
            self.model.addConstr(v + self.M * z >= pred.threshold - rho)
            self.model.addConstr(v - self.M * (1 - z) <= pred.threshold - rho)
#            raise NotImplementedError
        else:
            raise NotImplementedError

    def conjunction(self, formula, z, rho, t):
        '''Adds a conjunction to the model.'''
        assert formula.op == Operation.AND
        for child in formula.children:
            self.to_milp(child, formula, t, t_parent=t)


    def disjunction(self, formula, z, rho, t):
        '''Adds a disjunction to the model.'''
        assert formula.op == Operation.OR
        z_children, rho_children = zip(*[self.to_milp(f, formula, t, t_parent=t)
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

    def eventually(self, formula, z, rho, t):
        '''Adds an eventually to the model.'''
        assert formula.op == Operation.EVENT
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children, rho_children = zip(*[self.to_milp(child, formula, t+tau, 
                                                      t_parent=t)
                                         for tau in range(a, b+1)])
        z_hat_children, _ = zip(*[self.add_hat_variable(child, formula, t+tau)
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

    def globally(self, formula, z, rho, t):
        '''Adds a globally to the model.'''
        assert formula.op == Operation.ALWAYS
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        for tau in range(a, b+1):
            self.to_milp(child, formula, t + tau, t_parent=t) 
            

    def until(self, formula, z, rho, t):
        '''Adds an until to the model.'''
        assert formula.op == Operation.UNTIL
        raise NotImplementedError
        # a, b = int(formula.low), int(formula.high)
        # z_children_left = [self.to_milp(formula.left, tau)
        #                                          for tau in range(t, t+b+1)]
        # z_children_right = [self.to_milp(formula.right, tau)
        #                                        for tau in range(t+a, t+b+1)]

        # z_aux = []
        # phi_alw = None
        # if a > 0:
        #     phi_alw = STLFormula(Operation.ALWAYS, child=formula.left,
        #                          low=t, high=t+a-1)
        # for tau in range(t+a, t+b+1):
        #     if tau > t+a:
        #         phi_alw_u = STLFormula(Operation.ALWAYS, child=formula.left,
        #                                low=t+a, high=tau)
        #     else:
        #         phi_alw_u = formula.left
        #     children = [formula.right, phi_alw_u]
        #     if phi_alw is not None:
        #         children.append(phi_alw)
        #     phi = STLFormula(Operation.AND, children=children)
        #     z_aux.append(self.add_formula_variable(phi, t)[0])

        # for k, z_right in enumerate(z_children_right):
        #     z_conj = z_aux[k]
        #     self.model.addConstr(z_conj <= z_right)
        #     for z_left in z_children_left[:t+a+k+1]:
        #         self.model.addConstr(z_conj <= z_left)
        #     m = 1 + (t + a + k + 1)
        #     self.model.addConstr(z_conj >= 1-m + z_right
        #                          + sum(z_children_left[:t+a+k+1]))

        #     self.model.addConstr(z <= z_conj)
        # self.model.addConstr(z <= sum(z_aux))
    def release(self, formula, z, rho, t):
        '''Adds an release to the model.'''
        assert formula.op == Operation.release

        raise NotImplementedError #TODO: under construction