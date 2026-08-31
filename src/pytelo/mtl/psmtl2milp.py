'''
 Copyright (c) 2023, Explainable Robotics Lab (ERL), Lehigh University
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile

 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
 See license.txt file for license information.
'''

import gurobipy as grb

from pytelo.mtl import Operation


class psmtl2milp(object):
    '''
    Tools to generate an MILP to assessing partial satisfaction from the AST of an MTL formula.
    Provides special optimization functions which maximize the number of satisfying subformulae even
    if there are no satisfying trajectories for the full specification.
    
    Instance Attributes
    ----------
    formula (MTLFormula): AST root node
    model (grb.Model): MILP model with constraints consistent with the MTL formula.
    variables (dict): All variables, identified by name, tracking the degree of satisfaction for each
                      subformula within the MILP.
    variables_z (dict): All variables, identified by name, tracking the discrete satisfaction or violation
                        of each subformula within the MILP.
    objectives (dict): all expressions, organized by AST depth from the root node, describing the number
                       of satisfying and violating subformulae, used for some of the optimization options.
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
        self.variables_z = dict()
        self.objectives = dict()

        self.__milp_call = {
            Operation.PRED : self.predicate,
            Operation.AND : self.conjunction,
            Operation.OR : self.disjunction,
            Operation.EVENT : self.eventually,
            Operation.ALWAYS : self.globally,
            Operation.UNTIL : self.until
        }

    def translate(self): 
        '''Generates MILP constraints on self.model from the MTL formula. Note: this always constructs the
        constraints with respect to satisfaction at t=0.

        Returns:
        ----------
        z (grb.Variable): The gurobi variable indicating the degree of satisfaction or violation of the MTL
                          formula, measured from 0 to 1. A value of 1 after optimization indicates the entire
                          formula was satisfiable, 0 indicates that no subformulae were satisfiable within 
                          the entire specification.
        '''
        z = self.to_milp(self.formula)
        return z

    def to_milp(self, formula, t=0, depth=0, z_ancestors=None):
        '''Generates the MILP constraints and optimization objectives from an MTL formula.
                
        Parameters:
        ----------
        formula (MTLFormula): Root node of AST generated from the desired MTL formula
        t (int): default=0 - The time at which the formula should be evaluated.
        depth (int): default=0 - The depth from the true root of the AST. Used for recursion to order 
                                 optimization objective priorities.
        z_ancestors (list): default=None - List of the variables indicating discrete satisfaction or violation
                                           of all parent AST nodes. Used for recursion.

        Returns:
        ----------
        z (grb.Variable): The gurobi variable constrained to indicate the degree of satisfaction or violation 
                          for the formula or subformula.
        '''
        if depth not in self.objectives:
            self.objectives[depth] = 0
        if z_ancestors is None:
            z_ancestors = []
        z, added, z_var = self.add_formula_variable(formula, t, depth, 
                                                    z_ancestors)
        if added:
            self.__milp_call[formula.op](formula, z, t, depth, z_ancestors 
                                         + [z_var])
        return z

    def add_formula_variable(self, formula, t, depth, z_ancestors): 
        '''Adds variables to self.model to track the satisfaction of violation of the parent node of passed
        MTL AST at time t. Creates variables tracking both discrete satisfaction and degree of satisfaction.
        
        Parameters:
        ----------
        formula (MTLFormula): Root node of AST for desired formula (or subformula)
        t (int): time at which the formula (or subformula)'s satisfaction must be evaluated
        depth (int): The depth from the true root of the AST.
        z_ancestors (list): List of the variables indicating discrete satisfaction of all parent AST nodes.
        
        Returns:
        ----------
        z (grb.Variable): A gurobi variable to indicate the degree of satisfaction or violation of the formula 
                          (or subformula) at time t. Continuous from 0 to 1 except for predicate operations 
                          (in which case it is discrete).
        added (bool): True if a variable for this (or identical) formula did not previously exist in self.model. 
                        False otherwise.
        z_var (grb.Variable): A gurobi variable to indicate the discrete satisfaction or violation of the 
                              formula or subformula.
        '''
        if formula not in self.variables:               
            self.variables[formula] = dict()
            self.variables_z[formula] = dict()
    
        if t not in self.variables[formula]:            
            opname = Operation.getString(formula.op)
            identifier = formula.identifier()
            name = '{}_{}_{}'.format(opname, identifier, t)
    
            if formula.op == Operation.PRED:
                variable = self.model.addVar(vtype=grb.GRB.BINARY, name=name)
    
            else:
                variable = self.model.addVar(vtype=grb.GRB.CONTINUOUS,
                                             name=name, lb=0, ub=1)
            variable_z = self.model.addVar(vtype=grb.GRB.BINARY,
                                            name=name + '_zi')
            self.objectives[depth] += variable_z
            self.model.update()
            self.model.addConstr(variable_z <= variable)
    
            for variable_z_ancestor in z_ancestors:
                self.model.addConstr(variable_z <= 1 - variable_z_ancestor)

            self.variables_z[formula][t] = variable_z
            self.variables[formula][t] = variable
            self.model.update()

            return variable, True, variable_z
        return self.variables[formula][t], False, self.variables_z[formula][t]
    
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

    def predicate(self, pred, z, t, depth, z_ancestors):
        '''Adds appropriate reference data for a subformula that is a predicate only.
                
        Parameters:
        ----------
        pred (MTLFormula): AST formula root (must be a predicate).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate satisfaction.
        depth (int): Not used.
        z_ancestors (list): Not used.
        '''
        assert pred.op == Operation.PRED
        self.add_state(pred.variable, t, z)
        

    def conjunction(self, formula, z, t, depth, z_ancestors):
        '''Adds constraints for a subformula with conjunction as its root operation. 
        Recursively constructs child constraints.
        
        Parameters:
        ----------
        formula (MTLFormula): AST formula root (must be a conjunction operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate the degree of satisfaction.
        depth (int): The depth from the true root of the AST.
        z_ancestors (list): List of the variables indicating discrete satisfaction of all parent AST nodes.
        '''
        assert formula.op == Operation.AND
        z_children = [self.to_milp(f, t, depth+1, z_ancestors) 
                      for f in formula.children]
        self.model.addConstr(z == sum(z_children) / len(z_children) )

    def disjunction(self, formula, z, t, depth, z_ancestors):
        '''Adds constraints for a subformula with disjunction as its root operation. 
        Recursively constructs child constraints.
        
        Parameters:
        ----------
        formula (MTLFormula): AST formula root (must be a disjunction operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate the degree of satisfaction.
        depth (int): The depth from the true root of the AST.
        z_ancestors (list): List of the variables indicating discrete satisfaction of all parent AST nodes.
        '''
        assert formula.op == Operation.OR
        z_children = [self.to_milp(f, t, depth+1, z_ancestors) 
                      for f in formula.children]
        self.model.addConstr(z == grb.max_(z_children))

    def eventually(self, formula, z, t, depth, z_ancestors):
        '''Adds constraints for a subformula with eventually as its root operation. 
        Recursively constructs child constraints.
        
        Parameters:
        ----------
        formula (MTLFormula): AST formula root (must be an eventually operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate the degree of satisfaction.
        depth (int): The depth from the true root of the AST.
        z_ancestors (list): List of the variables indicating discrete satisfaction of all parent AST nodes.
        '''
        assert formula.op == Operation.EVENT
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau, depth+1, z_ancestors) 
                      for tau in range(a, b+1)]
        self.model.addConstr(z == grb.max_(z_children))

    def globally(self, formula, z, t, depth, z_ancestors):
        '''Adds constraints for a subformula with always as its root operation. 
        Recursively constructs child constraints.
        
        Parameters:
        ----------
        formula (MTLFormula): AST formula root (must be an always operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate the degree of satisfaction.
        depth (int): The depth from the true root of the AST.
        z_ancestors (list): List of the variables indicating discrete satisfaction of all parent AST nodes.
        '''
        assert formula.op == Operation.ALWAYS
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau, depth+1, z_ancestors) 
                      for tau in range(a, b+1)]
        self.model.addConstr(z == sum(z_children) / (b-a+1))    

    def until(self, formula, z, t, depth, z_ancestors):
        '''Adds constraints for a subformula with until as its root operation. 
        Recursively constructs child constraints.
        
        Parameters:
        ----------
        formula (MTLFormula): AST formula root (must be an until operation).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate the degree of satisfaction.
        depth (int): The depth from the true root of the AST.
        z_ancestors (list): List of the variables indicating discrete satisfaction of all parent AST nodes.
        '''
        a, b = int(formula.low), int(formula.high)
        z_children = []
        for t_ in range(a,b+1):
            z_children_left =  [self.to_milp(formula.left, t+t__, depth+1, 
                                             z_ancestors) 
                                             for t__ in range(0,t_)]
            z_children_right = [self.to_milp(formula.right, t+t_, depth+1, 
                                             z_ancestors)]
            z_children.append(z_children_right + sum(z_children_left))

        self.model.addConstr(z == grb.max_(z_children))

    def hierarchical(self, model_name='model_test.lp', optimize=True): 
        '''
        Performs a hierarchical optimization formulation 
        (lexicografical) from root node all the way to the leaves (predicates).
        
        Parameters:
        ----------
        model_name (str): default='model_test.lp' - File name to generate Gurobi information about the 
                                                    optimization problem.
        optimize (bool): default=True - If set to a truthy value, optimization is performed. If falsy,
                                        optimization problem is generated to be performed later using
                                        model.optimize().
        
        Returns:
        ----------
        depth: The depth of the AST (and consequentially the number of objectives optimized).
        '''
        max_depth = max(self.objectives)
        for d in range(max_depth+1):
            self.model.setObjectiveN(-self.objectives[d], d, 
                                     priority=max_depth-d)
            self.model.update()

        if optimize is True:
            self.model.optimize()
            self.model.write(model_name)
        return d
    
    def ldf(self, model_name='model_test.lp', optimize=True): 
        '''
        This method computes a lowest depth first optimization formulation without using gurobi's 
        multi-objective optimization features by penalizing subformulae satisfaction scores based on 
        the depth of the relevant AST nodes.

        Parameters:
        ----------
        model_name (str): default='model_test.lp' - File name to generate Gurobi information about the 
                                                    optimization problem.
        optimize (bool): default=True - If set to a truthy value, optimization is performed. If falsy,
                                        optimization problem is generated to be performed later using
                                        model.optimize().
        '''
        M2 = 20 # FIXME: computed based on formula size
        reward = sum([term * M2**(-d) for d, term in self.objectives.items()])
        self.model.setObjective(reward, grb.GRB.MAXIMIZE)
        self.model.update()
        
        if optimize is True:
            self.model.optimize()
            self.model.write(model_name)

    def wln(self, z, model_name='model_test.lp', optimize=True):
        '''
        This method computes a Weighted Largest Number optimization formulation. This still weights
        the satisfaction priority by depth, but not so strongly as to guarantee the lowest-depth
        subformulae are always satisfied. Typically results in faster performance.
    
        Parameters:
        ----------
        z (grb.Variable): The gurobi variable indicating degree of satisfaction for the root node of 
                          the AST.
        model_name (str): default='model_test.lp' - File name to generate Gurobi information about the 
                                                    optimization problem.
        optimize (bool): default=True - If set to a truthy value, optimization is performed. If falsy,
                                        optimization problem is generated to be performed later using
                                        model.optimize().
        '''
        self.model.setObjective(z, grb.GRB.MAXIMIZE)
        self.model.update()

        if optimize is True:
            self.model.optimize()
            self.model.write(model_name)