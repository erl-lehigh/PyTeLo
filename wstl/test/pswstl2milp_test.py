"""
 Copyright (c) 2023, Explainable Robotics Lab (ERL)
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
"""
import sys
sys.path.append('..')

from wstl import to_ast
from pswstl2milp import pswstl2milp

def partial_wstl_test():
    formula = "&&^w1 (F[2,3]^w1 (x>=2), F[2,3]^w1 (b>=1))"
    # formula = "F[0, 1]^w3 (y)"
    weights = {
            'p1': lambda i: i+1,
            'p2': lambda i: 2 - i,
            'w1': lambda x: 1,
            'w2': lambda k: [0.4, 0.6][k],
            'w3': lambda k: [0.6, 0.4][k]
        }
    ast = to_ast(formula, weights)
    nvar = ast.variables() 
    print('AST:', str(ast))

    wstl_milp = pswstl2milp(ast)
    z = wstl_milp.translate()

    # creating the need of partial satisfaction
    wstl_milp.model.addConstr(wstl_milp.variables['b'][2] == 0)
    wstl_milp.model.addConstr(wstl_milp.variables['b'][3] == 0)

    '''
        we have implemented three different methods to capture partial satisfaction
        method = 1:
            is a hierarchical approach, resembling the lexicographical optimization
            problem. Where subformulae are optimized in order from root to leaves.
        method = 2:
            Lowest depth first, it is single objective, with the expression capturing
            all subformulae and penalizing for being far from the root.
        method = 3:
            Weighted Largest Number, considers the partial satisfaction of as much
            as possible from maximizing the root variable.
    '''
    method = 3
    if method == 1:
        d = wstl_milp.hierarchical()
        obj = [wstl_milp.model.getObjective(objectives) 
                for objectives in range(d+1)]
        print(str(obj), ':', [obj[i].getValue() for i in range(d+1)], "MILP")
    elif method == 2: 
        wstl_milp.ldf()
        print('Objective')
        obj = wstl_milp.model.getObjective()
        print(str(obj), obj.getValue(), "MILP")
    elif method == 3:
        wstl_milp.wln(z)
        print('Objective')
        obj = wstl_milp.model.getObjective()
        print(str(obj), obj.getValue(), "MILP")

    wstl_milp.model.update()
    wstl_milp.model.optimize()

    print('Constraints')
    for constr in wstl_milp.model.getConstrs():
        print(':', str(constr))

    print('Vars')
    for var in wstl_milp.model.getVars():
        print(var.VarName, ':', var.x)

    print('Objective')
    obj = wstl_milp.model.getObjective()
    print(str(obj), ':', obj.getValue())
    
    print('Satisfaction score')
    print(wstl_milp.satis_score(ast))

if __name__ == '__main__':
    partial_wstl_test()