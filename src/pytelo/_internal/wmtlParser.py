# Generated from wmtl.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


'''
 Copyright (c) 2023, Explainable Robotics Lab (ERL)
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
'''

def serializedATN():
    return [
        4,1,17,105,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,21,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,3,0,32,8,0,1,0,1,0,1,0,1,0,3,0,38,8,0,1,0,1,0,1,0,1,0,4,
        0,44,8,0,11,0,12,0,45,1,0,1,0,1,0,1,0,1,0,3,0,53,8,0,1,0,1,0,1,0,
        1,0,4,0,59,8,0,11,0,12,0,60,1,0,1,0,3,0,65,8,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,3,0,74,8,0,1,0,1,0,1,0,1,0,1,0,3,0,81,8,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,93,8,0,1,0,5,0,96,8,0,10,0,12,0,
        99,9,0,1,1,1,1,3,1,103,8,1,1,1,0,1,0,2,0,2,0,0,122,0,64,1,0,0,0,
        2,102,1,0,0,0,4,5,6,0,-1,0,5,6,5,1,0,0,6,7,3,0,0,0,7,8,5,2,0,0,8,
        65,1,0,0,0,9,65,3,2,1,0,10,11,5,10,0,0,11,65,3,0,0,9,12,13,5,11,
        0,0,13,14,5,3,0,0,14,15,5,16,0,0,15,16,5,4,0,0,16,17,5,16,0,0,17,
        20,5,5,0,0,18,19,5,6,0,0,19,21,5,15,0,0,20,18,1,0,0,0,20,21,1,0,
        0,0,21,22,1,0,0,0,22,65,3,0,0,8,23,24,5,12,0,0,24,25,5,3,0,0,25,
        26,5,16,0,0,26,27,5,4,0,0,27,28,5,16,0,0,28,31,5,5,0,0,29,30,5,6,
        0,0,30,32,5,15,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,0,33,
        65,3,0,0,7,34,37,5,7,0,0,35,36,5,6,0,0,36,38,5,15,0,0,37,35,1,0,
        0,0,37,38,1,0,0,0,38,39,1,0,0,0,39,40,5,1,0,0,40,43,3,0,0,0,41,42,
        5,4,0,0,42,44,3,0,0,0,43,41,1,0,0,0,44,45,1,0,0,0,45,43,1,0,0,0,
        45,46,1,0,0,0,46,47,1,0,0,0,47,48,5,2,0,0,48,65,1,0,0,0,49,52,5,
        8,0,0,50,51,5,6,0,0,51,53,5,15,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,
        54,1,0,0,0,54,55,5,1,0,0,55,58,3,0,0,0,56,57,5,4,0,0,57,59,3,0,0,
        0,58,56,1,0,0,0,59,60,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,62,
        1,0,0,0,62,63,5,2,0,0,63,65,1,0,0,0,64,4,1,0,0,0,64,9,1,0,0,0,64,
        10,1,0,0,0,64,12,1,0,0,0,64,23,1,0,0,0,64,34,1,0,0,0,64,49,1,0,0,
        0,65,97,1,0,0,0,66,67,10,6,0,0,67,68,5,9,0,0,68,96,3,0,0,7,69,70,
        10,5,0,0,70,73,5,7,0,0,71,72,5,6,0,0,72,74,5,15,0,0,73,71,1,0,0,
        0,73,74,1,0,0,0,74,75,1,0,0,0,75,96,3,0,0,6,76,77,10,3,0,0,77,80,
        5,8,0,0,78,79,5,6,0,0,79,81,5,15,0,0,80,78,1,0,0,0,80,81,1,0,0,0,
        81,82,1,0,0,0,82,96,3,0,0,4,83,84,10,1,0,0,84,85,5,13,0,0,85,86,
        5,3,0,0,86,87,5,16,0,0,87,88,5,4,0,0,88,89,5,16,0,0,89,92,5,5,0,
        0,90,91,5,6,0,0,91,93,5,15,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,94,
        1,0,0,0,94,96,3,0,0,2,95,66,1,0,0,0,95,69,1,0,0,0,95,76,1,0,0,0,
        95,83,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,1,1,0,
        0,0,99,97,1,0,0,0,100,103,5,15,0,0,101,103,5,14,0,0,102,100,1,0,
        0,0,102,101,1,0,0,0,103,3,1,0,0,0,13,20,31,37,45,52,60,64,73,80,
        92,95,97,102
    ]

