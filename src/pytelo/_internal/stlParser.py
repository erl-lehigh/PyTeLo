# Generated from stl.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


'''
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''

def serializedATN():
    return [
        4,1,27,88,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,29,
        8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,65,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,5,1,76,8,1,10,1,12,1,79,9,1,1,2,1,2,1,2,1,2,1,2,3,2,86,8,2,1,2,
        0,2,0,2,3,0,2,4,0,4,2,0,1,1,6,6,1,0,8,9,1,0,10,11,1,0,12,16,99,0,
        28,1,0,0,0,2,64,1,0,0,0,4,85,1,0,0,0,6,7,6,0,-1,0,7,8,5,1,0,0,8,
        9,3,0,0,0,9,10,5,2,0,0,10,29,1,0,0,0,11,29,3,4,2,0,12,13,5,20,0,
        0,13,29,3,0,0,7,14,15,5,21,0,0,15,16,5,3,0,0,16,17,5,26,0,0,17,18,
        5,4,0,0,18,19,5,26,0,0,19,20,5,5,0,0,20,29,3,0,0,6,21,22,5,22,0,
        0,22,23,5,3,0,0,23,24,5,26,0,0,24,25,5,4,0,0,25,26,5,26,0,0,26,27,
        5,5,0,0,27,29,3,0,0,5,28,6,1,0,0,0,28,11,1,0,0,0,28,12,1,0,0,0,28,
        14,1,0,0,0,28,21,1,0,0,0,29,49,1,0,0,0,30,31,10,4,0,0,31,32,5,19,
        0,0,32,48,3,0,0,5,33,34,10,3,0,0,34,35,5,17,0,0,35,48,3,0,0,4,36,
        37,10,2,0,0,37,38,5,18,0,0,38,48,3,0,0,3,39,40,10,1,0,0,40,41,5,
        23,0,0,41,42,5,3,0,0,42,43,5,26,0,0,43,44,5,4,0,0,44,45,5,26,0,0,
        45,46,5,5,0,0,46,48,3,0,0,2,47,30,1,0,0,0,47,33,1,0,0,0,47,36,1,
        0,0,0,47,39,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,
        1,1,0,0,0,51,49,1,0,0,0,52,53,6,1,-1,0,53,54,7,0,0,0,54,55,3,2,1,
        0,55,56,5,2,0,0,56,65,1,0,0,0,57,58,5,25,0,0,58,59,5,1,0,0,59,60,
        3,2,1,0,60,61,5,2,0,0,61,65,1,0,0,0,62,65,5,26,0,0,63,65,5,25,0,
        0,64,52,1,0,0,0,64,57,1,0,0,0,64,62,1,0,0,0,64,63,1,0,0,0,65,77,
        1,0,0,0,66,67,10,6,0,0,67,68,5,7,0,0,68,76,3,2,1,6,69,70,10,4,0,
        0,70,71,7,1,0,0,71,76,3,2,1,5,72,73,10,3,0,0,73,74,7,2,0,0,74,76,
        3,2,1,4,75,66,1,0,0,0,75,69,1,0,0,0,75,72,1,0,0,0,76,79,1,0,0,0,
        77,75,1,0,0,0,77,78,1,0,0,0,78,3,1,0,0,0,79,77,1,0,0,0,80,81,3,2,
        1,0,81,82,7,3,0,0,82,83,3,2,1,0,83,86,1,0,0,0,84,86,5,24,0,0,85,
        80,1,0,0,0,85,84,1,0,0,0,86,5,1,0,0,0,7,28,47,49,64,75,77,85
    ]

class stlParser ( Parser ):

    grammarFileName = "stl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "','", "']'", "'-('", 
                     "'^'", "'*'", "'/'", "'+'", "'-'", "'<'", "'<='", "'='", 
                     "'>='", "'>'", "<INVALID>", "<INVALID>", "'=>'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'U'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "AND", "OR", "IMPLIES", "NOT", "EVENT", 
                      "ALWAYS", "UNTIL", "BOOLEAN", "VARIABLE", "RATIONAL", 
                      "WS" ]

    RULE_stlProperty = 0
    RULE_expr = 1
    RULE_booleanExpr = 2

    ruleNames =  [ "stlProperty", "expr", "booleanExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    AND=17
    OR=18
    IMPLIES=19
    NOT=20
    EVENT=21
    ALWAYS=22
    UNTIL=23
    BOOLEAN=24
    VARIABLE=25
    RATIONAL=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StlPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stlParser.RULE_stlProperty

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BooleanPredContext(StlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.StlPropertyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanExpr(self):
            return self.getTypedRuleContext(stlParser.BooleanExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanPred" ):
                listener.enterBooleanPred(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanPred" ):
                listener.exitBooleanPred(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanPred" ):
                return visitor.visitBooleanPred(self)
            else:
                return visitor.visitChildren(self)


    class FormulaContext(StlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.StlPropertyContext
            super().__init__(parser)
            self.left = None # StlPropertyContext
            self.op = None # Token
            self.child = None # StlPropertyContext
            self.low = None # Token
            self.high = None # Token
            self.right = None # StlPropertyContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(stlParser.NOT, 0)
        def stlProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.StlPropertyContext)
            else:
                return self.getTypedRuleContext(stlParser.StlPropertyContext,i)

        def EVENT(self):
            return self.getToken(stlParser.EVENT, 0)
        def RATIONAL(self, i:int=None):
            if i is None:
                return self.getTokens(stlParser.RATIONAL)
            else:
                return self.getToken(stlParser.RATIONAL, i)
        def ALWAYS(self):
            return self.getToken(stlParser.ALWAYS, 0)
        def IMPLIES(self):
            return self.getToken(stlParser.IMPLIES, 0)
        def AND(self):
            return self.getToken(stlParser.AND, 0)
        def OR(self):
            return self.getToken(stlParser.OR, 0)
        def UNTIL(self):
            return self.getToken(stlParser.UNTIL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormula" ):
                return visitor.visitFormula(self)
            else:
                return visitor.visitChildren(self)


    class ParpropContext(StlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stlParser.StlPropertyContext
            super().__init__(parser)
            self.child = None # StlPropertyContext
            self.copyFrom(ctx)

        def stlProperty(self):
            return self.getTypedRuleContext(stlParser.StlPropertyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParprop" ):
                listener.enterParprop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParprop" ):
                listener.exitParprop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParprop" ):
                return visitor.visitParprop(self)
            else:
                return visitor.visitChildren(self)



    def stlProperty(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = stlParser.StlPropertyContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_stlProperty, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = stlParser.ParpropContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(stlParser.T__0)
                self.state = 8
                localctx.child = self.stlProperty(0)
                self.state = 9
                self.match(stlParser.T__1)
                pass

            elif la_ == 2:
                localctx = stlParser.BooleanPredContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.booleanExpr()
                pass

            elif la_ == 3:
                localctx = stlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                localctx.op = self.match(stlParser.NOT)
                self.state = 13
                localctx.child = self.stlProperty(7)
                pass

            elif la_ == 4:
                localctx = stlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                localctx.op = self.match(stlParser.EVENT)
                self.state = 15
                self.match(stlParser.T__2)
                self.state = 16
                localctx.low = self.match(stlParser.RATIONAL)
                self.state = 17
                self.match(stlParser.T__3)
                self.state = 18
                localctx.high = self.match(stlParser.RATIONAL)
                self.state = 19
                self.match(stlParser.T__4)
                self.state = 20
                localctx.child = self.stlProperty(6)
                pass

            elif la_ == 5:
                localctx = stlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                localctx.op = self.match(stlParser.ALWAYS)
                self.state = 22
                self.match(stlParser.T__2)
                self.state = 23
                localctx.low = self.match(stlParser.RATIONAL)
                self.state = 24
                self.match(stlParser.T__3)
                self.state = 25
                localctx.high = self.match(stlParser.RATIONAL)
                self.state = 26
                self.match(stlParser.T__4)
                self.state = 27
                localctx.child = self.stlProperty(5)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 47
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = stlParser.FormulaContext(self, stlParser.StlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_stlProperty)
                        self.state = 30
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 31
                        localctx.op = self.match(stlParser.IMPLIES)
                        self.state = 32
                        localctx.right = self.stlProperty(5)
                        pass

                    elif la_ == 2:
                        localctx = stlParser.FormulaContext(self, stlParser.StlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_stlProperty)
                        self.state = 33
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 34
                        localctx.op = self.match(stlParser.AND)
                        self.state = 35
                        localctx.right = self.stlProperty(4)
                        pass

                    elif la_ == 3:
                        localctx = stlParser.FormulaContext(self, stlParser.StlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_stlProperty)
                        self.state = 36
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 37
                        localctx.op = self.match(stlParser.OR)
                        self.state = 38
                        localctx.right = self.stlProperty(3)
                        pass

                    elif la_ == 4:
                        localctx = stlParser.FormulaContext(self, stlParser.StlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_stlProperty)
                        self.state = 39
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 40
                        localctx.op = self.match(stlParser.UNTIL)
                        self.state = 41
                        self.match(stlParser.T__2)
                        self.state = 42
                        localctx.low = self.match(stlParser.RATIONAL)
                        self.state = 43
                        self.match(stlParser.T__3)
                        self.state = 44
                        localctx.high = self.match(stlParser.RATIONAL)
                        self.state = 45
                        self.match(stlParser.T__4)
                        self.state = 46
                        localctx.right = self.stlProperty(2)
                        pass

             
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.ExprContext)
            else:
                return self.getTypedRuleContext(stlParser.ExprContext,i)


        def VARIABLE(self):
            return self.getToken(stlParser.VARIABLE, 0)

        def RATIONAL(self):
            return self.getToken(stlParser.RATIONAL, 0)

        def getRuleIndex(self):
            return stlParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = stlParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 53
                _la = self._input.LA(1)
                if not(_la==1 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 54
                self.expr(0)
                self.state = 55
                self.match(stlParser.T__1)
                pass

            elif la_ == 2:
                self.state = 57
                self.match(stlParser.VARIABLE)
                self.state = 58
                self.match(stlParser.T__0)
                self.state = 59
                self.expr(0)
                self.state = 60
                self.match(stlParser.T__1)
                pass

            elif la_ == 3:
                self.state = 62
                self.match(stlParser.RATIONAL)
                pass

            elif la_ == 4:
                self.state = 63
                self.match(stlParser.VARIABLE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 75
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = stlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 67
                        self.match(stlParser.T__6)
                        self.state = 68
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = stlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 70
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = stlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 73
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        self.expr(4)
                        pass

             
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BooleanExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stlParser.ExprContext)
            else:
                return self.getTypedRuleContext(stlParser.ExprContext,i)


        def BOOLEAN(self):
            return self.getToken(stlParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return stlParser.RULE_booleanExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpr" ):
                listener.enterBooleanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpr" ):
                listener.exitBooleanExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanExpr" ):
                return visitor.visitBooleanExpr(self)
            else:
                return visitor.visitChildren(self)




    def booleanExpr(self):

        localctx = stlParser.BooleanExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_booleanExpr)
        self._la = 0 # Token type
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 6, 25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                localctx.left = self.expr(0)
                self.state = 81
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 82
                localctx.right = self.expr(0)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                localctx.op = self.match(stlParser.BOOLEAN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.stlProperty_sempred
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def stlProperty_sempred(self, localctx:StlPropertyContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




