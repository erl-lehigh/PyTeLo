# Generated from mtl.g4 by ANTLR 4.13.0
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
        4,1,16,55,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,27,8,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        5,0,46,8,0,10,0,12,0,49,9,0,1,1,1,1,3,1,53,8,1,1,1,0,1,0,2,0,2,0,
        0,61,0,26,1,0,0,0,2,52,1,0,0,0,4,5,6,0,-1,0,5,6,5,1,0,0,6,7,3,0,
        0,0,7,8,5,2,0,0,8,27,1,0,0,0,9,27,3,2,1,0,10,11,5,9,0,0,11,27,3,
        0,0,7,12,13,5,10,0,0,13,14,5,3,0,0,14,15,5,15,0,0,15,16,5,4,0,0,
        16,17,5,15,0,0,17,18,5,5,0,0,18,27,3,0,0,6,19,20,5,11,0,0,20,21,
        5,3,0,0,21,22,5,15,0,0,22,23,5,4,0,0,23,24,5,15,0,0,24,25,5,5,0,
        0,25,27,3,0,0,5,26,4,1,0,0,0,26,9,1,0,0,0,26,10,1,0,0,0,26,12,1,
        0,0,0,26,19,1,0,0,0,27,47,1,0,0,0,28,29,10,4,0,0,29,30,5,8,0,0,30,
        46,3,0,0,5,31,32,10,3,0,0,32,33,5,6,0,0,33,46,3,0,0,4,34,35,10,2,
        0,0,35,36,5,7,0,0,36,46,3,0,0,3,37,38,10,1,0,0,38,39,5,12,0,0,39,
        40,5,3,0,0,40,41,5,15,0,0,41,42,5,4,0,0,42,43,5,15,0,0,43,44,5,5,
        0,0,44,46,3,0,0,2,45,28,1,0,0,0,45,31,1,0,0,0,45,34,1,0,0,0,45,37,
        1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,1,1,0,0,0,49,
        47,1,0,0,0,50,53,5,13,0,0,51,53,5,14,0,0,52,50,1,0,0,0,52,51,1,0,
        0,0,53,3,1,0,0,0,4,26,45,47,52
    ]

