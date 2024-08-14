"""
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
"""
import numpy as np
import gurobipy as grb
import sys
sys.path.append('..')

from wstl2milp import wstl2milp
from wstl import to_ast

formula ="(x < 10) &&^p1 F[0, 2]^w1 y > 2 ||^p2 G[1, 3]^w2 z<=8"

weights = {
        'p1': lambda i: i + 1,
        'p2': lambda i: 2 - i,
        'w1': lambda x: 2 - np.abs(x - 1),
        'w2': lambda x: 1 + (x-2)**2
    }

ast = to_ast(formula, weights)
print('AST:', str(ast))

wstl_milp = wstl2milp(ast)
z_formula, rho_formula = wstl_milp.translate(satisfaction=True)
wstl_milp.model.setObjective(rho_formula, grb.GRB.MAXIMIZE)
wstl_milp.model.update()

wstl_milp.model.optimize()

print('Vars')
for var in wstl_milp.model.getVars():
    print(var.VarName, ':', var.x)

print('Constraints')
for constr in wstl_milp.model.getConstrs():
    print(':', str(constr))

print('Objective')
obj = wstl_milp.model.getObjective()
print(str(obj), ':', obj.getValue())

wstl_milp.model.write('wstl2milp.lp')
