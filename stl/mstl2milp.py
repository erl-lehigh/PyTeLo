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

        self.variables = dict()

        self.objectives = dict()

        self.rhoVariables = dict()

        self.rhoObjectives = dict()

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
        if formula not in self.variables:         
            self.variables[formula] = dict()
        if t not in self.variables[formula]:           
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
            self.variables[formula][t] = z
            self.model.update()
            return True, z
        return False, self.variables[formula][t]
    
    def add_state(self, model, state, t):
        '''Adds the `state` at time `t` as a variable.'''
        if state not in self.variables:
            self.variables[state] = dict()
        if t not in self.variables[state]:
            low, high = self.ranges[state]
            vtype = self.vtypes[state]
            name='{}_{}_'.format(state, t)
            v = model.addVar(vtype=vtype, lb=low, ub=high, name=name)
            self.variables[state][t] = v
            model.update()
        return self.variables[state][t]

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
            self.balanceSatisfactionObjectives[depth][child][t] = self.variables[child][t]
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
            self.balanceSatisfactionObjectives[depth][child][t + tau] = self.variables[child][t + tau]
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
            # Create an auxiliary variable to hold the min result
            name = 'Until_{}_{}_{}'.format(formula.identifier(), t, t_)
            z_aux = self.model.addVar(vtype=grb.GRB.BINARY, 
                                    name=name + "_z")
            self.model.addConstr(z_aux == grb.min_(z_children_right + z_children_left))
            z_children.append(z_aux)
            if not formula.right in self.balanceSatisfactionObjectives[depth]:
                self.balanceSatisfactionObjectives[depth][formula.right] = {}
            self.balanceSatisfactionObjectives[depth][formula.right][t + t_] = z_aux
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
        
        self.generate_QP_robust_constraints(self.formula, lp, self.rho, t)

        return lp
        
    def outerOptim(self, lp, balance=True):
        ''' Optimizes the LP model according to the robust constraints.'''
        self.custom_qp_optim(lp, self.rho, balance)
        return lp
    
    def custom_qp_optim(self, qp, rho, balance=True):
        '''
        Sets the objective functions for the QP model based on the balanceObjectives
        generated during the robust constraint generation and overall robustness and
        optimizes the model objectives in order manually since Gurobi does not support
        multi-objective QP optimization. If the balance flag is not set, the system 
        will not balance the robustness values, reducing the problem to an LP.
        '''
        if rho is not None:
            qp.setObjective(rho, sense=grb.GRB.MAXIMIZE)
            qp.update()
            qp.optimize()
        if balance:
            if rho is not None:
                maxRho = qp.getObjective().getValue()
                qp.addConstr(rho >= maxRho, name='Fixed_Rho')
                qp.update()
            objective_expr = None
            for depth, terms in enumerate(self.balanceRobustnessObjectives):
                if terms and len(terms)>0:
                    if objective_expr is not None:
                        maxBalanceObj = qp.getObjective().getValue()
                        qp.addConstr(objective_expr <= maxBalanceObj, name=f'Fixed_Balance_Robustness_{depth}')
                    qp.update()
                    objective_expr = sum(terms)
                    qp.setObjective(objective_expr, sense=grb.GRB.MINIMIZE)
                    qp.update()
                    qp.optimize()
                
        
    def generate_QP_robust_constraints(self, formula, lp, rho, t=0, depth=0, lp_state_vars=None):
        '''
        Uses the current state of the z variables in the current MILP model
        to recursively generate constraints for rho in the LP model.
        '''
        if lp_state_vars is None:
            lp_state_vars = {}
        if self.variables[formula][t].x > 0.5:
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
                self.generate_QP_robust_constraints(child, lp, childRho, t, depth+1, lp_state_vars)
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
                self.generate_QP_robust_constraints(child, lp, childRho, t, depth+1, lp_state_vars)
                childRhoVars.append(childRho*self.variables[child][t].x)
                childZVars.append(self.variables[child][t].x)
                self.balanceRobustnessObjectives[depth].append((childRho*childRho)*self.variables[child][t].x)
            lp.addConstr(rho == sum(childRhoVars)/sum(childZVars))
        elif op == Operation.ALWAYS:
            childRhoVars = []
            a, b = int(formula.low)+t, int(formula.high)+t
            child = formula.child
            for tau in range(a, b+1):
                opname = Operation.getString(child.op)
                identifier = child.identifier()
                name = '{}_{}_{}'.format(opname, identifier, tau)
                rho_min, rho_max = self.ranges['rho']
                childRho = lp.addVar(vtype=grb.GRB.CONTINUOUS,
                                    name=name + '_rho', lb=rho_min, ub=rho_max)
                lp.update()
                self.generate_QP_robust_constraints(child, lp, childRho, tau, depth+1, lp_state_vars)
                childRhoVars.append(childRho)  
            minRho = grb.min_(childRhoVars)
            lp.addConstr(rho == minRho)
        elif op == Operation.EVENT:
            childRhoVars = []
            childZVars = []
            a, b = int(formula.low)+t, int(formula.high)+t
            child = formula.child
            for tau in range(a, b+1):
                opname = Operation.getString(child.op)
                identifier = child.identifier()
                name = '{}_{}_{}'.format(opname, identifier, tau)
                rho_min, rho_max = self.ranges['rho']
                childRho = lp.addVar(vtype=grb.GRB.CONTINUOUS,
                                    name=name + '_rho', lb=rho_min, ub=rho_max)
                lp.update()
                self.generate_QP_robust_constraints(child, lp, childRho, tau, depth+1, lp_state_vars)
                childRhoVars.append(childRho*self.variables[child][tau].x) 
                childZVars.append(self.variables[child][tau].x)
                self.balanceRobustnessObjectives[depth].append((childRho*childRho)*self.variables[child][tau].x)
            lp.addConstr(rho == sum(childRhoVars)/sum(childZVars))
        elif op == Operation.UNTIL:
            childRhoVars = []
            childZVars = []
            a, b = int(formula.low)+t, int(formula.high)+t
            for t_ in range(a,b+1):
                zValsInner = []
                childRhoInner = []
                for t__ in range(0,t_):
                    childLeft = formula.left
                    zValsInner.append(self.variables[childLeft][t + t__].x)
                    opname = Operation.getString(childLeft.op)
                    identifier = childLeft.identifier()
                    name = 'Until_Inner_{}_{}_{}'.format(identifier, t, t__)
                    rho_min, rho_max = self.ranges['rho']
                    childRhoLeft = lp.addVar(vtype=grb.GRB.CONTINUOUS,
                                    name=name + '_rho', lb=rho_min, ub=rho_max)
                    lp.update()
                    self.generate_QP_robust_constraints(childLeft, lp, childRhoLeft, t + t__, depth+1, lp_state_vars)
                    childRhoInner.append(childRhoLeft)  
                child_right = formula.right
                zValsInner.append(self.variables[child_right][t + t_].x)
                opname = Operation.getString(child_right.op)
                identifier = child_right.identifier()
                name = 'Until_Outer_{}_{}_{}'.format(identifier, t, t_)
                rho_min, rho_max = self.ranges['rho']
                childRhoRight = lp.addVar(vtype=grb.GRB.CONTINUOUS,
                                    name=name + '_rho', lb=rho_min, ub=rho_max)
                lp.update()
                self.generate_QP_robust_constraints(child_right, lp, childRhoRight, t + t_, depth+1, lp_state_vars)
                childRhoInner.append(childRhoRight)
                zValsInnerProduct = min(zValsInner)
                # Create auxiliary variable for the min result
                name = 'Until_{}_{}_{}_inner'.format(formula.identifier(), t, t_)
                minRhoInner = lp.addVar(vtype=grb.GRB.CONTINUOUS, 
                                    name=name + "_rho", lb=rho_min, ub=rho_max)
                lp.addConstr(minRhoInner == grb.min_(childRhoInner))
                childRhoVars.append(zValsInnerProduct*minRhoInner)
                childZVars.append(zValsInnerProduct)
                self.balanceRobustnessObjectives[depth].append((minRhoInner*minRhoInner)*zValsInnerProduct)
            lp.addConstr(rho == sum(childRhoVars)/sum(childZVars))
        lp.update()


    def generate_MIQP_robustness_constraints(self, formula, t=0, depth=0, balance=True):
        '''
        This function adds robustness variables to the MILP/MIQP model
        directly using big M method, resulting in a truly optimal solution to 
        the bi-level optimization problem for runtime comparison purposes.
        '''
        op = formula.op
        rho_min, rho_max = -grb.GRB.INFINITY, self.M - 1
        if formula not in self.rhoVariables:
            self.rhoVariables[formula] = dict()
        if t not in self.rhoVariables[formula]:
            opname = Operation.getString(op)
            identifier = formula.identifier()
            name = '{}_{}_{}'.format(opname, identifier, t)
            rho_var = self.model.addVar(vtype=grb.GRB.CONTINUOUS,
                                            name=name + '_rho', lb=rho_min, ub=rho_max)
            self.model.addConstr(rho_var >= (self.variables[formula][t]-1)*self.M)
            self.model.update()
            self.rhoVariables[formula][t] = rho_var
            if depth not in self.rhoObjectives:
                self.rhoObjectives[depth] = 0
            self.rhoObjectives[depth] += rho_var
        if balance and depth-1<len(self.balanceRobustnessObjectives):
                self.balanceRobustnessObjectives.append([])
        if op == Operation.PRED:
            v = self.variables[formula.variable][t]
            if formula.relation in (RelOperation.GE, RelOperation.GT):
                self.model.addConstr(v - formula.threshold >= self.rhoVariables[formula][t])
            elif formula.relation in (RelOperation.LE, RelOperation.LT):
                self.model.addConstr(formula.threshold - v >= self.rhoVariables[formula][t])
            self.model.update()
        elif op == Operation.AND:
            childRhoVars = []
            for child in formula.children:
                self.generate_MIQP_robustness_constraints(child, t, depth+1, balance)
                childRhoVars.append(self.rhoVariables[child][t])
            minRho = grb.min_(childRhoVars)
            self.model.addConstr(self.rhoVariables[formula][t] == minRho)
            self.model.update()
        elif op == Operation.OR:
            childRhoVars = []
            for child in formula.children:
                self.generate_MIQP_robustness_constraints(child, t, depth+1, balance)
                opname = Operation.getString(op)
                childId = child.identifier()
                identifier = formula.identifier()
                name = '{}_{}_{}_{}'.format(opname, identifier, childId, t)
                childRho = self.model.addVar(vtype=grb.GRB.CONTINUOUS,
                                                name=name + '_rho', lb=rho_min, ub=rho_max)
                self.model.addConstr(childRho <= self.rhoVariables[child][t])
                self.model.update()
                childRhoVars.append(childRho)
                if balance:
                    self.balanceRobustnessObjectives[depth].append(childRho*childRho)
            self.model.addConstr(self.rhoVariables[formula][t] == sum(childRhoVars)/len(formula.children))
        elif op == Operation.ALWAYS:
            childRhoVars = []
            a, b = int(formula.low)+t, int(formula.high)+t
            child = formula.child
            for tau in range(a, b+1):
                self.generate_MIQP_robustness_constraints(child, tau, depth+1, balance)
                childRhoVars.append(self.rhoVariables[child][tau])
            minRho = grb.min_(childRhoVars)
            self.model.addConstr(self.rhoVariables[formula][t] == minRho)
        elif op == Operation.EVENT:
            childRhoVars = []
            childZVars = []
            a, b = int(formula.low)+t, int(formula.high)+t
            child = formula.child
            for tau in range(a, b+1):
                self.generate_MIQP_robustness_constraints(child, tau, depth+1, balance)
                opname = Operation.getString(op)
                childId = child.identifier()
                identifier = formula.identifier()
                name = '{}_{}_{}_{}'.format(opname, identifier, tau, t)
                childRho = self.model.addVar(vtype=grb.GRB.CONTINUOUS,
                                                name=name + '_rho', lb=rho_min, ub=rho_max)
                self.model.addConstr(childRho <= self.rhoVariables[child][tau])
                self.model.update()
                childRhoVars.append(childRho*self.variables[child][tau]) 
                if balance:
                    self.balanceRobustnessObjectives[depth].append((childRho*childRho))
            self.model.addConstr(self.rhoVariables[formula][t] == sum(childRhoVars)/(b-a+1))
        elif op == Operation.UNTIL:
            childRhoVars = []
            childZVars = []
            a, b = int(formula.low)+t, int(formula.high)+t
            for t_ in range(a,b+1):
                zValsInner = []
                childRhoInner = []
                for t__ in range(0,t_):
                    childLeft = formula.left
                    self.generate_MIQP_robustness_constraints(childLeft, t + t__, depth+1, balance)
                    childRhoInner.append(self.rhoVariables[childLeft][t + t__])
                    zValsInner.append(self.variables[childLeft][t + t__])
                child_right = formula.right
                self.generate_MIQP_robustness_constraints(child_right, t + t_, depth+1, balance)
                childRhoInner.append(self.rhoVariables[child_right][t + t_])
                zValsInner.append(self.variables[child_right][t + t_])
                # Create auxiliary variable for the min result
                name = 'Until_Inner_{}_{}_{}'.format(formula.identifier(), t, t_)
                minZInner = self.model.addVar(vtype=grb.GRB.BINARY, 
                                    name=name + "_z")
                name = 'Until_Inner_{}_{}_{}'.format(formula.identifier(), t, t_)
                minRhoInner = self.model.addVar(vtype=grb.GRB.CONTINUOUS, 
                                    name=name + "_rho", lb=rho_min, ub=rho_max)
                self.model.addConstr(minZInner == grb.min_(zValsInner))
                self.model.addConstr(minRhoInner == grb.min_(childRhoInner))
                name = 'Until_Outer_{}_{}_{}'.format(formula.identifier(), t, t_)
                rhoOuter = self.model.addVar(vtype=grb.GRB.CONTINUOUS, 
                                    name=name + "_rho", lb=rho_min, ub=rho_max)
                self.model.addConstr(rhoOuter <= minRhoInner)
                childRhoVars.append(rhoOuter)
                childZVars.append(minZInner)
                if balance:
                    self.balanceRobustnessObjectives[depth].append((rhoOuter*rhoOuter))
            self.model.addConstr(self.rhoVariables[formula][t] == sum(childRhoVars)/(b-a+1))
        self.model.update()

    def hierarchical(self, model_name='model_test.lp', optimize=True, balance=True, completeSolve=False):
        '''
        This method computes a hierarchical optimization formulation 
        (lexicographical) from root node all the way to the leaves (predicates)
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
                                     priority=2*max_depth-d+1)
            self.model.update()
        if optimize:
            if completeSolve:
                self.generate_MIQP_robustness_constraints(self.formula, balance=balance)
                self.model.update()
                
                self.model.setObjectiveN(-self.rhoVariables[self.formula][0], max_depth+1, 
                                        priority=max_depth+1)
                self.model.update()
                self.model.optimize()
                if balance:
                    currentOptimalObj = [self.model.getObjective(i).getValue() 
                                    for i in range(max_depth+2)]
                    print("Current Optimal Objectives:", currentOptimalObj)
                    print([Operation.getString(child.op) + str(self.rhoVariables[child][0].x) for child in self.formula.children])
                    self.model.addConstrs((self.objectives[d] >= -currentOptimalObj[d] 
                                        for d in range(max_depth+1)), name='Fixed_Primary_Objectives')
                    self.model.addConstr(self.rhoVariables[self.formula][0] >= -currentOptimalObj[-1], 
                                         name='Fixed_Robustness_Objective')
                    self.model.NumObj = 0
                    self.model.update()
                    self.custom_qp_optim(self.model, None)
                    latestSpatialBalanceObj = self.model.getObjective().getValue()
                    self.model.addConstr(sum(self.balanceRobustnessObjectives[-1]) <= latestSpatialBalanceObj,
                                         name='Fixed_Balance_Robustness_Final')
                    formula_terms = None
                    for d in range(max_depth+1):
                        if len(self.balanceSatisfactionObjectives[d])>0:
                            if formula_terms is not None:
                                balanceOptimalObj = self.model.getObjective().getValue()
                                self.model.addConstr(sum(formula_terms) <= balanceOptimalObj, name=f"Fixed_Balance_{d}")
                            self.model.NumObj = 0
                            self.model.update()
                            formula_terms = [sum(self.balanceSatisfactionObjectives[d][f].values())*sum(self.balanceSatisfactionObjectives[d][f].values())
                                            for f in self.balanceSatisfactionObjectives[d].keys()]
                            self.model.setObjective(sum(formula_terms), grb.GRB.MINIMIZE)
                            self.model.update()
                            self.model.optimize()
            elif balance:
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
                        formula_terms = [sum(self.balanceSatisfactionObjectives[d][f].values())*sum(self.balanceSatisfactionObjectives[d][f].values())
                                        for f in self.balanceSatisfactionObjectives[d].keys()]
                        self.model.setObjective(sum(formula_terms), grb.GRB.MINIMIZE)
                        self.model.update()
                        self.model.optimize()
            else:
                self.model.optimize()
            self.model.write(model_name)
        return d
