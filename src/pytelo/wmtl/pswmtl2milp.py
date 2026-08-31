'''
 Copyright (c) 2023, Explainable Robotics Lab (ERL), Lehigh University
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile

 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
 See license.txt file for license information.
'''
import gurobipy as grb
from pytelo.wmtl import Operation, MTLFormula

class pswmtl2milp(object):
    '''Tools to generate an MILP for partial satisfaction of a weighted MTL
    formula.

    Instance Attributes
    ----------
    formula (WMTLFormula): AST root node
    model (grb.Model): MILP model with constraints consistent with the formula
    variables (dict): Variables tracking satisfaction of formula subtrees and
                      signal states
    '''
    def __init__(self, formula, model=None):
        '''Construct a weighted MTL partial-satisfaction optimization problem.

        Parameters:
        ----------
        formula (WMTLFormula): root node of the desired weighted MTL formula
        model (grb.Model): default=None - existing Gurobi model to extend; if
                                          None, a new model is created
        '''
        self.formula = formula

        self.model = model
        if model is None:
            self.model = grb.Model('pwMTL formula: {}'.format(formula))
            
        self.variables = dict()

        self.__milp_call = {
            Operation.PRED : self.predicate,
            Operation.AND : self.conjunction,
            Operation.OR : self.disjunction,
            Operation.EVENT : self.eventually,
            Operation.ALWAYS : self.globally,
            # Operation.UNTIL : self.until
        }
        
    def translate(self): 
        '''Generates MILP constraints from self.formula at time t=0.

        Returns:
        ----------
        z (grb.Variable): Variable indicating the weighted degree of
                          satisfaction of the root formula.
        '''
        z = self.to_milp(self.formula)
        return z

    def to_milp(self, formula, t=0):
        '''Generates MILP constraints for a weighted MTL formula or subformula.

        Parameters:
        ----------
        formula (WMTLFormula): formula or subformula to encode
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
        if t not in self.variables[formula]:            
            opname = Operation.getString(formula.op)
            identifier = formula.identifier()
            name = 'z_{}_{}_{}'.format(opname, identifier, t)
            if formula.op == Operation.PRED:
                variable = self.model.addVar(vtype=grb.GRB.BINARY, name=name)
            else:
                variable = self.model.addVar(vtype=grb.GRB.CONTINUOUS,
                                             name=name, lb=0, ub=1)
            self.variables[formula][t] = variable
            self.model.update()
            return variable, True
        return self.variables[formula][t], False
    
    def add_state(self, state, t, z):
        '''Associates a signal state with its satisfaction variable.

        Parameters:
        ----------
        state (str): signal variable name
        t (int): time at which the state is used
        z (grb.Variable): variable linked to the state satisfaction

        Returns:
        ----------
        z (grb.Variable): The stored state variable.
        '''
        if state not in self.variables:
            self.variables[state] = dict()

        if t not in self.variables[state]:
            self.variables[state][t] = z
            self.model.update()
        return self.variables[state][t]

    def predicate(self, pred, z, t):
        '''Adds a weighted predicate to the model.

        Parameters:
        ----------
        pred (WMTLFormula): predicate formula
        z (grb.Variable): satisfaction variable for the predicate
        t (int): time at which the predicate is evaluated
        '''
        assert pred.op == Operation.PRED
        self.add_state(pred.variable, t, z)
   
    def conjunction(self, formula, z, t):
        '''Adds weighted conjunction constraints and recursively encodes children.

        Parameters:
        ----------
        formula (WMTLFormula): conjunction formula
        z (grb.Variable): satisfaction variable for the conjunction
        t (int): time at which the conjunction is evaluated
        '''
        assert formula.op == Operation.AND
        z_children = [self.to_milp(f, t) for f in formula.children]
        weights = []
        vars_children = []
        max_weights = max([formula.weight(k) for k in range(len(z_children))])
        for k, (z_child) in enumerate(z_children):
            weight = formula.weight(k)/max_weights
            weights.append(weight)
            vars_children.append(z_child * weight)
        self.model.addConstr(z == sum(vars_children) / sum(weights))
         
    def disjunction(self, formula, z, t):
        '''Adds weighted disjunction constraints and recursively encodes children.

        Parameters:
        ----------
        formula (WMTLFormula): disjunction formula
        z (grb.Variable): satisfaction variable for the disjunction
        t (int): time at which the disjunction is evaluated
        '''
        assert formula.op == Operation.OR
        z_children = [self.to_milp(f, t) for f in formula.children]
        vars_children = []
        max_weights= max([formula.weight(k) for k in range(len(z_children))])
        for k, (z_child) in enumerate(z_children):
            weight = formula.weight(k)
            name = 'z_aux_dist_{}_{}'.format(weight,k) 
            z_aux = self.model.addVar(vtype=grb.GRB.CONTINUOUS,
                                             name=name, lb=0, ub=1)
            self.model.addConstr(z_aux == z_child*weight/max_weights)
            vars_children.append(z_aux)                  
        self.model.addConstr(z == grb.max_(vars_children))

    def eventually(self, formula, z, t):
        '''Adds weighted eventually constraints over the formula interval.

        Parameters:
        ----------
        formula (WMTLFormula): eventually formula
        z (grb.Variable): satisfaction variable for the formula
        t (int): time at which the formula is evaluated
        '''
        assert formula.op == Operation.EVENT
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau) for tau in range(a, b+1)]
        zip_children = zip(range(a, b+1), z_children)
        vars_children = []
        max_weights= max([formula.weight(tau) for tau in range(a, b+1)])

        for tau, z_child in zip_children:
            weight = formula.weight(tau)
            name = 'z_aux_event_{}_{}'.format(weight, tau) 
            z_aux = self.model.addVar(vtype=grb.GRB.CONTINUOUS,
                                             name=name, lb=0, ub=1)
            self.model.addConstr(z_aux == z_child*weight/max_weights)
            vars_children.append(z_aux)                                                 
        self.model.addConstr(z == grb.max_(vars_children))

    def globally(self, formula, z, t):
        '''Adds weighted globally constraints over the formula interval.

        Parameters:
        ----------
        formula (WMTLFormula): globally formula
        z (grb.Variable): satisfaction variable for the formula
        t (int): time at which the formula is evaluated
        '''
        assert formula.op == Operation.ALWAYS
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
        
    def predicate_pairs(self, formula, t=0):
        '''Finds predicate-time pairs selected by the optimized formula.

        Parameters:
        ----------
        formula (WMTLFormula): formula for which to find predicate pairs
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
            # ret = [set.union(self.predicate_pairs(f, t)) for f in formula.children]

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
            # ret = [set.union(self.predicate_pairs(f, t)) for t in interval]

        elif formula.op == Operation.EVENT:
            f = formula.child
            interval = range (int(formula.low), int(formula.high+1))
            for t in interval:
                if self.variables[f][t].x == 1:
                    ret = ret.union(self.predicate_pairs(f, t))
                    break

        return ret

    def hierarchical(self, model_name='model_test.lp', optimize=True): 
        '''Performs hierarchical lexicographic optimization from the root node to
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
    
    def ldf(self, model_name='model_test.lp', optimize=True): 
        '''Performs lowest-depth-first optimization by penalizing satisfaction
        according to AST depth.

        Parameters:
        ----------
        model_name (str): default='model_test.lp' - file name for Gurobi model output
        optimize (bool): default=True - whether to optimize immediately; if falsy, 
                                        only the objective function is generated
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
        formula (WMTLFormula): formula whose score is computed
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