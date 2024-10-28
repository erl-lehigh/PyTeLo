"""
 Copyright (c) 2023, Explainable Robotics Lab (ERL)
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
"""
import sys
sys.path.append('..')

from mtl import to_ast
from mtl2milp import mtl2milp

formula = "(x) && F[0, 2] y  && G[1, 6] z "

ast = to_ast(formula)
print('type: ', type(ast))
nvar = ast.variables() 

mtl_milp = mtl2milp(ast)
mtl_milp.translate(satisfaction=True)

mtl_milp.model.addConstr(mtl_milp.variables['y'][0] == 0)
# mtl_milp.model.addConstr(mtl_milp.variables['y'][1] == 0)
mtl_milp.model.addConstr(mtl_milp.variables['y'][2] == 0)

mtl_milp.model.update()
mtl_milp.model.optimize()

print('Vars')
for var in mtl_milp.model.getVars():
    print(var.VarName, ':', var.x)

print('Constraints')
for constr in mtl_milp.model.getConstrs():
    print(':', str(constr))

print('Objective')
obj = mtl_milp.model.getObjective()
print(str(obj), ':', obj.getValue())
