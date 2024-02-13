// Generated from mtl.g4 by ANTLR 4.7.1

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
public class mtlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, AND=6, OR=7, IMPLIES=8, NOT=9, 
		EVENT=10, ALWAYS=11, UNTIL=12, BOOLEAN=13, VARIABLE=14, RATIONAL=15, WS=16;
	public static final int
		RULE_mtlProperty = 0, RULE_booleanExpr = 1;
	public static final String[] ruleNames = {
		"mtlProperty", "booleanExpr"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'('", "')'", "'['", "','", "']'", null, null, "'=>'", null, null, 
		null, "'U'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, "AND", "OR", "IMPLIES", "NOT", "EVENT", 
		"ALWAYS", "UNTIL", "BOOLEAN", "VARIABLE", "RATIONAL", "WS"
	};
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
	public String getGrammarFileName() { return "mtl.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public mtlParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class MtlPropertyContext extends ParserRuleContext {
		public MtlPropertyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mtlProperty; }
	 
		public MtlPropertyContext() { }
		public void copyFrom(MtlPropertyContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class BooleanPredContext extends MtlPropertyContext {
		public BooleanExprContext booleanExpr() {
			return getRuleContext(BooleanExprContext.class,0);
		}
		public BooleanPredContext(MtlPropertyContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mtlListener ) ((mtlListener)listener).enterBooleanPred(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mtlListener ) ((mtlListener)listener).exitBooleanPred(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mtlVisitor ) return ((mtlVisitor<? extends T>)visitor).visitBooleanPred(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class FormulaContext extends MtlPropertyContext {
		public MtlPropertyContext left;
		public Token op;
		public MtlPropertyContext child;
		public Token low;
		public Token high;
		public MtlPropertyContext right;
		public TerminalNode NOT() { return getToken(mtlParser.NOT, 0); }
		public List<MtlPropertyContext> mtlProperty() {
			return getRuleContexts(MtlPropertyContext.class);
		}
		public MtlPropertyContext mtlProperty(int i) {
			return getRuleContext(MtlPropertyContext.class,i);
		}
		public TerminalNode EVENT() { return getToken(mtlParser.EVENT, 0); }
		public List<TerminalNode> RATIONAL() { return getTokens(mtlParser.RATIONAL); }
		public TerminalNode RATIONAL(int i) {
			return getToken(mtlParser.RATIONAL, i);
		}
		public TerminalNode ALWAYS() { return getToken(mtlParser.ALWAYS, 0); }
		public TerminalNode IMPLIES() { return getToken(mtlParser.IMPLIES, 0); }
		public TerminalNode AND() { return getToken(mtlParser.AND, 0); }
		public TerminalNode OR() { return getToken(mtlParser.OR, 0); }
		public TerminalNode UNTIL() { return getToken(mtlParser.UNTIL, 0); }
		public FormulaContext(MtlPropertyContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mtlListener ) ((mtlListener)listener).enterFormula(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mtlListener ) ((mtlListener)listener).exitFormula(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mtlVisitor ) return ((mtlVisitor<? extends T>)visitor).visitFormula(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class ParpropContext extends MtlPropertyContext {
		public MtlPropertyContext child;
		public MtlPropertyContext mtlProperty() {
			return getRuleContext(MtlPropertyContext.class,0);
		}
		public ParpropContext(MtlPropertyContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mtlListener ) ((mtlListener)listener).enterParprop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mtlListener ) ((mtlListener)listener).exitParprop(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mtlVisitor ) return ((mtlVisitor<? extends T>)visitor).visitParprop(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MtlPropertyContext mtlProperty() throws RecognitionException {
		return mtlProperty(0);
	}

	private MtlPropertyContext mtlProperty(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		MtlPropertyContext _localctx = new MtlPropertyContext(_ctx, _parentState);
		MtlPropertyContext _prevctx = _localctx;
		int _startState = 0;
		enterRecursionRule(_localctx, 0, RULE_mtlProperty, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				{
				_localctx = new ParpropContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(5);
				match(T__0);
				setState(6);
				((ParpropContext)_localctx).child = mtlProperty(0);
				setState(7);
				match(T__1);
				}
				break;
			case BOOLEAN:
			case VARIABLE:
				{
				_localctx = new BooleanPredContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(9);
				booleanExpr();
				}
				break;
			case NOT:
				{
				_localctx = new FormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(10);
				((FormulaContext)_localctx).op = match(NOT);
				setState(11);
				((FormulaContext)_localctx).child = mtlProperty(7);
				}
				break;
			case EVENT:
				{
				_localctx = new FormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(12);
				((FormulaContext)_localctx).op = match(EVENT);
				setState(13);
				match(T__2);
				setState(14);
				((FormulaContext)_localctx).low = match(RATIONAL);
				setState(15);
				match(T__3);
				setState(16);
				((FormulaContext)_localctx).high = match(RATIONAL);
				setState(17);
				match(T__4);
				setState(18);
				((FormulaContext)_localctx).child = mtlProperty(6);
				}
				break;
			case ALWAYS:
				{
				_localctx = new FormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(19);
				((FormulaContext)_localctx).op = match(ALWAYS);
				setState(20);
				match(T__2);
				setState(21);
				((FormulaContext)_localctx).low = match(RATIONAL);
				setState(22);
				match(T__3);
				setState(23);
				((FormulaContext)_localctx).high = match(RATIONAL);
				setState(24);
				match(T__4);
				setState(25);
				((FormulaContext)_localctx).child = mtlProperty(5);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(47);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(45);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						_localctx = new FormulaContext(new MtlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_mtlProperty);
						setState(28);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(29);
						((FormulaContext)_localctx).op = match(IMPLIES);
						setState(30);
						((FormulaContext)_localctx).right = mtlProperty(5);
						}
						break;
					case 2:
						{
						_localctx = new FormulaContext(new MtlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_mtlProperty);
						setState(31);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(32);
						((FormulaContext)_localctx).op = match(AND);
						setState(33);
						((FormulaContext)_localctx).right = mtlProperty(4);
						}
						break;
					case 3:
						{
						_localctx = new FormulaContext(new MtlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_mtlProperty);
						setState(34);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(35);
						((FormulaContext)_localctx).op = match(OR);
						setState(36);
						((FormulaContext)_localctx).right = mtlProperty(3);
						}
						break;
					case 4:
						{
						_localctx = new FormulaContext(new MtlPropertyContext(_parentctx, _parentState));
						((FormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_mtlProperty);
						setState(37);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(38);
						((FormulaContext)_localctx).op = match(UNTIL);
						setState(39);
						match(T__2);
						setState(40);
						((FormulaContext)_localctx).low = match(RATIONAL);
						setState(41);
						match(T__3);
						setState(42);
						((FormulaContext)_localctx).high = match(RATIONAL);
						setState(43);
						match(T__4);
						setState(44);
						((FormulaContext)_localctx).right = mtlProperty(2);
						}
						break;
					}
					} 
				}
				setState(49);
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

	public static class BooleanExprContext extends ParserRuleContext {
		public Token op;
		public TerminalNode BOOLEAN() { return getToken(mtlParser.BOOLEAN, 0); }
		public TerminalNode VARIABLE() { return getToken(mtlParser.VARIABLE, 0); }
		public BooleanExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_booleanExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mtlListener ) ((mtlListener)listener).enterBooleanExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mtlListener ) ((mtlListener)listener).exitBooleanExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mtlVisitor ) return ((mtlVisitor<? extends T>)visitor).visitBooleanExpr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BooleanExprContext booleanExpr() throws RecognitionException {
		BooleanExprContext _localctx = new BooleanExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_booleanExpr);
		try {
			setState(52);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOLEAN:
				enterOuterAlt(_localctx, 1);
				{
				setState(50);
				((BooleanExprContext)_localctx).op = match(BOOLEAN);
				}
				break;
			case VARIABLE:
				enterOuterAlt(_localctx, 2);
				{
				setState(51);
				((BooleanExprContext)_localctx).op = match(VARIABLE);
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
			return mtlProperty_sempred((MtlPropertyContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean mtlProperty_sempred(MtlPropertyContext _localctx, int predIndex) {
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\229\4\2\t\2\4\3\t"+
		"\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\5\2\35\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\60\n\2\f\2\16\2\63\13\2\3\3\3\3\5\3"+
		"\67\n\3\3\3\2\3\2\4\2\4\2\2\2?\2\34\3\2\2\2\4\66\3\2\2\2\6\7\b\2\1\2\7"+
		"\b\7\3\2\2\b\t\5\2\2\2\t\n\7\4\2\2\n\35\3\2\2\2\13\35\5\4\3\2\f\r\7\13"+
		"\2\2\r\35\5\2\2\t\16\17\7\f\2\2\17\20\7\5\2\2\20\21\7\21\2\2\21\22\7\6"+
		"\2\2\22\23\7\21\2\2\23\24\7\7\2\2\24\35\5\2\2\b\25\26\7\r\2\2\26\27\7"+
		"\5\2\2\27\30\7\21\2\2\30\31\7\6\2\2\31\32\7\21\2\2\32\33\7\7\2\2\33\35"+
		"\5\2\2\7\34\6\3\2\2\2\34\13\3\2\2\2\34\f\3\2\2\2\34\16\3\2\2\2\34\25\3"+
		"\2\2\2\35\61\3\2\2\2\36\37\f\6\2\2\37 \7\n\2\2 \60\5\2\2\7!\"\f\5\2\2"+
		"\"#\7\b\2\2#\60\5\2\2\6$%\f\4\2\2%&\7\t\2\2&\60\5\2\2\5\'(\f\3\2\2()\7"+
		"\16\2\2)*\7\5\2\2*+\7\21\2\2+,\7\6\2\2,-\7\21\2\2-.\7\7\2\2.\60\5\2\2"+
		"\4/\36\3\2\2\2/!\3\2\2\2/$\3\2\2\2/\'\3\2\2\2\60\63\3\2\2\2\61/\3\2\2"+
		"\2\61\62\3\2\2\2\62\3\3\2\2\2\63\61\3\2\2\2\64\67\7\17\2\2\65\67\7\20"+
		"\2\2\66\64\3\2\2\2\66\65\3\2\2\2\67\5\3\2\2\2\6\34/\61\66";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}