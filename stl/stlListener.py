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


# This class defines a complete listener for a parse tree produced by stlParser.
class stlListener(ParseTreeListener):

    # Enter a parse tree produced by stlParser#booleanPred.
    def enterBooleanPred(self, ctx:stlParser.BooleanPredContext):
        pass

    # Exit a parse tree produced by stlParser#booleanPred.
    def exitBooleanPred(self, ctx:stlParser.BooleanPredContext):
        pass


    # Enter a parse tree produced by stlParser#formula.
    def enterFormula(self, ctx:stlParser.FormulaContext):
        pass

    # Exit a parse tree produced by stlParser#formula.
    def exitFormula(self, ctx:stlParser.FormulaContext):
        pass


    # Enter a parse tree produced by stlParser#parprop.
    def enterParprop(self, ctx:stlParser.ParpropContext):
        pass

    # Exit a parse tree produced by stlParser#parprop.
    def exitParprop(self, ctx:stlParser.ParpropContext):
        pass


    # Enter a parse tree produced by stlParser#expr.
    def enterExpr(self, ctx:stlParser.ExprContext):
        pass

    # Exit a parse tree produced by stlParser#expr.
    def exitExpr(self, ctx:stlParser.ExprContext):
        pass


    # Enter a parse tree produced by stlParser#booleanExpr.
    def enterBooleanExpr(self, ctx:stlParser.BooleanExprContext):
        pass

    # Exit a parse tree produced by stlParser#booleanExpr.
    def exitBooleanExpr(self, ctx:stlParser.BooleanExprContext):
        pass



del stlParser