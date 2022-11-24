// Generated from /home/gustavo/lehigh/erl/python-stl/stl/stl.g4 by ANTLR 4.9.2

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
public class stlLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, AND=17, 
		EAND=18, OR=19, EOR=20, IMPLIES=21, NOT=22, EVENT=23, EEVENT=24, ALWAYS=25, 
		EALWAYS=26, UNTIL=27, BOOLEAN=28, VARIABLE=29, RATIONAL=30, WS=31;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "AND", 
			"EAND", "OR", "EOR", "IMPLIES", "NOT", "EVENT", "EEVENT", "ALWAYS", "EALWAYS", 
			"UNTIL", "BOOLEAN", "VARIABLE", "RATIONAL", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'['", "','", "']'", "'-('", "'^'", "'*'", "'/'", 
			"'+'", "'-'", "'<'", "'<='", "'='", "'>='", "'>'", null, "'&'", null, 
			"'|'", "'=>'", null, "'F'", "'/F'", "'G'", "'/G'", "'U'"
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


	public stlLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "stl.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2!\u00c5\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \3\2"+
		"\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3"+
		"\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3"+
		"\21\3\21\3\22\3\22\3\22\3\22\5\22i\n\22\3\23\3\23\3\24\3\24\3\24\3\24"+
		"\5\24q\n\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31"+
		"\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35"+
		"\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0098\n\35"+
		"\3\36\5\36\u009b\n\36\3\36\7\36\u009e\n\36\f\36\16\36\u00a1\13\36\3\37"+
		"\5\37\u00a4\n\37\3\37\7\37\u00a7\n\37\f\37\16\37\u00aa\13\37\3\37\5\37"+
		"\u00ad\n\37\3\37\6\37\u00b0\n\37\r\37\16\37\u00b1\3\37\3\37\3\37\5\37"+
		"\u00b7\n\37\3\37\7\37\u00ba\n\37\f\37\16\37\u00bd\13\37\3 \6 \u00c0\n"+
		" \r \16 \u00c1\3 \3 \2\2!\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25"+
		"\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32"+
		"\63\33\65\34\67\359\36;\37= ?!\3\2\7\4\2##\u0080\u0080\4\2C\\c|\6\2\62"+
		";C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2\u00d2\2\3\3\2\2\2\2\5\3\2\2\2\2"+
		"\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2"+
		"\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2"+
		"\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2"+
		"\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2"+
		"\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2"+
		"\2\3A\3\2\2\2\5C\3\2\2\2\7E\3\2\2\2\tG\3\2\2\2\13I\3\2\2\2\rK\3\2\2\2"+
		"\17N\3\2\2\2\21P\3\2\2\2\23R\3\2\2\2\25T\3\2\2\2\27V\3\2\2\2\31X\3\2\2"+
		"\2\33Z\3\2\2\2\35]\3\2\2\2\37_\3\2\2\2!b\3\2\2\2#h\3\2\2\2%j\3\2\2\2\'"+
		"p\3\2\2\2)r\3\2\2\2+t\3\2\2\2-w\3\2\2\2/y\3\2\2\2\61{\3\2\2\2\63~\3\2"+
		"\2\2\65\u0080\3\2\2\2\67\u0083\3\2\2\29\u0097\3\2\2\2;\u009a\3\2\2\2="+
		"\u00a3\3\2\2\2?\u00bf\3\2\2\2AB\7*\2\2B\4\3\2\2\2CD\7+\2\2D\6\3\2\2\2"+
		"EF\7]\2\2F\b\3\2\2\2GH\7.\2\2H\n\3\2\2\2IJ\7_\2\2J\f\3\2\2\2KL\7/\2\2"+
		"LM\7*\2\2M\16\3\2\2\2NO\7`\2\2O\20\3\2\2\2PQ\7,\2\2Q\22\3\2\2\2RS\7\61"+
		"\2\2S\24\3\2\2\2TU\7-\2\2U\26\3\2\2\2VW\7/\2\2W\30\3\2\2\2XY\7>\2\2Y\32"+
		"\3\2\2\2Z[\7>\2\2[\\\7?\2\2\\\34\3\2\2\2]^\7?\2\2^\36\3\2\2\2_`\7@\2\2"+
		"`a\7?\2\2a \3\2\2\2bc\7@\2\2c\"\3\2\2\2de\7(\2\2ei\7(\2\2fg\7\61\2\2g"+
		"i\7^\2\2hd\3\2\2\2hf\3\2\2\2i$\3\2\2\2jk\7(\2\2k&\3\2\2\2lm\7~\2\2mq\7"+
		"~\2\2no\7^\2\2oq\7\61\2\2pl\3\2\2\2pn\3\2\2\2q(\3\2\2\2rs\7~\2\2s*\3\2"+
		"\2\2tu\7?\2\2uv\7@\2\2v,\3\2\2\2wx\t\2\2\2x.\3\2\2\2yz\7H\2\2z\60\3\2"+
		"\2\2{|\7\61\2\2|}\7H\2\2}\62\3\2\2\2~\177\7I\2\2\177\64\3\2\2\2\u0080"+
		"\u0081\7\61\2\2\u0081\u0082\7I\2\2\u0082\66\3\2\2\2\u0083\u0084\7W\2\2"+
		"\u00848\3\2\2\2\u0085\u0086\7v\2\2\u0086\u0087\7t\2\2\u0087\u0088\7w\2"+
		"\2\u0088\u0098\7g\2\2\u0089\u008a\7V\2\2\u008a\u008b\7t\2\2\u008b\u008c"+
		"\7w\2\2\u008c\u0098\7g\2\2\u008d\u008e\7h\2\2\u008e\u008f\7c\2\2\u008f"+
		"\u0090\7n\2\2\u0090\u0091\7u\2\2\u0091\u0098\7g\2\2\u0092\u0093\7H\2\2"+
		"\u0093\u0094\7c\2\2\u0094\u0095\7n\2\2\u0095\u0096\7u\2\2\u0096\u0098"+
		"\7g\2\2\u0097\u0085\3\2\2\2\u0097\u0089\3\2\2\2\u0097\u008d\3\2\2\2\u0097"+
		"\u0092\3\2\2\2\u0098:\3\2\2\2\u0099\u009b\t\3\2\2\u009a\u0099\3\2\2\2"+
		"\u009b\u009f\3\2\2\2\u009c\u009e\t\4\2\2\u009d\u009c\3\2\2\2\u009e\u00a1"+
		"\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0<\3\2\2\2\u00a1"+
		"\u009f\3\2\2\2\u00a2\u00a4\7/\2\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2"+
		"\2\2\u00a4\u00a8\3\2\2\2\u00a5\u00a7\t\5\2\2\u00a6\u00a5\3\2\2\2\u00a7"+
		"\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ac\3\2"+
		"\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00ad\7\60\2\2\u00ac\u00ab\3\2\2\2\u00ac"+
		"\u00ad\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00b0\t\5\2\2\u00af\u00ae\3\2"+
		"\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2"+
		"\u00b6\3\2\2\2\u00b3\u00b7\7G\2\2\u00b4\u00b5\7G\2\2\u00b5\u00b7\7/\2"+
		"\2\u00b6\u00b3\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00bb"+
		"\3\2\2\2\u00b8\u00ba\t\5\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb"+
		"\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc>\3\2\2\2\u00bd\u00bb\3\2\2\2"+
		"\u00be\u00c0\t\6\2\2\u00bf\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00bf"+
		"\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\b \2\2\u00c4"+
		"@\3\2\2\2\20\2hp\u0097\u009a\u009d\u009f\u00a3\u00a8\u00ac\u00b1\u00b6"+
		"\u00bb\u00c1\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}