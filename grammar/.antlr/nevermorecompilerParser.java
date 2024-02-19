// Generated from /home/katana/NevermoreCompile/grammar/nevermorecompiler.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class nevermorecompilerParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, ID=11, INT=12, DOUBLE=13, END_STATE=14, ADD=15, SUB=16, MUL=17, 
		DIV=18, LPAREN=19, RPAREN=20, GT=21, LT=22, EQ_EQ=23, NOT_EQ=24, RCORNER=25, 
		LCORNER=26, INCREMENT=27, EQ=28, WS=29, NEWLINE=30;
	public static final int
		RULE_prog = 0, RULE_stat = 1, RULE_ifStatement = 2, RULE_ifElseStatement = 3, 
		RULE_ifBody = 4, RULE_elseBody = 5, RULE_forStatement = 6, RULE_forModify = 7, 
		RULE_forInit = 8, RULE_forBody = 9, RULE_whileStatement = 10, RULE_doWhileStatement = 11, 
		RULE_whileBody = 12, RULE_expr = 13, RULE_printState = 14, RULE_printBody = 15, 
		RULE_globalStatement = 16, RULE_globalBody = 17, RULE_equation = 18, RULE_relop = 19, 
		RULE_assignmentStatement = 20, RULE_type = 21;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stat", "ifStatement", "ifElseStatement", "ifBody", "elseBody", 
			"forStatement", "forModify", "forInit", "forBody", "whileStatement", 
			"doWhileStatement", "whileBody", "expr", "printState", "printBody", "globalStatement", 
			"globalBody", "equation", "relop", "assignmentStatement", "type"
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

	@Override
	public String getGrammarFileName() { return "nevermorecompiler.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public nevermorecompilerParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1073743610L) != 0)) {
				{
				{
				setState(44);
				stat();
				}
				}
				setState(49);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	@SuppressWarnings("CheckReturnValue")
	public static class StatContext extends ParserRuleContext {
		public AssignmentStatementContext assignmentStatement() {
			return getRuleContext(AssignmentStatementContext.class,0);
		}
		public PrintStateContext printState() {
			return getRuleContext(PrintStateContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public IfElseStatementContext ifElseStatement() {
			return getRuleContext(IfElseStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public DoWhileStatementContext doWhileStatement() {
			return getRuleContext(DoWhileStatementContext.class,0);
		}
		public GlobalStatementContext globalStatement() {
			return getRuleContext(GlobalStatementContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(nevermorecompilerParser.NEWLINE, 0); }
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		try {
			setState(59);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(50);
				assignmentStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(51);
				printState();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(52);
				ifStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(53);
				ifElseStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(54);
				forStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(55);
				whileStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(56);
				doWhileStatement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(57);
				globalStatement();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(58);
				match(NEWLINE);
				}
				break;
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

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public EquationContext equation() {
			return getRuleContext(EquationContext.class,0);
		}
		public TerminalNode RCORNER() { return getToken(nevermorecompilerParser.RCORNER, 0); }
		public IfBodyContext ifBody() {
			return getRuleContext(IfBodyContext.class,0);
		}
		public TerminalNode LCORNER() { return getToken(nevermorecompilerParser.LCORNER, 0); }
		public TerminalNode END_STATE() { return getToken(nevermorecompilerParser.END_STATE, 0); }
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_ifStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(T__0);
			setState(62);
			equation();
			setState(63);
			match(RCORNER);
			setState(64);
			ifBody();
			setState(65);
			match(LCORNER);
			setState(66);
			match(END_STATE);
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

	@SuppressWarnings("CheckReturnValue")
	public static class IfElseStatementContext extends ParserRuleContext {
		public EquationContext equation() {
			return getRuleContext(EquationContext.class,0);
		}
		public List<TerminalNode> RCORNER() { return getTokens(nevermorecompilerParser.RCORNER); }
		public TerminalNode RCORNER(int i) {
			return getToken(nevermorecompilerParser.RCORNER, i);
		}
		public IfBodyContext ifBody() {
			return getRuleContext(IfBodyContext.class,0);
		}
		public List<TerminalNode> LCORNER() { return getTokens(nevermorecompilerParser.LCORNER); }
		public TerminalNode LCORNER(int i) {
			return getToken(nevermorecompilerParser.LCORNER, i);
		}
		public ElseBodyContext elseBody() {
			return getRuleContext(ElseBodyContext.class,0);
		}
		public TerminalNode END_STATE() { return getToken(nevermorecompilerParser.END_STATE, 0); }
		public IfElseStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifElseStatement; }
	}

	public final IfElseStatementContext ifElseStatement() throws RecognitionException {
		IfElseStatementContext _localctx = new IfElseStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ifElseStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(T__0);
			setState(69);
			equation();
			setState(70);
			match(RCORNER);
			setState(71);
			ifBody();
			setState(72);
			match(LCORNER);
			setState(73);
			match(T__1);
			setState(74);
			match(RCORNER);
			setState(75);
			elseBody();
			setState(76);
			match(LCORNER);
			setState(77);
			match(END_STATE);
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

	@SuppressWarnings("CheckReturnValue")
	public static class IfBodyContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public IfBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifBody; }
	}

	public final IfBodyContext ifBody() throws RecognitionException {
		IfBodyContext _localctx = new IfBodyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_ifBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1073743610L) != 0)) {
				{
				{
				setState(79);
				stat();
				}
				}
				setState(84);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	@SuppressWarnings("CheckReturnValue")
	public static class ElseBodyContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ElseBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseBody; }
	}

	public final ElseBodyContext elseBody() throws RecognitionException {
		ElseBodyContext _localctx = new ElseBodyContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_elseBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1073743610L) != 0)) {
				{
				{
				setState(85);
				stat();
				}
				}
				setState(90);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	@SuppressWarnings("CheckReturnValue")
	public static class ForStatementContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(nevermorecompilerParser.LPAREN, 0); }
		public ForInitContext forInit() {
			return getRuleContext(ForInitContext.class,0);
		}
		public EquationContext equation() {
			return getRuleContext(EquationContext.class,0);
		}
		public TerminalNode END_STATE() { return getToken(nevermorecompilerParser.END_STATE, 0); }
		public ForModifyContext forModify() {
			return getRuleContext(ForModifyContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(nevermorecompilerParser.RPAREN, 0); }
		public TerminalNode RCORNER() { return getToken(nevermorecompilerParser.RCORNER, 0); }
		public ForBodyContext forBody() {
			return getRuleContext(ForBodyContext.class,0);
		}
		public TerminalNode LCORNER() { return getToken(nevermorecompilerParser.LCORNER, 0); }
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_forStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(T__2);
			setState(92);
			match(LPAREN);
			setState(93);
			forInit();
			setState(94);
			equation();
			setState(95);
			match(END_STATE);
			setState(96);
			forModify();
			setState(97);
			match(RPAREN);
			setState(98);
			match(RCORNER);
			setState(99);
			forBody();
			setState(100);
			match(LCORNER);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ForModifyContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(nevermorecompilerParser.ID, 0); }
		public TerminalNode INCREMENT() { return getToken(nevermorecompilerParser.INCREMENT, 0); }
		public ForModifyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forModify; }
	}

	public final ForModifyContext forModify() throws RecognitionException {
		ForModifyContext _localctx = new ForModifyContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_forModify);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(ID);
			setState(103);
			match(INCREMENT);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ForInitContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(nevermorecompilerParser.ID, 0); }
		public TerminalNode EQ() { return getToken(nevermorecompilerParser.EQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode END_STATE() { return getToken(nevermorecompilerParser.END_STATE, 0); }
		public ForInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forInit; }
	}

	public final ForInitContext forInit() throws RecognitionException {
		ForInitContext _localctx = new ForInitContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_forInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			type();
			setState(106);
			match(ID);
			setState(107);
			match(EQ);
			setState(108);
			expr(0);
			setState(109);
			match(END_STATE);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ForBodyContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ForBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forBody; }
	}

	public final ForBodyContext forBody() throws RecognitionException {
		ForBodyContext _localctx = new ForBodyContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_forBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1073743610L) != 0)) {
				{
				{
				setState(111);
				stat();
				}
				}
				setState(116);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatementContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(nevermorecompilerParser.LPAREN, 0); }
		public EquationContext equation() {
			return getRuleContext(EquationContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(nevermorecompilerParser.RPAREN, 0); }
		public TerminalNode RCORNER() { return getToken(nevermorecompilerParser.RCORNER, 0); }
		public WhileBodyContext whileBody() {
			return getRuleContext(WhileBodyContext.class,0);
		}
		public TerminalNode LCORNER() { return getToken(nevermorecompilerParser.LCORNER, 0); }
		public TerminalNode END_STATE() { return getToken(nevermorecompilerParser.END_STATE, 0); }
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_whileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(T__3);
			setState(118);
			match(LPAREN);
			setState(119);
			equation();
			setState(120);
			match(RPAREN);
			setState(121);
			match(RCORNER);
			setState(122);
			whileBody();
			setState(123);
			match(LCORNER);
			setState(124);
			match(END_STATE);
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

	@SuppressWarnings("CheckReturnValue")
	public static class DoWhileStatementContext extends ParserRuleContext {
		public TerminalNode RCORNER() { return getToken(nevermorecompilerParser.RCORNER, 0); }
		public WhileBodyContext whileBody() {
			return getRuleContext(WhileBodyContext.class,0);
		}
		public TerminalNode LCORNER() { return getToken(nevermorecompilerParser.LCORNER, 0); }
		public TerminalNode LPAREN() { return getToken(nevermorecompilerParser.LPAREN, 0); }
		public EquationContext equation() {
			return getRuleContext(EquationContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(nevermorecompilerParser.RPAREN, 0); }
		public TerminalNode END_STATE() { return getToken(nevermorecompilerParser.END_STATE, 0); }
		public DoWhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doWhileStatement; }
	}

	public final DoWhileStatementContext doWhileStatement() throws RecognitionException {
		DoWhileStatementContext _localctx = new DoWhileStatementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_doWhileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			match(T__4);
			setState(127);
			match(RCORNER);
			setState(128);
			whileBody();
			setState(129);
			match(LCORNER);
			setState(130);
			match(T__3);
			setState(131);
			match(LPAREN);
			setState(132);
			equation();
			setState(133);
			match(RPAREN);
			setState(134);
			match(END_STATE);
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

	@SuppressWarnings("CheckReturnValue")
	public static class WhileBodyContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public WhileBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileBody; }
	}

	public final WhileBodyContext whileBody() throws RecognitionException {
		WhileBodyContext _localctx = new WhileBodyContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_whileBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1073743610L) != 0)) {
				{
				{
				setState(136);
				stat();
				}
				}
				setState(141);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(nevermorecompilerParser.INT, 0); }
		public TerminalNode ID() { return getToken(nevermorecompilerParser.ID, 0); }
		public TerminalNode DOUBLE() { return getToken(nevermorecompilerParser.DOUBLE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MUL() { return getToken(nevermorecompilerParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(nevermorecompilerParser.DIV, 0); }
		public TerminalNode ADD() { return getToken(nevermorecompilerParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(nevermorecompilerParser.SUB, 0); }
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
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				setState(143);
				match(INT);
				}
				break;
			case ID:
				{
				setState(144);
				match(ID);
				}
				break;
			case DOUBLE:
				{
				setState(145);
				match(DOUBLE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(156);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(154);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(148);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(149);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(150);
						expr(6);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(151);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(152);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(153);
						expr(5);
						}
						break;
					}
					} 
				}
				setState(158);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
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
	public static class PrintStateContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(nevermorecompilerParser.LPAREN, 0); }
		public PrintBodyContext printBody() {
			return getRuleContext(PrintBodyContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(nevermorecompilerParser.RPAREN, 0); }
		public TerminalNode END_STATE() { return getToken(nevermorecompilerParser.END_STATE, 0); }
		public PrintStateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printState; }
	}

	public final PrintStateContext printState() throws RecognitionException {
		PrintStateContext _localctx = new PrintStateContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_printState);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			match(T__5);
			setState(160);
			match(LPAREN);
			setState(161);
			printBody();
			setState(162);
			match(RPAREN);
			setState(163);
			match(END_STATE);
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

	@SuppressWarnings("CheckReturnValue")
	public static class PrintBodyContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(nevermorecompilerParser.ID, 0); }
		public TerminalNode INT() { return getToken(nevermorecompilerParser.INT, 0); }
		public TerminalNode DOUBLE() { return getToken(nevermorecompilerParser.DOUBLE, 0); }
		public PrintBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printBody; }
	}

	public final PrintBodyContext printBody() throws RecognitionException {
		PrintBodyContext _localctx = new PrintBodyContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_printBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 14336L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	@SuppressWarnings("CheckReturnValue")
	public static class GlobalStatementContext extends ParserRuleContext {
		public TerminalNode END_STATE() { return getToken(nevermorecompilerParser.END_STATE, 0); }
		public List<GlobalBodyContext> globalBody() {
			return getRuleContexts(GlobalBodyContext.class);
		}
		public GlobalBodyContext globalBody(int i) {
			return getRuleContext(GlobalBodyContext.class,i);
		}
		public GlobalStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_globalStatement; }
	}

	public final GlobalStatementContext globalStatement() throws RecognitionException {
		GlobalStatementContext _localctx = new GlobalStatementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_globalStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(T__6);
			setState(171);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__8 || _la==T__9) {
				{
				{
				setState(168);
				globalBody();
				}
				}
				setState(173);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(174);
			match(END_STATE);
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

	@SuppressWarnings("CheckReturnValue")
	public static class GlobalBodyContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(nevermorecompilerParser.ID, 0); }
		public GlobalBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_globalBody; }
	}

	public final GlobalBodyContext globalBody() throws RecognitionException {
		GlobalBodyContext _localctx = new GlobalBodyContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_globalBody);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			type();
			setState(177);
			match(T__7);
			setState(178);
			match(ID);
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

	@SuppressWarnings("CheckReturnValue")
	public static class EquationContext extends ParserRuleContext {
		public RelopContext op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public RelopContext relop() {
			return getRuleContext(RelopContext.class,0);
		}
		public EquationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equation; }
	}

	public final EquationContext equation() throws RecognitionException {
		EquationContext _localctx = new EquationContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_equation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			expr(0);
			setState(181);
			((EquationContext)_localctx).op = relop();
			setState(182);
			expr(0);
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

	@SuppressWarnings("CheckReturnValue")
	public static class RelopContext extends ParserRuleContext {
		public TerminalNode EQ_EQ() { return getToken(nevermorecompilerParser.EQ_EQ, 0); }
		public TerminalNode GT() { return getToken(nevermorecompilerParser.GT, 0); }
		public TerminalNode LT() { return getToken(nevermorecompilerParser.LT, 0); }
		public TerminalNode NOT_EQ() { return getToken(nevermorecompilerParser.NOT_EQ, 0); }
		public RelopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relop; }
	}

	public final RelopContext relop() throws RecognitionException {
		RelopContext _localctx = new RelopContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_relop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 31457280L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentStatementContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(nevermorecompilerParser.ID, 0); }
		public TerminalNode EQ() { return getToken(nevermorecompilerParser.EQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode END_STATE() { return getToken(nevermorecompilerParser.END_STATE, 0); }
		public AssignmentStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentStatement; }
	}

	public final AssignmentStatementContext assignmentStatement() throws RecognitionException {
		AssignmentStatementContext _localctx = new AssignmentStatementContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_assignmentStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			type();
			setState(187);
			match(ID);
			setState(188);
			match(EQ);
			setState(189);
			expr(0);
			setState(190);
			match(END_STATE);
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

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			_la = _input.LA(1);
			if ( !(_la==T__8 || _la==T__9) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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
		case 13:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001e\u00c3\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007"+
		"\u0015\u0001\u0000\u0005\u0000.\b\u0000\n\u0000\f\u00001\t\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0003\u0001<\b\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0005"+
		"\u0004Q\b\u0004\n\u0004\f\u0004T\t\u0004\u0001\u0005\u0005\u0005W\b\u0005"+
		"\n\u0005\f\u0005Z\t\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\t\u0005\tq\b\t\n\t\f\tt\t\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0005\f\u008a\b\f\n\f\f\f"+
		"\u008d\t\f\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u0093\b\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r\u009b\b\r\n\r\f\r\u009e\t\r"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0005\u0010\u00aa\b\u0010"+
		"\n\u0010\f\u0010\u00ad\t\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0000"+
		"\u0001\u001a\u0016\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&(*\u0000\u0005\u0001\u0000\u0011\u0012"+
		"\u0001\u0000\u000f\u0010\u0001\u0000\u000b\r\u0001\u0000\u0015\u0018\u0001"+
		"\u0000\t\n\u00be\u0000/\u0001\u0000\u0000\u0000\u0002;\u0001\u0000\u0000"+
		"\u0000\u0004=\u0001\u0000\u0000\u0000\u0006D\u0001\u0000\u0000\u0000\b"+
		"R\u0001\u0000\u0000\u0000\nX\u0001\u0000\u0000\u0000\f[\u0001\u0000\u0000"+
		"\u0000\u000ef\u0001\u0000\u0000\u0000\u0010i\u0001\u0000\u0000\u0000\u0012"+
		"r\u0001\u0000\u0000\u0000\u0014u\u0001\u0000\u0000\u0000\u0016~\u0001"+
		"\u0000\u0000\u0000\u0018\u008b\u0001\u0000\u0000\u0000\u001a\u0092\u0001"+
		"\u0000\u0000\u0000\u001c\u009f\u0001\u0000\u0000\u0000\u001e\u00a5\u0001"+
		"\u0000\u0000\u0000 \u00a7\u0001\u0000\u0000\u0000\"\u00b0\u0001\u0000"+
		"\u0000\u0000$\u00b4\u0001\u0000\u0000\u0000&\u00b8\u0001\u0000\u0000\u0000"+
		"(\u00ba\u0001\u0000\u0000\u0000*\u00c0\u0001\u0000\u0000\u0000,.\u0003"+
		"\u0002\u0001\u0000-,\u0001\u0000\u0000\u0000.1\u0001\u0000\u0000\u0000"+
		"/-\u0001\u0000\u0000\u0000/0\u0001\u0000\u0000\u00000\u0001\u0001\u0000"+
		"\u0000\u00001/\u0001\u0000\u0000\u00002<\u0003(\u0014\u00003<\u0003\u001c"+
		"\u000e\u00004<\u0003\u0004\u0002\u00005<\u0003\u0006\u0003\u00006<\u0003"+
		"\f\u0006\u00007<\u0003\u0014\n\u00008<\u0003\u0016\u000b\u00009<\u0003"+
		" \u0010\u0000:<\u0005\u001e\u0000\u0000;2\u0001\u0000\u0000\u0000;3\u0001"+
		"\u0000\u0000\u0000;4\u0001\u0000\u0000\u0000;5\u0001\u0000\u0000\u0000"+
		";6\u0001\u0000\u0000\u0000;7\u0001\u0000\u0000\u0000;8\u0001\u0000\u0000"+
		"\u0000;9\u0001\u0000\u0000\u0000;:\u0001\u0000\u0000\u0000<\u0003\u0001"+
		"\u0000\u0000\u0000=>\u0005\u0001\u0000\u0000>?\u0003$\u0012\u0000?@\u0005"+
		"\u0019\u0000\u0000@A\u0003\b\u0004\u0000AB\u0005\u001a\u0000\u0000BC\u0005"+
		"\u000e\u0000\u0000C\u0005\u0001\u0000\u0000\u0000DE\u0005\u0001\u0000"+
		"\u0000EF\u0003$\u0012\u0000FG\u0005\u0019\u0000\u0000GH\u0003\b\u0004"+
		"\u0000HI\u0005\u001a\u0000\u0000IJ\u0005\u0002\u0000\u0000JK\u0005\u0019"+
		"\u0000\u0000KL\u0003\n\u0005\u0000LM\u0005\u001a\u0000\u0000MN\u0005\u000e"+
		"\u0000\u0000N\u0007\u0001\u0000\u0000\u0000OQ\u0003\u0002\u0001\u0000"+
		"PO\u0001\u0000\u0000\u0000QT\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000"+
		"\u0000RS\u0001\u0000\u0000\u0000S\t\u0001\u0000\u0000\u0000TR\u0001\u0000"+
		"\u0000\u0000UW\u0003\u0002\u0001\u0000VU\u0001\u0000\u0000\u0000WZ\u0001"+
		"\u0000\u0000\u0000XV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000"+
		"Y\u000b\u0001\u0000\u0000\u0000ZX\u0001\u0000\u0000\u0000[\\\u0005\u0003"+
		"\u0000\u0000\\]\u0005\u0013\u0000\u0000]^\u0003\u0010\b\u0000^_\u0003"+
		"$\u0012\u0000_`\u0005\u000e\u0000\u0000`a\u0003\u000e\u0007\u0000ab\u0005"+
		"\u0014\u0000\u0000bc\u0005\u0019\u0000\u0000cd\u0003\u0012\t\u0000de\u0005"+
		"\u001a\u0000\u0000e\r\u0001\u0000\u0000\u0000fg\u0005\u000b\u0000\u0000"+
		"gh\u0005\u001b\u0000\u0000h\u000f\u0001\u0000\u0000\u0000ij\u0003*\u0015"+
		"\u0000jk\u0005\u000b\u0000\u0000kl\u0005\u001c\u0000\u0000lm\u0003\u001a"+
		"\r\u0000mn\u0005\u000e\u0000\u0000n\u0011\u0001\u0000\u0000\u0000oq\u0003"+
		"\u0002\u0001\u0000po\u0001\u0000\u0000\u0000qt\u0001\u0000\u0000\u0000"+
		"rp\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000s\u0013\u0001\u0000"+
		"\u0000\u0000tr\u0001\u0000\u0000\u0000uv\u0005\u0004\u0000\u0000vw\u0005"+
		"\u0013\u0000\u0000wx\u0003$\u0012\u0000xy\u0005\u0014\u0000\u0000yz\u0005"+
		"\u0019\u0000\u0000z{\u0003\u0018\f\u0000{|\u0005\u001a\u0000\u0000|}\u0005"+
		"\u000e\u0000\u0000}\u0015\u0001\u0000\u0000\u0000~\u007f\u0005\u0005\u0000"+
		"\u0000\u007f\u0080\u0005\u0019\u0000\u0000\u0080\u0081\u0003\u0018\f\u0000"+
		"\u0081\u0082\u0005\u001a\u0000\u0000\u0082\u0083\u0005\u0004\u0000\u0000"+
		"\u0083\u0084\u0005\u0013\u0000\u0000\u0084\u0085\u0003$\u0012\u0000\u0085"+
		"\u0086\u0005\u0014\u0000\u0000\u0086\u0087\u0005\u000e\u0000\u0000\u0087"+
		"\u0017\u0001\u0000\u0000\u0000\u0088\u008a\u0003\u0002\u0001\u0000\u0089"+
		"\u0088\u0001\u0000\u0000\u0000\u008a\u008d\u0001\u0000\u0000\u0000\u008b"+
		"\u0089\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c"+
		"\u0019\u0001\u0000\u0000\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008e"+
		"\u008f\u0006\r\uffff\uffff\u0000\u008f\u0093\u0005\f\u0000\u0000\u0090"+
		"\u0093\u0005\u000b\u0000\u0000\u0091\u0093\u0005\r\u0000\u0000\u0092\u008e"+
		"\u0001\u0000\u0000\u0000\u0092\u0090\u0001\u0000\u0000\u0000\u0092\u0091"+
		"\u0001\u0000\u0000\u0000\u0093\u009c\u0001\u0000\u0000\u0000\u0094\u0095"+
		"\n\u0005\u0000\u0000\u0095\u0096\u0007\u0000\u0000\u0000\u0096\u009b\u0003"+
		"\u001a\r\u0006\u0097\u0098\n\u0004\u0000\u0000\u0098\u0099\u0007\u0001"+
		"\u0000\u0000\u0099\u009b\u0003\u001a\r\u0005\u009a\u0094\u0001\u0000\u0000"+
		"\u0000\u009a\u0097\u0001\u0000\u0000\u0000\u009b\u009e\u0001\u0000\u0000"+
		"\u0000\u009c\u009a\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000"+
		"\u0000\u009d\u001b\u0001\u0000\u0000\u0000\u009e\u009c\u0001\u0000\u0000"+
		"\u0000\u009f\u00a0\u0005\u0006\u0000\u0000\u00a0\u00a1\u0005\u0013\u0000"+
		"\u0000\u00a1\u00a2\u0003\u001e\u000f\u0000\u00a2\u00a3\u0005\u0014\u0000"+
		"\u0000\u00a3\u00a4\u0005\u000e\u0000\u0000\u00a4\u001d\u0001\u0000\u0000"+
		"\u0000\u00a5\u00a6\u0007\u0002\u0000\u0000\u00a6\u001f\u0001\u0000\u0000"+
		"\u0000\u00a7\u00ab\u0005\u0007\u0000\u0000\u00a8\u00aa\u0003\"\u0011\u0000"+
		"\u00a9\u00a8\u0001\u0000\u0000\u0000\u00aa\u00ad\u0001\u0000\u0000\u0000"+
		"\u00ab\u00a9\u0001\u0000\u0000\u0000\u00ab\u00ac\u0001\u0000\u0000\u0000"+
		"\u00ac\u00ae\u0001\u0000\u0000\u0000\u00ad\u00ab\u0001\u0000\u0000\u0000"+
		"\u00ae\u00af\u0005\u000e\u0000\u0000\u00af!\u0001\u0000\u0000\u0000\u00b0"+
		"\u00b1\u0003*\u0015\u0000\u00b1\u00b2\u0005\b\u0000\u0000\u00b2\u00b3"+
		"\u0005\u000b\u0000\u0000\u00b3#\u0001\u0000\u0000\u0000\u00b4\u00b5\u0003"+
		"\u001a\r\u0000\u00b5\u00b6\u0003&\u0013\u0000\u00b6\u00b7\u0003\u001a"+
		"\r\u0000\u00b7%\u0001\u0000\u0000\u0000\u00b8\u00b9\u0007\u0003\u0000"+
		"\u0000\u00b9\'\u0001\u0000\u0000\u0000\u00ba\u00bb\u0003*\u0015\u0000"+
		"\u00bb\u00bc\u0005\u000b\u0000\u0000\u00bc\u00bd\u0005\u001c\u0000\u0000"+
		"\u00bd\u00be\u0003\u001a\r\u0000\u00be\u00bf\u0005\u000e\u0000\u0000\u00bf"+
		")\u0001\u0000\u0000\u0000\u00c0\u00c1\u0007\u0004\u0000\u0000\u00c1+\u0001"+
		"\u0000\u0000\u0000\n/;RXr\u008b\u0092\u009a\u009c\u00ab";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}