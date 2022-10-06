#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 17:07:07 2018

@author: sadra
"""
from antlr4 import InputStream, CommonTokenStream

import sys
sys.path.append('/home/gustavo/lehigh/erl/python-stl/stl')

from stl import Operation, RelOperation, STLFormula
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor

from stl import STLAbstractSyntaxTreeExtractor

from stl2milp import stl2milp

#lexer = stlLexer(InputStream("(x > 10) && F[0, 2] y > 2 || G[1, 6] z > 8"))
#lexer = stlLexer(InputStream("G[2,4]F[1,3](x>=3)"))
lexer = stlLexer(InputStream("(x <= 10) && F[0, 2] y > 2 && G[1, 6] (z < 8) && G[1,6] (z > 3)"))
tokens = CommonTokenStream(lexer)
parser = stlParser(tokens)
t = parser.stlProperty()
print(t.toStringTree())
ast = STLAbstractSyntaxTreeExtractor().visit(t)
print ("AST:", ast)

MILP=stl2milp(ast, ranges={'x': [-10, 10], 'y':[-10, 10], 'z':[10,10]}, 
              robust=True)


z=MILP.to_milp(ast,t=0)
MILP.model.addConstr(z==1)
MILP.model.optimize()

#from stl import STLFormula
#phi=STLFormula(ast)
