#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 17:07:07 2018

@author: sadra
"""
from antlr4 import InputStream, CommonTokenStream

import sys
sys.path.append('../')
import time
from stl import Operation, RelOperation, STLFormula
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor

from stl import STLAbstractSyntaxTreeExtractor

from dstl2milp import dstl2milp

#lexer = stlLexer(InputStream("(x > 10) && F[0, 2] y > 2 || G[1, 6] z > 8"))
# lexer = stlLexer(InputStream("G[2,4](x>=3)"))
# lexer = stlLexer(InputStream("(x <= 2) || x > 3 "))

lexer = stlLexer(InputStream("(G[0,2000]x<=2 && G[3, 4000]y>3) || (G[0,2000]x>3 && G[3, 4000]y<=2)"))
tokens = CommonTokenStream(lexer)
parser = stlParser(tokens)
t = parser.stlProperty()
print(t.toStringTree())
ast = STLAbstractSyntaxTreeExtractor().visit(t)
print ("AST:", ast)

dstl_milp=dstl2milp(ast, ranges={'x': [-10, 10], 'y':[-10, 10], 'z':[10,10]}, 
              robust=True)

dstl_start = time.time()        
z=dstl_milp.translate()
# MILP.model.addConstr(z==1)
dstl_milp.model.optimize()
dstl_end = time.time()
dstl_time= dstl_end-dstl_start
print("TIME: ", dstl_time)
dstl_milp.model.write('dstl2milp_milp.lp')
# x_vals = [var.x for var in dstl_milp.variables['x'].values()]
# y_vals = [var.x for var in dstl_milp.variables['y'].values()]
# print(x_vals, y_vals)
# print(x_vals)

