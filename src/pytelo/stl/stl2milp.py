'''
 Copyright (c) 2018-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab (ERL), Lehigh University
 
 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
 See license.txt file for license information.
'''

import gurobipy as grb

from pytelo.stl import Operation, RelOperation, STLFormula


class stl2milp(object):
    '''Tools to generate an MILP from the AST of an STL formula
    
    Instance Attributes
    ----------
    formula (STLFormula): AST root node
    model (grb.Model): MILP model with constraints consistent with the MTL formula.
    variables (dict): All variables, identified by name, tracking internal states within the MILP model.
    M (int): A large constant used to enforce the satisfaction of predicates.
    robust (bool): If True, the LP for inner optimization will include a variable rho which can be maximized
                   to find the most robust trajectory.
    ranges (dict): A dictionary mapping variable names to their respective (min, max) bounds.
    vtypes (dict): A dictionary mapping variable names to their respective Gurobi variable types.
    '''
    def __init__(self, formula, ranges, vtypes=None, model=None, robust=False):
        '''
        Parameters:
        ----------
        formula (STLFormula): root node of AST generated from the desired STL formula
        ranges (dict): A dictionary mapping variable names to their respective (min, max) bounds.
        vtypes (dict): default=None - A dictionary mapping variable names to their respective Gurobi variable 
                                      types. If set to None, all variables will be initialized as continuous.
        model (grb.Model): default=None - Existing gurobi MIP. Constraints to track satisfaction of the MTL 
                                            formula will be added to this model if passed. If set to None, a 
                                            new model will be created.
        robust (bool): default=False - If True, the LP for inner optimization will include a variable rho which
                                       can be maximized to find the most robust trajectory.
        '''
        self.formula = formula

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
        '''Generates MILP constraints on self.model from the STL formula stored in self.formula. Note: this always
        constructs the constraints with respect to satisfaction at t=0.
        
        Parameters:
        ----------
        satisfaction (bool): default=True - If truthy, failure to find a satisfying solution will raise a GurobiError 
                                            for infeasibility upon optimization.
                                            Otherwise, the formula is allowed to satisfy or violate, and satisfying
                                            solutions may be found by using the returned z variable as an optimization
                                            objective, or by using self.rho as an objective if optimizing for
                                            robustness.

        Returns:
        ----------
        z (grb.Variable): The gurobi variable indicating the satisfaction or violation of the STL formula. 
                          A value of 1 after optimization indicates a solution was found which satisfied the formula.
                          A value of 0 indicates that no satisfying solution was found.
        '''
        z = self.to_milp(self.formula)
        if satisfaction:
            self.model.addConstr(z == 1, 'formula_satisfaction')
        return z

    def to_milp(self, formula, t=0):
        '''Generates the MILP constraints and optimization objectives from an STL formula.
        
        Parameters:
        ----------
        formula (STLFormula): Root node of AST generated from the desired STL formula.
        t (int): default=0 - The time at which the formula should be evaluated.
        
        Returns:
        ----------
        z (grb.Variable): The gurobi variable constrained to indicate the satisfaction or violation for the formula 
                          or subformula.
        '''
        z, added = self.add_formula_variable(formula, t)
        if added:
            self.__milp_call[formula.op](formula, z, t)
        return z

    def add_formula_variable(self, formula, t, vtype=grb.GRB.BINARY):
        '''Add a variables to self.model to track the satisfaction or violation of the parent node of passed
        STL AST at time t. 
        
        Parameters:
        ----------
        formula (STLFormula): Root node of AST for desired formula (or subformula).
        t (int): time at which the formula (or subformula)'s satisfaction must be evaluated.
        vtype (int): default=grb.GRB.BINARY - The type of variable (usually either binary or continuous) to 
                                              create for tracking formula satisfaction.
        
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

    def add_state(self, state, t):
        '''Create variables for signal state at time t if they have not already been created. Adds 
        variables for trajectory states as special entries in self.variables. This allows trajectory 
        states to be extracted by the string variable name.
        
        Parameters:
        ----------
        state (str): Name of the state variable in the STL formula.
        t (int): Time at which the value is being used to constrain the MILP.
        
        Returns:
        ----------
        v (grb.Variable): The gurobi variable for the specified state variable at time t.
        '''
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

    def predicate(self, pred, z, t):
        '''Adds appropriate reference data for a subformula that is a predicate only. Creates state variables
        for the predicate signal variable at time t if needed. Adds model constraints to ensure that the z
        variable provided is consistent with the predicate's satisfaction or violation at time t. If optimizing
        for robustness, the robustness is factored in to the predicates where needed as self.rho.
        
        Parameters:
        ----------
        pred (STLFormula): AST formula root (must be a predicate).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate satisfaction.
        '''
        assert pred.op == Operation.PRED
        v = self.add_state(pred.variable, t)
        if pred.relation in (RelOperation.GE, RelOperation.GT):
            self.model.addConstr(v - self.M * z <= pred.threshold + self.rho)
            self.model.addConstr(v + self.M * (1 - z) >= pred.threshold + self.rho)
        elif pred.relation in (RelOperation.LE, RelOperation.LT):
            self.model.addConstr(v + self.M * z >= pred.threshold - self.rho)
            self.model.addConstr(v - self.M * (1 - z) <= pred.threshold - self.rho)
        else:
            raise NotImplementedError

    def conjunction(self, formula, z, t):
        '''Adds constraints for a subformula with conjunction as its root operation. 
        Recursively constructs child constraints.
        
        Parameters:
        ----------
        formula (STLFormula): AST formula root (must be a conjunction operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate the degree of satisfaction.
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
        formula (STLFormula): AST formula root (must be a disjunction operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate the degree of satisfaction.
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
        formula (STLFormula): AST formula root (must be an eventually operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate the degree of satisfaction.
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
        formula (STLFormula): AST formula root (must be an always operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate the degree of satisfaction.
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
        formula (STLFormula): AST formula root (must be an until operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate the degree of satisfaction.
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
