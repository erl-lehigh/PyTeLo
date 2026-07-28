# Generated from mtl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .mtlParser import mtlParser
else:
    from pytelo._internal.mtlParser import mtlParser

'''
 Copyright (c) 2023, Explainable Robotics Lab (ERL)
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
'''


# This class defines a complete listener for a parse tree produced by mtlParser.
class mtlListener(ParseTreeListener):

    # Enter a parse tree produced by mtlParser#booleanPred.
    def enterBooleanPred(self, ctx:mtlParser.BooleanPredContext):
        pass

    # Exit a parse tree produced by mtlParser#booleanPred.
    def exitBooleanPred(self, ctx:mtlParser.BooleanPredContext):
        pass


    # Enter a parse tree produced by mtlParser#formula.
    def enterFormula(self, ctx:mtlParser.FormulaContext):
        pass

    # Exit a parse tree produced by mtlParser#formula.
    def exitFormula(self, ctx:mtlParser.FormulaContext):
        pass


    # Enter a parse tree produced by mtlParser#parprop.
    def enterParprop(self, ctx:mtlParser.ParpropContext):
        pass

    # Exit a parse tree produced by mtlParser#parprop.
    def exitParprop(self, ctx:mtlParser.ParpropContext):
        pass


    # Enter a parse tree produced by mtlParser#booleanExpr.
    def enterBooleanExpr(self, ctx:mtlParser.BooleanExprContext):
        pass

    # Exit a parse tree produced by mtlParser#booleanExpr.
    def exitBooleanExpr(self, ctx:mtlParser.BooleanExprContext):
        pass



del mtlParser