# Generated from wmtl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .wmtlParser import wmtlParser
else:
    from pytelo._internal.wmtlParser import wmtlParser

'''
 Copyright (c) 2023, Explainable Robotics Lab (ERL)
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
'''


# This class defines a complete generic visitor for a parse tree produced by wmtlParser.

class wmtlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by wmtlParser#booleanPred.
    def visitBooleanPred(self, ctx:wmtlParser.BooleanPredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wmtlParser#longFormula.
    def visitLongFormula(self, ctx:wmtlParser.LongFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wmtlParser#formula.
    def visitFormula(self, ctx:wmtlParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wmtlParser#parprop.
    def visitParprop(self, ctx:wmtlParser.ParpropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wmtlParser#booleanExpr.
    def visitBooleanExpr(self, ctx:wmtlParser.BooleanExprContext):
        return self.visitChildren(ctx)



del wmtlParser