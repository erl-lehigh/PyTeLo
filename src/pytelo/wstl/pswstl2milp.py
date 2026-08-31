'''
 Copyright (C) 2018-2023,
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab (ERL), Lehigh University
 @author: Cristian Ioan Vasile

 Copyright (c) 2023, Explainable Robotics Lab (ERL), Lehigh University
 @author: Gustavo A. Cardona

 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
 See license.txt file for license information.
'''
import gurobipy as grb

from stl import Operation, RelOperation

class pswstl2milp(object):
    '''Tools to generate an MILP for partial satisfaction of a weighted STL
    formula.

    Instance Attributes
    ----------
    formula (WSTLFormula): AST root node
    model (grb.Model): MILP model with constraints consistent with the formula
    variables (dict): Variables tracking satisfaction of formula subtrees and
                      signal states
    M (int): Large constant used to enforce predicate constraints
    robust (bool): Whether inner robustness optimization is enabled
    ranges (dict): Bounds for signal variables
    vtypes (dict): Gurobi variable types for signal variables
    '''
    def __init__(self, formula, ranges=None, vtypes=None, model=None, 
                robust=False):
        '''Construct a weighted STL partial-satisfaction converter.
        
        Parameters:
        ----------
        formula (WSTLFormula): root node of the desired weighted STL formula
        ranges (dict): optional mapping of variable names to (min, max) bounds;
                       defaults to (-10, 10) for each formula variable
        vtypes (dict): optional mapping of variable names to Gurobi variable
                       types; defaults to continuous variables
        model (grb.Model): optional existing Gurobi model to extend
        robust (bool): default=False - whether robustness optimization is
                       enabled for the inner linear program
        '''
        self.formula = formula
        self.robust = robust
        self.M = 1000
        self.ranges = ranges
        if ranges is None:
            self.ranges = {v: (-10, 10) for v in self.formula.variables()}

        assert set(self.formula.variables()) <= set(self.ranges)

        self.vtypes = vtypes
        if vtypes is None:
            self.vtypes = {v: grb.GRB.CONTINUOUS for v in self.ranges}

        self.model = model
        if model is None:
            self.model = grb.Model('pswSTL formula: {}'.format(formula))
            
        self.variables = dict()
        self.__milp_call = {
            Operation.PRED : self.predicate,
            Operation.AND : self.conjunction,
            Operation.OR : self.disjunction,
            Operation.EVENT : self.eventually,
            Operation.ALWAYS : self.globally,
        }
        
    def translate(self): # translate all the formula to milp at time 0
        '''Generates MILP constraints from self.formula at time t=0.

        Returns:
        ----------
        z (grb.Variable): Variable indicating the weighted degree of
                          satisfaction of the root formula.
        '''
        z = self.to_milp(self.formula)
        return z

    def to_milp(self, formula, t=0):
        '''Generates MILP constraints for a weighted STL formula or subformula.

        Parameters:
        ----------
        formula (WSTLFormula): formula or subformula to encode
        t (int): default=0 - time at which the formula is evaluated

        Returns:
        ----------
        z (grb.Variable): Variable indicating the weighted degree of
                          satisfaction of the formula.
        '''
        z, added = self.add_formula_variable(formula, t)
        if added:
            self.__milp_call[formula.op](formula, z, t) 
        return z

    def add_formula_variable(self, formula, t): 
        '''Adds a satisfaction variable for a weighted formula at time t.

        Returns:
        ----------
        z (grb.Variable): Variable tracking the formula satisfaction.
        added (bool): True if a variable was newly created, otherwise False.
        '''
        if formula not in self.variables:              
            self.variables[formula] = dict()
        if t not in self.variables[formula]:            # updates t 
            opname = Operation.getString(formula.op)
            identifier = formula.identifier()
            name = 'z_{}_{}_{}'.format(opname, identifier, t)
            if formula.op is Operation.PRED:
                variable = self.model.addVar(vtype=grb.GRB.BINARY, name=name)
            else:
                variable = self.model.addVar(vtype=grb.GRB.CONTINUOUS,
                                             name=name, lb=0, ub=1)
            self.variables[formula][t] = variable
            self.model.update()
            return variable, True
        return self.variables[formula][t], False
    
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

    def predicate(self, pred, z, t):
        '''Adds predicate constraints to the model.

        Parameters:
        ----------
        pred (WSTLFormula): predicate formula
        z (grb.Variable): satisfaction variable for the predicate
        t (int): time at which the predicate is evaluated
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

    def conjunction(self, formula, z, t):
        '''Adds weighted conjunction constraints and recursively encodes children.

        Parameters:
        ----------
        formula (WSTLFormula): conjunction formula
        z (grb.Variable): satisfaction variable for the conjunction
        t (int): time at which the conjunction is evaluated
        '''
        assert formula.op is Operation.AND
        z_children = [self.to_milp(f, t) for f in formula.children]
        weights = []
        vars_children = []
        max_weights= max([formula.weight(k) for k in range(len(z_children))])
        for k, (z_child) in enumerate(z_children):
            weight = formula.weight(k)/max_weights
            weights.append(weight)
            vars_children.append(z_child * weight)
        self.model.addConstr(z == sum(vars_children) / sum(weights))
        
    def disjunction(self, formula, z, t):
        '''Adds weighted disjunction constraints and recursively encodes children.

        Parameters:
        ----------
        formula (WSTLFormula): disjunction formula
        z (grb.Variable): satisfaction variable for the disjunction
        t (int): time at which the disjunction is evaluated
        '''
        assert formula.op is Operation.OR
        z_children = [self.to_milp(f, t) for f in formula.children]
        vars_children = []
        max_weights= max([formula.weight(k) for k in range(len(z_children))])
        for k, (z_child) in enumerate(z_children):
            weight = formula.weight(k)
            name = 'y_dist_{}'.format(k) 
            z_aux = self.model.addVar(vtype=grb.GRB.CONTINUOUS,
                                             name=name, lb=0, ub=1)
            self.model.addConstr(z_aux == z_child*weight/max_weights)
            vars_children.append(z_aux)

        self.model.addConstr(z == grb.max_(vars_children))

    def eventually(self, formula, z, t):
        '''Adds weighted eventually constraints over the formula interval.

        Parameters:
        ----------
        formula (WSTLFormula): eventually formula
        z (grb.Variable): satisfaction variable for the formula
        t (int): time at which the formula is evaluated
        '''
        assert formula.op is Operation.EVENT
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau) for tau in range(a, b+1)]
        zip_children = zip(range(a, b+1), z_children)
        vars_children = []
        max_weights= max([formula.weight(tau) for tau in range(a, b+1)])
        for tau, z_child in zip_children:
            weight = formula.weight(tau)
            name = 'y_event_{}'.format(tau) 
            z_aux = self.model.addVar(vtype=grb.GRB.CONTINUOUS,
                                             name=name, lb=0, ub=1)
            self.model.addConstr(z_aux == z_child*weight/max_weights)
            vars_children.append(z_aux)
        self.model.addConstr(z == grb.max_(vars_children))

    def globally(self, formula, z, t):
        '''Adds weighted globally constraints over the formula interval.

        Parameters:
        ----------
        formula (WSTLFormula): globally formula
        z (grb.Variable): satisfaction variable for the formula
        t (int): time at which the formula is evaluated
        '''
        assert formula.op is Operation.ALWAYS
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau) for tau in range(a, b+1)]
        zip_children = zip(range(a, b+1), z_children)
        weights = []
        vars_children = []
        max_weights= max([formula.weight(k) for k in range(len(z_children))])
        for tau, z_child in zip_children:
            weight = formula.weight(tau)
            weights.append(weight)
            vars_children.append(z_child * weight/max_weights)

        self.model.addConstr(z == sum(vars_children) / sum(weights))  

    def pstl2lp(self, formula, t=0):
        '''Generates a linear program for the robustness of selected predicates.

        Parameters:
        ----------
        formula (WSTLFormula): root node of the weighted STL formula
        t (int): default=0 - time at which the formula is evaluated

        Returns:
        ----------
        lp (grb.Model): The Gurobi linear program.
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
        
        lp.optimize()
        obj = lp.getObjective()
        return lp
        
    def predicate_pairs(self, formula, t=0):
        '''Finds predicate-time pairs selected by the optimized formula.

        Parameters:
        ----------
        formula (WSTLFormula): formula for which to find predicate pairs
        t (int): default=0 - time at which to evaluate the formula

        Returns:
        ----------
        ret (set): Set of predicate-time pairs satisfying as much of the
                   weighted formula as possible.
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
        Performs hierarchical lexicographic optimization from the root node to
        the predicate leaves.

        Parameters:
        ----------
        model_name (str): default='model_test.lp' - file name for Gurobi model output
        optimize (bool): default=True - whether to optimize immediately; if falsy, 
                                        only the objective functions are generated

        Returns:
        ----------
        depth (int): Depth of the formula AST.
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
    
    def ldf(self, model_name='model_test.lp', optimize=True, spec_bound=20):
        '''
        Performs lowest-depth-first optimization by penalizing satisfaction
        according to AST depth.

        Parameters:
        ----------
        model_name (str): default='model_test.lp' - file name for Gurobi model output
        optimize (bool): default=True - whether to optimize immediately; if falsy, 
                                        only the objective function is generated
        spec_bound (int or float): default=20 - base used to scale the depth penalties
        ''' 
        reward = sum([term * spec_bound**(-d) for d, term in self.objectives.items()])
        self.model.setObjective(reward, grb.GRB.MAXIMIZE)
        self.model.update()

        if optimize is True:
            self.model.optimize()
            self.model.write(model_name)

    def wln(self, z, model_name='model_test.lp', optimize=True):
        '''
        Performs weighted-largest-number optimization using the root variable.

        Parameters:
        ----------
        z (grb.Variable): Decision variable capturing root-node satisfaction
        model_name (str): default='model_test.lp' - file name for Gurobi model output
        optimize (bool): default=True - whether to optimize immediately; if falsy, 
                                        only the objective function is generated
        '''
        self.model.setObjective(z, grb.GRB.MAXIMIZE)
        self.model.update()

        if optimize is True:
            self.model.optimize()
            self.model.write(model_name)
            
    def satis_score(self, formula, t=0):
        '''
        Computes the unweighted satisfaction score of an optimized solution.

        Parameters:
        ----------
        formula (WSTLFormula): formula whose score is computed
        t (int): default=0 - time at which to evaluate the formula

        Note:
        The MILP encoding captures user preferences through weights, but this
        score intentionally reports the ordinary satisfaction percentage. For
        disjunction and eventually operators, the two values are not
        equivalent.
        '''
        if formula.op == Operation.PRED:
            return self.variables[formula][t].x
        
        if formula.op == Operation.AND:
            children_score = [self.satis_score(f, t) for f in formula.children]
            return sum(children_score) / len(formula.children)
        
        if formula.op == Operation.OR:
            children_score = [self.satis_score(f, t) for f in formula.children]
            return max(children_score)
        
        if formula.op == Operation.ALWAYS:
            f = formula.child
            interval = range(int(formula.low)+t, int(formula.high+1)+t)
            children_score = [self.satis_score(f,t) for t in interval]
            return sum(children_score) / len(interval)
        
        if formula.op == Operation.EVENT:
            f = formula.child
            interval = range(int(formula.low)+t, int(formula.high+1)+t)
            children_score = [self.satis_score(f,t) for t in interval]
            return  max(children_score)