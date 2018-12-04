#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 17:07:07 2018

@author: sadra
"""
from antlr4 import InputStream, CommonTokenStream

import sys
sys.path.append('..')

from stl import Operation, RelOperation, STLFormula
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor

from stl import STLAbstractSyntaxTreeExtractor


lexer = stlLexer(InputStream("!(x < 10) && F[0, 2] y > 2 || G[1, 3] z<=8"))
tokens = CommonTokenStream(lexer)
parser = stlParser(tokens)
t = parser.stlProperty()
print(t.toStringTree())
ast = STLAbstractSyntaxTreeExtractor().visit(t)
print('AST:', ast)