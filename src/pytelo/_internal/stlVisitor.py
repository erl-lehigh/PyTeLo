# Generated from stl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .stlParser import stlParser
else:
    from stlParser import stlParser

'''
 Copyright (c) 2015-2020 
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab (ERL), Lehigh University
 @author: Cristian Ioan Vasile <cvasile@lehigh.edu>

 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
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