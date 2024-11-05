// Generated from /home/klaus/Repositories/MLexer/src/PyM/PowerQueryParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PowerQueryParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		WHITESPACE=1, NEW_LINE_CHAR=2, COMMENT=3, CHARACHTER_ESCAPE_SEQUENCE=4, 
		EQUALS=5, COMMA=6, OPEN_BRACKET=7, CLOSE_BRACKET=8, OPEN_BRACE=9, CLOSE_BRACE=10, 
		OPEN_PAREN=11, CLOSE_PAREN=12, OPTIONAL=13, OPTIONAL_TEXT=14, TABLE=15, 
		NULLABLE=16, SEMICOLON=17, SECTION=18, SHARED=19, AND=20, OR=21, OTHERWISE=22, 
		TRY=23, ERROR=24, FUNCTION_START=25, ELLIPSES=26, TYPE=27, EACH=28, LET=29, 
		IN=30, IF=31, THEN=32, ELSE=33, TEXT=34, RECORD=35, NUMBER=36, NONE=37, 
		LOGICAL=38, LIST=39, FUNCTION=40, DURATION=41, DATETIMEZONE=42, ANY=43, 
		ANYNONNULL=44, BINARY=45, DATE=46, DATETIME=47, AT=48, AS=49, ARROW=50, 
		DOTDOT=51, BANG=52, NOT=53, PLUS=54, MINUS=55, META=56, IS=57, NEQ=58, 
		GE=59, LE=60, SLASH=61, STAR=62, AMP=63, LEQ=64, GEQ=65, TABLE_NESTED_JOIN=66, 
		TABLE_EXPAND_TABLE_COLUMN=67, LITERAL=68, TEXT_LITERAL=69, COLUMN_REFERENCE=70, 
		IDENTIFIER=71, REGULAR_IDENTIFIER=72, AVAILABLE_IDENTIFIER=73, KEYWORD_OR_IDENTIFIER=74;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_letExpression = 2, RULE_assignmentList = 3, 
		RULE_assignment = 4, RULE_expression = 5, RULE_tableNestedJoinFunction = 6, 
		RULE_tableExpandTableColumnFunction = 7, RULE_literalList = 8, RULE_functionCall = 9, 
		RULE_argumentList = 10, RULE_otherExpression = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "letExpression", "assignmentList", "assignment", 
			"expression", "tableNestedJoinFunction", "tableExpandTableColumnFunction", 
			"literalList", "functionCall", "argumentList", "otherExpression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, "'='", "','", "'['", "']'", "'{'", "'}'", 
			"'('", "')'", "'?'", "'optional'", "'table'", "'nullable'", "';'", "'section'", 
			"'shared'", "'and'", "'or'", "'otherwise'", "'try'", "'error'", "'function ('", 
			"'...'", "'type'", "'each'", "'let'", "'in'", "'if'", "'then'", "'else'", 
			"'text'", "'record'", "'number'", "'none'", "'logical'", "'list'", "'fuction'", 
			"'duration'", "'datetimezone'", "'any'", "'anynonnull'", "'binary'", 
			"'date'", "'datetime'", "'@'", "'as'", "'=>'", "'..'", "'!'", "'not'", 
			"'+'", "'-'", "'meta'", "'is'", "'<>'", "'>'", "'<'", "'/'", "'*'", "'&'", 
			"'<='", "'>='", "'Table.NestedJoin'", "'Table.ExpandTableColumn'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WHITESPACE", "NEW_LINE_CHAR", "COMMENT", "CHARACHTER_ESCAPE_SEQUENCE", 
			"EQUALS", "COMMA", "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", 
			"OPEN_PAREN", "CLOSE_PAREN", "OPTIONAL", "OPTIONAL_TEXT", "TABLE", "NULLABLE", 
			"SEMICOLON", "SECTION", "SHARED", "AND", "OR", "OTHERWISE", "TRY", "ERROR", 
			"FUNCTION_START", "ELLIPSES", "TYPE", "EACH", "LET", "IN", "IF", "THEN", 
			"ELSE", "TEXT", "RECORD", "NUMBER", "NONE", "LOGICAL", "LIST", "FUNCTION", 
			"DURATION", "DATETIMEZONE", "ANY", "ANYNONNULL", "BINARY", "DATE", "DATETIME", 
			"AT", "AS", "ARROW", "DOTDOT", "BANG", "NOT", "PLUS", "MINUS", "META", 
			"IS", "NEQ", "GE", "LE", "SLASH", "STAR", "AMP", "LEQ", "GEQ", "TABLE_NESTED_JOIN", 
			"TABLE_EXPAND_TABLE_COLUMN", "LITERAL", "TEXT_LITERAL", "COLUMN_REFERENCE", 
			"IDENTIFIER", "REGULAR_IDENTIFIER", "AVAILABLE_IDENTIFIER", "KEYWORD_OR_IDENTIFIER"
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
	public String getGrammarFileName() { return "PowerQueryParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PowerQueryParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(PowerQueryParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(24);
				statement();
				}
				}
				setState(27); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( ((((_la - 29)) & ~0x3f) == 0 && ((1L << (_la - 29)) & 4535485464577L) != 0) );
			setState(29);
			match(EOF);
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
	public static class StatementContext extends ParserRuleContext {
		public LetExpressionContext letExpression() {
			return getRuleContext(LetExpressionContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(33);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LET:
				enterOuterAlt(_localctx, 1);
				{
				setState(31);
				letExpression();
				}
				break;
			case TABLE_NESTED_JOIN:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(32);
				expression();
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

	@SuppressWarnings("CheckReturnValue")
	public static class LetExpressionContext extends ParserRuleContext {
		public TerminalNode LET() { return getToken(PowerQueryParser.LET, 0); }
		public AssignmentListContext assignmentList() {
			return getRuleContext(AssignmentListContext.class,0);
		}
		public TerminalNode IN() { return getToken(PowerQueryParser.IN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LetExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letExpression; }
	}

	public final LetExpressionContext letExpression() throws RecognitionException {
		LetExpressionContext _localctx = new LetExpressionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_letExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			match(LET);
			setState(36);
			assignmentList();
			setState(37);
			match(IN);
			setState(38);
			expression();
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
	public static class AssignmentListContext extends ParserRuleContext {
		public List<AssignmentContext> assignment() {
			return getRuleContexts(AssignmentContext.class);
		}
		public AssignmentContext assignment(int i) {
			return getRuleContext(AssignmentContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PowerQueryParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PowerQueryParser.COMMA, i);
		}
		public AssignmentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentList; }
	}

	public final AssignmentListContext assignmentList() throws RecognitionException {
		AssignmentListContext _localctx = new AssignmentListContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_assignmentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			assignment();
			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(41);
				match(COMMA);
				setState(42);
				assignment();
				}
				}
				setState(47);
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
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(PowerQueryParser.IDENTIFIER, 0); }
		public TerminalNode EQUALS() { return getToken(PowerQueryParser.EQUALS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			match(IDENTIFIER);
			setState(49);
			match(EQUALS);
			setState(50);
			expression();
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
	public static class ExpressionContext extends ParserRuleContext {
		public TableNestedJoinFunctionContext tableNestedJoinFunction() {
			return getRuleContext(TableNestedJoinFunctionContext.class,0);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_expression);
		try {
			setState(54);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TABLE_NESTED_JOIN:
				enterOuterAlt(_localctx, 1);
				{
				setState(52);
				tableNestedJoinFunction();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(53);
				functionCall();
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

	@SuppressWarnings("CheckReturnValue")
	public static class TableNestedJoinFunctionContext extends ParserRuleContext {
		public Token firstTable;
		public LiteralListContext firstKeyColumns;
		public Token secondTable;
		public LiteralListContext secondKeyColumns;
		public Token newColumnName;
		public Token joinKind;
		public Token keyEqualityComparer;
		public TerminalNode TABLE_NESTED_JOIN() { return getToken(PowerQueryParser.TABLE_NESTED_JOIN, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(PowerQueryParser.OPEN_PAREN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(PowerQueryParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PowerQueryParser.COMMA, i);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(PowerQueryParser.CLOSE_PAREN, 0); }
		public List<TerminalNode> IDENTIFIER() { return getTokens(PowerQueryParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(PowerQueryParser.IDENTIFIER, i);
		}
		public List<LiteralListContext> literalList() {
			return getRuleContexts(LiteralListContext.class);
		}
		public LiteralListContext literalList(int i) {
			return getRuleContext(LiteralListContext.class,i);
		}
		public TerminalNode LITERAL() { return getToken(PowerQueryParser.LITERAL, 0); }
		public TableNestedJoinFunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tableNestedJoinFunction; }
	}

	public final TableNestedJoinFunctionContext tableNestedJoinFunction() throws RecognitionException {
		TableNestedJoinFunctionContext _localctx = new TableNestedJoinFunctionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_tableNestedJoinFunction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			match(TABLE_NESTED_JOIN);
			setState(57);
			match(OPEN_PAREN);
			setState(58);
			((TableNestedJoinFunctionContext)_localctx).firstTable = match(IDENTIFIER);
			setState(59);
			match(COMMA);
			setState(60);
			((TableNestedJoinFunctionContext)_localctx).firstKeyColumns = literalList();
			setState(61);
			match(COMMA);
			setState(62);
			((TableNestedJoinFunctionContext)_localctx).secondTable = match(IDENTIFIER);
			setState(63);
			match(COMMA);
			setState(64);
			((TableNestedJoinFunctionContext)_localctx).secondKeyColumns = literalList();
			setState(65);
			match(COMMA);
			setState(66);
			((TableNestedJoinFunctionContext)_localctx).newColumnName = match(LITERAL);
			setState(69);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(67);
				match(COMMA);
				setState(68);
				((TableNestedJoinFunctionContext)_localctx).joinKind = match(IDENTIFIER);
				}
				break;
			}
			setState(73);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(71);
				match(COMMA);
				setState(72);
				((TableNestedJoinFunctionContext)_localctx).keyEqualityComparer = match(IDENTIFIER);
				}
			}

			setState(75);
			match(CLOSE_PAREN);
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
	public static class TableExpandTableColumnFunctionContext extends ParserRuleContext {
		public Token table;
		public LiteralListContext columnsList;
		public LiteralListContext NewColumnNamesList;
		public TerminalNode TABLE_EXPAND_TABLE_COLUMN() { return getToken(PowerQueryParser.TABLE_EXPAND_TABLE_COLUMN, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(PowerQueryParser.OPEN_PAREN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(PowerQueryParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PowerQueryParser.COMMA, i);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(PowerQueryParser.CLOSE_PAREN, 0); }
		public TerminalNode IDENTIFIER() { return getToken(PowerQueryParser.IDENTIFIER, 0); }
		public List<LiteralListContext> literalList() {
			return getRuleContexts(LiteralListContext.class);
		}
		public LiteralListContext literalList(int i) {
			return getRuleContext(LiteralListContext.class,i);
		}
		public TableExpandTableColumnFunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tableExpandTableColumnFunction; }
	}

	public final TableExpandTableColumnFunctionContext tableExpandTableColumnFunction() throws RecognitionException {
		TableExpandTableColumnFunctionContext _localctx = new TableExpandTableColumnFunctionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_tableExpandTableColumnFunction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(TABLE_EXPAND_TABLE_COLUMN);
			setState(78);
			match(OPEN_PAREN);
			setState(79);
			((TableExpandTableColumnFunctionContext)_localctx).table = match(IDENTIFIER);
			setState(80);
			match(COMMA);
			setState(81);
			((TableExpandTableColumnFunctionContext)_localctx).columnsList = literalList();
			setState(84);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(82);
				match(COMMA);
				setState(83);
				((TableExpandTableColumnFunctionContext)_localctx).NewColumnNamesList = literalList();
				}
			}

			setState(86);
			match(CLOSE_PAREN);
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
	public static class LiteralListContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACE() { return getToken(PowerQueryParser.OPEN_BRACE, 0); }
		public List<TerminalNode> LITERAL() { return getTokens(PowerQueryParser.LITERAL); }
		public TerminalNode LITERAL(int i) {
			return getToken(PowerQueryParser.LITERAL, i);
		}
		public TerminalNode CLOSE_BRACE() { return getToken(PowerQueryParser.CLOSE_BRACE, 0); }
		public List<TerminalNode> COMMA() { return getTokens(PowerQueryParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PowerQueryParser.COMMA, i);
		}
		public LiteralListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literalList; }
	}

	public final LiteralListContext literalList() throws RecognitionException {
		LiteralListContext _localctx = new LiteralListContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_literalList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(OPEN_BRACE);
			setState(89);
			match(LITERAL);
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(90);
				match(COMMA);
				setState(91);
				match(LITERAL);
				}
				}
				setState(96);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(97);
			match(CLOSE_BRACE);
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
	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(PowerQueryParser.IDENTIFIER, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(PowerQueryParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(PowerQueryParser.CLOSE_PAREN, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(IDENTIFIER);
			setState(100);
			match(OPEN_PAREN);
			setState(102);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TABLE_NESTED_JOIN || _la==IDENTIFIER) {
				{
				setState(101);
				argumentList();
				}
			}

			setState(104);
			match(CLOSE_PAREN);
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
	public static class ArgumentListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PowerQueryParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PowerQueryParser.COMMA, i);
		}
		public ArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentList; }
	}

	public final ArgumentListContext argumentList() throws RecognitionException {
		ArgumentListContext _localctx = new ArgumentListContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			expression();
			setState(111);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(107);
				match(COMMA);
				setState(108);
				expression();
				}
				}
				setState(113);
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
	public static class OtherExpressionContext extends ParserRuleContext {
		public OtherExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_otherExpression; }
	}

	public final OtherExpressionContext otherExpression() throws RecognitionException {
		OtherExpressionContext _localctx = new OtherExpressionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_otherExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
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

	public static final String _serializedATN =
		"\u0004\u0001Ju\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002\u0002"+
		"\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002\u0005"+
		"\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002\b\u0007"+
		"\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0001\u0000"+
		"\u0004\u0000\u001a\b\u0000\u000b\u0000\f\u0000\u001b\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0003\u0001\"\b\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0005\u0003,\b\u0003\n\u0003\f\u0003/\t\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0003\u00057\b"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0003\u0006F\b\u0006\u0001\u0006\u0001\u0006\u0003"+
		"\u0006J\b\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007U\b"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0005\b"+
		"]\b\b\n\b\f\b`\t\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0003\tg\b"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0005\nn\b\n\n\n\f\nq\t\n\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0000\u0000\f\u0000\u0002\u0004\u0006\b"+
		"\n\f\u000e\u0010\u0012\u0014\u0016\u0000\u0000r\u0000\u0019\u0001\u0000"+
		"\u0000\u0000\u0002!\u0001\u0000\u0000\u0000\u0004#\u0001\u0000\u0000\u0000"+
		"\u0006(\u0001\u0000\u0000\u0000\b0\u0001\u0000\u0000\u0000\n6\u0001\u0000"+
		"\u0000\u0000\f8\u0001\u0000\u0000\u0000\u000eM\u0001\u0000\u0000\u0000"+
		"\u0010X\u0001\u0000\u0000\u0000\u0012c\u0001\u0000\u0000\u0000\u0014j"+
		"\u0001\u0000\u0000\u0000\u0016r\u0001\u0000\u0000\u0000\u0018\u001a\u0003"+
		"\u0002\u0001\u0000\u0019\u0018\u0001\u0000\u0000\u0000\u001a\u001b\u0001"+
		"\u0000\u0000\u0000\u001b\u0019\u0001\u0000\u0000\u0000\u001b\u001c\u0001"+
		"\u0000\u0000\u0000\u001c\u001d\u0001\u0000\u0000\u0000\u001d\u001e\u0005"+
		"\u0000\u0000\u0001\u001e\u0001\u0001\u0000\u0000\u0000\u001f\"\u0003\u0004"+
		"\u0002\u0000 \"\u0003\n\u0005\u0000!\u001f\u0001\u0000\u0000\u0000! \u0001"+
		"\u0000\u0000\u0000\"\u0003\u0001\u0000\u0000\u0000#$\u0005\u001d\u0000"+
		"\u0000$%\u0003\u0006\u0003\u0000%&\u0005\u001e\u0000\u0000&\'\u0003\n"+
		"\u0005\u0000\'\u0005\u0001\u0000\u0000\u0000(-\u0003\b\u0004\u0000)*\u0005"+
		"\u0006\u0000\u0000*,\u0003\b\u0004\u0000+)\u0001\u0000\u0000\u0000,/\u0001"+
		"\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000\u0000"+
		".\u0007\u0001\u0000\u0000\u0000/-\u0001\u0000\u0000\u000001\u0005G\u0000"+
		"\u000012\u0005\u0005\u0000\u000023\u0003\n\u0005\u00003\t\u0001\u0000"+
		"\u0000\u000047\u0003\f\u0006\u000057\u0003\u0012\t\u000064\u0001\u0000"+
		"\u0000\u000065\u0001\u0000\u0000\u00007\u000b\u0001\u0000\u0000\u0000"+
		"89\u0005B\u0000\u00009:\u0005\u000b\u0000\u0000:;\u0005G\u0000\u0000;"+
		"<\u0005\u0006\u0000\u0000<=\u0003\u0010\b\u0000=>\u0005\u0006\u0000\u0000"+
		">?\u0005G\u0000\u0000?@\u0005\u0006\u0000\u0000@A\u0003\u0010\b\u0000"+
		"AB\u0005\u0006\u0000\u0000BE\u0005D\u0000\u0000CD\u0005\u0006\u0000\u0000"+
		"DF\u0005G\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000"+
		"FI\u0001\u0000\u0000\u0000GH\u0005\u0006\u0000\u0000HJ\u0005G\u0000\u0000"+
		"IG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000"+
		"\u0000KL\u0005\f\u0000\u0000L\r\u0001\u0000\u0000\u0000MN\u0005C\u0000"+
		"\u0000NO\u0005\u000b\u0000\u0000OP\u0005G\u0000\u0000PQ\u0005\u0006\u0000"+
		"\u0000QT\u0003\u0010\b\u0000RS\u0005\u0006\u0000\u0000SU\u0003\u0010\b"+
		"\u0000TR\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000UV\u0001\u0000"+
		"\u0000\u0000VW\u0005\f\u0000\u0000W\u000f\u0001\u0000\u0000\u0000XY\u0005"+
		"\t\u0000\u0000Y^\u0005D\u0000\u0000Z[\u0005\u0006\u0000\u0000[]\u0005"+
		"D\u0000\u0000\\Z\u0001\u0000\u0000\u0000]`\u0001\u0000\u0000\u0000^\\"+
		"\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_a\u0001\u0000\u0000"+
		"\u0000`^\u0001\u0000\u0000\u0000ab\u0005\n\u0000\u0000b\u0011\u0001\u0000"+
		"\u0000\u0000cd\u0005G\u0000\u0000df\u0005\u000b\u0000\u0000eg\u0003\u0014"+
		"\n\u0000fe\u0001\u0000\u0000\u0000fg\u0001\u0000\u0000\u0000gh\u0001\u0000"+
		"\u0000\u0000hi\u0005\f\u0000\u0000i\u0013\u0001\u0000\u0000\u0000jo\u0003"+
		"\n\u0005\u0000kl\u0005\u0006\u0000\u0000ln\u0003\n\u0005\u0000mk\u0001"+
		"\u0000\u0000\u0000nq\u0001\u0000\u0000\u0000om\u0001\u0000\u0000\u0000"+
		"op\u0001\u0000\u0000\u0000p\u0015\u0001\u0000\u0000\u0000qo\u0001\u0000"+
		"\u0000\u0000rs\u0001\u0000\u0000\u0000s\u0017\u0001\u0000\u0000\u0000"+
		"\n\u001b!-6EIT^fo";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}