# Generated from wstl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .wstlParser import wstlParser
else:
    from pytelo._internal.wstlParser import wstlParser

'''
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
'''


# This class defines a complete listener for a parse tree produced by wstlParser.
class wstlListener(ParseTreeListener):

    # Enter a parse tree produced by wstlParser#booleanPred.
    def enterBooleanPred(self, ctx:wstlParser.BooleanPredContext):
        pass

    # Exit a parse tree produced by wstlParser#booleanPred.
    def exitBooleanPred(self, ctx:wstlParser.BooleanPredContext):
        pass


    # Enter a parse tree produced by wstlParser#longFormula.
    def enterLongFormula(self, ctx:wstlParser.LongFormulaContext):
        pass

    # Exit a parse tree produced by wstlParser#longFormula.
    def exitLongFormula(self, ctx:wstlParser.LongFormulaContext):
        pass


    # Enter a parse tree produced by wstlParser#formula.
    def enterFormula(self, ctx:wstlParser.FormulaContext):
        pass

    # Exit a parse tree produced by wstlParser#formula.
    def exitFormula(self, ctx:wstlParser.FormulaContext):
        pass


    # Enter a parse tree produced by wstlParser#parprop.
    def enterParprop(self, ctx:wstlParser.ParpropContext):
        pass

    # Exit a parse tree produced by wstlParser#parprop.
    def exitParprop(self, ctx:wstlParser.ParpropContext):
        pass


    # Enter a parse tree produced by wstlParser#expr.
    def enterExpr(self, ctx:wstlParser.ExprContext):
        pass

    # Exit a parse tree produced by wstlParser#expr.
    def exitExpr(self, ctx:wstlParser.ExprContext):
        pass


    # Enter a parse tree produced by wstlParser#booleanExpr.
    def enterBooleanExpr(self, ctx:wstlParser.BooleanExprContext):
        pass

    # Exit a parse tree produced by wstlParser#booleanExpr.
    def exitBooleanExpr(self, ctx:wstlParser.BooleanExprContext):
        pass



del wstlParser