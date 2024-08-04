"""
 Copyright (c) 2023, Explainable Robotics Lab (ERL)
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
"""

import numpy as np
import sys

sys.path.append('..')
from wmtl import to_ast
from pswmtl2milp import pswmtl2milp

def partial_wmtl_test():
    formula = "&&^w1 (F[2,3]^w1 (a), F[2,3]^w1 (b))"
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

    mtl_milp = pswmtl2milp(ast)
    z = mtl_milp.translate()

    # creating the need of partial satisfaction
    # mtl_milp.model.addConstr(mtl_milp.variables['a'][0] == 0)
    # mtl_milp.model.addConstr(mtl_milp.variables['b'][0] == 0)
    mtl_milp.model.addConstr(mtl_milp.variables['b'][2] == 0)

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
        d = mtl_milp.hierarchical()
        obj = [mtl_milp.model.getObjective(objectives) 
                for objectives in range(d+1)]
        print(str(obj), ':', [obj[i].getValue() for i in range(d+1)], "MILP")
    elif method == 2: 
        mtl_milp.ldf()
        print('Objective')
        obj = mtl_milp.model.getObjective()
        print(str(obj), obj.getValue(), "MILP")
    elif method == 3:
        mtl_milp.wln(z)
        print('Objective')
        obj = mtl_milp.model.getObjective()
        print(str(obj), obj.getValue(), "MILP")

    mtl_milp.model.update()
    mtl_milp.model.optimize()

    print('Constraints')
    for constr in mtl_milp.model.getConstrs():
        print(':', str(constr))

    print('Vars')
    for var in mtl_milp.model.getVars():
        print(var.VarName, ':', var.x)

    print('Objective')
    obj = mtl_milp.model.getObjective()
    print(str(obj), ':', obj.getValue())
    
    print('Satisfaction score')
    print(mtl_milp.satis_score(ast))

if __name__ == '__main__':
    partial_wmtl_test()