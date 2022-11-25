// Generated from /home/gustavo/lehigh/erl/python-stl/stl/wstl.g4 by ANTLR 4.9.2

'''
 Copyright (C) 2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
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
public class wstlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, AND=17, 
		EAND=18, OR=19, EOR=20, IMPLIES=21, NOT=22, EVENT=23, EEVENT=24, ALWAYS=25, 
		EALWAYS=26, UNTIL=27, RELEASE=28, BOOLEAN=29, VARIABLE=30, RATIONAL=31, 
		WS=32;
	public static final int
		RULE_wstlProperty = 0, RULE_expr = 1, RULE_booleanExpr = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"wstlProperty", "expr", "booleanExpr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'['", "','", "']'", "'^'", "'-('", "'*'", "'/'", 
			"'+'", "'-'", "'<'", "'<='", "'='", "'>='", "'>'", null, "'&'", null, 
			"'|'", "'=>'", null, null, "'E'", null, "'A'", "'U'", "'R'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "AND", "EAND", "OR", "EOR", "IMPLIES", 
			"NOT", "EVENT", "EEVENT", "ALWAYS", "EALWAYS", "UNTIL", "RELEASE", "BOOLEAN", 
			"VARIABLE", "RATIONAL", "WS"
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
	public String getGrammarFileName() { return "wstl.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public wstlParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class WstlPropertyContext extends ParserRuleContext {
		public WstlPropertyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wstlProperty; }
	 
		public WstlPropertyContext() { }
		public void copyFrom(WstlPropertyContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class BooleanPredContext extends WstlPropertyContext {
		public BooleanExprContext booleanExpr() {
			return getRuleContext(BooleanExprContext.class,0);
		}
		public BooleanPredContext(WstlPropertyContext ctx) { copyFrom(ctx); }
	}
	public static class LongFormulaContext extends WstlPropertyContext {
		public Token op;
		public Token weight;
		public List<WstlPropertyContext> wstlProperty() {
			return getRuleContexts(WstlPropertyContext.class);
		}
		public WstlPropertyContext wstlProperty(int i) {
			return getRuleContext(WstlPropertyContext.class,i);
		}
		public TerminalNode AND() { return getToken(wstlParser.AND, 0); }
		public TerminalNode VARIABLE() { return getToken(wstlParser.VARIABLE, 0); }
		public TerminalNode EAND() { return getToken(wstlParser.EAND, 0); }
		public TerminalNode OR() { return getToken(wstlParser.OR, 0); }
		public TerminalNode EOR() { return getToken(wstlParser.EOR, 0); }
		public LongFormulaContext(WstlPropertyContext ctx) { copyFrom(ctx); }
	}
	public static class FormulaContext extends WstlPropertyContext {
		public WstlPropertyContext left;
		public Token op;
		public WstlPropertyContext child;
		public Token low;
		public Token high;
		public Token weight;
		public WstlPropertyContext right;
		public TerminalNode NOT() { return getToken(wstlParser.NOT, 0); }
		public List<WstlPropertyContext> wstlProperty() {
			return getRuleContexts(WstlPropertyContext.class);
		}
		public WstlPropertyContext wstlProperty(int i) {
			return getRuleContext(WstlPropertyContext.class,i);
		}
		public TerminalNode EVENT() { return getToken(wstlParser.EVENT, 0); }
		public List<TerminalNode> RATIONAL() { return getTokens(wstlParser.RATIONAL); }
		public TerminalNode RATIONAL(int i) {
			return getToken(wstlParser.RATIONAL, i);
		}
		public TerminalNode VARIABLE() { return getToken(wstlParser.VARIABLE, 0); }
		public TerminalNode EEVENT() { return getToken(wstlParser.EEVENT, 0); }
		public TerminalNode ALWAYS() { return getToken(wstlParser.ALWAYS, 0); }
		public TerminalNode EALWAYS() { return getToken(wstlParser.EALWAYS, 0); }
		public TerminalNode IMPLIES() { return getToken(wstlParser.IMPLIES, 0); }
		public TerminalNode AND() { return getToken(wstlParser.AND, 0); }
		public TerminalNode EAND() { return getToken(wstlParser.EAND, 0); }
		public TerminalNode OR() { return getToken(wstlParser.OR, 0); }
		public TerminalNode EOR() { return getToken(wstlParser.EOR, 0); }
		public TerminalNode UNTIL() { return getToken(wstlParser.UNTIL, 0); }
		public TerminalNode RELEASE() { return getToken(wstlParser.RELEASE, 0); }
		public FormulaContext(WstlPropertyContext ctx) { copyFrom(ctx); }
	}
	public static class ParpropContext extends WstlPropertyContext {
		public WstlPropertyContext child;
		public WstlPropertyContext wstlProperty() {
			return getRuleContext(WstlPropertyContext.class,0);
		}
		public ParpropContext(WstlPropertyContext ctx) { copyFrom(ctx); }
	}

	public final WstlPropertyContext wstlProperty() throws RecognitionException {
		return wstlProperty(0);
	}

	private WstlPropertyContext wstlProperty(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		WstlPropertyContext _localctx = new WstlPropertyContext(_ctx, _parentState);
		WstlPropertyContext _prevctx = _localctx;
		int _startState = 0;
		enterRecursionRule(_localctx, 0, RULE_wstlProperty, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				_localctx = new ParpropContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(7);
				match(T__0);
				setState(8);
				((ParpropContext)_localctx).child = wstlProperty(0);
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
				((FormulaContext)_localctx).child = wstlProperty(16);
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
				setState(22);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__5) {
					{
					setState(20);
					match(T__5);
					setState(21);
					((FormulaContext)_localctx).weight = match(VARIABLE);
					}
				}

				setState(24);
				((FormulaContext)_localctx).child = wstlProperty(15);
				}
				break;
			case 5:
				{
				_localctx = new FormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(25);
				((FormulaContext)_localctx).op = match(EEVENT);
				setState(26);
				match(T__2);
				setState(27);
				((FormulaContext)_localctx).low = match(RATIONAL);
				setState(28);
				match(T__3);
				setState(29);
				((FormulaContext)_localctx).high = match(RATIONAL);
				setState(30);
				match(T__4);
				setState(33);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__5) {
					{
					setState(31);
					match(T__5);
					setState(32);
					((FormulaContext)_localctx).weight = match(VARIABLE);
					}
				}

				setState(35);
				((FormulaContext)_localctx).child = wstlProperty(14);
				}
				break;
			case 6:
				{
				_localctx = new FormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(36);
				((FormulaContext)_localctx).op = match(ALWAYS);
				setState(37);
				match(T__2);
				setState(38);
				((FormulaContext)_localctx).low = match(RATIONAL);
				setState(39);
				match(T__3);
				setState(40);
				((FormulaContext)_localctx).high = match(RATIONAL);
				setState(41);
				match(T__4);
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__5) {
					{
					setState(42);
					match(T__5);
					setState(43);
					((FormulaContext)_localctx).weight = match(VARIABLE);
					}
				}

				setState(46);
				((FormulaContext)_localctx).child = wstlProperty(13);
				}
				break;
			case 7:
				{
				_localctx = new FormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(47);
				((FormulaContext)_localctx).op = match(EALWAYS);
				setState(48);
				match(T__2);
				setState(49);
				((FormulaContext)_localctx).low = match(RATIONAL);
				setState(50);
				match(T__3);
				setState(51);
				((FormulaContext)_localctx).high = match(RATIONAL);
				setState(52);
				match(T__4);
				setState(55);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__5) {
					{
					setState(53);
					match(T__5);
					setState(54);
					((FormulaContext)_localctx).weight = match(VARIABLE);
					}
				}

				setState(57);
				((FormulaContext)_localctx).child = wstlProperty(12);
				}
				break;
			case 8:
				{
				_localctx = new LongFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(58);
				((LongFormulaContext)_localctx).op = match(AND);
				setState(61);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__5) {
					{
					setState(59);
					match(T__5);
					setState(60);
					((LongFormulaContext)_localctx).weight = match(VARIABLE);
					}
				}

				setState(63);
				match(T__0);
				setState(64);
				wstlProperty(0);
				setState(67); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(65);
					match(T__3);
					setState(66);
					wstlProperty(0);
					}
					}
					setState(69); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__3 );
				setState(71);
				match(T__1);
				}
				break;
			case 9:
				{
				_localctx = new LongFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(73);
				((LongFormulaContext)_localctx).op = match(EAND);
				setState(76);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__5) {
					{
					setState(74);
					match(T__5);
					setState(75);
					((LongFormulaContext)_localctx).weight = match(VARIABLE);
					}
				}

				setState(78);
				match(T__0);
				setState(79);
				wstlProperty(0);
				setState(82); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(80);
					match(T__3);
					setState(81);
					wstlProperty(0);
					}
					}
					setState(84); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__3 );
				setState(86);
				match(T__1);
				}
				break;
			case 10:
				{
				_localctx = new LongFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(88);
				((LongFormulaContext)_localctx).op = match(OR);
				setState(91);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__5) {
					{
					setState(89);
					match(T__5);
					setState(90);
					((LongFormulaContext)_localctx).weight = match(VARIABLE);
					}
				}

				setState(93);
				match(T__0);
				setState(94);
				wstlProperty(0);
				setState(97); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(95);
					match(T__3);
					setState(96);
					wstlProperty(0);
					}
					}
					setState(99); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__3 );
				setState(101);
				match(T__1);
				}
				break;
			case 11:
				{
				_localctx = new LongFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(103);
				((LongFormulaContext)_localctx).op = match(EOR);
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__5) {
					{
					setState(104);
					match(T__5);
					setState(105);
					((LongFormulaContext)_localctx).weight = match(VARIABLE);
					}
				}

				setState(108);
				match(T__0);
				setState(109);
				wstlProperty(0);
				setState(112); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(110);
					match(T__3);
					setState(111);
					wstlProperty(0);
					}
					}
					setState(114); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__3 );
				setState(116);
				match(T__1);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(177);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(175);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
					case 1:
						{
						_localctx = new FormulaContext(new WstlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_wstlProperty);
						setState(120);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(121);
						((FormulaContext)_localctx).op = match(IMPLIES);
						setState(122);
						((FormulaContext)_localctx).right = wstlProperty(12);
						}
						break;
					case 2:
						{
						_localctx = new FormulaContext(new WstlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_wstlProperty);
						setState(123);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(124);
						((FormulaContext)_localctx).op = match(AND);
						setState(127);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==T__5) {
							{
							setState(125);
							match(T__5);
							setState(126);
							((FormulaContext)_localctx).weight = match(VARIABLE);
							}
						}

						setState(129);
						((FormulaContext)_localctx).right = wstlProperty(11);
						}
						break;
					case 3:
						{
						_localctx = new FormulaContext(new WstlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_wstlProperty);
						setState(130);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(131);
						((FormulaContext)_localctx).op = match(EAND);
						setState(134);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==T__5) {
							{
							setState(132);
							match(T__5);
							setState(133);
							((FormulaContext)_localctx).weight = match(VARIABLE);
							}
						}

						setState(136);
						((FormulaContext)_localctx).right = wstlProperty(9);
						}
						break;
					case 4:
						{
						_localctx = new FormulaContext(new WstlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_wstlProperty);
						setState(137);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(138);
						((FormulaContext)_localctx).op = match(OR);
						setState(141);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==T__5) {
							{
							setState(139);
							match(T__5);
							setState(140);
							((FormulaContext)_localctx).weight = match(VARIABLE);
							}
						}

						setState(143);
						((FormulaContext)_localctx).right = wstlProperty(7);
						}
						break;
					case 5:
						{
						_localctx = new FormulaContext(new WstlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_wstlProperty);
						setState(144);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(145);
						((FormulaContext)_localctx).op = match(EOR);
						setState(148);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==T__5) {
							{
							setState(146);
							match(T__5);
							setState(147);
							((FormulaContext)_localctx).weight = match(VARIABLE);
							}
						}

						setState(150);
						((FormulaContext)_localctx).right = wstlProperty(5);
						}
						break;
					case 6:
						{
						_localctx = new FormulaContext(new WstlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_wstlProperty);
						setState(151);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(152);
						((FormulaContext)_localctx).op = match(UNTIL);
						setState(153);
						match(T__2);
						setState(154);
						((FormulaContext)_localctx).low = match(RATIONAL);
						setState(155);
						match(T__3);
						setState(156);
						((FormulaContext)_localctx).high = match(RATIONAL);
						setState(157);
						match(T__4);
						setState(160);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==T__5) {
							{
							setState(158);
							match(T__5);
							setState(159);
							((FormulaContext)_localctx).weight = match(VARIABLE);
							}
						}

						setState(162);
						((FormulaContext)_localctx).right = wstlProperty(3);
						}
						break;
					case 7:
						{
						_localctx = new FormulaContext(new WstlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_wstlProperty);
						setState(163);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(164);
						((FormulaContext)_localctx).op = match(RELEASE);
						setState(165);
						match(T__2);
						setState(166);
						((FormulaContext)_localctx).low = match(RATIONAL);
						setState(167);
						match(T__3);
						setState(168);
						((FormulaContext)_localctx).high = match(RATIONAL);
						setState(169);
						match(T__4);
						setState(172);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==T__5) {
							{
							setState(170);
							match(T__5);
							setState(171);
							((FormulaContext)_localctx).weight = match(VARIABLE);
							}
						}

						setState(174);
						((FormulaContext)_localctx).right = wstlProperty(2);
						}
						break;
					}
					} 
				}
				setState(179);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
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
		public TerminalNode VARIABLE() { return getToken(wstlParser.VARIABLE, 0); }
		public TerminalNode RATIONAL() { return getToken(wstlParser.RATIONAL, 0); }
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
			setState(192);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(181);
				_la = _input.LA(1);
				if ( !(_la==T__0 || _la==T__6) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(182);
				expr(0);
				setState(183);
				match(T__1);
				}
				break;
			case 2:
				{
				setState(185);
				match(VARIABLE);
				setState(186);
				match(T__0);
				setState(187);
				expr(0);
				setState(188);
				match(T__1);
				}
				break;
			case 3:
				{
				setState(190);
				match(RATIONAL);
				}
				break;
			case 4:
				{
				setState(191);
				match(VARIABLE);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(205);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(203);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(194);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(195);
						match(T__5);
						setState(196);
						expr(6);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(197);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(198);
						_la = _input.LA(1);
						if ( !(_la==T__7 || _la==T__8) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(199);
						expr(5);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(200);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(201);
						_la = _input.LA(1);
						if ( !(_la==T__9 || _la==T__10) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(202);
						expr(4);
						}
						break;
					}
					} 
				}
				setState(207);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
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
		public TerminalNode BOOLEAN() { return getToken(wstlParser.BOOLEAN, 0); }
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
			setState(213);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__6:
			case VARIABLE:
			case RATIONAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(208);
				((BooleanExprContext)_localctx).left = expr(0);
				setState(209);
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
				setState(210);
				((BooleanExprContext)_localctx).right = expr(0);
				}
				break;
			case BOOLEAN:
				enterOuterAlt(_localctx, 2);
				{
				setState(212);
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
			return wstlProperty_sempred((WstlPropertyContext)_localctx, predIndex);
		case 1:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean wstlProperty_sempred(WstlPropertyContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 11);
		case 1:
			return precpred(_ctx, 10);
		case 2:
			return precpred(_ctx, 8);
		case 3:
			return precpred(_ctx, 6);
		case 4:
			return precpred(_ctx, 4);
		case 5:
			return precpred(_ctx, 2);
		case 6:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 7:
			return precpred(_ctx, 6);
		case 8:
			return precpred(_ctx, 4);
		case 9:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"\u00da\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\5\2\31\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2$\n\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2/\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\5\2:\n\2\3\2\3\2\3\2\3\2\5\2@\n\2\3\2\3\2\3\2\3\2\6\2F\n\2\r\2"+
		"\16\2G\3\2\3\2\3\2\3\2\3\2\5\2O\n\2\3\2\3\2\3\2\3\2\6\2U\n\2\r\2\16\2"+
		"V\3\2\3\2\3\2\3\2\3\2\5\2^\n\2\3\2\3\2\3\2\3\2\6\2d\n\2\r\2\16\2e\3\2"+
		"\3\2\3\2\3\2\3\2\5\2m\n\2\3\2\3\2\3\2\3\2\6\2s\n\2\r\2\16\2t\3\2\3\2\5"+
		"\2y\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u0082\n\2\3\2\3\2\3\2\3\2\3\2"+
		"\5\2\u0089\n\2\3\2\3\2\3\2\3\2\3\2\5\2\u0090\n\2\3\2\3\2\3\2\3\2\3\2\5"+
		"\2\u0097\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u00a3\n\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u00af\n\2\3\2\7\2\u00b2\n\2\f"+
		"\2\16\2\u00b5\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3"+
		"\u00c3\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\u00ce\n\3\f\3\16\3"+
		"\u00d1\13\3\3\4\3\4\3\4\3\4\3\4\5\4\u00d8\n\4\3\4\2\4\2\4\5\2\4\6\2\6"+
		"\4\2\3\3\t\t\3\2\n\13\3\2\f\r\3\2\16\22\2\u0100\2x\3\2\2\2\4\u00c2\3\2"+
		"\2\2\6\u00d7\3\2\2\2\b\t\b\2\1\2\t\n\7\3\2\2\n\13\5\2\2\2\13\f\7\4\2\2"+
		"\fy\3\2\2\2\ry\5\6\4\2\16\17\7\30\2\2\17y\5\2\2\22\20\21\7\31\2\2\21\22"+
		"\7\5\2\2\22\23\7!\2\2\23\24\7\6\2\2\24\25\7!\2\2\25\30\7\7\2\2\26\27\7"+
		"\b\2\2\27\31\7 \2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\32\3\2\2\2\32y\5\2"+
		"\2\21\33\34\7\32\2\2\34\35\7\5\2\2\35\36\7!\2\2\36\37\7\6\2\2\37 \7!\2"+
		"\2 #\7\7\2\2!\"\7\b\2\2\"$\7 \2\2#!\3\2\2\2#$\3\2\2\2$%\3\2\2\2%y\5\2"+
		"\2\20&\'\7\33\2\2\'(\7\5\2\2()\7!\2\2)*\7\6\2\2*+\7!\2\2+.\7\7\2\2,-\7"+
		"\b\2\2-/\7 \2\2.,\3\2\2\2./\3\2\2\2/\60\3\2\2\2\60y\5\2\2\17\61\62\7\34"+
		"\2\2\62\63\7\5\2\2\63\64\7!\2\2\64\65\7\6\2\2\65\66\7!\2\2\669\7\7\2\2"+
		"\678\7\b\2\28:\7 \2\29\67\3\2\2\29:\3\2\2\2:;\3\2\2\2;y\5\2\2\16<?\7\23"+
		"\2\2=>\7\b\2\2>@\7 \2\2?=\3\2\2\2?@\3\2\2\2@A\3\2\2\2AB\7\3\2\2BE\5\2"+
		"\2\2CD\7\6\2\2DF\5\2\2\2EC\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3\2"+
		"\2\2IJ\7\4\2\2Jy\3\2\2\2KN\7\24\2\2LM\7\b\2\2MO\7 \2\2NL\3\2\2\2NO\3\2"+
		"\2\2OP\3\2\2\2PQ\7\3\2\2QT\5\2\2\2RS\7\6\2\2SU\5\2\2\2TR\3\2\2\2UV\3\2"+
		"\2\2VT\3\2\2\2VW\3\2\2\2WX\3\2\2\2XY\7\4\2\2Yy\3\2\2\2Z]\7\25\2\2[\\\7"+
		"\b\2\2\\^\7 \2\2][\3\2\2\2]^\3\2\2\2^_\3\2\2\2_`\7\3\2\2`c\5\2\2\2ab\7"+
		"\6\2\2bd\5\2\2\2ca\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2\2fg\3\2\2\2gh\7"+
		"\4\2\2hy\3\2\2\2il\7\26\2\2jk\7\b\2\2km\7 \2\2lj\3\2\2\2lm\3\2\2\2mn\3"+
		"\2\2\2no\7\3\2\2or\5\2\2\2pq\7\6\2\2qs\5\2\2\2rp\3\2\2\2st\3\2\2\2tr\3"+
		"\2\2\2tu\3\2\2\2uv\3\2\2\2vw\7\4\2\2wy\3\2\2\2x\b\3\2\2\2x\r\3\2\2\2x"+
		"\16\3\2\2\2x\20\3\2\2\2x\33\3\2\2\2x&\3\2\2\2x\61\3\2\2\2x<\3\2\2\2xK"+
		"\3\2\2\2xZ\3\2\2\2xi\3\2\2\2y\u00b3\3\2\2\2z{\f\r\2\2{|\7\27\2\2|\u00b2"+
		"\5\2\2\16}~\f\f\2\2~\u0081\7\23\2\2\177\u0080\7\b\2\2\u0080\u0082\7 \2"+
		"\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u00b2"+
		"\5\2\2\r\u0084\u0085\f\n\2\2\u0085\u0088\7\24\2\2\u0086\u0087\7\b\2\2"+
		"\u0087\u0089\7 \2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a"+
		"\3\2\2\2\u008a\u00b2\5\2\2\13\u008b\u008c\f\b\2\2\u008c\u008f\7\25\2\2"+
		"\u008d\u008e\7\b\2\2\u008e\u0090\7 \2\2\u008f\u008d\3\2\2\2\u008f\u0090"+
		"\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u00b2\5\2\2\t\u0092\u0093\f\6\2\2\u0093"+
		"\u0096\7\26\2\2\u0094\u0095\7\b\2\2\u0095\u0097\7 \2\2\u0096\u0094\3\2"+
		"\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u00b2\5\2\2\7\u0099"+
		"\u009a\f\4\2\2\u009a\u009b\7\35\2\2\u009b\u009c\7\5\2\2\u009c\u009d\7"+
		"!\2\2\u009d\u009e\7\6\2\2\u009e\u009f\7!\2\2\u009f\u00a2\7\7\2\2\u00a0"+
		"\u00a1\7\b\2\2\u00a1\u00a3\7 \2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2"+
		"\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00b2\5\2\2\5\u00a5\u00a6\f\3\2\2\u00a6"+
		"\u00a7\7\36\2\2\u00a7\u00a8\7\5\2\2\u00a8\u00a9\7!\2\2\u00a9\u00aa\7\6"+
		"\2\2\u00aa\u00ab\7!\2\2\u00ab\u00ae\7\7\2\2\u00ac\u00ad\7\b\2\2\u00ad"+
		"\u00af\7 \2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\3\2"+
		"\2\2\u00b0\u00b2\5\2\2\4\u00b1z\3\2\2\2\u00b1}\3\2\2\2\u00b1\u0084\3\2"+
		"\2\2\u00b1\u008b\3\2\2\2\u00b1\u0092\3\2\2\2\u00b1\u0099\3\2\2\2\u00b1"+
		"\u00a5\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2"+
		"\2\2\u00b4\3\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\b\3\1\2\u00b7\u00b8"+
		"\t\2\2\2\u00b8\u00b9\5\4\3\2\u00b9\u00ba\7\4\2\2\u00ba\u00c3\3\2\2\2\u00bb"+
		"\u00bc\7 \2\2\u00bc\u00bd\7\3\2\2\u00bd\u00be\5\4\3\2\u00be\u00bf\7\4"+
		"\2\2\u00bf\u00c3\3\2\2\2\u00c0\u00c3\7!\2\2\u00c1\u00c3\7 \2\2\u00c2\u00b6"+
		"\3\2\2\2\u00c2\u00bb\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3"+
		"\u00cf\3\2\2\2\u00c4\u00c5\f\b\2\2\u00c5\u00c6\7\b\2\2\u00c6\u00ce\5\4"+
		"\3\b\u00c7\u00c8\f\6\2\2\u00c8\u00c9\t\3\2\2\u00c9\u00ce\5\4\3\7\u00ca"+
		"\u00cb\f\5\2\2\u00cb\u00cc\t\4\2\2\u00cc\u00ce\5\4\3\6\u00cd\u00c4\3\2"+
		"\2\2\u00cd\u00c7\3\2\2\2\u00cd\u00ca\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf"+
		"\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\5\3\2\2\2\u00d1\u00cf\3\2\2\2"+
		"\u00d2\u00d3\5\4\3\2\u00d3\u00d4\t\5\2\2\u00d4\u00d5\5\4\3\2\u00d5\u00d8"+
		"\3\2\2\2\u00d6\u00d8\7\37\2\2\u00d7\u00d2\3\2\2\2\u00d7\u00d6\3\2\2\2"+
		"\u00d8\7\3\2\2\2\33\30#.9?GNV]eltx\u0081\u0088\u008f\u0096\u00a2\u00ae"+
		"\u00b1\u00b3\u00c2\u00cd\u00cf\u00d7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}