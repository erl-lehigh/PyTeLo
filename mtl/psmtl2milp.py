'''
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
'''

import gurobipy as grb
from mtl import Operation


class psmtl2milp(object):
    '''
    Translate an MTL formula to an MILP that captures partial satisfaction.
    '''
    def __init__(self, formula, model=None):
        
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
        '''Translates the MTL formula to MILP from time 0.'''
        z = self.to_milp(self.formula)
        return z

    def to_milp(self, formula, t=0, depth=0, z_ancestors=None):
        '''Generates the MILP from the MTL formula.'''
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
        '''Adds a variable for the `formula` at time `t`.'''
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
        '''Adds the `state` at time `t` as a variable.'''
        if state not in self.variables:
            self.variables[state] = dict()
            
        if t not in self.variables[state]:
            self.variables[state][t] = z
            self.model.update()
        return self.variables[state][t]

    def predicate(self, pred, z, t, depth, z_ancestors):
        '''Adds a predicate to the model.'''
        assert pred.op == Operation.PRED
        self.add_state(pred.variable, t, z)
        

    def conjunction(self, formula, z, t, depth, z_ancestors):
        '''Adds a conjunction to the model.'''
        assert formula.op == Operation.AND
        z_children = [self.to_milp(f, t, depth+1, z_ancestors) 
                      for f in formula.children]
        self.model.addConstr(z == sum(z_children) / len(z_children) )

    def disjunction(self, formula, z, t, depth, z_ancestors):
        '''Adds a disjunction to the model.'''
        assert formula.op == Operation.OR
        z_children = [self.to_milp(f, t, depth+1, z_ancestors) 
                      for f in formula.children]
        self.model.addConstr(z == grb.max_(z_children))

    def eventually(self, formula, z, t, depth, z_ancestors):
        '''Adds an eventually to the model.'''
        assert formula.op == Operation.EVENT
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau, depth+1, z_ancestors) 
                      for tau in range(a, b+1)]
        self.model.addConstr(z == grb.max_(z_children))

    def globally(self, formula, z, t, depth, z_ancestors):
        '''Adds a globally to the model.'''
        assert formula.op == Operation.ALWAYS
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau, depth+1, z_ancestors) 
                      for tau in range(a, b+1)]
        self.model.addConstr(z == sum(z_children) / (b-a+1))    

    def until(self, formula, z, t, depth, z_ancestors):
        '''Adds an until to the model.'''
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

    def hierarchical(self): #(Hierarchical Optimization)
        max_depth = max(self.objectives)
        for d in range(max_depth+1):
            self.model.setObjectiveN(-self.objectives[d], d, 
                                     priority=max_depth-d)
            self.model.update()
        
        self.model.optimize()
        self.model.write('model_test.lp')
        return d
    
    def ldf(self): #(Lowest depth first)
        M2 = 20 # FIXME: computed based on formula size
        reward = sum([term * M2**(-d) for d, term in self.objectives.items()])
        self.model.setObjective(reward, grb.GRB.MAXIMIZE)
        self.model.update()
        self.model.optimize()
        self.model.write('model_test.lp')

    def wln(self, z): #(Weighted Largest Number)
        self.model.setObjective(z, grb.GRB.MAXIMIZE)
        self.model.update()
        self.model.optimize()
        self.model.write('model_test.lp')