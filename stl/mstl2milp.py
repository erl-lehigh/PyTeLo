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

        self.zVariables = dict()

        self.objectives = dict()

        self.balanceSatisfactionObjectives = []

        self.balanceRobustnessObjectives = []

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
        if depth-1<len(self.balanceSatisfactionObjectives):
            self.balanceSatisfactionObjectives.append({})
        if z_ancestors is None:
            z_ancestors = []
        added, z = self.add_formula_variable(formula, t, depth, 
                                                    z_ancestors)
        if added:
            children = self.__milp_call[formula.op](formula, z, t, depth, 
                                                    z_ancestors + [z])
        return z

    def add_formula_variable(self, formula, t, depth, z_ancestors): 
        '''Adds a variable for the `formula` at time `t`.'''
        if formula not in self.zVariables:         
            self.zVariables[formula] = dict()
        if t not in self.zVariables[formula]:           
            opname = Operation.getString(formula.op)
            identifier = formula.identifier()
            name = '{}_{}_{}'.format(opname, identifier, t)
            z = self.model.addVar(vtype=grb.GRB.BINARY,
                                            name=name + '_zi')
            self.objectives[depth] += z 
            self.model.update()

            for z_ancestor in z_ancestors:
                #For z to be 1, then all its ancestors' z must be 1
                self.model.addConstr(z <= z_ancestor)
            self.zVariables[formula][t] = z
            self.model.update()
            return True, z
        return False, self.zVariables[formula][t]
    
    def add_state(self, model, state, t):
        '''Adds the `state` at time `t` as a variable.'''
        if state not in self.zVariables:
            self.zVariables[state] = dict()
        if t not in self.zVariables[state]:
            low, high = self.ranges[state]
            vtype = self.vtypes[state]
            name='{}_{}_'.format(state, t)
            v = model.addVar(vtype=vtype, lb=low, ub=high, name=name)
            self.zVariables[state][t] = v
            model.update()
        return self.zVariables[state][t]

    def predicate(self, pred, z, t, depth, z_ancestors):
        '''Adds a predicate to the model.'''
        assert pred.op == Operation.PRED
        v = self.add_state(self.model,pred.variable, t)
        if pred.relation in (RelOperation.GE, RelOperation.GT):  
            self.model.addConstr(v  - self.M * z <= pred.threshold)         
            self.model.addConstr(v + self.M * (1 - z) >= pred.threshold)
        elif pred.relation in (RelOperation.LE, RelOperation.LT):
            self.model.addConstr(v + self.M * z >= pred.threshold)          
            self.model.addConstr(v - self.M * (1 - z) <= pred.threshold)       
        else:
            raise NotImplementedError
        return 0

    def conjunction(self, formula, z, t, depth, z_ancestors):
        '''Adds a conjunction to the model.'''
        assert formula.op == Operation.AND
        z_children = [self.to_milp(f, t, depth+1, z_ancestors) 
                      for f in formula.children]
        # zero if any child is not fully satisfied, 1 otherwise
        self.model.addConstr(z == grb.min_(z_children))
        return 0

    def disjunction(self, formula, z, t, depth, z_ancestors):
        '''Adds a disjunction to the model.'''
        assert formula.op == Operation.OR
        z_children = []
        for child in formula.children:
            z_child = self.to_milp(child, t, depth+1, z_ancestors)
            z_children.append(z_child)
            if not child in self.balanceSatisfactionObjectives[depth]:
                self.balanceSatisfactionObjectives[depth][child] = {}
            self.balanceSatisfactionObjectives[depth][child][t] = self.zVariables[child][t]
        # one if any child is fully satisfied, 0 otherwise
        self.model.addConstr(z == grb.max_(z_children))
        return sum(z_children)

    def eventually(self, formula, z, t, depth, z_ancestors):
        '''Adds an eventually to the model.'''
        assert formula.op == Operation.EVENT
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = []
        for tau in range(a, b+1):
            z_children.append(self.to_milp(child, t + tau, depth+1, z_ancestors))
            if not child in self.balanceSatisfactionObjectives[depth]:
                self.balanceSatisfactionObjectives[depth][child] = {}
            self.balanceSatisfactionObjectives[depth][child][t + tau] = self.zVariables[child][t + tau]
        self.model.addConstr(z == grb.max_(z_children))
        return sum(z_children)

    def globally(self, formula, z, t, depth, z_ancestors):
        '''Adds a globally to the model.'''
        assert formula.op == Operation.ALWAYS
        a, b = int(formula.low), int(formula.high)
        child = formula.child
        z_children = [self.to_milp(child, t + tau, depth+1, z_ancestors) 
                      for tau in range(a, b+1)]
        self.model.addConstr(z == grb.min_(z_children))  
        return 0 

    def until(self, formula, z, t, depth, z_ancestors):
        '''Adds an until to the model.'''
        assert formula.op == Operation.UNTIL
        a, b = int(formula.low), int(formula.high)
        z_children = []
        for t_ in range(a, b+1):
            z_children_left =  [self.to_milp(formula.left, t+t__, depth+1, 
                                             z_ancestors) 
                                for t__ in range(0,t_)]
            z_children_right = [self.to_milp(formula.right, t+t_, depth+1, 
                                             z_ancestors)]
            z_children.append(grb.min_(z_children_right + z_children_left))
            if not formula.right in self.balanceSatisfactionObjectives[depth]:
                self.balanceSatisfactionObjectives[depth][formula.right] = {}
            self.balanceSatisfactionObjectives[depth][formula.right][t + t_] = self.zVariables[formula.right][t + t_]
        self.model.addConstr(z == grb.max_(z_children))
        return sum(z_children)

    def mstl2lp(self, t=0, optimize=True):
        ''' Creates a linear problem from the solved MILP formulae.'''
        lp = grb.Model("LP")

        if self.robust and 'rho' not in self.ranges:
            self.ranges['rho'] = (-grb.GRB.INFINITY, self.M - 1)
        if self.robust:
            rho_min, rho_max = self.ranges['rho']
            self.rho = lp.addVar(vtype=grb.GRB.CONTINUOUS, name='rho',
                                        lb=rho_min, ub=rho_max)
            lp.update()
        else:
            self.rho = 0
        
        self.generate_robust_constraints(self.formula, lp, self.rho, t)

        return lp
        
    def lpOptim(self, lp):
        ''' Optimizes the LP model according to the robust constraints.'''
        self.custom_qp_optim(lp, self.rho)
        return lp
    
    def custom_qp_optim(self, lp, rho):
        '''
        Sets the objective functions for the QP model based on the balanceObjectives
        generated during the robust constraint generation and overall robustness and
        optimizes the model objectives in order manually since Gurobi does not support
        multi-objective QP optimization.
        '''
        lp.setObjective(rho, sense=grb.GRB.MAXIMIZE)
        lp.update()
        lp.optimize()
        maxRho = lp.getObjective().getValue()
        lp.addConstr(rho >= maxRho, name='Fixed_Rho')
        lp.update()
        objective_expr = None
        for depth, terms in enumerate(self.balanceRobustnessObjectives):
            if terms and len(terms)>0:
                if objective_expr is not None:
                    maxBalanceObj = lp.getObjective().getValue()
                    lp.addConstr(objective_expr <= maxBalanceObj, name=f'Fixed_Balance_Robustness_{depth}')
                lp.update()
                objective_expr = sum(terms)
                lp.setObjective(objective_expr, sense=grb.GRB.MINIMIZE)
                lp.update()
                lp.optimize()
                
        
    def generate_robust_constraints(self, formula, lp, rho, t=0, depth=0, lp_state_vars=None):
        '''
        Uses the current state of the z variables in the current MILP model
        to recursively generate constraints for rho in the LP model.
        '''
        if lp_state_vars is None:
            lp_state_vars = {}
        if self.zVariables[formula][t].x > 0.5:
            lp.addConstr(rho >= 0)
        op = formula.op
        if depth-1<len(self.balanceRobustnessObjectives):
                self.balanceRobustnessObjectives.append([])
        if op == Operation.PRED:
            # Create state variables for the LP model (separate from MILP model)
            if formula.variable not in lp_state_vars:
                lp_state_vars[formula.variable] = {}
            if t not in lp_state_vars[formula.variable]:
                low, high = self.ranges[formula.variable]
                vtype = self.vtypes[formula.variable]
                name = '{}_{}'.format(formula.variable, t)
                v = lp.addVar(vtype=vtype, lb=low, ub=high, name=name + '_lp')
                lp_state_vars[formula.variable][t] = v
                lp.update()
            else:
                v = lp_state_vars[formula.variable][t]
            if formula.relation in (RelOperation.GE, RelOperation.GT):
                lp.addConstr(v - formula.threshold >= rho)
            elif formula.relation in (RelOperation.LE, RelOperation.LT):
                lp.addConstr(formula.threshold - v >= rho)
        elif op == Operation.AND:
            childRhoVars = []
            for child in formula.children:
                opname = Operation.getString(child.op)
                identifier = child.identifier()
                name = '{}_{}_{}'.format(opname, identifier, t)
                rho_min, rho_max = self.ranges['rho']
                childRho = lp.addVar(vtype=grb.GRB.CONTINUOUS,
                                    name=name + '_rho', lb=rho_min, ub=rho_max)
                lp.update()
                self.generate_robust_constraints(child, lp, childRho, t, depth+1, lp_state_vars)
                childRhoVars.append(childRho)  
            minRho = grb.min_(childRhoVars)
            lp.addConstr(rho == minRho)
        elif op == Operation.OR:
            childRhoVars = []
            childZVars = []
            for child in formula.children:
                opname = Operation.getString(child.op)
                identifier = child.identifier()
                name = '{}_{}_{}'.format(opname, identifier, t)
                rho_min, rho_max = self.ranges['rho']
                childRho = lp.addVar(vtype=grb.GRB.CONTINUOUS,
                                    name=name + '_rho', lb=rho_min, ub=rho_max)
                lp.update()
                self.generate_robust_constraints(child, lp, childRho, t, depth+1, lp_state_vars)
                childRhoVars.append(childRho*self.zVariables[child][t].x)
                childZVars.append(self.zVariables[child][t].x)
                self.balanceRobustnessObjectives[depth].append((childRho*childRho)*self.zVariables[child][t].x)
            lp.addConstr(rho == sum(childRhoVars)/sum(childZVars))
        elif op == Operation.ALWAYS:
            childRhoVars = []
            a, b = int(formula.low), int(formula.high)
            child = formula.child
            for tau in range(a, b+1):
                opname = Operation.getString(child.op)
                identifier = child.identifier()
                name = '{}_{}_{}'.format(opname, identifier, tau)
                rho_min, rho_max = self.ranges['rho']
                childRho = lp.addVar(vtype=grb.GRB.CONTINUOUS,
                                    name=name + '_rho', lb=rho_min, ub=rho_max)
                lp.update()
                self.generate_robust_constraints(child, lp, childRho, tau, depth+1, lp_state_vars)
                childRhoVars.append(childRho)  
            minRho = grb.min_(childRhoVars)
            lp.addConstr(rho == minRho)
        elif op == Operation.EVENT:
            childRhoVars = []
            childZVars = []
            a, b = int(formula.low), int(formula.high)
            child = formula.child
            for tau in range(a, b+1):
                opname = Operation.getString(child.op)
                identifier = child.identifier()
                name = '{}_{}_{}'.format(opname, identifier, tau)
                rho_min, rho_max = self.ranges['rho']
                childRho = lp.addVar(vtype=grb.GRB.CONTINUOUS,
                                    name=name + '_rho', lb=rho_min, ub=rho_max)
                lp.update()
                self.generate_robust_constraints(child, lp, childRho, tau, depth+1, lp_state_vars)
                childRhoVars.append(childRho*self.zVariables[child][tau].x) 
                childZVars.append(self.zVariables[child][tau].x)
                self.balanceRobustnessObjectives[depth].append((childRho*childRho)*self.zVariables[child][tau].x)
            lp.addConstr(rho == sum(childRhoVars)/sum(childZVars))
        elif op == Operation.UNTIL:
            childRhoVars = []
            childZVars = []
            a, b = int(formula.low), int(formula.high)
            for t_ in range(a,b+1):
                zValsInner = []
                childRhoInner = []
                for t__ in range(0,t_):
                    childLeft = formula.left
                    zValsInner.append(self.zVariables[childLeft][t + t__].x)
                    opname = Operation.getString(childLeft.op)
                    identifier = childLeft.identifier()
                    name = '{}_{}_{}'.format(opname, identifier, t + t__)
                    rho_min, rho_max = self.ranges['rho']
                    childRhoLeft = lp.addVar(vtype=grb.GRB.CONTINUOUS,
                                    name=name + '_rho', lb=rho_min, ub=rho_max)
                    lp.update()
                    self.generate_robust_constraints(childLeft, lp, childRhoLeft, t + t__, depth+1, lp_state_vars)
                    childRhoInner.append(childRhoLeft)  
                child_right = formula.right
                zValsInner.append(self.zVariables[child_right][t + t_].x)
                opname = Operation.getString(child_right.op)
                identifier = child_right.identifier()
                name = '{}_{}_{}'.format(opname, identifier, t + t_)
                rho_min, rho_max = self.ranges['rho']
                childRhoRight = lp.addVar(vtype=grb.GRB.CONTINUOUS,
                                    name=name + '_rho', lb=rho_min, ub=rho_max)
                lp.update()
                self.generate_robust_constraints(child_right, lp, childRhoRight, t + t_, depth+1, lp_state_vars)
                childRhoInner.append(childRhoRight)
                zValsInnerProduct = 1
                for zVal in zValsInner:
                    zValsInnerProduct *= zVal
                childRhoVars.append(grb.min_(childRhoInner)*zValsInnerProduct)
                childZVars.append(zValsInnerProduct)
                self.balanceRobustnessObjectives[depth].append((grb.min_(childRhoInner)*grb.min_(childRhoInner))*zValsInnerProduct)
            lp.addConstr(rho == sum(childRhoVars)/sum(childZVars))
        lp.update()




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
                                     priority=2*max_depth-d)
            self.model.update()
        if optimize is True:
            self.model.optimize()
            self.model.update()
            currentOptimalObj = [self.model.getObjective(i).getValue() 
                                 for i in range(max_depth+1)]
            self.model.addConstrs((self.objectives[d] >= -currentOptimalObj[d] 
                                   for d in range(max_depth+1)), name='Fixed_Primary_Objectives')
            formula_terms = None
            for d in range(max_depth+1):
                if len(self.balanceSatisfactionObjectives[d])>0:
                    if formula_terms is not None:
                        balanceOptimalObj = self.model.getObjective().getValue()
                        self.model.addConstr(sum(formula_terms) <= balanceOptimalObj, name=f"Fixed_Balance_{d}")
                    self.model.NumObj = 0
                    self.model.update()
                    formula_terms = [sum(self.balanceSatisfactionObjectives[d][f].values())*sum(self.balanceSatisfactionObjectives[d][f].values()) for f in self.balanceSatisfactionObjectives[d].keys()]
                    self.model.setObjective(sum(formula_terms), grb.GRB.MINIMIZE)
                    self.model.update()
                    self.model.optimize()
                    
            self.model.write(model_name)
        return d
