# Generated from stl.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .stlParser import stlParser
else:
    from stlParser import stlParser

'''
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''


# This class defines a complete generic visitor for a parse tree produced by stlParser.

class stlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by stlParser#booleanPred.
    def visitBooleanPred(self, ctx:stlParser.BooleanPredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#formula.
    def visitFormula(self, ctx:stlParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#parprop.
    def visitParprop(self, ctx:stlParser.ParpropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#expr.
    def visitExpr(self, ctx:stlParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#booleanExpr.
    def visitBooleanExpr(self, ctx:stlParser.BooleanExprContext):
        return self.visitChildren(ctx)



del stlParser