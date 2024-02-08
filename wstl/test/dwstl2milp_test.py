#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 17:07:07 2018

@author: Gustavo A. Cardona
"""
from antlr4 import InputStream, CommonTokenStream

import sys
sys.path.append('../')
import time
from stl import Operation, RelOperation, STLFormula
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor
from wstlLexer import wstlLexer
from wstlParser import wstlParser
from wstlVisitor import wstlVisitor
from stl import STLAbstractSyntaxTreeExtractor
from wstl import WSTLAbstractSyntaxTreeExtractor
from dwstl2milp import dwstl2milp
from gurobipy import *

#lexer = stlLexer(InputStream("(x > 10) && F[0, 2] y > 2 || G[1, 6] z > 8"))
# lexer = stlLexer(InputStream("G[2,4](x>=3)"))
# lexer = stlLexer(InputStream("(x <= 2) || x > 3 "))
# lexer = wstlLexer(InputStream("&&^weight2 ((x<=1), (x>=2))"))
lexer = wstlLexer(InputStream("(G[0,2]^weight3  (x>=3))"))

# wstl_formula = " &&^weight2 (&&^weight1 ( (x<=3), (x>=6)) , (x>=2))"
# lexer = stlLexer(InputStream("(G[0,2000]x<=2 && G[3, 4000]y>3) || (G[0,2000]x>3 && G[3, 4000]y<=2)"))
tokens = CommonTokenStream(lexer)
parser = wstlParser(tokens)
t = parser.wstlProperty()
print(t.toStringTree())
weights = {'weight1': lambda x: 5, 'weight2': lambda k: [3, 10][k], 
           'weight3': lambda k: [3, 10, 1][k]}
ast = WSTLAbstractSyntaxTreeExtractor(weights).visit(t)
print ("AST:", ast)

dwstl_milp=dwstl2milp(ast, ranges={'x': [0, 10], 'y':[-10, 10], 'z':[-10,10]})

dstl_start = time.time()        
z,rho_formula = dwstl_milp.translate()
dwstl_milp.model.setObjective(rho_formula, GRB.MAXIMIZE)
dwstl_milp.model.update()
dwstl_milp.model.optimize()

dstl_end = time.time()
dstl_time= dstl_end-dstl_start

print("TIME: ", dstl_time)
dwstl_milp.model.write('dwstl2milp_milp.lp')
x_vals = [var.x for var in dwstl_milp.variables['x'].values()]
# y_vals = [var.x for var in dwstl_milp.variables['y'].values()]
# z_vals = [var.x for var in dwstl_milp.variables['z'].values()]
# print(x_vals, y_vals, z_vals)
# print(y_vals, z_vals)
print(x_vals)