class wmtlParser ( Parser ):

    grammarFileName = "wmtl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "','", "']'", "'^'", 
                     "<INVALID>", "<INVALID>", "'=>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'U'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "AND", "OR", 
                      "IMPLIES", "NOT", "EVENT", "ALWAYS", "UNTIL", "BOOLEAN", 
                      "VARIABLE", "RATIONAL", "WS" ]

    RULE_wmtlProperty = 0
    RULE_booleanExpr = 1

    ruleNames =  [ "wmtlProperty", "booleanExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    AND=7
    OR=8
    IMPLIES=9
    NOT=10
    EVENT=11
    ALWAYS=12
    UNTIL=13
    BOOLEAN=14
    VARIABLE=15
    RATIONAL=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class WmtlPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return wmtlParser.RULE_wmtlProperty

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BooleanPredContext(WmtlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a wmtlParser.WmtlPropertyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanExpr(self):
            return self.getTypedRuleContext(wmtlParser.BooleanExprContext,0)


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


    class LongFormulaContext(WmtlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a wmtlParser.WmtlPropertyContext
            super().__init__(parser)
            self.op = None # Token
            self.weight = None # Token
            self.copyFrom(ctx)

        def wmtlProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(wmtlParser.WmtlPropertyContext)
            else:
                return self.getTypedRuleContext(wmtlParser.WmtlPropertyContext,i)

        def AND(self):
            return self.getToken(wmtlParser.AND, 0)
        def VARIABLE(self):
            return self.getToken(wmtlParser.VARIABLE, 0)
        def OR(self):
            return self.getToken(wmtlParser.OR, 0)

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


    class FormulaContext(WmtlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a wmtlParser.WmtlPropertyContext
            super().__init__(parser)
            self.left = None # WmtlPropertyContext
            self.op = None # Token
            self.child = None # WmtlPropertyContext
            self.low = None # Token
            self.high = None # Token
            self.weight = None # Token
            self.right = None # WmtlPropertyContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(wmtlParser.NOT, 0)
        def wmtlProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(wmtlParser.WmtlPropertyContext)
            else:
                return self.getTypedRuleContext(wmtlParser.WmtlPropertyContext,i)

        def EVENT(self):
            return self.getToken(wmtlParser.EVENT, 0)
        def RATIONAL(self, i:int=None):
            if i is None:
                return self.getTokens(wmtlParser.RATIONAL)
            else:
                return self.getToken(wmtlParser.RATIONAL, i)
        def VARIABLE(self):
            return self.getToken(wmtlParser.VARIABLE, 0)
        def ALWAYS(self):
            return self.getToken(wmtlParser.ALWAYS, 0)
        def IMPLIES(self):
            return self.getToken(wmtlParser.IMPLIES, 0)
        def AND(self):
            return self.getToken(wmtlParser.AND, 0)
        def OR(self):
            return self.getToken(wmtlParser.OR, 0)
        def UNTIL(self):
            return self.getToken(wmtlParser.UNTIL, 0)

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


    class ParpropContext(WmtlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a wmtlParser.WmtlPropertyContext
            super().__init__(parser)
            self.child = None # WmtlPropertyContext
            self.copyFrom(ctx)

        def wmtlProperty(self):
            return self.getTypedRuleContext(wmtlParser.WmtlPropertyContext,0)


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



    def wmtlProperty(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = wmtlParser.WmtlPropertyContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_wmtlProperty, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = wmtlParser.ParpropContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                self.match(wmtlParser.T__0)
                self.state = 6
                localctx.child = self.wmtlProperty(0)
                self.state = 7
                self.match(wmtlParser.T__1)
                pass
            elif token in [14, 15]:
                localctx = wmtlParser.BooleanPredContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.booleanExpr()
                pass
            elif token in [10]:
                localctx = wmtlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                localctx.op = self.match(wmtlParser.NOT)
                self.state = 11
                localctx.child = self.wmtlProperty(9)
                pass
            elif token in [11]:
                localctx = wmtlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                localctx.op = self.match(wmtlParser.EVENT)
                self.state = 13
                self.match(wmtlParser.T__2)
                self.state = 14
                localctx.low = self.match(wmtlParser.RATIONAL)
                self.state = 15
                self.match(wmtlParser.T__3)
                self.state = 16
                localctx.high = self.match(wmtlParser.RATIONAL)
                self.state = 17
                self.match(wmtlParser.T__4)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 18
                    self.match(wmtlParser.T__5)
                    self.state = 19
                    localctx.weight = self.match(wmtlParser.VARIABLE)


                self.state = 22
                localctx.child = self.wmtlProperty(8)
                pass
            elif token in [12]:
                localctx = wmtlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                localctx.op = self.match(wmtlParser.ALWAYS)
                self.state = 24
                self.match(wmtlParser.T__2)
                self.state = 25
                localctx.low = self.match(wmtlParser.RATIONAL)
                self.state = 26
                self.match(wmtlParser.T__3)
                self.state = 27
                localctx.high = self.match(wmtlParser.RATIONAL)
                self.state = 28
                self.match(wmtlParser.T__4)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 29
                    self.match(wmtlParser.T__5)
                    self.state = 30
                    localctx.weight = self.match(wmtlParser.VARIABLE)


                self.state = 33
                localctx.child = self.wmtlProperty(7)
                pass
            elif token in [7]:
                localctx = wmtlParser.LongFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                localctx.op = self.match(wmtlParser.AND)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 35
                    self.match(wmtlParser.T__5)
                    self.state = 36
                    localctx.weight = self.match(wmtlParser.VARIABLE)


                self.state = 39
                self.match(wmtlParser.T__0)
                self.state = 40
                self.wmtlProperty(0)
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 41
                    self.match(wmtlParser.T__3)
                    self.state = 42
                    self.wmtlProperty(0)
                    self.state = 45 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==4):
                        break

                self.state = 47
                self.match(wmtlParser.T__1)
                pass
            elif token in [8]:
                localctx = wmtlParser.LongFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                localctx.op = self.match(wmtlParser.OR)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 50
                    self.match(wmtlParser.T__5)
                    self.state = 51
                    localctx.weight = self.match(wmtlParser.VARIABLE)


                self.state = 54
                self.match(wmtlParser.T__0)
                self.state = 55
                self.wmtlProperty(0)
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 56
                    self.match(wmtlParser.T__3)
                    self.state = 57
                    self.wmtlProperty(0)
                    self.state = 60 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==4):
                        break

                self.state = 62
                self.match(wmtlParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 95
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = wmtlParser.FormulaContext(self, wmtlParser.WmtlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wmtlProperty)
                        self.state = 66
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 67
                        localctx.op = self.match(wmtlParser.IMPLIES)
                        self.state = 68
                        localctx.right = self.wmtlProperty(7)
                        pass

                    elif la_ == 2:
                        localctx = wmtlParser.FormulaContext(self, wmtlParser.WmtlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wmtlProperty)
                        self.state = 69
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 70
                        localctx.op = self.match(wmtlParser.AND)
                        self.state = 73
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==6:
                            self.state = 71
                            self.match(wmtlParser.T__5)
                            self.state = 72
                            localctx.weight = self.match(wmtlParser.VARIABLE)


                        self.state = 75
                        localctx.right = self.wmtlProperty(6)
                        pass

                    elif la_ == 3:
                        localctx = wmtlParser.FormulaContext(self, wmtlParser.WmtlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wmtlProperty)
                        self.state = 76
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 77
                        localctx.op = self.match(wmtlParser.OR)
                        self.state = 80
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==6:
                            self.state = 78
                            self.match(wmtlParser.T__5)
                            self.state = 79
                            localctx.weight = self.match(wmtlParser.VARIABLE)


                        self.state = 82
                        localctx.right = self.wmtlProperty(4)
                        pass

                    elif la_ == 4:
                        localctx = wmtlParser.FormulaContext(self, wmtlParser.WmtlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wmtlProperty)
                        self.state = 83
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 84
                        localctx.op = self.match(wmtlParser.UNTIL)
                        self.state = 85
                        self.match(wmtlParser.T__2)
                        self.state = 86
                        localctx.low = self.match(wmtlParser.RATIONAL)
                        self.state = 87
                        self.match(wmtlParser.T__3)
                        self.state = 88
                        localctx.high = self.match(wmtlParser.RATIONAL)
                        self.state = 89
                        self.match(wmtlParser.T__4)
                        self.state = 92
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==6:
                            self.state = 90
                            self.match(wmtlParser.T__5)
                            self.state = 91
                            localctx.weight = self.match(wmtlParser.VARIABLE)


                        self.state = 94
                        localctx.right = self.wmtlProperty(2)
                        pass

             
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
            self.op = None # Token

        def VARIABLE(self):
            return self.getToken(wmtlParser.VARIABLE, 0)

        def BOOLEAN(self):
            return self.getToken(wmtlParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return wmtlParser.RULE_booleanExpr

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

        localctx = wmtlParser.BooleanExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_booleanExpr)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                localctx.op = self.match(wmtlParser.VARIABLE)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                localctx.op = self.match(wmtlParser.BOOLEAN)
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
        self._predicates[0] = self.wmtlProperty_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def wmtlProperty_sempred(self, localctx:WmtlPropertyContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




