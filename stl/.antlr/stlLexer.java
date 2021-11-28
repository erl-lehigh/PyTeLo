// Generated from /home/gustavo/lehigh/erl/python-stl/stl/stl.g4 by ANTLR 4.8

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
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, AND=17, 
		OR=18, IMPLIES=19, NOT=20, EVENT=21, ALWAYS=22, UNTIL=23, BOOLEAN=24, 
		VARIABLE=25, RATIONAL=26, WS=27;
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
			"OR", "IMPLIES", "NOT", "EVENT", "ALWAYS", "UNTIL", "BOOLEAN", "VARIABLE", 
			"RATIONAL", "WS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\35\u00bb\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3"+
		"\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3"+
		"\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22\3"+
		"\22\5\22b\n\22\3\23\3\23\3\23\3\23\3\23\5\23i\n\23\3\24\3\24\3\24\3\25"+
		"\3\25\3\26\3\26\3\26\5\26s\n\26\3\27\3\27\3\27\5\27x\n\27\3\30\3\30\3"+
		"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3"+
		"\31\3\31\3\31\3\31\5\31\u008e\n\31\3\32\5\32\u0091\n\32\3\32\7\32\u0094"+
		"\n\32\f\32\16\32\u0097\13\32\3\33\5\33\u009a\n\33\3\33\7\33\u009d\n\33"+
		"\f\33\16\33\u00a0\13\33\3\33\5\33\u00a3\n\33\3\33\6\33\u00a6\n\33\r\33"+
		"\16\33\u00a7\3\33\3\33\3\33\5\33\u00ad\n\33\3\33\7\33\u00b0\n\33\f\33"+
		"\16\33\u00b3\13\33\3\34\6\34\u00b6\n\34\r\34\16\34\u00b7\3\34\3\34\2\2"+
		"\35\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35"+
		"\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35\3\2"+
		"\7\4\2##\u0080\u0080\4\2C\\c|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\""+
		"\"\2\u00cc\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2"+
		"\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27"+
		"\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2"+
		"\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2"+
		"\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\39\3\2"+
		"\2\2\5;\3\2\2\2\7=\3\2\2\2\t?\3\2\2\2\13A\3\2\2\2\rC\3\2\2\2\17F\3\2\2"+
		"\2\21H\3\2\2\2\23J\3\2\2\2\25L\3\2\2\2\27N\3\2\2\2\31P\3\2\2\2\33R\3\2"+
		"\2\2\35U\3\2\2\2\37W\3\2\2\2!Z\3\2\2\2#a\3\2\2\2%h\3\2\2\2\'j\3\2\2\2"+
		")m\3\2\2\2+r\3\2\2\2-w\3\2\2\2/y\3\2\2\2\61\u008d\3\2\2\2\63\u0090\3\2"+
		"\2\2\65\u0099\3\2\2\2\67\u00b5\3\2\2\29:\7*\2\2:\4\3\2\2\2;<\7+\2\2<\6"+
		"\3\2\2\2=>\7]\2\2>\b\3\2\2\2?@\7.\2\2@\n\3\2\2\2AB\7_\2\2B\f\3\2\2\2C"+
		"D\7/\2\2DE\7*\2\2E\16\3\2\2\2FG\7`\2\2G\20\3\2\2\2HI\7,\2\2I\22\3\2\2"+
		"\2JK\7\61\2\2K\24\3\2\2\2LM\7-\2\2M\26\3\2\2\2NO\7/\2\2O\30\3\2\2\2PQ"+
		"\7>\2\2Q\32\3\2\2\2RS\7>\2\2ST\7?\2\2T\34\3\2\2\2UV\7?\2\2V\36\3\2\2\2"+
		"WX\7@\2\2XY\7?\2\2Y \3\2\2\2Z[\7@\2\2[\"\3\2\2\2\\b\7(\2\2]^\7(\2\2^b"+
		"\7(\2\2_`\7\61\2\2`b\7^\2\2a\\\3\2\2\2a]\3\2\2\2a_\3\2\2\2b$\3\2\2\2c"+
		"i\7~\2\2de\7~\2\2ei\7~\2\2fg\7^\2\2gi\7\61\2\2hc\3\2\2\2hd\3\2\2\2hf\3"+
		"\2\2\2i&\3\2\2\2jk\7?\2\2kl\7@\2\2l(\3\2\2\2mn\t\2\2\2n*\3\2\2\2os\7H"+
		"\2\2pq\7>\2\2qs\7@\2\2ro\3\2\2\2rp\3\2\2\2s,\3\2\2\2tx\7I\2\2uv\7]\2\2"+
		"vx\7_\2\2wt\3\2\2\2wu\3\2\2\2x.\3\2\2\2yz\7W\2\2z\60\3\2\2\2{|\7v\2\2"+
		"|}\7t\2\2}~\7w\2\2~\u008e\7g\2\2\177\u0080\7V\2\2\u0080\u0081\7t\2\2\u0081"+
		"\u0082\7w\2\2\u0082\u008e\7g\2\2\u0083\u0084\7h\2\2\u0084\u0085\7c\2\2"+
		"\u0085\u0086\7n\2\2\u0086\u0087\7u\2\2\u0087\u008e\7g\2\2\u0088\u0089"+
		"\7H\2\2\u0089\u008a\7c\2\2\u008a\u008b\7n\2\2\u008b\u008c\7u\2\2\u008c"+
		"\u008e\7g\2\2\u008d{\3\2\2\2\u008d\177\3\2\2\2\u008d\u0083\3\2\2\2\u008d"+
		"\u0088\3\2\2\2\u008e\62\3\2\2\2\u008f\u0091\t\3\2\2\u0090\u008f\3\2\2"+
		"\2\u0091\u0095\3\2\2\2\u0092\u0094\t\4\2\2\u0093\u0092\3\2\2\2\u0094\u0097"+
		"\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\64\3\2\2\2\u0097"+
		"\u0095\3\2\2\2\u0098\u009a\7/\2\2\u0099\u0098\3\2\2\2\u0099\u009a\3\2"+
		"\2\2\u009a\u009e\3\2\2\2\u009b\u009d\t\5\2\2\u009c\u009b\3\2\2\2\u009d"+
		"\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a2\3\2"+
		"\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a3\7\60\2\2\u00a2\u00a1\3\2\2\2\u00a2"+
		"\u00a3\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u00a6\t\5\2\2\u00a5\u00a4\3\2"+
		"\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8"+
		"\u00ac\3\2\2\2\u00a9\u00ad\7G\2\2\u00aa\u00ab\7G\2\2\u00ab\u00ad\7/\2"+
		"\2\u00ac\u00a9\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00b1"+
		"\3\2\2\2\u00ae\u00b0\t\5\2\2\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1"+
		"\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\66\3\2\2\2\u00b3\u00b1\3\2\2"+
		"\2\u00b4\u00b6\t\6\2\2\u00b5\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b5"+
		"\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\b\34\2\2"+
		"\u00ba8\3\2\2\2\22\2ahrw\u008d\u0090\u0093\u0095\u0099\u009e\u00a2\u00a7"+
		"\u00ac\u00b1\u00b7\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}