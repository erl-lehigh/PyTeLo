# Generated from wstl.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


'''
 Copyright (c) 2023, Explainable Robotics Lab (ERL), Lehigh University
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile

 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @editor: Crockett L. Hensley
 See license.txt file for license information.
'''

def serializedATN():
    return [
        4,1,28,150,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,23,8,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,3,0,34,8,0,1,0,1,0,1,0,1,0,3,0,40,8,0,1,0,1,0,1,
        0,1,0,4,0,46,8,0,11,0,12,0,47,1,0,1,0,1,0,1,0,1,0,3,0,55,8,0,1,0,
        1,0,1,0,1,0,4,0,61,8,0,11,0,12,0,62,1,0,1,0,3,0,67,8,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,3,0,76,8,0,1,0,1,0,1,0,1,0,1,0,3,0,83,8,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,95,8,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,3,0,107,8,0,1,0,5,0,110,8,0,10,0,12,0,113,
        9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,127,8,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,138,8,1,10,1,12,1,141,9,
        1,1,2,1,2,1,2,1,2,1,2,3,2,148,8,2,1,2,0,2,0,2,3,0,2,4,0,4,2,0,1,
        1,7,7,1,0,8,9,1,0,10,11,1,0,12,16,174,0,66,1,0,0,0,2,126,1,0,0,0,
        4,147,1,0,0,0,6,7,6,0,-1,0,7,8,5,1,0,0,8,9,3,0,0,0,9,10,5,2,0,0,
        10,67,1,0,0,0,11,67,3,4,2,0,12,13,5,20,0,0,13,67,3,0,0,10,14,15,
        5,21,0,0,15,16,5,3,0,0,16,17,5,27,0,0,17,18,5,4,0,0,18,19,5,27,0,
        0,19,22,5,5,0,0,20,21,5,6,0,0,21,23,5,26,0,0,22,20,1,0,0,0,22,23,
        1,0,0,0,23,24,1,0,0,0,24,67,3,0,0,9,25,26,5,22,0,0,26,27,5,3,0,0,
        27,28,5,27,0,0,28,29,5,4,0,0,29,30,5,27,0,0,30,33,5,5,0,0,31,32,
        5,6,0,0,32,34,5,26,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,35,1,0,0,0,
        35,67,3,0,0,8,36,39,5,17,0,0,37,38,5,6,0,0,38,40,5,26,0,0,39,37,
        1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,1,0,0,42,45,3,0,0,0,
        43,44,5,4,0,0,44,46,3,0,0,0,45,43,1,0,0,0,46,47,1,0,0,0,47,45,1,
        0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,2,0,0,50,67,1,0,0,0,51,
        54,5,18,0,0,52,53,5,6,0,0,53,55,5,26,0,0,54,52,1,0,0,0,54,55,1,0,
        0,0,55,56,1,0,0,0,56,57,5,1,0,0,57,60,3,0,0,0,58,59,5,4,0,0,59,61,
        3,0,0,0,60,58,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,
        63,64,1,0,0,0,64,65,5,2,0,0,65,67,1,0,0,0,66,6,1,0,0,0,66,11,1,0,
        0,0,66,12,1,0,0,0,66,14,1,0,0,0,66,25,1,0,0,0,66,36,1,0,0,0,66,51,
        1,0,0,0,67,111,1,0,0,0,68,69,10,7,0,0,69,70,5,19,0,0,70,110,3,0,
        0,8,71,72,10,6,0,0,72,75,5,17,0,0,73,74,5,6,0,0,74,76,5,26,0,0,75,
        73,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,110,3,0,0,7,78,79,10,4,
        0,0,79,82,5,18,0,0,80,81,5,6,0,0,81,83,5,26,0,0,82,80,1,0,0,0,82,
        83,1,0,0,0,83,84,1,0,0,0,84,110,3,0,0,5,85,86,10,2,0,0,86,87,5,23,
        0,0,87,88,5,3,0,0,88,89,5,27,0,0,89,90,5,4,0,0,90,91,5,27,0,0,91,
        94,5,5,0,0,92,93,5,6,0,0,93,95,5,26,0,0,94,92,1,0,0,0,94,95,1,0,
        0,0,95,96,1,0,0,0,96,110,3,0,0,3,97,98,10,1,0,0,98,99,5,24,0,0,99,
        100,5,3,0,0,100,101,5,27,0,0,101,102,5,4,0,0,102,103,5,27,0,0,103,
        106,5,5,0,0,104,105,5,6,0,0,105,107,5,26,0,0,106,104,1,0,0,0,106,
        107,1,0,0,0,107,108,1,0,0,0,108,110,3,0,0,2,109,68,1,0,0,0,109,71,
        1,0,0,0,109,78,1,0,0,0,109,85,1,0,0,0,109,97,1,0,0,0,110,113,1,0,
        0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,1,1,0,0,0,113,111,1,0,0,
        0,114,115,6,1,-1,0,115,116,7,0,0,0,116,117,3,2,1,0,117,118,5,2,0,
        0,118,127,1,0,0,0,119,120,5,26,0,0,120,121,5,1,0,0,121,122,3,2,1,
        0,122,123,5,2,0,0,123,127,1,0,0,0,124,127,5,27,0,0,125,127,5,26,
        0,0,126,114,1,0,0,0,126,119,1,0,0,0,126,124,1,0,0,0,126,125,1,0,
        0,0,127,139,1,0,0,0,128,129,10,6,0,0,129,130,5,6,0,0,130,138,3,2,
        1,6,131,132,10,4,0,0,132,133,7,1,0,0,133,138,3,2,1,5,134,135,10,
        3,0,0,135,136,7,2,0,0,136,138,3,2,1,4,137,128,1,0,0,0,137,131,1,
        0,0,0,137,134,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,
        0,0,0,140,3,1,0,0,0,141,139,1,0,0,0,142,143,3,2,1,0,143,144,7,3,
        0,0,144,145,3,2,1,0,145,148,1,0,0,0,146,148,5,25,0,0,147,142,1,0,
        0,0,147,146,1,0,0,0,148,5,1,0,0,0,17,22,33,39,47,54,62,66,75,82,
        94,106,109,111,126,137,139,147
    ]

