// Generated from /home/gustavo/lehigh/erl/python-stl/stl/stl.g4 by ANTLR 4.9.2

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

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class stlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, AND=17, 
		EAND=18, OR=19, EOR=20, IMPLIES=21, NOT=22, EVENT=23, EEVENT=24, ALWAYS=25, 
		EALWAYS=26, UNTIL=27, BOOLEAN=28, VARIABLE=29, RATIONAL=30, WS=31;
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
			"'+'", "'-'", "'<'", "'<='", "'='", "'>='", "'>'", null, "'&'", null, 
			"'|'", "'=>'", null, "'F'", "'E'", "'G'", "'A'", "'U'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "AND", "EAND", "OR", "EOR", "IMPLIES", 
			"NOT", "EVENT", "EEVENT", "ALWAYS", "EALWAYS", "UNTIL", "BOOLEAN", "VARIABLE", 
			"RATIONAL", "WS"
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
	public static class BooleanPredContext extends StlPropertyContext {
		public BooleanExprContext booleanExpr() {
			return getRuleContext(BooleanExprContext.class,0);
		}
		public BooleanPredContext(StlPropertyContext ctx) { copyFrom(ctx); }
	}
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
		public TerminalNode EEVENT() { return getToken(stlParser.EEVENT, 0); }
		public TerminalNode ALWAYS() { return getToken(stlParser.ALWAYS, 0); }
		public TerminalNode EALWAYS() { return getToken(stlParser.EALWAYS, 0); }
		public TerminalNode IMPLIES() { return getToken(stlParser.IMPLIES, 0); }
		public TerminalNode AND() { return getToken(stlParser.AND, 0); }
		public TerminalNode EAND() { return getToken(stlParser.EAND, 0); }
		public TerminalNode OR() { return getToken(stlParser.OR, 0); }
		public TerminalNode EOR() { return getToken(stlParser.EOR, 0); }
		public TerminalNode UNTIL() { return getToken(stlParser.UNTIL, 0); }
		public FormulaContext(StlPropertyContext ctx) { copyFrom(ctx); }
	}
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
			setState(42);
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
				((FormulaContext)_localctx).child = stlProperty(11);
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
				((FormulaContext)_localctx).child = stlProperty(10);
				}
				break;
			case 5:
				{
				_localctx = new FormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(21);
				((FormulaContext)_localctx).op = match(EEVENT);
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
				((FormulaContext)_localctx).child = stlProperty(9);
				}
				break;
			case 6:
				{
				_localctx = new FormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(28);
				((FormulaContext)_localctx).op = match(ALWAYS);
				setState(29);
				match(T__2);
				setState(30);
				((FormulaContext)_localctx).low = match(RATIONAL);
				setState(31);
				match(T__3);
				setState(32);
				((FormulaContext)_localctx).high = match(RATIONAL);
				setState(33);
				match(T__4);
				setState(34);
				((FormulaContext)_localctx).child = stlProperty(8);
				}
				break;
			case 7:
				{
				_localctx = new FormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(35);
				((FormulaContext)_localctx).op = match(EALWAYS);
				setState(36);
				match(T__2);
				setState(37);
				((FormulaContext)_localctx).low = match(RATIONAL);
				setState(38);
				match(T__3);
				setState(39);
				((FormulaContext)_localctx).high = match(RATIONAL);
				setState(40);
				match(T__4);
				setState(41);
				((FormulaContext)_localctx).child = stlProperty(7);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(69);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(67);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						_localctx = new FormulaContext(new StlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_stlProperty);
						setState(44);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(45);
						((FormulaContext)_localctx).op = match(IMPLIES);
						setState(46);
						((FormulaContext)_localctx).right = stlProperty(7);
						}
						break;
					case 2:
						{
						_localctx = new FormulaContext(new StlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_stlProperty);
						setState(47);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(48);
						((FormulaContext)_localctx).op = match(AND);
						setState(49);
						((FormulaContext)_localctx).right = stlProperty(6);
						}
						break;
					case 3:
						{
						_localctx = new FormulaContext(new StlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_stlProperty);
						setState(50);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(51);
						((FormulaContext)_localctx).op = match(EAND);
						setState(52);
						((FormulaContext)_localctx).right = stlProperty(5);
						}
						break;
					case 4:
						{
						_localctx = new FormulaContext(new StlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_stlProperty);
						setState(53);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(54);
						((FormulaContext)_localctx).op = match(OR);
						setState(55);
						((FormulaContext)_localctx).right = stlProperty(4);
						}
						break;
					case 5:
						{
						_localctx = new FormulaContext(new StlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_stlProperty);
						setState(56);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(57);
						((FormulaContext)_localctx).op = match(EOR);
						setState(58);
						((FormulaContext)_localctx).right = stlProperty(3);
						}
						break;
					case 6:
						{
						_localctx = new FormulaContext(new StlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_stlProperty);
						setState(59);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(60);
						((FormulaContext)_localctx).op = match(UNTIL);
						setState(61);
						match(T__2);
						setState(62);
						((FormulaContext)_localctx).low = match(RATIONAL);
						setState(63);
						match(T__3);
						setState(64);
						((FormulaContext)_localctx).high = match(RATIONAL);
						setState(65);
						match(T__4);
						setState(66);
						((FormulaContext)_localctx).right = stlProperty(2);
						}
						break;
					}
					} 
				}
				setState(71);
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
			setState(84);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(73);
				_la = _input.LA(1);
				if ( !(_la==T__0 || _la==T__5) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(74);
				expr(0);
				setState(75);
				match(T__1);
				}
				break;
			case 2:
				{
				setState(77);
				match(VARIABLE);
				setState(78);
				match(T__0);
				setState(79);
				expr(0);
				setState(80);
				match(T__1);
				}
				break;
			case 3:
				{
				setState(82);
				match(RATIONAL);
				}
				break;
			case 4:
				{
				setState(83);
				match(VARIABLE);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(97);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(95);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(86);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(87);
						match(T__6);
						setState(88);
						expr(6);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(89);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(90);
						_la = _input.LA(1);
						if ( !(_la==T__7 || _la==T__8) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(91);
						expr(5);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(92);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(93);
						_la = _input.LA(1);
						if ( !(_la==T__9 || _la==T__10) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(94);
						expr(4);
						}
						break;
					}
					} 
				}
				setState(99);
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
			setState(105);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__5:
			case VARIABLE:
			case RATIONAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(100);
				((BooleanExprContext)_localctx).left = expr(0);
				setState(101);
				((BooleanExprContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15))) != 0)) ) {
					((BooleanExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(102);
				((BooleanExprContext)_localctx).right = expr(0);
				}
				break;
			case BOOLEAN:
				enterOuterAlt(_localctx, 2);
				{
				setState(104);
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
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		case 2:
			return precpred(_ctx, 4);
		case 3:
			return precpred(_ctx, 3);
		case 4:
			return precpred(_ctx, 2);
		case 5:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 6:
			return precpred(_ctx, 6);
		case 7:
			return precpred(_ctx, 4);
		case 8:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3!n\4\2\t\2\4\3\t\3"+
		"\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\5\2-\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2F\n\2\f\2\16\2I\13\2\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3W\n\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\7\3b\n\3\f\3\16\3e\13\3\3\4\3\4\3\4\3\4\3\4\5\4"+
		"l\n\4\3\4\2\4\2\4\5\2\4\6\2\6\4\2\3\3\b\b\3\2\n\13\3\2\f\r\3\2\16\22\2"+
		"}\2,\3\2\2\2\4V\3\2\2\2\6k\3\2\2\2\b\t\b\2\1\2\t\n\7\3\2\2\n\13\5\2\2"+
		"\2\13\f\7\4\2\2\f-\3\2\2\2\r-\5\6\4\2\16\17\7\30\2\2\17-\5\2\2\r\20\21"+
		"\7\31\2\2\21\22\7\5\2\2\22\23\7 \2\2\23\24\7\6\2\2\24\25\7 \2\2\25\26"+
		"\7\7\2\2\26-\5\2\2\f\27\30\7\32\2\2\30\31\7\5\2\2\31\32\7 \2\2\32\33\7"+
		"\6\2\2\33\34\7 \2\2\34\35\7\7\2\2\35-\5\2\2\13\36\37\7\33\2\2\37 \7\5"+
		"\2\2 !\7 \2\2!\"\7\6\2\2\"#\7 \2\2#$\7\7\2\2$-\5\2\2\n%&\7\34\2\2&\'\7"+
		"\5\2\2\'(\7 \2\2()\7\6\2\2)*\7 \2\2*+\7\7\2\2+-\5\2\2\t,\b\3\2\2\2,\r"+
		"\3\2\2\2,\16\3\2\2\2,\20\3\2\2\2,\27\3\2\2\2,\36\3\2\2\2,%\3\2\2\2-G\3"+
		"\2\2\2./\f\b\2\2/\60\7\27\2\2\60F\5\2\2\t\61\62\f\7\2\2\62\63\7\23\2\2"+
		"\63F\5\2\2\b\64\65\f\6\2\2\65\66\7\24\2\2\66F\5\2\2\7\678\f\5\2\289\7"+
		"\25\2\29F\5\2\2\6:;\f\4\2\2;<\7\26\2\2<F\5\2\2\5=>\f\3\2\2>?\7\35\2\2"+
		"?@\7\5\2\2@A\7 \2\2AB\7\6\2\2BC\7 \2\2CD\7\7\2\2DF\5\2\2\4E.\3\2\2\2E"+
		"\61\3\2\2\2E\64\3\2\2\2E\67\3\2\2\2E:\3\2\2\2E=\3\2\2\2FI\3\2\2\2GE\3"+
		"\2\2\2GH\3\2\2\2H\3\3\2\2\2IG\3\2\2\2JK\b\3\1\2KL\t\2\2\2LM\5\4\3\2MN"+
		"\7\4\2\2NW\3\2\2\2OP\7\37\2\2PQ\7\3\2\2QR\5\4\3\2RS\7\4\2\2SW\3\2\2\2"+
		"TW\7 \2\2UW\7\37\2\2VJ\3\2\2\2VO\3\2\2\2VT\3\2\2\2VU\3\2\2\2Wc\3\2\2\2"+
		"XY\f\b\2\2YZ\7\t\2\2Zb\5\4\3\b[\\\f\6\2\2\\]\t\3\2\2]b\5\4\3\7^_\f\5\2"+
		"\2_`\t\4\2\2`b\5\4\3\6aX\3\2\2\2a[\3\2\2\2a^\3\2\2\2be\3\2\2\2ca\3\2\2"+
		"\2cd\3\2\2\2d\5\3\2\2\2ec\3\2\2\2fg\5\4\3\2gh\t\5\2\2hi\5\4\3\2il\3\2"+
		"\2\2jl\7\36\2\2kf\3\2\2\2kj\3\2\2\2l\7\3\2\2\2\t,EGVack";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}