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


# This class defines a complete listener for a parse tree produced by wmtlParser.
class wmtlListener(ParseTreeListener):

    # Enter a parse tree produced by wmtlParser#booleanPred.
    def enterBooleanPred(self, ctx:wmtlParser.BooleanPredContext):
        pass

    # Exit a parse tree produced by wmtlParser#booleanPred.
    def exitBooleanPred(self, ctx:wmtlParser.BooleanPredContext):
        pass


    # Enter a parse tree produced by wmtlParser#longFormula.
    def enterLongFormula(self, ctx:wmtlParser.LongFormulaContext):
        pass

    # Exit a parse tree produced by wmtlParser#longFormula.
    def exitLongFormula(self, ctx:wmtlParser.LongFormulaContext):
        pass


    # Enter a parse tree produced by wmtlParser#formula.
    def enterFormula(self, ctx:wmtlParser.FormulaContext):
        pass

    # Exit a parse tree produced by wmtlParser#formula.
    def exitFormula(self, ctx:wmtlParser.FormulaContext):
        pass


    # Enter a parse tree produced by wmtlParser#parprop.
    def enterParprop(self, ctx:wmtlParser.ParpropContext):
        pass

    # Exit a parse tree produced by wmtlParser#parprop.
    def exitParprop(self, ctx:wmtlParser.ParpropContext):
        pass


    # Enter a parse tree produced by wmtlParser#booleanExpr.
    def enterBooleanExpr(self, ctx:wmtlParser.BooleanExprContext):
        pass

    # Exit a parse tree produced by wmtlParser#booleanExpr.
    def exitBooleanExpr(self, ctx:wmtlParser.BooleanExprContext):
        pass



del wmtlParser