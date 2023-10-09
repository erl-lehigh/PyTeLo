#!/usr/bin/env python3

"""
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.

 @author: Sadra Sadradinni, Cristian-Ioan Vasile
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

from mtl2milp import mtl2milp

# formula = "(x > 10) && F[0, 2] y > 2 || G[1, 6] z > 8"
# formula = "G[2,4] F[1,3](x>=3)"
formula = "(x) && F[0, 2] y  && G[1, 6] z "
# formula = 'G[0,1] x >= 3 && y>2 '

lexer = mtlLexer(InputStream(formula))
tokens = CommonTokenStream(lexer)
parser = mtlParser(tokens)
t = parser.mtlProperty()
ast = MTLAbstractSyntaxTreeExtractor().visit(t)
print('type: ', type(ast))
nvar = ast.variables() 


print("HERE:", nvar)

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
