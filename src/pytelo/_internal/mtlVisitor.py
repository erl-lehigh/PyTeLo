# Generated from mtl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .mtlParser import mtlParser
else:
    from mtlParser import mtlParser

'''
 Copyright (c) 2023, Explainable Robotics Lab (ERL), Lehigh University
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
 See license.txt file for license information.
'''


# This class defines a complete generic visitor for a parse tree produced by mtlParser.

class mtlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mtlParser#booleanPred.
    def visitBooleanPred(self, ctx:mtlParser.BooleanPredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mtlParser#formula.
    def visitFormula(self, ctx:mtlParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mtlParser#parprop.
    def visitParprop(self, ctx:mtlParser.ParpropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mtlParser#booleanExpr.
    def visitBooleanExpr(self, ctx:mtlParser.BooleanExprContext):
        return self.visitChildren(ctx)



del mtlParser