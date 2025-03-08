// Generated from c:/Users/KlausFolz/Desktop/Repositories/MLexer/src/PyM/PowerQueryParser.g4 by ANTLR 4.13.1
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
		TABLE_EXPAND_TABLE_COLUMN=67, DOT=68, LITERAL=69, TEXT_LITERAL=70, COLUMN_REFERENCE=71, 
		IDENTIFIER=72, REGULAR_IDENTIFIER=73, AVAILABLE_IDENTIFIER=74, KEYWORD_OR_IDENTIFIER=75;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_letExpression = 2, RULE_assignmentList = 3, 
		RULE_assignment = 4, RULE_expression = 5, RULE_literal_expression = 6, 
		RULE_parenthesized_expression = 7, RULE_each_expression = 8, RULE_meta_expression = 9, 
		RULE_type_expression = 10, RULE_type_body = 11, RULE_dottedTypeName = 12, 
		RULE_functionCall = 13, RULE_argumentList = 14, RULE_tableNestedJoinFunction = 15, 
		RULE_tableExpandTableColumnFunction = 16, RULE_dottedIdentifier = 17, 
		RULE_literalList = 18, RULE_list_expression = 19, RULE_record_expression = 20, 
		RULE_record_field = 21;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "letExpression", "assignmentList", "assignment", 
			"expression", "literal_expression", "parenthesized_expression", "each_expression", 
			"meta_expression", "type_expression", "type_body", "dottedTypeName", 
			"functionCall", "argumentList", "tableNestedJoinFunction", "tableExpandTableColumnFunction", 
			"dottedIdentifier", "literalList", "list_expression", "record_expression", 
			"record_field"
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
			"'<='", "'>='", "'Table.NestedJoin'", "'Table.ExpandTableColumn'", "'.'"
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
			"TABLE_EXPAND_TABLE_COLUMN", "DOT", "LITERAL", "TEXT_LITERAL", "COLUMN_REFERENCE", 
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
			setState(45); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(44);
				statement();
				}
				}
				setState(47); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 939526784L) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 75L) != 0) );
			setState(49);
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
			setState(53);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LET:
				enterOuterAlt(_localctx, 1);
				{
				setState(51);
				letExpression();
				}
				break;
			case OPEN_BRACKET:
			case OPEN_BRACE:
			case OPEN_PAREN:
			case TYPE:
			case EACH:
			case TABLE_NESTED_JOIN:
			case TABLE_EXPAND_TABLE_COLUMN:
			case LITERAL:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(52);
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
			setState(55);
			match(LET);
			setState(56);
			assignmentList();
			setState(57);
			match(IN);
			setState(58);
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
			setState(60);
			assignment();
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(61);
				match(COMMA);
				setState(62);
				assignment();
				}
				}
				setState(67);
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
			setState(68);
			match(IDENTIFIER);
			setState(69);
			match(EQUALS);
			setState(70);
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
		public TableExpandTableColumnFunctionContext tableExpandTableColumnFunction() {
			return getRuleContext(TableExpandTableColumnFunctionContext.class,0);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public Literal_expressionContext literal_expression() {
			return getRuleContext(Literal_expressionContext.class,0);
		}
		public Parenthesized_expressionContext parenthesized_expression() {
			return getRuleContext(Parenthesized_expressionContext.class,0);
		}
		public Meta_expressionContext meta_expression() {
			return getRuleContext(Meta_expressionContext.class,0);
		}
		public Type_expressionContext type_expression() {
			return getRuleContext(Type_expressionContext.class,0);
		}
		public Each_expressionContext each_expression() {
			return getRuleContext(Each_expressionContext.class,0);
		}
		public List_expressionContext list_expression() {
			return getRuleContext(List_expressionContext.class,0);
		}
		public Record_expressionContext record_expression() {
			return getRuleContext(Record_expressionContext.class,0);
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
			setState(82);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(72);
				tableNestedJoinFunction();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(73);
				tableExpandTableColumnFunction();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(74);
				functionCall();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(75);
				literal_expression();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(76);
				parenthesized_expression();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(77);
				meta_expression();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(78);
				type_expression();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(79);
				each_expression();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(80);
				list_expression();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(81);
				record_expression();
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
	public static class Literal_expressionContext extends ParserRuleContext {
		public TerminalNode LITERAL() { return getToken(PowerQueryParser.LITERAL, 0); }
		public Literal_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal_expression; }
	}

	public final Literal_expressionContext literal_expression() throws RecognitionException {
		Literal_expressionContext _localctx = new Literal_expressionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_literal_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(LITERAL);
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
	public static class Parenthesized_expressionContext extends ParserRuleContext {
		public TerminalNode OPEN_PAREN() { return getToken(PowerQueryParser.OPEN_PAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(PowerQueryParser.CLOSE_PAREN, 0); }
		public Parenthesized_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parenthesized_expression; }
	}

	public final Parenthesized_expressionContext parenthesized_expression() throws RecognitionException {
		Parenthesized_expressionContext _localctx = new Parenthesized_expressionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_parenthesized_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(OPEN_PAREN);
			setState(87);
			expression();
			setState(88);
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
	public static class Each_expressionContext extends ParserRuleContext {
		public TerminalNode EACH() { return getToken(PowerQueryParser.EACH, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Each_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_each_expression; }
	}

	public final Each_expressionContext each_expression() throws RecognitionException {
		Each_expressionContext _localctx = new Each_expressionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_each_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(EACH);
			setState(91);
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
	public static class Meta_expressionContext extends ParserRuleContext {
		public Parenthesized_expressionContext parenthesized_expression() {
			return getRuleContext(Parenthesized_expressionContext.class,0);
		}
		public TerminalNode META() { return getToken(PowerQueryParser.META, 0); }
		public Record_expressionContext record_expression() {
			return getRuleContext(Record_expressionContext.class,0);
		}
		public Meta_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_meta_expression; }
	}

	public final Meta_expressionContext meta_expression() throws RecognitionException {
		Meta_expressionContext _localctx = new Meta_expressionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_meta_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			parenthesized_expression();
			setState(94);
			match(META);
			setState(95);
			record_expression();
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
	public static class Type_expressionContext extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(PowerQueryParser.TYPE, 0); }
		public Type_bodyContext type_body() {
			return getRuleContext(Type_bodyContext.class,0);
		}
		public TerminalNode NULLABLE() { return getToken(PowerQueryParser.NULLABLE, 0); }
		public Type_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_expression; }
	}

	public final Type_expressionContext type_expression() throws RecognitionException {
		Type_expressionContext _localctx = new Type_expressionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_type_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(TYPE);
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NULLABLE) {
				{
				setState(98);
				match(NULLABLE);
				}
			}

			setState(101);
			type_body();
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
	public static class Type_bodyContext extends ParserRuleContext {
		public TerminalNode TABLE() { return getToken(PowerQueryParser.TABLE, 0); }
		public Record_expressionContext record_expression() {
			return getRuleContext(Record_expressionContext.class,0);
		}
		public DottedTypeNameContext dottedTypeName() {
			return getRuleContext(DottedTypeNameContext.class,0);
		}
		public Type_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_body; }
	}

	public final Type_bodyContext type_body() throws RecognitionException {
		Type_bodyContext _localctx = new Type_bodyContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_type_body);
		try {
			setState(106);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TABLE:
				enterOuterAlt(_localctx, 1);
				{
				setState(103);
				match(TABLE);
				setState(104);
				record_expression();
				}
				break;
			case EOF:
			case EQUALS:
			case COMMA:
			case OPEN_BRACKET:
			case CLOSE_BRACKET:
			case OPEN_BRACE:
			case CLOSE_BRACE:
			case OPEN_PAREN:
			case CLOSE_PAREN:
			case TYPE:
			case EACH:
			case LET:
			case IN:
			case TEXT:
			case NUMBER:
			case LOGICAL:
			case DURATION:
			case DATETIMEZONE:
			case BINARY:
			case DATETIME:
			case TABLE_NESTED_JOIN:
			case TABLE_EXPAND_TABLE_COLUMN:
			case DOT:
			case LITERAL:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(105);
				dottedTypeName();
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
	public static class DottedTypeNameContext extends ParserRuleContext {
		public List<TerminalNode> DOT() { return getTokens(PowerQueryParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(PowerQueryParser.DOT, i);
		}
		public List<TerminalNode> IDENTIFIER() { return getTokens(PowerQueryParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(PowerQueryParser.IDENTIFIER, i);
		}
		public TerminalNode TEXT() { return getToken(PowerQueryParser.TEXT, 0); }
		public TerminalNode NUMBER() { return getToken(PowerQueryParser.NUMBER, 0); }
		public TerminalNode DATETIME() { return getToken(PowerQueryParser.DATETIME, 0); }
		public TerminalNode DATETIMEZONE() { return getToken(PowerQueryParser.DATETIMEZONE, 0); }
		public TerminalNode LOGICAL() { return getToken(PowerQueryParser.LOGICAL, 0); }
		public TerminalNode BINARY() { return getToken(PowerQueryParser.BINARY, 0); }
		public TerminalNode DURATION() { return getToken(PowerQueryParser.DURATION, 0); }
		public DottedTypeNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dottedTypeName; }
	}

	public final DottedTypeNameContext dottedTypeName() throws RecognitionException {
		DottedTypeNameContext _localctx = new DottedTypeNameContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_dottedTypeName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 182879707463680L) != 0)) {
				{
				setState(108);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 182879707463680L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(115);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DOT) {
				{
				{
				setState(111);
				match(DOT);
				setState(112);
				match(IDENTIFIER);
				}
				}
				setState(117);
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
	public static class FunctionCallContext extends ParserRuleContext {
		public DottedIdentifierContext dottedIdentifier() {
			return getRuleContext(DottedIdentifierContext.class,0);
		}
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
		enterRule(_localctx, 26, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			dottedIdentifier();
			setState(119);
			match(OPEN_PAREN);
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 402655872L) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 75L) != 0)) {
				{
				setState(120);
				argumentList();
				}
			}

			setState(123);
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
		enterRule(_localctx, 28, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			expression();
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(126);
				match(COMMA);
				setState(127);
				expression();
				}
				}
				setState(132);
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
		enterRule(_localctx, 30, RULE_tableNestedJoinFunction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			match(TABLE_NESTED_JOIN);
			setState(134);
			match(OPEN_PAREN);
			setState(135);
			((TableNestedJoinFunctionContext)_localctx).firstTable = match(IDENTIFIER);
			setState(136);
			match(COMMA);
			setState(137);
			((TableNestedJoinFunctionContext)_localctx).firstKeyColumns = literalList();
			setState(138);
			match(COMMA);
			setState(139);
			((TableNestedJoinFunctionContext)_localctx).secondTable = match(IDENTIFIER);
			setState(140);
			match(COMMA);
			setState(141);
			((TableNestedJoinFunctionContext)_localctx).secondKeyColumns = literalList();
			setState(142);
			match(COMMA);
			setState(143);
			((TableNestedJoinFunctionContext)_localctx).newColumnName = match(LITERAL);
			setState(146);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(144);
				match(COMMA);
				setState(145);
				((TableNestedJoinFunctionContext)_localctx).joinKind = match(IDENTIFIER);
				}
				break;
			}
			setState(150);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(148);
				match(COMMA);
				setState(149);
				((TableNestedJoinFunctionContext)_localctx).keyEqualityComparer = match(IDENTIFIER);
				}
			}

			setState(152);
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
		public Token column;
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
		public TerminalNode LITERAL() { return getToken(PowerQueryParser.LITERAL, 0); }
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
		enterRule(_localctx, 32, RULE_tableExpandTableColumnFunction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			match(TABLE_EXPAND_TABLE_COLUMN);
			setState(155);
			match(OPEN_PAREN);
			setState(156);
			((TableExpandTableColumnFunctionContext)_localctx).table = match(IDENTIFIER);
			setState(157);
			match(COMMA);
			setState(158);
			((TableExpandTableColumnFunctionContext)_localctx).column = match(LITERAL);
			setState(159);
			match(COMMA);
			setState(160);
			((TableExpandTableColumnFunctionContext)_localctx).columnsList = literalList();
			setState(163);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(161);
				match(COMMA);
				setState(162);
				((TableExpandTableColumnFunctionContext)_localctx).NewColumnNamesList = literalList();
				}
			}

			setState(165);
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
	public static class DottedIdentifierContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(PowerQueryParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(PowerQueryParser.IDENTIFIER, i);
		}
		public List<TerminalNode> DOT() { return getTokens(PowerQueryParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(PowerQueryParser.DOT, i);
		}
		public DottedIdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dottedIdentifier; }
	}

	public final DottedIdentifierContext dottedIdentifier() throws RecognitionException {
		DottedIdentifierContext _localctx = new DottedIdentifierContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_dottedIdentifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(IDENTIFIER);
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DOT) {
				{
				{
				setState(168);
				match(DOT);
				setState(169);
				match(IDENTIFIER);
				}
				}
				setState(174);
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
		enterRule(_localctx, 36, RULE_literalList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(OPEN_BRACE);
			setState(176);
			match(LITERAL);
			setState(181);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(177);
				match(COMMA);
				setState(178);
				match(LITERAL);
				}
				}
				setState(183);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(184);
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
	public static class List_expressionContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACE() { return getToken(PowerQueryParser.OPEN_BRACE, 0); }
		public TerminalNode CLOSE_BRACE() { return getToken(PowerQueryParser.CLOSE_BRACE, 0); }
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
		public List_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_expression; }
	}

	public final List_expressionContext list_expression() throws RecognitionException {
		List_expressionContext _localctx = new List_expressionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_list_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			match(OPEN_BRACE);
			setState(195);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 402655872L) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 75L) != 0)) {
				{
				setState(187);
				expression();
				setState(192);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(188);
					match(COMMA);
					setState(189);
					expression();
					}
					}
					setState(194);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(197);
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
	public static class Record_expressionContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACKET() { return getToken(PowerQueryParser.OPEN_BRACKET, 0); }
		public TerminalNode CLOSE_BRACKET() { return getToken(PowerQueryParser.CLOSE_BRACKET, 0); }
		public List<Record_fieldContext> record_field() {
			return getRuleContexts(Record_fieldContext.class);
		}
		public Record_fieldContext record_field(int i) {
			return getRuleContext(Record_fieldContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PowerQueryParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PowerQueryParser.COMMA, i);
		}
		public Record_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_record_expression; }
	}

	public final Record_expressionContext record_expression() throws RecognitionException {
		Record_expressionContext _localctx = new Record_expressionContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_record_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(199);
			match(OPEN_BRACKET);
			setState(208);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 402655872L) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 75L) != 0)) {
				{
				setState(200);
				record_field();
				setState(205);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(201);
					match(COMMA);
					setState(202);
					record_field();
					}
					}
					setState(207);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(210);
			match(CLOSE_BRACKET);
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
	public static class Record_fieldContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQUALS() { return getToken(PowerQueryParser.EQUALS, 0); }
		public Record_fieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_record_field; }
	}

	public final Record_fieldContext record_field() throws RecognitionException {
		Record_fieldContext _localctx = new Record_fieldContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_record_field);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			expression();
			setState(213);
			match(EQUALS);
			setState(214);
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

	public static final String _serializedATN =
		"\u0004\u0001K\u00d9\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0001\u0000\u0004\u0000.\b\u0000\u000b\u0000\f\u0000/\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0003\u00016\b\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0005\u0003@\b\u0003\n\u0003\f\u0003C\t\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0003\u0005S\b\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0001\n\u0001\n\u0003\nd\b\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0003\u000bk\b\u000b\u0001\f\u0003\fn\b\f\u0001"+
		"\f\u0001\f\u0005\fr\b\f\n\f\f\fu\t\f\u0001\r\u0001\r\u0001\r\u0003\rz"+
		"\b\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u0081"+
		"\b\u000e\n\u000e\f\u000e\u0084\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u0093\b\u000f"+
		"\u0001\u000f\u0001\u000f\u0003\u000f\u0097\b\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u00a4\b\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011\u00ab\b\u0011"+
		"\n\u0011\f\u0011\u00ae\t\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0005\u0012\u00b4\b\u0012\n\u0012\f\u0012\u00b7\t\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0005\u0013"+
		"\u00bf\b\u0013\n\u0013\f\u0013\u00c2\t\u0013\u0003\u0013\u00c4\b\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0005\u0014\u00cc\b\u0014\n\u0014\f\u0014\u00cf\t\u0014\u0003\u0014\u00d1"+
		"\b\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0000\u0000\u0016\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*\u0000\u0001\u0006"+
		"\u0000\"\"$$&&)*--//\u00dd\u0000-\u0001\u0000\u0000\u0000\u00025\u0001"+
		"\u0000\u0000\u0000\u00047\u0001\u0000\u0000\u0000\u0006<\u0001\u0000\u0000"+
		"\u0000\bD\u0001\u0000\u0000\u0000\nR\u0001\u0000\u0000\u0000\fT\u0001"+
		"\u0000\u0000\u0000\u000eV\u0001\u0000\u0000\u0000\u0010Z\u0001\u0000\u0000"+
		"\u0000\u0012]\u0001\u0000\u0000\u0000\u0014a\u0001\u0000\u0000\u0000\u0016"+
		"j\u0001\u0000\u0000\u0000\u0018m\u0001\u0000\u0000\u0000\u001av\u0001"+
		"\u0000\u0000\u0000\u001c}\u0001\u0000\u0000\u0000\u001e\u0085\u0001\u0000"+
		"\u0000\u0000 \u009a\u0001\u0000\u0000\u0000\"\u00a7\u0001\u0000\u0000"+
		"\u0000$\u00af\u0001\u0000\u0000\u0000&\u00ba\u0001\u0000\u0000\u0000("+
		"\u00c7\u0001\u0000\u0000\u0000*\u00d4\u0001\u0000\u0000\u0000,.\u0003"+
		"\u0002\u0001\u0000-,\u0001\u0000\u0000\u0000./\u0001\u0000\u0000\u0000"+
		"/-\u0001\u0000\u0000\u0000/0\u0001\u0000\u0000\u000001\u0001\u0000\u0000"+
		"\u000012\u0005\u0000\u0000\u00012\u0001\u0001\u0000\u0000\u000036\u0003"+
		"\u0004\u0002\u000046\u0003\n\u0005\u000053\u0001\u0000\u0000\u000054\u0001"+
		"\u0000\u0000\u00006\u0003\u0001\u0000\u0000\u000078\u0005\u001d\u0000"+
		"\u000089\u0003\u0006\u0003\u00009:\u0005\u001e\u0000\u0000:;\u0003\n\u0005"+
		"\u0000;\u0005\u0001\u0000\u0000\u0000<A\u0003\b\u0004\u0000=>\u0005\u0006"+
		"\u0000\u0000>@\u0003\b\u0004\u0000?=\u0001\u0000\u0000\u0000@C\u0001\u0000"+
		"\u0000\u0000A?\u0001\u0000\u0000\u0000AB\u0001\u0000\u0000\u0000B\u0007"+
		"\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000DE\u0005H\u0000\u0000"+
		"EF\u0005\u0005\u0000\u0000FG\u0003\n\u0005\u0000G\t\u0001\u0000\u0000"+
		"\u0000HS\u0003\u001e\u000f\u0000IS\u0003 \u0010\u0000JS\u0003\u001a\r"+
		"\u0000KS\u0003\f\u0006\u0000LS\u0003\u000e\u0007\u0000MS\u0003\u0012\t"+
		"\u0000NS\u0003\u0014\n\u0000OS\u0003\u0010\b\u0000PS\u0003&\u0013\u0000"+
		"QS\u0003(\u0014\u0000RH\u0001\u0000\u0000\u0000RI\u0001\u0000\u0000\u0000"+
		"RJ\u0001\u0000\u0000\u0000RK\u0001\u0000\u0000\u0000RL\u0001\u0000\u0000"+
		"\u0000RM\u0001\u0000\u0000\u0000RN\u0001\u0000\u0000\u0000RO\u0001\u0000"+
		"\u0000\u0000RP\u0001\u0000\u0000\u0000RQ\u0001\u0000\u0000\u0000S\u000b"+
		"\u0001\u0000\u0000\u0000TU\u0005E\u0000\u0000U\r\u0001\u0000\u0000\u0000"+
		"VW\u0005\u000b\u0000\u0000WX\u0003\n\u0005\u0000XY\u0005\f\u0000\u0000"+
		"Y\u000f\u0001\u0000\u0000\u0000Z[\u0005\u001c\u0000\u0000[\\\u0003\n\u0005"+
		"\u0000\\\u0011\u0001\u0000\u0000\u0000]^\u0003\u000e\u0007\u0000^_\u0005"+
		"8\u0000\u0000_`\u0003(\u0014\u0000`\u0013\u0001\u0000\u0000\u0000ac\u0005"+
		"\u001b\u0000\u0000bd\u0005\u0010\u0000\u0000cb\u0001\u0000\u0000\u0000"+
		"cd\u0001\u0000\u0000\u0000de\u0001\u0000\u0000\u0000ef\u0003\u0016\u000b"+
		"\u0000f\u0015\u0001\u0000\u0000\u0000gh\u0005\u000f\u0000\u0000hk\u0003"+
		"(\u0014\u0000ik\u0003\u0018\f\u0000jg\u0001\u0000\u0000\u0000ji\u0001"+
		"\u0000\u0000\u0000k\u0017\u0001\u0000\u0000\u0000ln\u0007\u0000\u0000"+
		"\u0000ml\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000ns\u0001\u0000"+
		"\u0000\u0000op\u0005D\u0000\u0000pr\u0005H\u0000\u0000qo\u0001\u0000\u0000"+
		"\u0000ru\u0001\u0000\u0000\u0000sq\u0001\u0000\u0000\u0000st\u0001\u0000"+
		"\u0000\u0000t\u0019\u0001\u0000\u0000\u0000us\u0001\u0000\u0000\u0000"+
		"vw\u0003\"\u0011\u0000wy\u0005\u000b\u0000\u0000xz\u0003\u001c\u000e\u0000"+
		"yx\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000z{\u0001\u0000\u0000"+
		"\u0000{|\u0005\f\u0000\u0000|\u001b\u0001\u0000\u0000\u0000}\u0082\u0003"+
		"\n\u0005\u0000~\u007f\u0005\u0006\u0000\u0000\u007f\u0081\u0003\n\u0005"+
		"\u0000\u0080~\u0001\u0000\u0000\u0000\u0081\u0084\u0001\u0000\u0000\u0000"+
		"\u0082\u0080\u0001\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000"+
		"\u0083\u001d\u0001\u0000\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000"+
		"\u0085\u0086\u0005B\u0000\u0000\u0086\u0087\u0005\u000b\u0000\u0000\u0087"+
		"\u0088\u0005H\u0000\u0000\u0088\u0089\u0005\u0006\u0000\u0000\u0089\u008a"+
		"\u0003$\u0012\u0000\u008a\u008b\u0005\u0006\u0000\u0000\u008b\u008c\u0005"+
		"H\u0000\u0000\u008c\u008d\u0005\u0006\u0000\u0000\u008d\u008e\u0003$\u0012"+
		"\u0000\u008e\u008f\u0005\u0006\u0000\u0000\u008f\u0092\u0005E\u0000\u0000"+
		"\u0090\u0091\u0005\u0006\u0000\u0000\u0091\u0093\u0005H\u0000\u0000\u0092"+
		"\u0090\u0001\u0000\u0000\u0000\u0092\u0093\u0001\u0000\u0000\u0000\u0093"+
		"\u0096\u0001\u0000\u0000\u0000\u0094\u0095\u0005\u0006\u0000\u0000\u0095"+
		"\u0097\u0005H\u0000\u0000\u0096\u0094\u0001\u0000\u0000\u0000\u0096\u0097"+
		"\u0001\u0000\u0000\u0000\u0097\u0098\u0001\u0000\u0000\u0000\u0098\u0099"+
		"\u0005\f\u0000\u0000\u0099\u001f\u0001\u0000\u0000\u0000\u009a\u009b\u0005"+
		"C\u0000\u0000\u009b\u009c\u0005\u000b\u0000\u0000\u009c\u009d\u0005H\u0000"+
		"\u0000\u009d\u009e\u0005\u0006\u0000\u0000\u009e\u009f\u0005E\u0000\u0000"+
		"\u009f\u00a0\u0005\u0006\u0000\u0000\u00a0\u00a3\u0003$\u0012\u0000\u00a1"+
		"\u00a2\u0005\u0006\u0000\u0000\u00a2\u00a4\u0003$\u0012\u0000\u00a3\u00a1"+
		"\u0001\u0000\u0000\u0000\u00a3\u00a4\u0001\u0000\u0000\u0000\u00a4\u00a5"+
		"\u0001\u0000\u0000\u0000\u00a5\u00a6\u0005\f\u0000\u0000\u00a6!\u0001"+
		"\u0000\u0000\u0000\u00a7\u00ac\u0005H\u0000\u0000\u00a8\u00a9\u0005D\u0000"+
		"\u0000\u00a9\u00ab\u0005H\u0000\u0000\u00aa\u00a8\u0001\u0000\u0000\u0000"+
		"\u00ab\u00ae\u0001\u0000\u0000\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000"+
		"\u00ac\u00ad\u0001\u0000\u0000\u0000\u00ad#\u0001\u0000\u0000\u0000\u00ae"+
		"\u00ac\u0001\u0000\u0000\u0000\u00af\u00b0\u0005\t\u0000\u0000\u00b0\u00b5"+
		"\u0005E\u0000\u0000\u00b1\u00b2\u0005\u0006\u0000\u0000\u00b2\u00b4\u0005"+
		"E\u0000\u0000\u00b3\u00b1\u0001\u0000\u0000\u0000\u00b4\u00b7\u0001\u0000"+
		"\u0000\u0000\u00b5\u00b3\u0001\u0000\u0000\u0000\u00b5\u00b6\u0001\u0000"+
		"\u0000\u0000\u00b6\u00b8\u0001\u0000\u0000\u0000\u00b7\u00b5\u0001\u0000"+
		"\u0000\u0000\u00b8\u00b9\u0005\n\u0000\u0000\u00b9%\u0001\u0000\u0000"+
		"\u0000\u00ba\u00c3\u0005\t\u0000\u0000\u00bb\u00c0\u0003\n\u0005\u0000"+
		"\u00bc\u00bd\u0005\u0006\u0000\u0000\u00bd\u00bf\u0003\n\u0005\u0000\u00be"+
		"\u00bc\u0001\u0000\u0000\u0000\u00bf\u00c2\u0001\u0000\u0000\u0000\u00c0"+
		"\u00be\u0001\u0000\u0000\u0000\u00c0\u00c1\u0001\u0000\u0000\u0000\u00c1"+
		"\u00c4\u0001\u0000\u0000\u0000\u00c2\u00c0\u0001\u0000\u0000\u0000\u00c3"+
		"\u00bb\u0001\u0000\u0000\u0000\u00c3\u00c4\u0001\u0000\u0000\u0000\u00c4"+
		"\u00c5\u0001\u0000\u0000\u0000\u00c5\u00c6\u0005\n\u0000\u0000\u00c6\'"+
		"\u0001\u0000\u0000\u0000\u00c7\u00d0\u0005\u0007\u0000\u0000\u00c8\u00cd"+
		"\u0003*\u0015\u0000\u00c9\u00ca\u0005\u0006\u0000\u0000\u00ca\u00cc\u0003"+
		"*\u0015\u0000\u00cb\u00c9\u0001\u0000\u0000\u0000\u00cc\u00cf\u0001\u0000"+
		"\u0000\u0000\u00cd\u00cb\u0001\u0000\u0000\u0000\u00cd\u00ce\u0001\u0000"+
		"\u0000\u0000\u00ce\u00d1\u0001\u0000\u0000\u0000\u00cf\u00cd\u0001\u0000"+
		"\u0000\u0000\u00d0\u00c8\u0001\u0000\u0000\u0000\u00d0\u00d1\u0001\u0000"+
		"\u0000\u0000\u00d1\u00d2\u0001\u0000\u0000\u0000\u00d2\u00d3\u0005\b\u0000"+
		"\u0000\u00d3)\u0001\u0000\u0000\u0000\u00d4\u00d5\u0003\n\u0005\u0000"+
		"\u00d5\u00d6\u0005\u0005\u0000\u0000\u00d6\u00d7\u0003\n\u0005\u0000\u00d7"+
		"+\u0001\u0000\u0000\u0000\u0013/5ARcjmsy\u0082\u0092\u0096\u00a3\u00ac"+
		"\u00b5\u00c0\u00c3\u00cd\u00d0";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}