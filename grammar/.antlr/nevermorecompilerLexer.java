// Generated from /home/katana/NevermoreCompile/grammar/nevermorecompiler.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class nevermorecompilerLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, ID=11, INT=12, DOUBLE=13, END_STATE=14, ADD=15, SUB=16, MUL=17, 
		DIV=18, LPAREN=19, RPAREN=20, GT=21, LT=22, EQ_EQ=23, NOT_EQ=24, RCORNER=25, 
		LCORNER=26, INCREMENT=27, EQ=28, WS=29, NEWLINE=30;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "ID", "DIGIT", "LETTER", "INT", "DOUBLE", "END_STATE", "ADD", 
			"SUB", "MUL", "DIV", "LPAREN", "RPAREN", "GT", "LT", "EQ_EQ", "NOT_EQ", 
			"RCORNER", "LCORNER", "INCREMENT", "EQ", "WS", "NEWLINE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'else'", "'for'", "'while'", "'do'", "'print'", "'global:'", 
			"':'", "'int'", "'double'", null, null, null, "';'", "'+'", "'-'", "'*'", 
			"'/'", "'('", "')'", "'>'", "'<'", "'=='", "'!='", "'{'", "'}'", null, 
			"'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, "ID", 
			"INT", "DOUBLE", "END_STATE", "ADD", "SUB", "MUL", "DIV", "LPAREN", "RPAREN", 
			"GT", "LT", "EQ_EQ", "NOT_EQ", "RCORNER", "LCORNER", "INCREMENT", "EQ", 
			"WS", "NEWLINE"
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


	public nevermorecompilerLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "nevermorecompiler.g4"; }

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
		"\u0004\u0000\u001e\u00b2\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a"+
		"\u0002\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d"+
		"\u0002\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0005\nt\b\n\n\n\f\nw\t\n\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0004\f|\b\f\u000b\f\f\f}\u0001\r\u0004\r\u0081\b\r\u000b\r\f\r\u0082"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a"+
		"\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001d"+
		"\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001f"+
		"\u0003\u001f\u00af\b\u001f\u0001\u001f\u0001\u001f\u0000\u0000 \u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\u0000\u0019\u0000\u001b\f\u001d"+
		"\r\u001f\u000e!\u000f#\u0010%\u0011\'\u0012)\u0013+\u0014-\u0015/\u0016"+
		"1\u00173\u00185\u00197\u001a9\u001b;\u001c=\u001d?\u001e\u0001\u0000\u0003"+
		"\u0001\u000009\u0003\u0000AZaz\u0410\u044f\u0003\u0000\t\n\r\r  \u00b3"+
		"\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000"+
		"\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000"+
		"\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000"+
		"\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000"+
		"\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/"+
		"\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u00003\u0001\u0000"+
		"\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001\u0000\u0000\u0000"+
		"\u00009\u0001\u0000\u0000\u0000\u0000;\u0001\u0000\u0000\u0000\u0000="+
		"\u0001\u0000\u0000\u0000\u0000?\u0001\u0000\u0000\u0000\u0001A\u0001\u0000"+
		"\u0000\u0000\u0003D\u0001\u0000\u0000\u0000\u0005I\u0001\u0000\u0000\u0000"+
		"\u0007M\u0001\u0000\u0000\u0000\tS\u0001\u0000\u0000\u0000\u000bV\u0001"+
		"\u0000\u0000\u0000\r\\\u0001\u0000\u0000\u0000\u000fd\u0001\u0000\u0000"+
		"\u0000\u0011f\u0001\u0000\u0000\u0000\u0013j\u0001\u0000\u0000\u0000\u0015"+
		"q\u0001\u0000\u0000\u0000\u0017x\u0001\u0000\u0000\u0000\u0019{\u0001"+
		"\u0000\u0000\u0000\u001b\u0080\u0001\u0000\u0000\u0000\u001d\u0084\u0001"+
		"\u0000\u0000\u0000\u001f\u0088\u0001\u0000\u0000\u0000!\u008a\u0001\u0000"+
		"\u0000\u0000#\u008c\u0001\u0000\u0000\u0000%\u008e\u0001\u0000\u0000\u0000"+
		"\'\u0090\u0001\u0000\u0000\u0000)\u0092\u0001\u0000\u0000\u0000+\u0094"+
		"\u0001\u0000\u0000\u0000-\u0096\u0001\u0000\u0000\u0000/\u0098\u0001\u0000"+
		"\u0000\u00001\u009a\u0001\u0000\u0000\u00003\u009d\u0001\u0000\u0000\u0000"+
		"5\u00a0\u0001\u0000\u0000\u00007\u00a2\u0001\u0000\u0000\u00009\u00a4"+
		"\u0001\u0000\u0000\u0000;\u00a7\u0001\u0000\u0000\u0000=\u00a9\u0001\u0000"+
		"\u0000\u0000?\u00ae\u0001\u0000\u0000\u0000AB\u0005i\u0000\u0000BC\u0005"+
		"f\u0000\u0000C\u0002\u0001\u0000\u0000\u0000DE\u0005e\u0000\u0000EF\u0005"+
		"l\u0000\u0000FG\u0005s\u0000\u0000GH\u0005e\u0000\u0000H\u0004\u0001\u0000"+
		"\u0000\u0000IJ\u0005f\u0000\u0000JK\u0005o\u0000\u0000KL\u0005r\u0000"+
		"\u0000L\u0006\u0001\u0000\u0000\u0000MN\u0005w\u0000\u0000NO\u0005h\u0000"+
		"\u0000OP\u0005i\u0000\u0000PQ\u0005l\u0000\u0000QR\u0005e\u0000\u0000"+
		"R\b\u0001\u0000\u0000\u0000ST\u0005d\u0000\u0000TU\u0005o\u0000\u0000"+
		"U\n\u0001\u0000\u0000\u0000VW\u0005p\u0000\u0000WX\u0005r\u0000\u0000"+
		"XY\u0005i\u0000\u0000YZ\u0005n\u0000\u0000Z[\u0005t\u0000\u0000[\f\u0001"+
		"\u0000\u0000\u0000\\]\u0005g\u0000\u0000]^\u0005l\u0000\u0000^_\u0005"+
		"o\u0000\u0000_`\u0005b\u0000\u0000`a\u0005a\u0000\u0000ab\u0005l\u0000"+
		"\u0000bc\u0005:\u0000\u0000c\u000e\u0001\u0000\u0000\u0000de\u0005:\u0000"+
		"\u0000e\u0010\u0001\u0000\u0000\u0000fg\u0005i\u0000\u0000gh\u0005n\u0000"+
		"\u0000hi\u0005t\u0000\u0000i\u0012\u0001\u0000\u0000\u0000jk\u0005d\u0000"+
		"\u0000kl\u0005o\u0000\u0000lm\u0005u\u0000\u0000mn\u0005b\u0000\u0000"+
		"no\u0005l\u0000\u0000op\u0005e\u0000\u0000p\u0014\u0001\u0000\u0000\u0000"+
		"qu\u0003\u0019\f\u0000rt\u0003\u0017\u000b\u0000sr\u0001\u0000\u0000\u0000"+
		"tw\u0001\u0000\u0000\u0000us\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000"+
		"\u0000v\u0016\u0001\u0000\u0000\u0000wu\u0001\u0000\u0000\u0000xy\u0007"+
		"\u0000\u0000\u0000y\u0018\u0001\u0000\u0000\u0000z|\u0007\u0001\u0000"+
		"\u0000{z\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}{\u0001\u0000"+
		"\u0000\u0000}~\u0001\u0000\u0000\u0000~\u001a\u0001\u0000\u0000\u0000"+
		"\u007f\u0081\u0003\u0017\u000b\u0000\u0080\u007f\u0001\u0000\u0000\u0000"+
		"\u0081\u0082\u0001\u0000\u0000\u0000\u0082\u0080\u0001\u0000\u0000\u0000"+
		"\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u001c\u0001\u0000\u0000\u0000"+
		"\u0084\u0085\u0003\u001b\r\u0000\u0085\u0086\u0005.\u0000\u0000\u0086"+
		"\u0087\u0003\u001b\r\u0000\u0087\u001e\u0001\u0000\u0000\u0000\u0088\u0089"+
		"\u0005;\u0000\u0000\u0089 \u0001\u0000\u0000\u0000\u008a\u008b\u0005+"+
		"\u0000\u0000\u008b\"\u0001\u0000\u0000\u0000\u008c\u008d\u0005-\u0000"+
		"\u0000\u008d$\u0001\u0000\u0000\u0000\u008e\u008f\u0005*\u0000\u0000\u008f"+
		"&\u0001\u0000\u0000\u0000\u0090\u0091\u0005/\u0000\u0000\u0091(\u0001"+
		"\u0000\u0000\u0000\u0092\u0093\u0005(\u0000\u0000\u0093*\u0001\u0000\u0000"+
		"\u0000\u0094\u0095\u0005)\u0000\u0000\u0095,\u0001\u0000\u0000\u0000\u0096"+
		"\u0097\u0005>\u0000\u0000\u0097.\u0001\u0000\u0000\u0000\u0098\u0099\u0005"+
		"<\u0000\u0000\u00990\u0001\u0000\u0000\u0000\u009a\u009b\u0005=\u0000"+
		"\u0000\u009b\u009c\u0005=\u0000\u0000\u009c2\u0001\u0000\u0000\u0000\u009d"+
		"\u009e\u0005!\u0000\u0000\u009e\u009f\u0005=\u0000\u0000\u009f4\u0001"+
		"\u0000\u0000\u0000\u00a0\u00a1\u0005{\u0000\u0000\u00a16\u0001\u0000\u0000"+
		"\u0000\u00a2\u00a3\u0005}\u0000\u0000\u00a38\u0001\u0000\u0000\u0000\u00a4"+
		"\u00a5\u0003!\u0010\u0000\u00a5\u00a6\u0003!\u0010\u0000\u00a6:\u0001"+
		"\u0000\u0000\u0000\u00a7\u00a8\u0005=\u0000\u0000\u00a8<\u0001\u0000\u0000"+
		"\u0000\u00a9\u00aa\u0007\u0002\u0000\u0000\u00aa\u00ab\u0001\u0000\u0000"+
		"\u0000\u00ab\u00ac\u0006\u001e\u0000\u0000\u00ac>\u0001\u0000\u0000\u0000"+
		"\u00ad\u00af\u0005\r\u0000\u0000\u00ae\u00ad\u0001\u0000\u0000\u0000\u00ae"+
		"\u00af\u0001\u0000\u0000\u0000\u00af\u00b0\u0001\u0000\u0000\u0000\u00b0"+
		"\u00b1\u0005\n\u0000\u0000\u00b1@\u0001\u0000\u0000\u0000\u0005\u0000"+
		"u}\u0082\u00ae\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}