"""
 Copyright (c) 2023, Explainable Robotics Lab (ERL)
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
"""
from antlr4 import InputStream, CommonTokenStream

import sys
sys.path.append('..')
from mtl import to_ast
from psmtl2milp import psmtl2milp

formula = "G[0, 2] y  && G[0, 2] z "
ast = to_ast(formula)
nvar = ast.variables() 
print('AST:', str(ast))

mtl_milp = psmtl2milp(ast)
z = mtl_milp.translate()

# creating the need of partial satisfaction
mtl_milp.model.addConstr(mtl_milp.variables['y'][1] == 0)

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