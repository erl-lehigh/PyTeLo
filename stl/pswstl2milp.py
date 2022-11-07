'''
 Copyright (C) 2018-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
'''
# from gurobipy import Model as GRBModel
import gurobipy as grb

from stl import Operation, RelOperation, STLFormula


class pswstl2milp(object):
    '''Translate an STL formula to an MILP.'''
    def __init__(self, formula, ranges=None, vtypes=None, model=None, 
                robust=False):
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
            Operation.UNTIL : self.until
        }
        
    def translate(self): # translate all the formula to milp at time 0
        '''Translates the STL formula to MILP from time 0.'''
        z = self.to_milp(self.formula)
        return z

    def to_milp(self, formula, t=0):
        '''Generates the MILP from the STL formula.'''
        z, added = self.add_formula_variable(formula, t)
        if added:
            self.__milp_call[formula.op](formula, z, t) 
        return z

    def add_formula_variable(self, formula, t): 
        '''Adds a variable for the `formula` at time `t`.'''
        if formula not in self.variables:               # checks if the variable previously existed
            self.variables[formula] = dict()
        if t not in self.variables[formula]:            # updates t 
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
            print ('Added state:', state, 'time:', t)
            self.model.update()
        return self.variables[state][t]

    def predicate(self, pred, z, t):
        '''Adds a predicate to the model.'''
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
        '''Adds a conjunction to the model.'''
        assert formula.op == Operation.AND
        z_children = [self.to_milp(f, t) for f in formula.children]
        weights = []
        vars_children = []
        for k, (z_child) in enumerate(z_children):
            weight = formula.weight(k)
            weights.append(weight)
            vars_children.append(z_child * k)

        assert sum(weights) == 1
        self.model.addConstr(z == sum(vars_children) / sum(weights))

    def disjunction(self, formula, z, t):
        '''Adds a disjunction to the model.'''
        assert formula.op == Operation.OR
        z_children = [self.to_milp(f, t) for f in formula.children]
        weights = []
        vars_children = []
        for k, (z_child) in enumerate(z_children):
            weight = formula.weight(k)
            weights.append(weight)
            vars_children.append(z_child * k)

        self.model.addConstr(z == grb.max_(vars_children)/max(weights))

    def eventually(self, formula, z, t):
        '''Adds an eventually to the model.'''
        assert formula.op == Operation.EVENT
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau) for tau in range(a, b+1)]
        zip_children = zip(range(a, b+1), z_children)
        weights = []
        vars_children = []
        for tau, z_child in zip_children:
            weight = formula.weight(tau)
            weights.append(weight)
            vars_children.append(z_child * weight)
        
        self.model.addConstr(z == grb.max_(vars_children) / max(weights))

    def globally(self, formula, z, t):
        '''Adds a globally to the model.'''
        assert formula.op == Operation.ALWAYS
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau) for tau in range(a, b+1)]
        zip_children = zip(range(a, b+1), z_children)
        weights = []
        vars_children = []
        for tau, z_child in zip_children:
            weight = formula.weight(tau)
            weights.append(weight)
            vars_children.append(z_child * weight)

        assert sum(weights) == 1
        self.model.addConstr(z == sum(vars_children) / sum(weights))  

    def until(self, formula, z, t):
        '''Adds an until to the model.'''
        a, b = int(formula.low), int(formula.high)
        z_children = []
        for t_ in range(a,b+1):
            z_children_left =  [self.to_milp(formula.left, t+t__) for t__ in range(0,t_)]
            z_children_right = [self.to_milp(formula.right, t+t_)]
            z_children.append(z_children_right + sum(z_children_left))
        self.model.addConstr(z == grb.max_(z_children))
    

    # def pstl2lp(self, formula, t=0):
    #     ''' It creates a linear problem from the formuale
    #          that needs to be satisfied '''
    #     lp = grb.Model("LP")
    #     if self.robust and 'rho' not in self.ranges:
    #         self.ranges['rho'] = (-grb.GRB.INFINITY, self.M - 1)
    #     if self.robust:
    #         rho_min, rho_max = self.ranges['rho']
    #         self.rho = lp.addVar(vtype=grb.GRB.CONTINUOUS, name='rho',
    #                                     lb=rho_min, ub=rho_max, obj=-1)        
    #     else:
    #         self.rho = 0
        
    #     formulae = self.predicate_pairs(formula, t)
    #     self.lpvariable = dict()
    #     # formulae, k = zip(*self.predicate_pairs(formula, t)) 
    #     for phi in formulae:
    #         self.lpvariable[phi[0]] = dict()
    #         name = '{}_{}'.format(phi[0], phi[1])
    #         var = lp.addVar(vtype=grb.GRB.CONTINUOUS, lb=-10, ub=10, name=name)
    #         self.lpvariable[phi[0]][phi[1]] = var

    #         if phi[0].relation in (RelOperation.GE, RelOperation.GT):
    #             lp.addConstr(var >= phi[0].threshold + self.rho)

    #         if phi[0].relation in (RelOperation.LE, RelOperation.LT):
    #             lp.addConstr(var <= phi[0].threshold - self.rho)    
    #         lp.update()
        
    #     lp.optimize()
    #     print('Objective2: ')
    #     obj = lp.getObjective()
    #     # print("TIMES HERE: ", formulae)
    #     print(str(obj), ':', obj.getValue(), "LP")
    #     return lp
        
    # def predicate_pairs(self, formula, t=0):
    #     '''It receives formula and time step and returns a set of the subformulae
    #          that needs to be satisfied at the specific time. Note that Disjunction
    #          and eventually are special cases'''
       
    #     ret = set()

    #     if formula.op == Operation.PRED:
    #         if self.variables[formula][t].x == 1:
    #             ret = {(formula, t)}
    #         else:
    #             ret = {}

    #     elif formula.op == Operation.AND:
    #         for f in formula.children:
    #             ret = ret.union(self.predicate_pairs(f, t))
    #         # ret = [set.union(self.predicate_pairs(f, t)) for f in formula.children]

    #     elif formula.op == Operation.OR:
    #         for f in formula.children:
    #             if self.variables[f][t].x == 1:
    #                 ret = ret.union(self.predicate_pairs(f, t))
    #                 break

    #     elif formula.op == Operation.ALWAYS:
    #         f = formula.child
    #         interval = range(int(formula.low), int(formula.high+1))
    #         for t in interval:
    #             ret = ret.union(self.predicate_pairs(f, t))
    #         # ret = [set.union(self.predicate_pairs(f, t)) for t in interval]

    #     elif formula.op == Operation.EVENT:
    #         f = formula.child
    #         interval = range (int(formula.low), int(formula.high+1))
    #         for t in interval:
    #             if self.variables[f][t].x == 1:
    #                 ret = ret.union(self.predicate_pairs(f, t))
    #                 break

    #     return ret


    # def method_1(self): #(Hierarchical Optimization)
    #     max_depth = max(self.objectives)
    #     for d in range(max_depth+1):
    #         self.model.setObjectiveN(-self.objectives[d], d, 
    #                                  priority=max_depth-d)
    #         self.model.update()
        
    #     self.model.optimize()
    #     self.model.write('model_test.lp')
    #     return d
    
    # def method_2(self): #(Lowest depth first)
    #     M2 = 20 # FIXME: computed based on formula size
    #     reward = sum([term * M2**(-d) for d, term in self.objectives.items()])
    #     self.model.setObjective(reward, grb.GRB.MAXIMIZE)
    #     self.model.update()
    #     self.model.optimize()
    #     self.model.write('model_test.lp')

    # def method_3(self, z): #(Weighted Largest Number)
    #     self.model.setObjective(z, grb.GRB.MAXIMIZE)
    #     self.model.update()
    #     self.model.optimize()
    #     self.model.write('model_test.lp')