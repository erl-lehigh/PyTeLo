// Generated from mtl.g4 by ANTLR 4.7.1

'''
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class mtlLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, AND=6, OR=7, IMPLIES=8, NOT=9, 
		EVENT=10, ALWAYS=11, UNTIL=12, BOOLEAN=13, VARIABLE=14, RATIONAL=15, WS=16;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "AND", "OR", "IMPLIES", "NOT", 
		"EVENT", "ALWAYS", "UNTIL", "BOOLEAN", "VARIABLE", "RATIONAL", "WS"
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


	public mtlLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "mtl.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22\u008c\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3"+
		"\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\63\n\7\3\b"+
		"\3\b\3\b\3\b\3\b\5\b:\n\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\5\13D\n\13"+
		"\3\f\3\f\3\f\5\fI\n\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16_\n\16\3\17\5\17"+
		"b\n\17\3\17\7\17e\n\17\f\17\16\17h\13\17\3\20\5\20k\n\20\3\20\7\20n\n"+
		"\20\f\20\16\20q\13\20\3\20\5\20t\n\20\3\20\6\20w\n\20\r\20\16\20x\3\20"+
		"\3\20\3\20\5\20~\n\20\3\20\7\20\u0081\n\20\f\20\16\20\u0084\13\20\3\21"+
		"\6\21\u0087\n\21\r\21\16\21\u0088\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13"+
		"\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22\3\2\7\4\2"+
		"##\u0080\u0080\4\2C\\c|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2\u009d"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2"+
		"\2\2\5%\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r\62\3\2\2\2\179\3"+
		"\2\2\2\21;\3\2\2\2\23>\3\2\2\2\25C\3\2\2\2\27H\3\2\2\2\31J\3\2\2\2\33"+
		"^\3\2\2\2\35a\3\2\2\2\37j\3\2\2\2!\u0086\3\2\2\2#$\7*\2\2$\4\3\2\2\2%"+
		"&\7+\2\2&\6\3\2\2\2\'(\7]\2\2(\b\3\2\2\2)*\7.\2\2*\n\3\2\2\2+,\7_\2\2"+
		",\f\3\2\2\2-\63\7(\2\2./\7(\2\2/\63\7(\2\2\60\61\7\61\2\2\61\63\7^\2\2"+
		"\62-\3\2\2\2\62.\3\2\2\2\62\60\3\2\2\2\63\16\3\2\2\2\64:\7~\2\2\65\66"+
		"\7~\2\2\66:\7~\2\2\678\7^\2\28:\7\61\2\29\64\3\2\2\29\65\3\2\2\29\67\3"+
		"\2\2\2:\20\3\2\2\2;<\7?\2\2<=\7@\2\2=\22\3\2\2\2>?\t\2\2\2?\24\3\2\2\2"+
		"@D\7H\2\2AB\7>\2\2BD\7@\2\2C@\3\2\2\2CA\3\2\2\2D\26\3\2\2\2EI\7I\2\2F"+
		"G\7]\2\2GI\7_\2\2HE\3\2\2\2HF\3\2\2\2I\30\3\2\2\2JK\7W\2\2K\32\3\2\2\2"+
		"LM\7v\2\2MN\7t\2\2NO\7w\2\2O_\7g\2\2PQ\7V\2\2QR\7t\2\2RS\7w\2\2S_\7g\2"+
		"\2TU\7h\2\2UV\7c\2\2VW\7n\2\2WX\7u\2\2X_\7g\2\2YZ\7H\2\2Z[\7c\2\2[\\\7"+
		"n\2\2\\]\7u\2\2]_\7g\2\2^L\3\2\2\2^P\3\2\2\2^T\3\2\2\2^Y\3\2\2\2_\34\3"+
		"\2\2\2`b\t\3\2\2a`\3\2\2\2bf\3\2\2\2ce\t\4\2\2dc\3\2\2\2eh\3\2\2\2fd\3"+
		"\2\2\2fg\3\2\2\2g\36\3\2\2\2hf\3\2\2\2ik\7/\2\2ji\3\2\2\2jk\3\2\2\2ko"+
		"\3\2\2\2ln\t\5\2\2ml\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2\2ps\3\2\2\2q"+
		"o\3\2\2\2rt\7\60\2\2sr\3\2\2\2st\3\2\2\2tv\3\2\2\2uw\t\5\2\2vu\3\2\2\2"+
		"wx\3\2\2\2xv\3\2\2\2xy\3\2\2\2y}\3\2\2\2z~\7G\2\2{|\7G\2\2|~\7/\2\2}z"+
		"\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0082\3\2\2\2\177\u0081\t\5\2\2\u0080\177"+
		"\3\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083"+
		" \3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0087\t\6\2\2\u0086\u0085\3\2\2\2"+
		"\u0087\u0088\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a"+
		"\3\2\2\2\u008a\u008b\b\21\2\2\u008b\"\3\2\2\2\22\2\629CH^adfjosx}\u0082"+
		"\u0088\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}