"""
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Gustavo Cardona, Cristian-Ioan Vasile, Crockett Lee Hensley
"""
import sys
sys.path.append('..')

from mstl2milp import mstl2milp
from stl import to_ast
import matplotlib.pyplot as plt

def partial_stl_test(method):
    '''
        we have implemented three different methods to capture partial satisfaction
        method = 1:
            is a hierarchical approach, resembling the lexicographical optimization
            problem. Where subformulae are optimized in order from root to leaves.
        method = 2:
            Lowest depth first, it is single objective, with the expression capturing
            all subformulae and penalizing for being far from the root.
    '''
    
    # formula = "(x > 10) && F[0, 2] y > 2 || G[1, 6] z > 8"
    # formula = "G[2,4] F[1,3](x>=3)"
    # formula = "(x <= 10) && F[0, 2] y > 2 && G[1, 6] (z < 8) && G[1,6] (z > 3)"
    formula = 'G[0,2] x >= 3 && F[0,2] y >= 2 || F[0,3] y<= -1'
    ast = to_ast(formula)

    print('AST:', str(ast))

    stl_milp = mstl2milp(ast, ranges={'x': [-4, 5], 'y': [-3, 3]}, robust=True)
    z = stl_milp.translate()

    
    if method == 1:
        d = stl_milp.hierarchical()
        obj = [stl_milp.model.getObjective(objectives) for objectives in range(d+1)]
        print(str(obj), ':', [obj[i].getValue() for i in range(d+1)], "MILP")
    elif method == 2: 
        stl_milp.ldf()
        print('Objective')
        obj = stl_milp.model.getObjective()
        print(str(obj), obj.getValue(), "MILP")

    mstlrobust = stl_milp.mstl2lp(ast)

    stl_milp.model.optimize()

    print('Constraints')
    for constr in stl_milp.model.getConstrs():
        print(':', str(constr))

    print('Vars')
    for var in stl_milp.model.getVars():
        print(var.VarName, ':', var.x)

    print('Objective')
    obj = stl_milp.model.getObjective()
    print(str(obj), ':', obj.getValue())

    # Plot x and y variables
    x_vals = []
    y_vals = []
    for var in stl_milp.model.getVars():
        name = var.VarName
        if 'x_' in name:
            x_vals.append((int(name.split('_')[1]), var.x))
        elif 'y_' in name:
            y_vals.append((int(name.split('_')[1]), var.x))
    
    plt.figure(figsize=(8, 4))
    if x_vals:
        plt.scatter([t for t, v in x_vals], [v for t, v in x_vals], label='x', alpha=0.6, color='blue')
    if y_vals:
        plt.scatter([t for t, v in y_vals], [v for t, v in y_vals], label='y', alpha=0.6, color='red')
    plt.xlabel('time')
    plt.ylabel('value')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

    

if __name__ == '__main__':
     partial_stl_test(1)