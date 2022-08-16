# Generated from stl.g4 by ANTLR 4.8
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
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("Z\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\5\2\37\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\62\n\2\f\2\16\2\65")
        buf.write("\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3C\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3N\n\3")
        buf.write("\f\3\16\3Q\13\3\3\4\3\4\3\4\3\4\3\4\5\4X\n\4\3\4\2\4\2")
        buf.write("\4\5\2\4\6\2\6\4\2\3\3\b\b\3\2\n\13\3\2\f\r\3\2\16\22")
        buf.write("\2e\2\36\3\2\2\2\4B\3\2\2\2\6W\3\2\2\2\b\t\b\2\1\2\t\n")
        buf.write("\7\3\2\2\n\13\5\2\2\2\13\f\7\4\2\2\f\37\3\2\2\2\r\37\5")
        buf.write("\6\4\2\16\17\7\26\2\2\17\37\5\2\2\t\20\21\7\27\2\2\21")
        buf.write("\22\7\5\2\2\22\23\7\34\2\2\23\24\7\6\2\2\24\25\7\34\2")
        buf.write("\2\25\26\7\7\2\2\26\37\5\2\2\b\27\30\7\30\2\2\30\31\7")
        buf.write("\5\2\2\31\32\7\34\2\2\32\33\7\6\2\2\33\34\7\34\2\2\34")
        buf.write("\35\7\7\2\2\35\37\5\2\2\7\36\b\3\2\2\2\36\r\3\2\2\2\36")
        buf.write("\16\3\2\2\2\36\20\3\2\2\2\36\27\3\2\2\2\37\63\3\2\2\2")
        buf.write(" !\f\6\2\2!\"\7\25\2\2\"\62\5\2\2\7#$\f\5\2\2$%\7\23\2")
        buf.write("\2%\62\5\2\2\6&\'\f\4\2\2\'(\7\24\2\2(\62\5\2\2\5)*\f")
        buf.write("\3\2\2*+\7\31\2\2+,\7\5\2\2,-\7\34\2\2-.\7\6\2\2./\7\34")
        buf.write("\2\2/\60\7\7\2\2\60\62\5\2\2\4\61 \3\2\2\2\61#\3\2\2\2")
        buf.write("\61&\3\2\2\2\61)\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63")
        buf.write("\64\3\2\2\2\64\3\3\2\2\2\65\63\3\2\2\2\66\67\b\3\1\2\67")
        buf.write("8\t\2\2\289\5\4\3\29:\7\4\2\2:C\3\2\2\2;<\7\33\2\2<=\7")
        buf.write("\3\2\2=>\5\4\3\2>?\7\4\2\2?C\3\2\2\2@C\7\34\2\2AC\7\33")
        buf.write("\2\2B\66\3\2\2\2B;\3\2\2\2B@\3\2\2\2BA\3\2\2\2CO\3\2\2")
        buf.write("\2DE\f\b\2\2EF\7\t\2\2FN\5\4\3\bGH\f\6\2\2HI\t\3\2\2I")
        buf.write("N\5\4\3\7JK\f\5\2\2KL\t\4\2\2LN\5\4\3\6MD\3\2\2\2MG\3")
        buf.write("\2\2\2MJ\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\5\3\2")
        buf.write("\2\2QO\3\2\2\2RS\5\4\3\2ST\t\5\2\2TU\5\4\3\2UX\3\2\2\2")
        buf.write("VX\7\32\2\2WR\3\2\2\2WV\3\2\2\2X\7\3\2\2\2\t\36\61\63")
        buf.write("BMOW")
        return buf.getvalue()


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
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StlPropertyContext(ParserRuleContext):

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
                if not(_la==stlParser.T__0 or _la==stlParser.T__5):
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
                        if not(_la==stlParser.T__7 or _la==stlParser.T__8):
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
                        if not(_la==stlParser.T__9 or _la==stlParser.T__10):
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
            if token in [stlParser.T__0, stlParser.T__5, stlParser.VARIABLE, stlParser.RATIONAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                localctx.left = self.expr(0)
                self.state = 81
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << stlParser.T__11) | (1 << stlParser.T__12) | (1 << stlParser.T__13) | (1 << stlParser.T__14) | (1 << stlParser.T__15))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 82
                localctx.right = self.expr(0)
                pass
            elif token in [stlParser.BOOLEAN]:
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
         




