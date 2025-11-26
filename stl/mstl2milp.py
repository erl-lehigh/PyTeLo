'''
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile, Crockett Lee Hensley
'''
import gurobipy as grb
from stl import Operation, RelOperation, STLFormula

class mstl2milp(object):
    '''Translate an STL formula to an MILP that captures maximal satisfaction.'''

    def __init__(self, formula, ranges, vtypes=None, model=None, robust=False):
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

        self.zetaVariables = dict()
        self.zVariables = dict()

        self.objectives = dict()

        self.__milp_call = {
            Operation.PRED : self.predicate,
            Operation.AND : self.conjunction,
            Operation.OR : self.disjunction,
            Operation.EVENT : self.eventually,
            Operation.ALWAYS : self.globally,
            Operation.UNTIL : self.until
        }

    def translate(self, satisfaction=True): 
        '''Translates the STL formula to MILP from time 0.'''
        z = self.to_milp(self.formula)
        return z

    def to_milp(self, formula, t=0, depth=0, z_ancestors=None):
        '''Generates the MILP from the STL formula.'''
        if depth not in self.objectives:
            self.objectives[depth] = 0
        if z_ancestors is None:
            z_ancestors = []
        zeta, added, z = self.add_formula_variable(formula, t, depth, 
                                                    z_ancestors)
        if added:
            children = self.__milp_call[formula.op](formula, zeta, t, depth, 
                                                    z_ancestors + [z])
            # If zeta is 0, then z must be 0 (or for predicates, if 
            # they are not satisfied, then z is 0)
            self.model.addConstr(z <= 1 - 1/(children+1) + zeta)
        return z

    def add_formula_variable(self, formula, t, depth, z_ancestors): 
        '''Adds a variable for the `formula` at time `t`.'''
        if formula not in self.zetaVariables:               
            self.zetaVariables[formula] = dict()
            self.zVariables[formula] = dict()
        if t not in self.zetaVariables[formula]:           
            opname = Operation.getString(formula.op)
            identifier = formula.identifier()
            name = '{}_{}_{}'.format(opname, identifier, t)
            if formula.op == Operation.PRED:
                #throw in binary variables with zetas for predicates since 
                #they don't have any fractional satisfaction
                #In the literature, these are actually z, not zeta.
                zeta = self.model.addVar(vtype=grb.GRB.BINARY, name=name)
            else:
                zeta = self.model.addVar(vtype=grb.GRB.CONTINUOUS,
                                             name=name, lb=0, ub=1)
            z = self.model.addVar(vtype=grb.GRB.BINARY,
                                            name=name + '_zi')
            #using zeta here maximizes sat. score of operator
            #you could also use z to maximize number of satisfied nodes
            #but using zeta allows this to be more generalizable to wstl.
            self.objectives[depth] += zeta 
            self.model.update()
            #If zeta is greater than 0, then z must be 1
            self.model.addConstr(z >= zeta)

            for z_ancestor in z_ancestors:
                #For z to be 1, then all its ancestors' z must be 1
                self.model.addConstr(z <= z_ancestor)
            self.zVariables[formula][t] = z
            self.zetaVariables[formula][t] = zeta
            self.model.update()
            return zeta, True, z
        return self.zetaVariables[formula][t], False, self.zVariables[formula][t]
    
    def add_state(self, state, t):
        '''Adds the `state` at time `t` as a variable.'''
        if state not in self.zetaVariables:
            self.zetaVariables[state] = dict()
        if t not in self.zetaVariables[state]:
            low, high = self.ranges[state]
            vtype = self.vtypes[state]
            name='{}_{}'.format(state, t)
            v = self.model.addVar(vtype=vtype, lb=low, ub=high, name=name)
            self.zetaVariables[state][t] = v
            self.model.update()
        return self.zetaVariables[state][t]

    def predicate(self, pred, z, t, depth, z_ancestors):
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
        return 0

    def conjunction(self, formula, zeta, t, depth, z_ancestors):
        '''Adds a conjunction to the model.'''
        assert formula.op == Operation.AND
        z_children = [self.to_milp(f, t, depth+1, z_ancestors) 
                      for f in formula.children]
        # zero if any child is not fully satisfied, 1 otherwise
        self.model.addConstr(zeta == grb.min_(z_children))
        return len(z_children)

    def disjunction(self, formula, zeta, t, depth, z_ancestors):
        '''Adds a disjunction to the model.'''
        assert formula.op == Operation.OR
        z_children = [self.to_milp(f, t, depth+1, z_ancestors) 
                      for f in formula.children]
        # zeta is the average satisfaction of children
        # TODO: support weights for wstl
        self.model.addConstr(zeta == sum(z_children) / len(z_children))
        return len(z_children)

    def eventually(self, formula, zeta, t, depth, z_ancestors):
        '''Adds an eventually to the model.'''
        assert formula.op == Operation.EVENT
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau, depth+1, z_ancestors) 
                      for tau in range(a, b+1)]
        # zeta is the average satisfaction over the interval
        # TODO: support integration over time function for wstl
        self.model.addConstr(zeta == sum(z_children) / len(z_children))
        return len(z_children)

    def globally(self, formula, zeta, t, depth, z_ancestors):
        '''Adds a globally to the model.'''
        assert formula.op == Operation.ALWAYS
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau, depth+1, z_ancestors) 
                      for tau in range(a, b+1)]
        # zero if any time in interval is not fully satisfied, 1 otherwise
        self.model.addConstr(zeta == grb.min_(z_children))  
        return len(z_children)  

    def until(self, formula, zeta, t, depth, z_ancestors):
        '''Adds an until to the model.'''
        assert formula.op == Operation.UNTIL
        a, b = int(formula.low), int(formula.high)
        z_children = []
        for t_ in range(a,b+1):
            z_children_left =  [self.to_milp(formula.left, t+t__, depth+1, 
                                             z_ancestors) 
                                for t__ in range(0,t_)]
            z_children_right = [self.to_milp(formula.right, t+t_, depth+1, 
                                             z_ancestors)]
            z_children.append(z_children_right + sum(z_children_left))
        # zeta in this case considers the length of overlap between the two
        # subformulae satisfactions as a fraction of the total interval
        # TODO: support integration over time function for wstl
        self.model.addConstr(zeta == sum(z_children) / len(z_children))
        return len(z_children)

    def mstl2lp(self, formula, t=0, optimize=True):
        ''' It creates a linear problem from the formulae
             that need to be satisfied '''
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
        '''
        It receives formula and time step and returns a set of the subformulae
        that needs to be satisfied at the specific time. 
        Note that Disjunction and eventually are special cases
        '''
       
        ret = set()

        if formula.op == Operation.PRED:
            if self.zetaVariables[formula][t].x == 1:
                ret = {(formula, t)}
            else:
                ret = {}

        elif formula.op == Operation.AND:
            for f in formula.children:
                ret = ret.union(self.predicate_pairs(f, t))

        elif formula.op == Operation.OR:
            for f in formula.children:
                if self.zetaVariables[f][t].x == 1:
                    ret = ret.union(self.predicate_pairs(f, t))

        elif formula.op == Operation.ALWAYS:
            f = formula.child
            interval = range(int(formula.low), int(formula.high+1))
            for t in interval:
                ret = ret.union(self.predicate_pairs(f, t))

        elif formula.op == Operation.EVENT:
            f = formula.child
            interval = range (int(formula.low), int(formula.high+1))
            for t in interval:
                if self.zetaVariables[f][t].x == 1:
                    ret = ret.union(self.predicate_pairs(f, t))

        elif formula.op == Operation.UNTIL:
            interval = range(int(formula.low), int(formula.high)+1)
            fL = formula.left
            fR = formula.right

            for t in interval:
                if self.zetaVariables[fL][t].x == 1:
                    ret = ret.union(self.predicate_pairs(fL))
                if self.zetaVariables[fR][t].x == 1:
                    ret = ret.union(self.predicate_pairs(fR))

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
        M2 = 30 # FIXME: computed based on formula size
        reward = sum([term * M2**(-d) for d, term in self.objectives.items()])
        self.model.setObjective(reward, grb.GRB.MAXIMIZE)
        self.model.update()

        if optimize is True:
            self.model.optimize()
            self.model.write(model_name)
