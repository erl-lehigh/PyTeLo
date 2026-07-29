'''
 Copyright (c) 2023, Explainable Robotics Lab (ERL), Lehigh University
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile

 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
 See license.txt file for license information.
'''

import gurobipy as grb

from pytelo.mtl import Operation, MTLFormula


class mtl2milp(object):
    '''Tools to generate an MILP from the AST of an MTL formula
    
    Instance Attributes
    ----------
    formula (MTLFormula): AST root node
    model (grb.Model): MILP model with constraints consistent with the MTL formula.
    variables (dict): All variables, identified by name, tracking internal states within the MILP model.
    '''

    def __init__(self, formula, model=None):
        '''
        Parameters:
        ----------
        formula (MTLFormula): root node of AST generated from the desired MTL formula
        model (grb.Model): default=None - Existing gurobi MIP. Constraints to track satisfaction of the MTL 
                                          formula will be added to this model if passed. If set to None, a new 
                                          model will be created.
        '''
        self.formula = formula

        self.model = model
        if model is None:
            self.model = grb.Model('MTL formula: {}'.format(formula))

        self.variables = dict()

        self.__milp_call = {
            Operation.PRED : self.predicate,
            Operation.AND : self.conjunction,
            Operation.OR : self.disjunction,
            Operation.EVENT : self.eventually,
            Operation.ALWAYS : self.globally,
            Operation.UNTIL : self.until
        }

    def translate(self, satisfaction=True):
        '''Generates MILP constraints on self.model from the MTL formula. Note: this always constructs the
        constraints with respect to satisfaction at t=0.

        Parameters:
        ----------
        satisfaction (bool): default=True - if this is truthy, a constraint will be added to the MILP requiring
                                            the formula to satisfy. If no satisfying path exists subject to the
                                            constraints on self.model, then calling model.optimize will raise a
                                            Gurobi error. If this is set to false, then satisfying trajectories
                                            must be found using a custom gurobi optimization objective.
        
        Returns:
        ----------
        z (grb.Variable): The gurobi variable indicating the satisfaction or violation of the MTL formula. If 
                          the satisfaction param is truthy or unused, this will always be 1 after calling 
                          model.optimize, unless a Gurobi error occurs due to model infeasibility. If the 
                          satisfaction param is falsy, this can be used as an optimization objective to find
                          a satisfying (maximize) or violating (minimize) trajectory, if one exists.
        '''
        z = self.to_milp(self.formula)
        if satisfaction:
            self.model.addConstr(z == 1, 'formula_satisfaction')
        return z

    def to_milp(self, formula, t=0):
        '''Generates the MILP constraints from an MTL formula.
        
        Parameters:
        ----------
        formula (MTLFormula): Root node of AST generated from the desired MTL formula.
        t (int): default=0 - The time at which the formula should be evaluated.

        Returns:
        ----------
        z (grb.Variable): The gurobi variable constrained to indicate satisfaction or violation of the formula.
        '''
        z, added = self.add_formula_variable(formula, t)
        if added:
            self.__milp_call[formula.op](formula, z, t)
        return z

    def add_formula_variable(self, formula, t, vtype=grb.GRB.BINARY):
        '''Adds a variable to self.model to track the satisfaction of violation of the parent node of passed
        MTL AST at time t.
        
        Parameters:
        ----------
        formula (MTLFormula): Root node of AST for desired formula (or subformula).
        t (int): time at which the formula (or subformula)'s satisfaction must be evaluated.
        vtype (char): default=grb.GRB.BINARY - status code indicating the gurobi variable type required to 
                                               track satisfaction.
        
        Returns:
        ----------
        z (grb.Variable): A gurobi variable to indicate the satisfaction or violation of the formula (or 
                          subformula) at time t.
        added (bool): True if a variable for this (or identical) formula did not previously exist in self.model. 
                      False otherwise.
        '''
        if formula not in self.variables:
            self.variables[formula] = dict()
        if t not in self.variables[formula]:
            opname = Operation.getName(formula.op)
            identifier = formula.identifier()
            name = '{}_{}_{}'.format(opname, identifier, t)
            self.variables[formula][t] = self.model.addVar(vtype=vtype,
                                                           name=name)
            self.model.update()
            return self.variables[formula][t], True
        return self.variables[formula][t], False

    def add_state(self, state, t, z):
        '''Adds variables for trajectory states as special entries in self.variables.
        This allows trajectory states to be extracted by the string variable name.

        Parameters:
        ----------
        state (str): Name of the state variable in the MTL formula.
        t (int): Time at which the value is being used to constrain the MILP.
        z (grb.Variable): Gurobi variable linked to the satisfaction or violation of the state and time.
        '''
        if state not in self.variables:
            self.variables[state] = dict()
        if t not in self.variables[state]:
            self.variables[state][t] = z
            self.model.update()
        return self.variables[state][t]

    def predicate(self, pred, z, t):
        '''Adds appropriate reference data for a subformula that is a predicate only.
        
        Parameters:
        ----------
        pred (MTLFormula): AST formula root (must be a predicate).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate satisfaction.
        '''
        assert pred.op == Operation.PRED
        self.add_state(pred.variable, t, z)

    def conjunction(self, formula, z, t):
        '''Adds constraints for a subformula with conjunction as its root operation. 
        Recursively constructs child constraints.
        
        Parameters:
        ----------
        formula (MTLFormula): AST formula root (must be a conjunction operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate satisfaction.
        '''
        assert formula.op == Operation.AND
        z_children = [self.to_milp(f, t) for f in formula.children]
        for z_child in z_children:
            self.model.addConstr(z <= z_child)
        self.model.addConstr(z >= 1 - len(z_children) + sum(z_children))

    def disjunction(self, formula, z, t):
        '''Adds constraints for a subformula with disjunction as its root operation. 
        Recursively constructs child constraints.
        
        Parameters:
        ----------
        formula (MTLFormula): AST formula root (must be a disjunction operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate satisfaction.
        '''
        assert formula.op == Operation.OR
        z_children = [self.to_milp(f, t) for f in formula.children]
        for z_child in z_children:
            self.model.addConstr(z >= z_child)
        self.model.addConstr(z <= sum(z_children))

    def eventually(self, formula, z, t):
        '''Adds constraints for a subformula with eventually as its root operation. 
        Recursively constructs child constraints.
        
        Parameters:
        ----------
        formula (MTLFormula): AST formula root (must be an eventually operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate satisfaction.
        '''
        assert formula.op == Operation.EVENT
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau) for tau in range(a, b+1)]
        for z_child in z_children:
            self.model.addConstr(z >= z_child)
        self.model.addConstr(z <= sum(z_children))

    def globally(self, formula, z, t):
        '''Adds constraints for a subformula with always as its root operation. 
        Recursively constructs child constraints.
        
        Parameters:
        ----------
        formula (MTLFormula): AST formula root (must be an always operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate satisfaction.
        '''
        assert formula.op == Operation.ALWAYS
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau) for tau in range(a, b+1)]
        for z_child in z_children:
            self.model.addConstr(z <= z_child)
        self.model.addConstr(z >= 1 - len(z_children) + sum(z_children))

    def until(self, formula, z, t):
        '''Adds constraints for a subformula with until as its root operation. 
        Recursively constructs child constraints.
        
        Parameters:
        ----------
        formula (MTLFormula): AST formula root (must be an until operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate satisfaction.
        '''
        assert formula.op == Operation.UNTIL

        a, b = int(formula.low), int(formula.high)
        z_children_left = [self.to_milp(formula.left, tau)
                                                 for tau in range(t, t+b+1)]
        z_children_right = [self.to_milp(formula.right, tau)
                                               for tau in range(t+a, t+b+1)]

        z_aux = []
        phi_alw = None
        if a > 0:
            phi_alw = MTLFormula(Operation.ALWAYS, child=formula.left,
                                 low=t, high=t+a-1)
        for tau in range(t+a, t+b+1):
            if tau > t+a:
                phi_alw_u = MTLFormula(Operation.ALWAYS, child=formula.left,
                                       low=t+a, high=tau)
            else:
                phi_alw_u = formula.left
            children = [formula.right, phi_alw_u]
            if phi_alw is not None:
                children.append(phi_alw)
            phi = MTLFormula(Operation.AND, children=children)
            z_aux.append(self.add_formula_variable(phi, t)[0])

        for k, z_right in enumerate(z_children_right):
            z_conj = z_aux[k]
            self.model.addConstr(z_conj <= z_right)
            for z_left in z_children_left[:t+a+k+1]:
                self.model.addConstr(z_conj <= z_left)
            m = 1 + (t + a + k + 1)
            self.model.addConstr(z_conj >= 1-m + z_right
                                 + sum(z_children_left[:t+a+k+1]))

            self.model.addConstr(z >= z_conj)
        self.model.addConstr(z <= sum(z_aux))