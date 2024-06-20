// Generated from /home/gustavo/lehigh/erl/PyTeLo/stl/stl.g4 by ANTLR 4.13.1

'''
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class stlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, AND=17, 
		OR=18, IMPLIES=19, NOT=20, EVENT=21, ALWAYS=22, UNTIL=23, BOOLEAN=24, 
		VARIABLE=25, RATIONAL=26, WS=27;
	public static final int
		RULE_stlProperty = 0, RULE_expr = 1, RULE_booleanExpr = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"stlProperty", "expr", "booleanExpr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'['", "','", "']'", "'-('", "'^'", "'*'", "'/'", 
			"'+'", "'-'", "'<'", "'<='", "'='", "'>='", "'>'", null, null, "'=>'", 
			null, null, null, "'U'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "AND", "OR", "IMPLIES", "NOT", "EVENT", 
			"ALWAYS", "UNTIL", "BOOLEAN", "VARIABLE", "RATIONAL", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "stl.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public stlParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StlPropertyContext extends ParserRuleContext {
		public StlPropertyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stlProperty; }
	 
		public StlPropertyContext() { }
		public void copyFrom(StlPropertyContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BooleanPredContext extends StlPropertyContext {
		public BooleanExprContext booleanExpr() {
			return getRuleContext(BooleanExprContext.class,0);
		}
		public BooleanPredContext(StlPropertyContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FormulaContext extends StlPropertyContext {
		public StlPropertyContext left;
		public Token op;
		public StlPropertyContext child;
		public Token low;
		public Token high;
		public StlPropertyContext right;
		public TerminalNode NOT() { return getToken(stlParser.NOT, 0); }
		public List<StlPropertyContext> stlProperty() {
			return getRuleContexts(StlPropertyContext.class);
		}
		public StlPropertyContext stlProperty(int i) {
			return getRuleContext(StlPropertyContext.class,i);
		}
		public TerminalNode EVENT() { return getToken(stlParser.EVENT, 0); }
		public List<TerminalNode> RATIONAL() { return getTokens(stlParser.RATIONAL); }
		public TerminalNode RATIONAL(int i) {
			return getToken(stlParser.RATIONAL, i);
		}
		public TerminalNode ALWAYS() { return getToken(stlParser.ALWAYS, 0); }
		public TerminalNode IMPLIES() { return getToken(stlParser.IMPLIES, 0); }
		public TerminalNode AND() { return getToken(stlParser.AND, 0); }
		public TerminalNode OR() { return getToken(stlParser.OR, 0); }
		public TerminalNode UNTIL() { return getToken(stlParser.UNTIL, 0); }
		public FormulaContext(StlPropertyContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParpropContext extends StlPropertyContext {
		public StlPropertyContext child;
		public StlPropertyContext stlProperty() {
			return getRuleContext(StlPropertyContext.class,0);
		}
		public ParpropContext(StlPropertyContext ctx) { copyFrom(ctx); }
	}

	public final StlPropertyContext stlProperty() throws RecognitionException {
		return stlProperty(0);
	}

	private StlPropertyContext stlProperty(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		StlPropertyContext _localctx = new StlPropertyContext(_ctx, _parentState);
		StlPropertyContext _prevctx = _localctx;
		int _startState = 0;
		enterRecursionRule(_localctx, 0, RULE_stlProperty, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				_localctx = new ParpropContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(7);
				match(T__0);
				setState(8);
				((ParpropContext)_localctx).child = stlProperty(0);
				setState(9);
				match(T__1);
				}
				break;
			case 2:
				{
				_localctx = new BooleanPredContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(11);
				booleanExpr();
				}
				break;
			case 3:
				{
				_localctx = new FormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(12);
				((FormulaContext)_localctx).op = match(NOT);
				setState(13);
				((FormulaContext)_localctx).child = stlProperty(7);
				}
				break;
			case 4:
				{
				_localctx = new FormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(14);
				((FormulaContext)_localctx).op = match(EVENT);
				setState(15);
				match(T__2);
				setState(16);
				((FormulaContext)_localctx).low = match(RATIONAL);
				setState(17);
				match(T__3);
				setState(18);
				((FormulaContext)_localctx).high = match(RATIONAL);
				setState(19);
				match(T__4);
				setState(20);
				((FormulaContext)_localctx).child = stlProperty(6);
				}
				break;
			case 5:
				{
				_localctx = new FormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(21);
				((FormulaContext)_localctx).op = match(ALWAYS);
				setState(22);
				match(T__2);
				setState(23);
				((FormulaContext)_localctx).low = match(RATIONAL);
				setState(24);
				match(T__3);
				setState(25);
				((FormulaContext)_localctx).high = match(RATIONAL);
				setState(26);
				match(T__4);
				setState(27);
				((FormulaContext)_localctx).child = stlProperty(5);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(49);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(47);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						_localctx = new FormulaContext(new StlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_stlProperty);
						setState(30);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(31);
						((FormulaContext)_localctx).op = match(IMPLIES);
						setState(32);
						((FormulaContext)_localctx).right = stlProperty(5);
						}
						break;
					case 2:
						{
						_localctx = new FormulaContext(new StlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_stlProperty);
						setState(33);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(34);
						((FormulaContext)_localctx).op = match(AND);
						setState(35);
						((FormulaContext)_localctx).right = stlProperty(4);
						}
						break;
					case 3:
						{
						_localctx = new FormulaContext(new StlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_stlProperty);
						setState(36);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(37);
						((FormulaContext)_localctx).op = match(OR);
						setState(38);
						((FormulaContext)_localctx).right = stlProperty(3);
						}
						break;
					case 4:
						{
						_localctx = new FormulaContext(new StlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_stlProperty);
						setState(39);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(40);
						((FormulaContext)_localctx).op = match(UNTIL);
						setState(41);
						match(T__2);
						setState(42);
						((FormulaContext)_localctx).low = match(RATIONAL);
						setState(43);
						match(T__3);
						setState(44);
						((FormulaContext)_localctx).high = match(RATIONAL);
						setState(45);
						match(T__4);
						setState(46);
						((FormulaContext)_localctx).right = stlProperty(2);
						}
						break;
					}
					} 
				}
				setState(51);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode VARIABLE() { return getToken(stlParser.VARIABLE, 0); }
		public TerminalNode RATIONAL() { return getToken(stlParser.RATIONAL, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 2;
		enterRecursionRule(_localctx, 2, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(53);
				_la = _input.LA(1);
				if ( !(_la==T__0 || _la==T__5) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(54);
				expr(0);
				setState(55);
				match(T__1);
				}
				break;
			case 2:
				{
				setState(57);
				match(VARIABLE);
				setState(58);
				match(T__0);
				setState(59);
				expr(0);
				setState(60);
				match(T__1);
				}
				break;
			case 3:
				{
				setState(62);
				match(RATIONAL);
				}
				break;
			case 4:
				{
				setState(63);
				match(VARIABLE);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(77);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(75);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(66);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(67);
						match(T__6);
						setState(68);
						expr(6);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(69);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(70);
						_la = _input.LA(1);
						if ( !(_la==T__7 || _la==T__8) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(71);
						expr(5);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(72);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(73);
						_la = _input.LA(1);
						if ( !(_la==T__9 || _la==T__10) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(74);
						expr(4);
						}
						break;
					}
					} 
				}
				setState(79);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BooleanExprContext extends ParserRuleContext {
		public ExprContext left;
		public Token op;
		public ExprContext right;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode BOOLEAN() { return getToken(stlParser.BOOLEAN, 0); }
		public BooleanExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_booleanExpr; }
	}

	public final BooleanExprContext booleanExpr() throws RecognitionException {
		BooleanExprContext _localctx = new BooleanExprContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_booleanExpr);
		int _la;
		try {
			setState(85);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__5:
			case VARIABLE:
			case RATIONAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(80);
				((BooleanExprContext)_localctx).left = expr(0);
				setState(81);
				((BooleanExprContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 126976L) != 0)) ) {
					((BooleanExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(82);
				((BooleanExprContext)_localctx).right = expr(0);
				}
				break;
			case BOOLEAN:
				enterOuterAlt(_localctx, 2);
				{
				setState(84);
				((BooleanExprContext)_localctx).op = match(BOOLEAN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 0:
			return stlProperty_sempred((StlPropertyContext)_localctx, predIndex);
		case 1:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean stlProperty_sempred(StlPropertyContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 6);
		case 5:
			return precpred(_ctx, 4);
		case 6:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001bX\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0003"+
		"\u0000\u001d\b\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0005\u00000\b\u0000\n\u0000\f\u00003\t\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001A\b"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001L\b\u0001\n\u0001"+
		"\f\u0001O\t\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0003\u0002V\b\u0002\u0001\u0002\u0000\u0002\u0000\u0002\u0003"+
		"\u0000\u0002\u0004\u0000\u0004\u0002\u0000\u0001\u0001\u0006\u0006\u0001"+
		"\u0000\b\t\u0001\u0000\n\u000b\u0001\u0000\f\u0010c\u0000\u001c\u0001"+
		"\u0000\u0000\u0000\u0002@\u0001\u0000\u0000\u0000\u0004U\u0001\u0000\u0000"+
		"\u0000\u0006\u0007\u0006\u0000\uffff\uffff\u0000\u0007\b\u0005\u0001\u0000"+
		"\u0000\b\t\u0003\u0000\u0000\u0000\t\n\u0005\u0002\u0000\u0000\n\u001d"+
		"\u0001\u0000\u0000\u0000\u000b\u001d\u0003\u0004\u0002\u0000\f\r\u0005"+
		"\u0014\u0000\u0000\r\u001d\u0003\u0000\u0000\u0007\u000e\u000f\u0005\u0015"+
		"\u0000\u0000\u000f\u0010\u0005\u0003\u0000\u0000\u0010\u0011\u0005\u001a"+
		"\u0000\u0000\u0011\u0012\u0005\u0004\u0000\u0000\u0012\u0013\u0005\u001a"+
		"\u0000\u0000\u0013\u0014\u0005\u0005\u0000\u0000\u0014\u001d\u0003\u0000"+
		"\u0000\u0006\u0015\u0016\u0005\u0016\u0000\u0000\u0016\u0017\u0005\u0003"+
		"\u0000\u0000\u0017\u0018\u0005\u001a\u0000\u0000\u0018\u0019\u0005\u0004"+
		"\u0000\u0000\u0019\u001a\u0005\u001a\u0000\u0000\u001a\u001b\u0005\u0005"+
		"\u0000\u0000\u001b\u001d\u0003\u0000\u0000\u0005\u001c\u0006\u0001\u0000"+
		"\u0000\u0000\u001c\u000b\u0001\u0000\u0000\u0000\u001c\f\u0001\u0000\u0000"+
		"\u0000\u001c\u000e\u0001\u0000\u0000\u0000\u001c\u0015\u0001\u0000\u0000"+
		"\u0000\u001d1\u0001\u0000\u0000\u0000\u001e\u001f\n\u0004\u0000\u0000"+
		"\u001f \u0005\u0013\u0000\u0000 0\u0003\u0000\u0000\u0005!\"\n\u0003\u0000"+
		"\u0000\"#\u0005\u0011\u0000\u0000#0\u0003\u0000\u0000\u0004$%\n\u0002"+
		"\u0000\u0000%&\u0005\u0012\u0000\u0000&0\u0003\u0000\u0000\u0003\'(\n"+
		"\u0001\u0000\u0000()\u0005\u0017\u0000\u0000)*\u0005\u0003\u0000\u0000"+
		"*+\u0005\u001a\u0000\u0000+,\u0005\u0004\u0000\u0000,-\u0005\u001a\u0000"+
		"\u0000-.\u0005\u0005\u0000\u0000.0\u0003\u0000\u0000\u0002/\u001e\u0001"+
		"\u0000\u0000\u0000/!\u0001\u0000\u0000\u0000/$\u0001\u0000\u0000\u0000"+
		"/\'\u0001\u0000\u0000\u000003\u0001\u0000\u0000\u00001/\u0001\u0000\u0000"+
		"\u000012\u0001\u0000\u0000\u00002\u0001\u0001\u0000\u0000\u000031\u0001"+
		"\u0000\u0000\u000045\u0006\u0001\uffff\uffff\u000056\u0007\u0000\u0000"+
		"\u000067\u0003\u0002\u0001\u000078\u0005\u0002\u0000\u00008A\u0001\u0000"+
		"\u0000\u00009:\u0005\u0019\u0000\u0000:;\u0005\u0001\u0000\u0000;<\u0003"+
		"\u0002\u0001\u0000<=\u0005\u0002\u0000\u0000=A\u0001\u0000\u0000\u0000"+
		">A\u0005\u001a\u0000\u0000?A\u0005\u0019\u0000\u0000@4\u0001\u0000\u0000"+
		"\u0000@9\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000@?\u0001\u0000"+
		"\u0000\u0000AM\u0001\u0000\u0000\u0000BC\n\u0006\u0000\u0000CD\u0005\u0007"+
		"\u0000\u0000DL\u0003\u0002\u0001\u0006EF\n\u0004\u0000\u0000FG\u0007\u0001"+
		"\u0000\u0000GL\u0003\u0002\u0001\u0005HI\n\u0003\u0000\u0000IJ\u0007\u0002"+
		"\u0000\u0000JL\u0003\u0002\u0001\u0004KB\u0001\u0000\u0000\u0000KE\u0001"+
		"\u0000\u0000\u0000KH\u0001\u0000\u0000\u0000LO\u0001\u0000\u0000\u0000"+
		"MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000N\u0003\u0001\u0000"+
		"\u0000\u0000OM\u0001\u0000\u0000\u0000PQ\u0003\u0002\u0001\u0000QR\u0007"+
		"\u0003\u0000\u0000RS\u0003\u0002\u0001\u0000SV\u0001\u0000\u0000\u0000"+
		"TV\u0005\u0018\u0000\u0000UP\u0001\u0000\u0000\u0000UT\u0001\u0000\u0000"+
		"\u0000V\u0005\u0001\u0000\u0000\u0000\u0007\u001c/1@KMU";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}