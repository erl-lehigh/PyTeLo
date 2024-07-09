"""
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Gustavo Cardona, Cristian-Ioan Vasile
"""
from pstl2milp import pstl2milp
import sys
sys.path.append('..')
from stl import to_ast

# formula = "(x > 10) && F[0, 2] y > 2 || G[1, 6] z > 8"
# formula = "G[2,4] F[1,3](x>=3)"
# formula = "(x <= 10) && F[0, 2] y > 2 && G[1, 6] (z < 8) && G[1,6] (z > 3)"
formula = 'G[0,2] x >= 3'
ast = to_ast(formula)

print('AST:', str(ast))

stl_milp = pstl2milp(ast, ranges={'x': [-4, 5]}, robust=True)
z = stl_milp.translate()

# creating the need of partial satisfaction
stl_milp.model.addConstr(stl_milp.variables['x'][1] == 0)

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
        d = stl_milp.hierarchical()
        obj = [stl_milp.model.getObjective(objectives) 
               for objectives in range(d+1)]
        print(str(obj), ':', [obj[i].getValue() for i in range(d+1)], "MILP")
elif method == 2: 
    stl_milp.ldf()
    print('Objective')
    obj = stl_milp.model.getObjective()
    print(str(obj), obj.getValue(), "MILP")
elif method == 3:
    stl_milp.wln(z)
    print('Objective')
    obj = stl_milp.model.getObjective()
    print(str(obj), obj.getValue(), "MILP")

pstlrobust = stl_milp.pstl2lp(ast)

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

stl_milp.model.write('stl2milp.lp')
