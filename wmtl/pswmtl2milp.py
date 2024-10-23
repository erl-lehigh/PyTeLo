'''
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
'''
import gurobipy as grb
from wmtl import Operation, MTLFormula

class pswmtl2milp(object):
    '''Translate an wMTL formula to an MILP.'''
    def __init__(self, formula, model=None):
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
        
    def translate(self): # translate all the formula to milp at time 0
        '''Translates the wMTL formula to MILP from time 0.'''
        z = self.to_milp(self.formula)
        return z

    def to_milp(self, formula, t=0):
        '''Generates the MILP from the wMTL formula.'''
        z, added = self.add_formula_variable(formula, t)
        if added:
            self.__milp_call[formula.op](formula, z, t) 
        return z

    def add_formula_variable(self, formula, t): 
        '''Adds a variable for the `formula` at time `t`.'''
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
        '''Adds the `state` at time `t` as a variable.'''
        if state not in self.variables:
            self.variables[state] = dict()

        if t not in self.variables[state]:
            self.variables[state][t] = z
            self.model.update()
        return self.variables[state][t]

    def predicate(self, pred, z, t):
        '''Adds a predicate to the model.'''
        assert pred.op == Operation.PRED
        self.add_state(pred.variable, t, z)
   
    def conjunction(self, formula, z, t):
        '''Adds a conjunction to the model.'''
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
        '''Adds a disjunction to the model.'''
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
        '''Adds an eventually to the model.'''
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
        '''Adds a globally to the model.'''
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
        '''It receives formula and time step and returns a set of the subformulae
             that needs to be satisfied at the specific time. Note that Disjunction
             and eventually are special cases'''
       
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
        '''
        This method computes a hierarchical optimization formulation 
        (lexicografical) from root node all the way to the leaves (predicates)
        Input:
            - model_name is a file name to generate Gurobi information about 
              the optimization problem
            - optimize is a flag type variable which is True by default performing
              the optimization of the problem, in case it is False it will only
              generate the objective function.
        
        Output:
            - depth of the formula
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
        This method computes a Lowest depht first optimization formulation 
        making and increasing penalization from being far from the root node
        Input:
            - model_name is a file name to generate Gurobi information about 
              the optimization problem
            - optimize is a flag type variable which is True by default performing
              the optimization of the problem, in case it is False it will only
              generate the objective function.
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
        This method computes a Weighted Largest Number optimization formulation 
    
        Input:
            - z this is the decision variable capturing the root node
            - model_name is a file name to generate Gurobi information about 
              the optimization problem
            - optimize is a flag type variable which is True by default performing
              the optimization of the problem, in case it is False it will only
              generate the objective function.
        '''
        self.model.setObjective(z, grb.GRB.MAXIMIZE)
        self.model.update()
        if optimize is True:
            self.model.optimize()
            self.model.write(model_name)
    
    def satis_score(self, formula, t=0):
        '''
        This method computes the actual satisfaction score/percentage of a given
        optimization solution.
        
        Note: Current encoding captures how satisfaction aligns to user preferences.
        For the case of disjunction and eventually this are not equivalent.
        Example: OR^(0.4, 0.6) (a,b)
        Make b=0 as a predefine constraint
        Then z_or= max(0.4/0.6 *1 ,  0.6/0.6*0) = 0.666
        But satisfaction score should be 1 since the other subformula was satisfied
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