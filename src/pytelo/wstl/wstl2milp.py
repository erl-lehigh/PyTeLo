'''
 Copyright (c) 2023, Explainable Robotics Lab (ERL), Lehigh University
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile

 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
 See license.txt file for license information.
'''

import gurobipy as grb

from stl import Operation, RelOperation

class wstl2milp(object):
    '''Tools to generate an MILP from the AST of a weighted STL formula.

    Instance Attributes
    ----------
    formula (WSTLFormula): AST root node
    model (grb.Model): MILP model with constraints consistent with the WSTL
                       formula
    variables (dict): Formula and signal variables indexed by formula and time
    hat_variables (dict): Binary variables selecting weighted disjunction or
                          eventually branches
    M (int): Large constant used to enforce predicate and robustness constraints
    ranges (dict): Bounds for signal variables
    vtypes (dict): Gurobi variable types for signal variables
    '''

    def __init__(self, formula, ranges=None, vtypes=None, model=None):
        '''Construct a weighted STL MILP converter.

        Parameters:
        ----------
        formula (WSTLFormula): root node of the desired WSTL formula
        ranges (dict): optional mapping of variable names to (min, max) bounds;
                       defaults to (-9, 9) for each formula variable
        vtypes (dict): optional mapping of variable names to Gurobi variable
                       types; defaults to continuous variables
        model (grb.Model): optional existing Gurobi model to which constraints
                           are added
        '''
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
        }

    def translate(self, satisfaction=True):
        '''Generates MILP constraints from self.formula at time t=0.

        Parameters:
        ----------
        satisfaction (bool): default=True - if truthy, adds a constraint
                             requiring the formula to satisfy

        Returns:
        ----------
        z (grb.Variable): Binary or continuous satisfaction variable for the
                          root formula.
        rho (grb.Variable): Robustness variable for the root formula.
        '''
        z, rho = self.to_milp(self.formula)
        if satisfaction:
            self.model.addConstr(z == 1, 'formula_satisfaction')
        return z, rho

    def to_milp(self, formula, t=0):
        '''Generates MILP constraints for a WSTL formula at a given time.

        Parameters:
        ----------
        formula (WSTLFormula): formula or subformula to encode
        t (int): default=0 - time at which the formula is evaluated

        Returns:
        ----------
        z (grb.Variable): satisfaction variable for the formula
        rho (grb.Variable): robustness variable for the formula
        '''
        (z, rho), added = self.add_formula_variables(formula, t)
        if added:
            self.__milp_call[formula.op](formula, z, rho, t)
        return z, rho

    def add_formula_variables(self, formula, t):
        '''Adds satisfaction and robustness variables for a formula at time t.

        Returns:
        ----------
        variables (tuple): The satisfaction and robustness variables.
        added (bool): True if the variables were newly created, otherwise
                      False.
        '''
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
        '''Adds a binary branch-selection variable for a weighted subformula.

        Parameters:
        ----------
        formula (WSTLFormula): weighted child formula
        parent (WSTLFormula): parent formula containing the child
        t (int): time at which the child is evaluated

        Returns:
        ----------
        z_hat (grb.Variable): Binary variable selecting the child branch.
        added (bool): True if the variable was newly created, otherwise False.
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
        '''Creates a signal-state variable at time t if needed.

        Parameters:
        ----------
        state (str): signal variable name
        t (int): time at which the signal is used

        Returns:
        ----------
        v (grb.Variable): The Gurobi variable for the signal state.
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

    def predicate(self, pred, z, rho, t):
        '''Adds weighted robustness constraints for a predicate.

        Parameters:
        ----------
        pred (WSTLFormula): AST formula root, which must be a predicate
        z (grb.Variable): satisfaction variable for the predicate
        rho (grb.Variable): robustness variable for the predicate
        t (int): time at which the predicate is evaluated
        '''
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
        '''Adds weighted conjunction constraints and recursively encodes children.

        Parameters:
        ----------
        formula (WSTLFormula): conjunction formula
        z (grb.Variable): satisfaction variable for the conjunction
        rho (grb.Variable): robustness variable for the conjunction
        t (int): time at which the conjunction is evaluated
        '''
        assert formula.op == Operation.AND
        vars_children = [self.to_milp(f, t) for f in formula.children]
    
        for k, (z_child, rho_child) in enumerate(vars_children):
            weight = formula.weight(k)
            self.model.addConstr(rho <= weight * rho_child)
            self.model.addConstr(z <= z_child)
        z_children, _ = zip(*vars_children)
        self.model.addConstr(z >= 1 - len(z_children) + sum(z_children))

    def disjunction(self, formula, z, rho, t):
        '''Adds weighted disjunction constraints and branch-selection variables.

        Parameters:
        ----------
        formula (WSTLFormula): disjunction formula
        z (grb.Variable): satisfaction variable for the disjunction
        rho (grb.Variable): robustness variable for the disjunction
        t (int): time at which the disjunction is evaluated
        '''
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
        '''Adds weighted globally constraints over the formula interval.

        Parameters:
        ----------
        formula (WSTLFormula): globally formula
        z (grb.Variable): satisfaction variable for the formula
        rho (grb.Variable): robustness variable for the formula
        t (int): time at which the formula is evaluated
        '''
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
        '''Adds weighted eventually constraints and branch-selection variables.

        Parameters:
        ----------
        formula (WSTLFormula): eventually formula
        z (grb.Variable): satisfaction variable for the formula
        rho (grb.Variable): robustness variable for the formula
        t (int): time at which the formula is evaluated
        '''
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
        '''Adds constraints for a weighted until formula.

        Parameters:
        ----------
        formula (WSTLFormula): until formula
        z (grb.Variable): satisfaction variable for the formula
        rho (grb.Variable): robustness variable for the formula
        t (int): time at which the formula is evaluated

        Raises:
        ----------
        NotImplementedError: Until constraints are not implemented.
        '''
        #TODO: create milp constraints for until operator
        assert formula.op == Operation.UNTIL

        raise NotImplementedError 
