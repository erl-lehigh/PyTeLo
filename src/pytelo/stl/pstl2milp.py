'''
 Copyright (c) 2022, Explainable Robotics Lab (ERL), Lehigh University
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile

 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
 See license.txt file for license information.
'''
import gurobipy as grb
from pytelo.stl import Operation, RelOperation, STLFormula

class pstl2milp(object):
    '''
    Tools to generate an MILP to assessing partial satisfaction from the AST of an STL formula.
    Provides special optimization functions which maximize the number of satisfying subformulae even
    if there are no satisfying trajectories for the full specification.
    
    Instance Attributes
    ----------
    formula (STLFormula): AST root node
    model (grb.Model): MILP model with constraints consistent with the STL formula.
    variables (dict): All variables, identified by name, tracking the degree of satisfaction for each
                      subformula within the MILP.
    variables_z (dict): All variables, identified by name, tracking the discrete satisfaction or violation
                        of each subformula within the MILP.
    objectives (dict): all expressions, organized by AST depth from the root node, describing the number
                       of satisfying and violating subformulae, used for some of the optimization options.
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
        self.robust = robust
        self.M = 1000
        self.ranges = ranges
        assert set(self.formula.variables()) <= set(self.ranges)

        self.vtypes = vtypes
        if vtypes is None:
            self.vtypes = {v: grb.GRB.CONTINUOUS for v in self.ranges}

        self.model = model
        if model is None:
            self.model = grb.Model('STL formula: {}'.format(formula))

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
        '''Generates MILP constraints on self.model from the STL formula stored in self.formula. Note: this always
        constructs the constraints with respect to satisfaction at t=0.

        Returns:
        ----------
        z (grb.Variable): The gurobi variable indicating the degree of satisfaction or violation of the STL
                            formula, measured from 0 to 1. A value of 1 after optimization indicates the entire
                            formula was satisfiable, 0 indicates that no subformulae were satisfiable within 
                            the entire specification.
        '''
        z = self.to_milp(self.formula)
        return z

    def to_milp(self, formula, t=0, depth=0, z_ancestors=None):
        '''Generates the MILP constraints and optimization objectives from an STL formula.
        
        Parameters:
        ----------
        formula (STLFormula): Root node of AST generated from the desired STL formula.
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
            self.__milp_call[formula.op](formula, z, t, depth, z_ancestors + 
                                         [z_var])
        return z

    def add_formula_variable(self, formula, t, depth, z_ancestors): 
        '''Adds variables to self.model to track the satisfaction or violation of the parent node of passed
        STL AST at time t. Creates variables tracking both discrete satisfaction and degree of satisfaction.
        
        Parameters:
        ----------
        formula (STLFormula): Root node of AST for desired formula (or subformula).
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

    def predicate(self, pred, z, t, depth, z_ancestors):
        '''Adds appropriate reference data for a subformula that is a predicate only. Creates state variables
        for the predicate signal variable at time t if needed. Adds model constraints to ensure that the z
        variable provided is consistent with the predicate's satisfaction or violation at time t.
        
        Parameters:
        ----------
        pred (STLFormula): AST formula root (must be a predicate).
        z (grb.Variable): Gurobi variable created to indicate satisfaction of this subformula.
        t (int): The time at which the variable z is meant to evaluate satisfaction.
        depth (int): Not used.
        z_ancestors (list): Not used.
        '''
        assert pred.op == Operation.PRED
        v = self.add_state(pred.variable, t)
        if pred.relation in (RelOperation.GE, RelOperation.GT):  
            self.model.addConstr(v  - self.M * z <= pred.threshold)         
            self.model.addConstr(v + self.M * (1 - z) >= pred.threshold)
        elif pred.relation in (RelOperation.LE, RelOperation.LT):
            self.model.addConstr(v + self.M * z >= pred.threshold)          
            self.model.addConstr(v - self.M * (1 - z) <= pred.threshold)       
        else:
            raise NotImplementedError

    def conjunction(self, formula, z, t, depth, z_ancestors):
        '''Adds constraints for a subformula with conjunction as its root operation. 
        Recursively constructs child constraints.
        
        Parameters:
        ----------
        formula (STLFormula): AST formula root (must be a conjunction operation).
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
        formula (STLFormula): AST formula root (must be a disjunction operation).
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
        formula (STLFormula): AST formula root (must be an eventually operation).
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
        formula (STLFormula): AST formula root (must be a globally operation).
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
        formula (STLFormula): AST formula root (must be an until operation).
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

    def pstl2lp(self, formula, t=0, optimize=True):
        '''Generates a linear programming to maximize the robustness of satisfiable subformulae as an inner
        optimization problem. This is used to find the most robust trajectory for a given STL formula.

        Parameters:
        ----------
        formula (STLFormula): Root node of AST generated from the desired STL formula
        t (int): default=0 - The time at which the formula should be evaluated.
        optimize (bool): default=True - Whether to immediately optimize the resulting linear program.

        Returns:
        ----------
        lp (grb.Model): The gurobi model for the linear program.
        '''
        lp = grb.Model("LP")
        if self.robust and 'rho' not in self.ranges:
            self.ranges['rho'] = (-grb.GRB.INFINITY, self.M - 1)
        if self.robust:
            rho_min, rho_max = self.ranges['rho']
            self.rho = lp.addVar(vtype=grb.GRB.CONTINUOUS, name='rho',
                                        lb=rho_min, ub=rho_max, obj=-1)        
        else:
            self.rho = 0
        
        formulae = self.predicate_pairs(formula, t)
        self.lpvariable = dict()

        for phi in formulae:
            self.lpvariable[phi[0]] = dict()
            name = '{}_{}'.format(phi[0], phi[1])
            var = lp.addVar(vtype=grb.GRB.CONTINUOUS, lb=-10, ub=10, name=name)
            self.lpvariable[phi[0]][phi[1]] = var

            if phi[0].relation in (RelOperation.GE, RelOperation.GT):
                lp.addConstr(var >= phi[0].threshold + self.rho)

            if phi[0].relation in (RelOperation.LE, RelOperation.LT):
                lp.addConstr(var <= phi[0].threshold - self.rho)    
            lp.update()
        
        if optimize is True:
            lp.optimize()

        return lp
        
    def predicate_pairs(self, formula, t=0):
        '''Finds all predicate pairs that require satisfaction at time t after the MILP for the outer
        optimization has been solved.

        Note: This method will raise an error if called before the MILP for the outer optimization has been solved.

        Parameters:
        ----------
        formula (STLFormula): The STL formula for which to find predicate pairs
        t (int): default = 0 - The time step at which to evaluate the formula

        Returns:
        -------
        ret (set): A set of predicate-time pairs (tuple) that satisfy as much of the formula as possible at time t.
        '''
       
        ret = set()

        if formula.op == Operation.PRED:
            if self.variables[formula][t].x == 1:
                ret = {(formula, t)}
            else:
                ret = {}

        elif formula.op == Operation.AND:
            for f in formula.children:
                ret = ret.union(self.predicate_pairs(f, t))

        elif formula.op == Operation.OR:
            for f in formula.children:
                if self.variables[f][t].x == 1:
                    ret = ret.union(self.predicate_pairs(f, t))
                    break

        elif formula.op == Operation.ALWAYS:
            f = formula.child
            interval = range(int(formula.low), int(formula.high+1))
            for t in interval:
                ret = ret.union(self.predicate_pairs(f, t))

        elif formula.op == Operation.EVENT:
            f = formula.child
            interval = range (int(formula.low), int(formula.high+1))
            for t in interval:
                if self.variables[f][t].x == 1:
                    ret = ret.union(self.predicate_pairs(f, t))
                    break

        return ret


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
        M2 = 30 # FIXME: computed based on formula size
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