class wstlParser ( Parser ):

    grammarFileName = "wstl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "','", "']'", "'^'", 
                     "'-('", "'*'", "'/'", "'+'", "'-'", "'<'", "'<='", 
                     "'='", "'>='", "'>'", "<INVALID>", "<INVALID>", "'=>'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'U'", "'R'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "AND", "OR", "IMPLIES", "NOT", "EVENT", 
                      "ALWAYS", "UNTIL", "RELEASE", "BOOLEAN", "VARIABLE", 
                      "RATIONAL", "WS" ]

    RULE_wstlProperty = 0
    RULE_expr = 1
    RULE_booleanExpr = 2

    ruleNames =  [ "wstlProperty", "expr", "booleanExpr" ]

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
    RELEASE=24
    BOOLEAN=25
    VARIABLE=26
    RATIONAL=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class WstlPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return wstlParser.RULE_wstlProperty

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BooleanPredContext(WstlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a wstlParser.WstlPropertyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanExpr(self):
            return self.getTypedRuleContext(wstlParser.BooleanExprContext,0)


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


    class LongFormulaContext(WstlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a wstlParser.WstlPropertyContext
            super().__init__(parser)
            self.op = None # Token
            self.weight = None # Token
            self.copyFrom(ctx)

        def wstlProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(wstlParser.WstlPropertyContext)
            else:
                return self.getTypedRuleContext(wstlParser.WstlPropertyContext,i)

        def AND(self):
            return self.getToken(wstlParser.AND, 0)
        def VARIABLE(self):
            return self.getToken(wstlParser.VARIABLE, 0)
        def OR(self):
            return self.getToken(wstlParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLongFormula" ):
                listener.enterLongFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLongFormula" ):
                listener.exitLongFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLongFormula" ):
                return visitor.visitLongFormula(self)
            else:
                return visitor.visitChildren(self)


    class FormulaContext(WstlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a wstlParser.WstlPropertyContext
            super().__init__(parser)
            self.left = None # WstlPropertyContext
            self.op = None # Token
            self.child = None # WstlPropertyContext
            self.low = None # Token
            self.high = None # Token
            self.weight = None # Token
            self.right = None # WstlPropertyContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(wstlParser.NOT, 0)
        def wstlProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(wstlParser.WstlPropertyContext)
            else:
                return self.getTypedRuleContext(wstlParser.WstlPropertyContext,i)

        def EVENT(self):
            return self.getToken(wstlParser.EVENT, 0)
        def RATIONAL(self, i:int=None):
            if i is None:
                return self.getTokens(wstlParser.RATIONAL)
            else:
                return self.getToken(wstlParser.RATIONAL, i)
        def VARIABLE(self):
            return self.getToken(wstlParser.VARIABLE, 0)
        def ALWAYS(self):
            return self.getToken(wstlParser.ALWAYS, 0)
        def IMPLIES(self):
            return self.getToken(wstlParser.IMPLIES, 0)
        def AND(self):
            return self.getToken(wstlParser.AND, 0)
        def OR(self):
            return self.getToken(wstlParser.OR, 0)
        def UNTIL(self):
            return self.getToken(wstlParser.UNTIL, 0)
        def RELEASE(self):
            return self.getToken(wstlParser.RELEASE, 0)

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


    class ParpropContext(WstlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a wstlParser.WstlPropertyContext
            super().__init__(parser)
            self.child = None # WstlPropertyContext
            self.copyFrom(ctx)

        def wstlProperty(self):
            return self.getTypedRuleContext(wstlParser.WstlPropertyContext,0)


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



    def wstlProperty(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = wstlParser.WstlPropertyContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_wstlProperty, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = wstlParser.ParpropContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(wstlParser.T__0)
                self.state = 8
                localctx.child = self.wstlProperty(0)
                self.state = 9
                self.match(wstlParser.T__1)
                pass

            elif la_ == 2:
                localctx = wstlParser.BooleanPredContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.booleanExpr()
                pass

            elif la_ == 3:
                localctx = wstlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                localctx.op = self.match(wstlParser.NOT)
                self.state = 13
                localctx.child = self.wstlProperty(10)
                pass

            elif la_ == 4:
                localctx = wstlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                localctx.op = self.match(wstlParser.EVENT)
                self.state = 15
                self.match(wstlParser.T__2)
                self.state = 16
                localctx.low = self.match(wstlParser.RATIONAL)
                self.state = 17
                self.match(wstlParser.T__3)
                self.state = 18
                localctx.high = self.match(wstlParser.RATIONAL)
                self.state = 19
                self.match(wstlParser.T__4)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 20
                    self.match(wstlParser.T__5)
                    self.state = 21
                    localctx.weight = self.match(wstlParser.VARIABLE)


                self.state = 24
                localctx.child = self.wstlProperty(9)
                pass

            elif la_ == 5:
                localctx = wstlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                localctx.op = self.match(wstlParser.ALWAYS)
                self.state = 26
                self.match(wstlParser.T__2)
                self.state = 27
                localctx.low = self.match(wstlParser.RATIONAL)
                self.state = 28
                self.match(wstlParser.T__3)
                self.state = 29
                localctx.high = self.match(wstlParser.RATIONAL)
                self.state = 30
                self.match(wstlParser.T__4)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 31
                    self.match(wstlParser.T__5)
                    self.state = 32
                    localctx.weight = self.match(wstlParser.VARIABLE)


                self.state = 35
                localctx.child = self.wstlProperty(8)
                pass

            elif la_ == 6:
                localctx = wstlParser.LongFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                localctx.op = self.match(wstlParser.AND)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 37
                    self.match(wstlParser.T__5)
                    self.state = 38
                    localctx.weight = self.match(wstlParser.VARIABLE)


                self.state = 41
                self.match(wstlParser.T__0)
                self.state = 42
                self.wstlProperty(0)
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 43
                    self.match(wstlParser.T__3)
                    self.state = 44
                    self.wstlProperty(0)
                    self.state = 47 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==4):
                        break

                self.state = 49
                self.match(wstlParser.T__1)
                pass

            elif la_ == 7:
                localctx = wstlParser.LongFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                localctx.op = self.match(wstlParser.OR)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 52
                    self.match(wstlParser.T__5)
                    self.state = 53
                    localctx.weight = self.match(wstlParser.VARIABLE)


                self.state = 56
                self.match(wstlParser.T__0)
                self.state = 57
                self.wstlProperty(0)
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 58
                    self.match(wstlParser.T__3)
                    self.state = 59
                    self.wstlProperty(0)
                    self.state = 62 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==4):
                        break

                self.state = 64
                self.match(wstlParser.T__1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 111
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 109
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = wstlParser.FormulaContext(self, wstlParser.WstlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wstlProperty)
                        self.state = 68
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 69
                        localctx.op = self.match(wstlParser.IMPLIES)
                        self.state = 70
                        localctx.right = self.wstlProperty(8)
                        pass

                    elif la_ == 2:
                        localctx = wstlParser.FormulaContext(self, wstlParser.WstlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wstlProperty)
                        self.state = 71
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 72
                        localctx.op = self.match(wstlParser.AND)
                        self.state = 75
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==6:
                            self.state = 73
                            self.match(wstlParser.T__5)
                            self.state = 74
                            localctx.weight = self.match(wstlParser.VARIABLE)


                        self.state = 77
                        localctx.right = self.wstlProperty(7)
                        pass

                    elif la_ == 3:
                        localctx = wstlParser.FormulaContext(self, wstlParser.WstlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wstlProperty)
                        self.state = 78
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 79
                        localctx.op = self.match(wstlParser.OR)
                        self.state = 82
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==6:
                            self.state = 80
                            self.match(wstlParser.T__5)
                            self.state = 81
                            localctx.weight = self.match(wstlParser.VARIABLE)


                        self.state = 84
                        localctx.right = self.wstlProperty(5)
                        pass

                    elif la_ == 4:
                        localctx = wstlParser.FormulaContext(self, wstlParser.WstlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wstlProperty)
                        self.state = 85
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 86
                        localctx.op = self.match(wstlParser.UNTIL)
                        self.state = 87
                        self.match(wstlParser.T__2)
                        self.state = 88
                        localctx.low = self.match(wstlParser.RATIONAL)
                        self.state = 89
                        self.match(wstlParser.T__3)
                        self.state = 90
                        localctx.high = self.match(wstlParser.RATIONAL)
                        self.state = 91
                        self.match(wstlParser.T__4)
                        self.state = 94
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==6:
                            self.state = 92
                            self.match(wstlParser.T__5)
                            self.state = 93
                            localctx.weight = self.match(wstlParser.VARIABLE)


                        self.state = 96
                        localctx.right = self.wstlProperty(3)
                        pass

                    elif la_ == 5:
                        localctx = wstlParser.FormulaContext(self, wstlParser.WstlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wstlProperty)
                        self.state = 97
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 98
                        localctx.op = self.match(wstlParser.RELEASE)
                        self.state = 99
                        self.match(wstlParser.T__2)
                        self.state = 100
                        localctx.low = self.match(wstlParser.RATIONAL)
                        self.state = 101
                        self.match(wstlParser.T__3)
                        self.state = 102
                        localctx.high = self.match(wstlParser.RATIONAL)
                        self.state = 103
                        self.match(wstlParser.T__4)
                        self.state = 106
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==6:
                            self.state = 104
                            self.match(wstlParser.T__5)
                            self.state = 105
                            localctx.weight = self.match(wstlParser.VARIABLE)


                        self.state = 108
                        localctx.right = self.wstlProperty(2)
                        pass

             
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
                return self.getTypedRuleContexts(wstlParser.ExprContext)
            else:
                return self.getTypedRuleContext(wstlParser.ExprContext,i)


        def VARIABLE(self):
            return self.getToken(wstlParser.VARIABLE, 0)

        def RATIONAL(self):
            return self.getToken(wstlParser.RATIONAL, 0)

        def getRuleIndex(self):
            return wstlParser.RULE_expr

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
        localctx = wstlParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 115
                _la = self._input.LA(1)
                if not(_la==1 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 116
                self.expr(0)
                self.state = 117
                self.match(wstlParser.T__1)
                pass

            elif la_ == 2:
                self.state = 119
                self.match(wstlParser.VARIABLE)
                self.state = 120
                self.match(wstlParser.T__0)
                self.state = 121
                self.expr(0)
                self.state = 122
                self.match(wstlParser.T__1)
                pass

            elif la_ == 3:
                self.state = 124
                self.match(wstlParser.RATIONAL)
                pass

            elif la_ == 4:
                self.state = 125
                self.match(wstlParser.VARIABLE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 137
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = wstlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 129
                        self.match(wstlParser.T__5)
                        self.state = 130
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = wstlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 131
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 132
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 133
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = wstlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 134
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 135
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 136
                        self.expr(4)
                        pass

             
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
                return self.getTypedRuleContexts(wstlParser.ExprContext)
            else:
                return self.getTypedRuleContext(wstlParser.ExprContext,i)


        def BOOLEAN(self):
            return self.getToken(wstlParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return wstlParser.RULE_booleanExpr

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

        localctx = wstlParser.BooleanExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_booleanExpr)
        self._la = 0 # Token type
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 7, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                localctx.left = self.expr(0)
                self.state = 143
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 144
                localctx.right = self.expr(0)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                localctx.op = self.match(wstlParser.BOOLEAN)
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
        self._predicates[0] = self.wstlProperty_sempred
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def wstlProperty_sempred(self, localctx:WstlPropertyContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         




