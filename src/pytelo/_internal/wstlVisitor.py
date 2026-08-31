# Generated from wstl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .wstlParser import wstlParser
else:
    from wstlParser import wstlParser

'''
 Copyright (c) 2023, Explainable Robotics Lab (ERL), Lehigh University
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile

 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
 See license.txt file for license information.
'''


# This class defines a complete generic visitor for a parse tree produced by wstlParser.

class wstlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by wstlParser#booleanPred.
    def visitBooleanPred(self, ctx:wstlParser.BooleanPredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wstlParser#longFormula.
    def visitLongFormula(self, ctx:wstlParser.LongFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wstlParser#formula.
    def visitFormula(self, ctx:wstlParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wstlParser#parprop.
    def visitParprop(self, ctx:wstlParser.ParpropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wstlParser#expr.
    def visitExpr(self, ctx:wstlParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wstlParser#booleanExpr.
    def visitBooleanExpr(self, ctx:wstlParser.BooleanExprContext):
        return self.visitChildren(ctx)



del wstlParser