class mtlParser ( Parser ):

    grammarFileName = "mtl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "','", "']'", "<INVALID>", 
                     "<INVALID>", "'=>'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'U'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "AND", "OR", "IMPLIES", 
                      "NOT", "EVENT", "ALWAYS", "UNTIL", "BOOLEAN", "VARIABLE", 
                      "RATIONAL", "WS" ]

    RULE_mtlProperty = 0
    RULE_booleanExpr = 1

    ruleNames =  [ "mtlProperty", "booleanExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    AND=6
    OR=7
    IMPLIES=8
    NOT=9
    EVENT=10
    ALWAYS=11
    UNTIL=12
    BOOLEAN=13
    VARIABLE=14
    RATIONAL=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MtlPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mtlParser.RULE_mtlProperty

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BooleanPredContext(MtlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mtlParser.MtlPropertyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanExpr(self):
            return self.getTypedRuleContext(mtlParser.BooleanExprContext,0)


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


    class FormulaContext(MtlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mtlParser.MtlPropertyContext
            super().__init__(parser)
            self.left = None # MtlPropertyContext
            self.op = None # Token
            self.child = None # MtlPropertyContext
            self.low = None # Token
            self.high = None # Token
            self.right = None # MtlPropertyContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(mtlParser.NOT, 0)
        def mtlProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mtlParser.MtlPropertyContext)
            else:
                return self.getTypedRuleContext(mtlParser.MtlPropertyContext,i)

        def EVENT(self):
            return self.getToken(mtlParser.EVENT, 0)
        def RATIONAL(self, i:int=None):
            if i is None:
                return self.getTokens(mtlParser.RATIONAL)
            else:
                return self.getToken(mtlParser.RATIONAL, i)
        def ALWAYS(self):
            return self.getToken(mtlParser.ALWAYS, 0)
        def IMPLIES(self):
            return self.getToken(mtlParser.IMPLIES, 0)
        def AND(self):
            return self.getToken(mtlParser.AND, 0)
        def OR(self):
            return self.getToken(mtlParser.OR, 0)
        def UNTIL(self):
            return self.getToken(mtlParser.UNTIL, 0)

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


    class ParpropContext(MtlPropertyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mtlParser.MtlPropertyContext
            super().__init__(parser)
            self.child = None # MtlPropertyContext
            self.copyFrom(ctx)

        def mtlProperty(self):
            return self.getTypedRuleContext(mtlParser.MtlPropertyContext,0)


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



    def mtlProperty(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mtlParser.MtlPropertyContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_mtlProperty, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = mtlParser.ParpropContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                self.match(mtlParser.T__0)
                self.state = 6
                localctx.child = self.mtlProperty(0)
                self.state = 7
                self.match(mtlParser.T__1)
                pass
            elif token in [13, 14]:
                localctx = mtlParser.BooleanPredContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.booleanExpr()
                pass
            elif token in [9]:
                localctx = mtlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                localctx.op = self.match(mtlParser.NOT)
                self.state = 11
                localctx.child = self.mtlProperty(7)
                pass
            elif token in [10]:
                localctx = mtlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                localctx.op = self.match(mtlParser.EVENT)
                self.state = 13
                self.match(mtlParser.T__2)
                self.state = 14
                localctx.low = self.match(mtlParser.RATIONAL)
                self.state = 15
                self.match(mtlParser.T__3)
                self.state = 16
                localctx.high = self.match(mtlParser.RATIONAL)
                self.state = 17
                self.match(mtlParser.T__4)
                self.state = 18
                localctx.child = self.mtlProperty(6)
                pass
            elif token in [11]:
                localctx = mtlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                localctx.op = self.match(mtlParser.ALWAYS)
                self.state = 20
                self.match(mtlParser.T__2)
                self.state = 21
                localctx.low = self.match(mtlParser.RATIONAL)
                self.state = 22
                self.match(mtlParser.T__3)
                self.state = 23
                localctx.high = self.match(mtlParser.RATIONAL)
                self.state = 24
                self.match(mtlParser.T__4)
                self.state = 25
                localctx.child = self.mtlProperty(5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 45
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = mtlParser.FormulaContext(self, mtlParser.MtlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mtlProperty)
                        self.state = 28
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 29
                        localctx.op = self.match(mtlParser.IMPLIES)
                        self.state = 30
                        localctx.right = self.mtlProperty(5)
                        pass

                    elif la_ == 2:
                        localctx = mtlParser.FormulaContext(self, mtlParser.MtlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mtlProperty)
                        self.state = 31
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 32
                        localctx.op = self.match(mtlParser.AND)
                        self.state = 33
                        localctx.right = self.mtlProperty(4)
                        pass

                    elif la_ == 3:
                        localctx = mtlParser.FormulaContext(self, mtlParser.MtlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mtlProperty)
                        self.state = 34
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 35
                        localctx.op = self.match(mtlParser.OR)
                        self.state = 36
                        localctx.right = self.mtlProperty(3)
                        pass

                    elif la_ == 4:
                        localctx = mtlParser.FormulaContext(self, mtlParser.MtlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mtlProperty)
                        self.state = 37
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 38
                        localctx.op = self.match(mtlParser.UNTIL)
                        self.state = 39
                        self.match(mtlParser.T__2)
                        self.state = 40
                        localctx.low = self.match(mtlParser.RATIONAL)
                        self.state = 41
                        self.match(mtlParser.T__3)
                        self.state = 42
                        localctx.high = self.match(mtlParser.RATIONAL)
                        self.state = 43
                        self.match(mtlParser.T__4)
                        self.state = 44
                        localctx.right = self.mtlProperty(2)
                        pass

             
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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

        def BOOLEAN(self):
            return self.getToken(mtlParser.BOOLEAN, 0)

        def VARIABLE(self):
            return self.getToken(mtlParser.VARIABLE, 0)

        def getRuleIndex(self):
            return mtlParser.RULE_booleanExpr

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

        localctx = mtlParser.BooleanExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_booleanExpr)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                localctx.op = self.match(mtlParser.BOOLEAN)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                localctx.op = self.match(mtlParser.VARIABLE)
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
        self._predicates[0] = self.mtlProperty_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def mtlProperty_sempred(self, localctx:MtlPropertyContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




