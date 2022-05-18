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

from stl import Operation, RelOperation, STLFormula
from stl.stlLexer import stlLexer
from stl.stlParser import stlParser
from stl.stlVisitor import stlVisitor

from stl import STLAbstractSyntaxTreeExtractor

from stl import stl2milp_pulp
import pulp

# formula = "(x > 10) && F[0, 2] y > 2 || G[1, 6] z > 8"
# formula = "G[2,4] F[1,3](x>=3)"
# formula = "(x <= 10) && F[0, 2] y > 2 && G[1, 6] (z < 8) && G[1,6] (z > 3)"
formula = 'G[0,1] x >= 3'

lexer = stlLexer(InputStream(formula))
tokens = CommonTokenStream(lexer)
parser = stlParser(tokens)
t = parser.stlProperty()
print(t.toStringTree())
ast = STLAbstractSyntaxTreeExtractor().visit(t)

print('AST:', str(ast))

stl_milp = stl2milp_pulp(ast, ranges={'x': [-4, 5]}, robust=True)
stl_milp.translate(satisfaction=True)
stl_milp.model.solve(solver=stl_milp.solver)

print('Vars')
for var in stl_milp.model.variables():
    print(var.name, ':', var.value())

print('Constraints')
for constr in list(stl_milp.model.constraints.keys()):
    print(':', str(constr))

print('Objective')
obj = stl_milp.model.objective
print(str(obj), ':', obj.value())

stl_milp.model.writeLP('stl2milp.lp')
