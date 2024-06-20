"""
 Copyright (c) 2023, Explainable Robotics Lab (ERL)
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
"""
from antlr4 import InputStream, CommonTokenStream

import sys
sys.path.append('..')

from mtl import Operation,  MTLFormula
from mtlLexer import mtlLexer
from mtlParser import mtlParser
from mtlVisitor import mtlVisitor
from collections import OrderedDict, namedtuple
from mtl import MTLAbstractSyntaxTreeExtractor
import gurobipy as grb
from gurobipy import GRB
from psmtl2milp import psmtl2milp

formula = "G[0, 2] y  && G[0, 2] z "

lexer = mtlLexer(InputStream(formula))
tokens = CommonTokenStream(lexer)
parser = mtlParser(tokens)
t = parser.mtlProperty()
ast = MTLAbstractSyntaxTreeExtractor().visit(t)

print('type: ', type(ast))
nvar = ast.variables() 

mtl_milp = psmtl2milp(ast)
partial_satisfaction = mtl_milp.translate()

# mtl_milp.model.addConstr(mtl_milp.variables['y'][0] == 0)
mtl_milp.model.addConstr(mtl_milp.variables['y'][1] == 0)
# mtl_milp.model.addConstr(mtl_milp.variables['y'][2] == 0)

# mtl_milp.model.addConstr(mtl_milp.variables['z'][0] == 1)
# mtl_milp.model.addConstr(mtl_milp.variables['z'][1] == 1)
# mtl_milp.model.addConstr(mtl_milp.variables['z'][2] == 1)

# mtl_milp.method_3(partial_satisfaction)
mtl_milp.method_1()
mtl_milp.model.update()
mtl_milp.model.optimize()


print('Vars')
for var in mtl_milp.model.getVars():
    print(var.VarName, ':', var.x)

# print('Constraints')
# for constr in mtl_milp.model.getConstrs():
#     print(':', str(constr))

print('Objective')
obj = mtl_milp.model.getObjective()
print(str(obj), ':', obj.getValue())
