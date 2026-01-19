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

def addDynamics(model):
    print("=============== ADD DYNAMICS ===============")
    print(model.getVars())
    for var in model.getVars():
        var_name = var.VarName
        print(var_name)
        if var_name.startswith('x_') or var_name.startswith('y_'):
            t = int(var_name.split('_')[1])
            if t > 0:
                model.addConstr(var - model.getVarByName(var_name.replace(f"_{t}_", f"_{t-1}_")) <= 3)
                model.addConstr(var - model.getVarByName(var_name.replace(f"_{t}_", f"_{t-1}_")) >= -3)
def partial_stl_test():
    # formula = "(x > 10) && F[0, 2] y > 2 || G[1, 6] z > 8"
    # formula = "G[2,4] F[1,3](x>=3)"
    # formula = "(x <= 10) && F[0, 2] y > 2 && G[1, 6] (z < 8) && G[1,6] (z > 3)"
    formula = 'F[0,4] x >= 3 && (x >= 1 U[2, 4] F[0,4] y <= -1) && F[0, 3] y >= 1 && G[7, 9] x <= 0 && G[4, 9] x>=-10'
    ast = to_ast(formula)

    print('AST:', str(ast))

    stl_milp = mstl2milp(ast, ranges={'x': [-4, 5], 'y': [-3, 3]}, robust=True)
    
    z = stl_milp.translate()
    addDynamics(stl_milp.model)
    d = stl_milp.hierarchical(balance=False, completeSolve=False)
    for var in stl_milp.model.getVars():
        print(var.VarName, ':', var.x)


    mstlrobust = stl_milp.mstl2lp()
    addDynamics(mstlrobust)
    stl_milp.outerOptim(mstlrobust, balance=False)

    print('LP Model Status:', mstlrobust.status)
    print('Constraints')
    #for constr in stl_milp.model.getConstrs():
    #    print(':', str(constr))

    print('Vars')
    for var in mstlrobust.getVars():
        print(var.VarName, ':', var.x)

    #print('Objective')
    #obj = stl_milp.model.getObjective()
    #print(str(obj), ':', obj.getValue())

    # Plot x and y variables
    x_vals = []
    y_vals = []
    for var in mstlrobust.getVars():
        name = var.VarName
        if 'x_' in name:
            x_vals.append((int(name.split('_')[1]), var.X))
        elif 'y_' in name:
            y_vals.append((int(name.split('_')[1]), var.X))
    
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
     partial_stl_test()