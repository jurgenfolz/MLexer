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
		WHITESPACE=1, NEW_LINE_CHAR=2, LINE_COMMENT=3, BLOCK_COMMENT=4, CHARACHTER_ESCAPE_SEQUENCE=5, 
		EQUALS=6, COMMA=7, OPEN_BRACKET=8, CLOSE_BRACKET=9, OPEN_BRACE=10, CLOSE_BRACE=11, 
		OPEN_PAREN=12, CLOSE_PAREN=13, OPTIONAL=14, OPTIONAL_TEXT=15, TABLE=16, 
		NULLABLE=17, SEMICOLON=18, SECTION=19, SHARED=20, AND=21, OR=22, OTHERWISE=23, 
		TRY=24, ERROR=25, FUNCTION_START=26, ELLIPSES=27, TYPE=28, EACH=29, LET=30, 
		IN=31, IF=32, THEN=33, ELSE=34, TEXT=35, RECORD=36, NUMBER=37, NONE=38, 
		LOGICAL=39, LIST=40, FUNCTION=41, DURATION=42, DATETIMEZONE=43, ANY=44, 
		ANYNONNULL=45, BINARY=46, DATE=47, DATETIME=48, AT=49, AS=50, ARROW=51, 
		DOTDOT=52, BANG=53, NOT=54, PLUS=55, MINUS=56, META=57, IS=58, NEQ=59, 
		GE=60, LE=61, SLASH=62, STAR=63, AMP=64, LEQ=65, GEQ=66, LITERAL=67, TEXT_LITERAL=68, 
		IDENTIFIER=69, REGULAR_IDENTIFIER=70, AVAILABLE_IDENTIFIER=71, KEYWORD_OR_IDENTIFIER=72;
	public static final int
		RULE_document = 0, RULE_section_document = 1, RULE_section = 2, RULE_section_name = 3, 
		RULE_section_members = 4, RULE_section_member = 5, RULE_section_member_name = 6, 
		RULE_expression_document = 7, RULE_expression = 8, RULE_logical_or_expression = 9, 
		RULE_logical_and_expression = 10, RULE_is_expression = 11, RULE_nullable_primitive_type = 12, 
		RULE_as_expression = 13, RULE_equality_expression = 14, RULE_relational_expression = 15, 
		RULE_additive_expression = 16, RULE_multiplicative_expression = 17, RULE_metadata_expression = 18, 
		RULE_unary_expression = 19, RULE_primary_expression = 20, RULE_atom = 21, 
		RULE_literal_expression = 22, RULE_identifier_expression = 23, RULE_identifier_reference = 24, 
		RULE_exclusive_identifier_reference = 25, RULE_inclusive_identifier_reference = 26, 
		RULE_section_access_expression = 27, RULE_parenthesized_expression = 28, 
		RULE_not_implemented_expression = 29, RULE_argument_list = 30, RULE_list_expression = 31, 
		RULE_item_list = 32, RULE_item = 33, RULE_record_expression = 34, RULE_field_list = 35, 
		RULE_field = 36, RULE_field_name = 37, RULE_item_selector = 38, RULE_field_selector = 39, 
		RULE_required_field_selector = 40, RULE_optional_field_selector = 41, 
		RULE_implicit_target_field_selection = 42, RULE_required_projection = 43, 
		RULE_optional_projection = 44, RULE_required_selector_list = 45, RULE_implicit_target_projection = 46, 
		RULE_function_expression = 47, RULE_function_body = 48, RULE_parameter_list = 49, 
		RULE_fixed_parameter_list = 50, RULE_parameter = 51, RULE_parameter_name = 52, 
		RULE_parameter_type = 53, RULE_return_type = 54, RULE_assertion = 55, 
		RULE_optional_parameter_list = 56, RULE_optional_parameter = 57, RULE_each_expression = 58, 
		RULE_each_expression_body = 59, RULE_let_expression = 60, RULE_variable_list = 61, 
		RULE_variable = 62, RULE_variable_name = 63, RULE_if_expression = 64, 
		RULE_if_condition = 65, RULE_true_expression = 66, RULE_false_expression = 67, 
		RULE_type_expression = 68, RULE_type_expr = 69, RULE_primary_type = 70, 
		RULE_primitive_type = 71, RULE_record_type = 72, RULE_field_specification_list = 73, 
		RULE_field_specification = 74, RULE_field_type_specification = 75, RULE_field_type = 76, 
		RULE_open_record_marker = 77, RULE_list_type = 78, RULE_item_type = 79, 
		RULE_function_type = 80, RULE_parameter_specification_list = 81, RULE_required_parameter_specification_list = 82, 
		RULE_required_parameter_specification = 83, RULE_optional_parameter_specification_list = 84, 
		RULE_optional_parameter_specification = 85, RULE_parameter_specification = 86, 
		RULE_table_type = 87, RULE_row_type = 88, RULE_nullable_type = 89, RULE_error_raising_expression = 90, 
		RULE_error_handling_expression = 91, RULE_protected_expression = 92, RULE_otherwise_clause = 93, 
		RULE_default_expression = 94, RULE_literal_attribs = 95, RULE_record_literal = 96, 
		RULE_literal_field_list = 97, RULE_literal_field = 98, RULE_list_literal = 99, 
		RULE_literal_item_list = 100, RULE_any_literal = 101;
	private static String[] makeRuleNames() {
		return new String[] {
			"document", "section_document", "section", "section_name", "section_members", 
			"section_member", "section_member_name", "expression_document", "expression", 
			"logical_or_expression", "logical_and_expression", "is_expression", "nullable_primitive_type", 
			"as_expression", "equality_expression", "relational_expression", "additive_expression", 
			"multiplicative_expression", "metadata_expression", "unary_expression", 
			"primary_expression", "atom", "literal_expression", "identifier_expression", 
			"identifier_reference", "exclusive_identifier_reference", "inclusive_identifier_reference", 
			"section_access_expression", "parenthesized_expression", "not_implemented_expression", 
			"argument_list", "list_expression", "item_list", "item", "record_expression", 
			"field_list", "field", "field_name", "item_selector", "field_selector", 
			"required_field_selector", "optional_field_selector", "implicit_target_field_selection", 
			"required_projection", "optional_projection", "required_selector_list", 
			"implicit_target_projection", "function_expression", "function_body", 
			"parameter_list", "fixed_parameter_list", "parameter", "parameter_name", 
			"parameter_type", "return_type", "assertion", "optional_parameter_list", 
			"optional_parameter", "each_expression", "each_expression_body", "let_expression", 
			"variable_list", "variable", "variable_name", "if_expression", "if_condition", 
			"true_expression", "false_expression", "type_expression", "type_expr", 
			"primary_type", "primitive_type", "record_type", "field_specification_list", 
			"field_specification", "field_type_specification", "field_type", "open_record_marker", 
			"list_type", "item_type", "function_type", "parameter_specification_list", 
			"required_parameter_specification_list", "required_parameter_specification", 
			"optional_parameter_specification_list", "optional_parameter_specification", 
			"parameter_specification", "table_type", "row_type", "nullable_type", 
			"error_raising_expression", "error_handling_expression", "protected_expression", 
			"otherwise_clause", "default_expression", "literal_attribs", "record_literal", 
			"literal_field_list", "literal_field", "list_literal", "literal_item_list", 
			"any_literal"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, "'='", "','", "'['", "']'", "'{'", 
			"'}'", "'('", "')'", "'?'", "'optional'", "'table'", "'nullable'", "';'", 
			"'section'", "'shared'", "'and'", "'or'", "'otherwise'", "'try'", "'error'", 
			"'function ('", "'...'", "'type'", "'each'", "'let'", "'in'", "'if'", 
			"'then'", "'else'", "'text'", "'record'", "'number'", "'none'", "'logical'", 
			"'list'", "'fuction'", "'duration'", "'datetimezone'", "'any'", "'anynonnull'", 
			"'binary'", "'date'", "'datetime'", "'@'", "'as'", "'=>'", "'..'", "'!'", 
			"'not'", "'+'", "'-'", "'meta'", "'is'", "'<>'", "'>'", "'<'", "'/'", 
			"'*'", "'&'", "'<='", "'>='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WHITESPACE", "NEW_LINE_CHAR", "LINE_COMMENT", "BLOCK_COMMENT", 
			"CHARACHTER_ESCAPE_SEQUENCE", "EQUALS", "COMMA", "OPEN_BRACKET", "CLOSE_BRACKET", 
			"OPEN_BRACE", "CLOSE_BRACE", "OPEN_PAREN", "CLOSE_PAREN", "OPTIONAL", 
			"OPTIONAL_TEXT", "TABLE", "NULLABLE", "SEMICOLON", "SECTION", "SHARED", 
			"AND", "OR", "OTHERWISE", "TRY", "ERROR", "FUNCTION_START", "ELLIPSES", 
			"TYPE", "EACH", "LET", "IN", "IF", "THEN", "ELSE", "TEXT", "RECORD", 
			"NUMBER", "NONE", "LOGICAL", "LIST", "FUNCTION", "DURATION", "DATETIMEZONE", 
			"ANY", "ANYNONNULL", "BINARY", "DATE", "DATETIME", "AT", "AS", "ARROW", 
			"DOTDOT", "BANG", "NOT", "PLUS", "MINUS", "META", "IS", "NEQ", "GE", 
			"LE", "SLASH", "STAR", "AMP", "LEQ", "GEQ", "LITERAL", "TEXT_LITERAL", 
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
	public static class DocumentContext extends ParserRuleContext {
		public Section_documentContext section_document() {
			return getRuleContext(Section_documentContext.class,0);
		}
		public Expression_documentContext expression_document() {
			return getRuleContext(Expression_documentContext.class,0);
		}
		public DocumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_document; }
	}

	public final DocumentContext document() throws RecognitionException {
		DocumentContext _localctx = new DocumentContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_document);
		try {
			setState(206);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(204);
				section_document();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(205);
				expression_document();
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
	public static class Section_documentContext extends ParserRuleContext {
		public SectionContext section() {
			return getRuleContext(SectionContext.class,0);
		}
		public Section_documentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_section_document; }
	}

	public final Section_documentContext section_document() throws RecognitionException {
		Section_documentContext _localctx = new Section_documentContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_section_document);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			section();
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
	public static class SectionContext extends ParserRuleContext {
		public TerminalNode SECTION() { return getToken(PowerQueryParser.SECTION, 0); }
		public Section_nameContext section_name() {
			return getRuleContext(Section_nameContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(PowerQueryParser.SEMICOLON, 0); }
		public Literal_attribsContext literal_attribs() {
			return getRuleContext(Literal_attribsContext.class,0);
		}
		public Section_membersContext section_members() {
			return getRuleContext(Section_membersContext.class,0);
		}
		public SectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_section; }
	}

	public final SectionContext section() throws RecognitionException {
		SectionContext _localctx = new SectionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_section);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPEN_BRACKET) {
				{
				setState(210);
				literal_attribs();
				}
			}

			setState(213);
			match(SECTION);
			setState(214);
			section_name();
			setState(215);
			match(SEMICOLON);
			setState(217);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & 2305843009213698049L) != 0)) {
				{
				setState(216);
				section_members();
				}
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
	public static class Section_nameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(PowerQueryParser.IDENTIFIER, 0); }
		public Section_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_section_name; }
	}

	public final Section_nameContext section_name() throws RecognitionException {
		Section_nameContext _localctx = new Section_nameContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_section_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			match(IDENTIFIER);
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
	public static class Section_membersContext extends ParserRuleContext {
		public Section_memberContext section_member() {
			return getRuleContext(Section_memberContext.class,0);
		}
		public Section_membersContext section_members() {
			return getRuleContext(Section_membersContext.class,0);
		}
		public Section_membersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_section_members; }
	}

	public final Section_membersContext section_members() throws RecognitionException {
		Section_membersContext _localctx = new Section_membersContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_section_members);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			section_member();
			setState(223);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & 2305843009213698049L) != 0)) {
				{
				setState(222);
				section_members();
				}
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
	public static class Section_memberContext extends ParserRuleContext {
		public Section_member_nameContext section_member_name() {
			return getRuleContext(Section_member_nameContext.class,0);
		}
		public TerminalNode EQUALS() { return getToken(PowerQueryParser.EQUALS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(PowerQueryParser.SEMICOLON, 0); }
		public Literal_attribsContext literal_attribs() {
			return getRuleContext(Literal_attribsContext.class,0);
		}
		public TerminalNode SHARED() { return getToken(PowerQueryParser.SHARED, 0); }
		public Section_memberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_section_member; }
	}

	public final Section_memberContext section_member() throws RecognitionException {
		Section_memberContext _localctx = new Section_memberContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_section_member);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPEN_BRACKET) {
				{
				setState(225);
				literal_attribs();
				}
			}

			setState(229);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SHARED) {
				{
				setState(228);
				match(SHARED);
				}
			}

			setState(231);
			section_member_name();
			setState(232);
			match(EQUALS);
			setState(233);
			expression();
			setState(234);
			match(SEMICOLON);
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
	public static class Section_member_nameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(PowerQueryParser.IDENTIFIER, 0); }
		public Section_member_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_section_member_name; }
	}

	public final Section_member_nameContext section_member_name() throws RecognitionException {
		Section_member_nameContext _localctx = new Section_member_nameContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_section_member_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			match(IDENTIFIER);
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
	public static class Expression_documentContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Expression_documentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_document; }
	}

	public final Expression_documentContext expression_document() throws RecognitionException {
		Expression_documentContext _localctx = new Expression_documentContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_expression_document);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
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
		public Each_expressionContext each_expression() {
			return getRuleContext(Each_expressionContext.class,0);
		}
		public Function_expressionContext function_expression() {
			return getRuleContext(Function_expressionContext.class,0);
		}
		public Let_expressionContext let_expression() {
			return getRuleContext(Let_expressionContext.class,0);
		}
		public If_expressionContext if_expression() {
			return getRuleContext(If_expressionContext.class,0);
		}
		public Error_raising_expressionContext error_raising_expression() {
			return getRuleContext(Error_raising_expressionContext.class,0);
		}
		public Error_handling_expressionContext error_handling_expression() {
			return getRuleContext(Error_handling_expressionContext.class,0);
		}
		public Logical_or_expressionContext logical_or_expression() {
			return getRuleContext(Logical_or_expressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expression);
		try {
			setState(247);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(240);
				each_expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(241);
				function_expression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(242);
				let_expression();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(243);
				if_expression();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(244);
				error_raising_expression();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(245);
				error_handling_expression();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(246);
				logical_or_expression();
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
	public static class Logical_or_expressionContext extends ParserRuleContext {
		public List<Logical_and_expressionContext> logical_and_expression() {
			return getRuleContexts(Logical_and_expressionContext.class);
		}
		public Logical_and_expressionContext logical_and_expression(int i) {
			return getRuleContext(Logical_and_expressionContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(PowerQueryParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(PowerQueryParser.OR, i);
		}
		public Logical_or_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_or_expression; }
	}

	public final Logical_or_expressionContext logical_or_expression() throws RecognitionException {
		Logical_or_expressionContext _localctx = new Logical_or_expressionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_logical_or_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(249);
			logical_and_expression();
			setState(254);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(250);
				match(OR);
				setState(251);
				logical_and_expression();
				}
				}
				setState(256);
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
	public static class Logical_and_expressionContext extends ParserRuleContext {
		public List<Is_expressionContext> is_expression() {
			return getRuleContexts(Is_expressionContext.class);
		}
		public Is_expressionContext is_expression(int i) {
			return getRuleContext(Is_expressionContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(PowerQueryParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(PowerQueryParser.AND, i);
		}
		public Logical_and_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_and_expression; }
	}

	public final Logical_and_expressionContext logical_and_expression() throws RecognitionException {
		Logical_and_expressionContext _localctx = new Logical_and_expressionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_logical_and_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			is_expression();
			setState(262);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(258);
				match(AND);
				setState(259);
				is_expression();
				}
				}
				setState(264);
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
	public static class Is_expressionContext extends ParserRuleContext {
		public As_expressionContext as_expression() {
			return getRuleContext(As_expressionContext.class,0);
		}
		public TerminalNode IS() { return getToken(PowerQueryParser.IS, 0); }
		public Nullable_primitive_typeContext nullable_primitive_type() {
			return getRuleContext(Nullable_primitive_typeContext.class,0);
		}
		public Is_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_is_expression; }
	}

	public final Is_expressionContext is_expression() throws RecognitionException {
		Is_expressionContext _localctx = new Is_expressionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_is_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(265);
			as_expression();
			setState(268);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IS) {
				{
				setState(266);
				match(IS);
				setState(267);
				nullable_primitive_type();
				}
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
	public static class Nullable_primitive_typeContext extends ParserRuleContext {
		public Primitive_typeContext primitive_type() {
			return getRuleContext(Primitive_typeContext.class,0);
		}
		public TerminalNode NULLABLE() { return getToken(PowerQueryParser.NULLABLE, 0); }
		public Nullable_primitive_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nullable_primitive_type; }
	}

	public final Nullable_primitive_typeContext nullable_primitive_type() throws RecognitionException {
		Nullable_primitive_typeContext _localctx = new Nullable_primitive_typeContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_nullable_primitive_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NULLABLE) {
				{
				setState(270);
				match(NULLABLE);
				}
			}

			setState(273);
			primitive_type();
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
	public static class As_expressionContext extends ParserRuleContext {
		public Equality_expressionContext equality_expression() {
			return getRuleContext(Equality_expressionContext.class,0);
		}
		public List<TerminalNode> AS() { return getTokens(PowerQueryParser.AS); }
		public TerminalNode AS(int i) {
			return getToken(PowerQueryParser.AS, i);
		}
		public List<Nullable_primitive_typeContext> nullable_primitive_type() {
			return getRuleContexts(Nullable_primitive_typeContext.class);
		}
		public Nullable_primitive_typeContext nullable_primitive_type(int i) {
			return getRuleContext(Nullable_primitive_typeContext.class,i);
		}
		public As_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_as_expression; }
	}

	public final As_expressionContext as_expression() throws RecognitionException {
		As_expressionContext _localctx = new As_expressionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_as_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(275);
			equality_expression();
			setState(280);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AS) {
				{
				{
				setState(276);
				match(AS);
				setState(277);
				nullable_primitive_type();
				}
				}
				setState(282);
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
	public static class Equality_expressionContext extends ParserRuleContext {
		public List<Relational_expressionContext> relational_expression() {
			return getRuleContexts(Relational_expressionContext.class);
		}
		public Relational_expressionContext relational_expression(int i) {
			return getRuleContext(Relational_expressionContext.class,i);
		}
		public List<TerminalNode> EQUALS() { return getTokens(PowerQueryParser.EQUALS); }
		public TerminalNode EQUALS(int i) {
			return getToken(PowerQueryParser.EQUALS, i);
		}
		public List<TerminalNode> NEQ() { return getTokens(PowerQueryParser.NEQ); }
		public TerminalNode NEQ(int i) {
			return getToken(PowerQueryParser.NEQ, i);
		}
		public Equality_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equality_expression; }
	}

	public final Equality_expressionContext equality_expression() throws RecognitionException {
		Equality_expressionContext _localctx = new Equality_expressionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_equality_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			relational_expression();
			setState(288);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==EQUALS || _la==NEQ) {
				{
				{
				setState(284);
				_la = _input.LA(1);
				if ( !(_la==EQUALS || _la==NEQ) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(285);
				relational_expression();
				}
				}
				setState(290);
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
	public static class Relational_expressionContext extends ParserRuleContext {
		public List<Additive_expressionContext> additive_expression() {
			return getRuleContexts(Additive_expressionContext.class);
		}
		public Additive_expressionContext additive_expression(int i) {
			return getRuleContext(Additive_expressionContext.class,i);
		}
		public List<TerminalNode> LE() { return getTokens(PowerQueryParser.LE); }
		public TerminalNode LE(int i) {
			return getToken(PowerQueryParser.LE, i);
		}
		public List<TerminalNode> GE() { return getTokens(PowerQueryParser.GE); }
		public TerminalNode GE(int i) {
			return getToken(PowerQueryParser.GE, i);
		}
		public List<TerminalNode> LEQ() { return getTokens(PowerQueryParser.LEQ); }
		public TerminalNode LEQ(int i) {
			return getToken(PowerQueryParser.LEQ, i);
		}
		public List<TerminalNode> GEQ() { return getTokens(PowerQueryParser.GEQ); }
		public TerminalNode GEQ(int i) {
			return getToken(PowerQueryParser.GEQ, i);
		}
		public Relational_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relational_expression; }
	}

	public final Relational_expressionContext relational_expression() throws RecognitionException {
		Relational_expressionContext _localctx = new Relational_expressionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_relational_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(291);
			additive_expression();
			setState(296);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 60)) & ~0x3f) == 0 && ((1L << (_la - 60)) & 99L) != 0)) {
				{
				{
				setState(292);
				_la = _input.LA(1);
				if ( !(((((_la - 60)) & ~0x3f) == 0 && ((1L << (_la - 60)) & 99L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(293);
				additive_expression();
				}
				}
				setState(298);
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
	public static class Additive_expressionContext extends ParserRuleContext {
		public List<Multiplicative_expressionContext> multiplicative_expression() {
			return getRuleContexts(Multiplicative_expressionContext.class);
		}
		public Multiplicative_expressionContext multiplicative_expression(int i) {
			return getRuleContext(Multiplicative_expressionContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(PowerQueryParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(PowerQueryParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(PowerQueryParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(PowerQueryParser.MINUS, i);
		}
		public List<TerminalNode> AMP() { return getTokens(PowerQueryParser.AMP); }
		public TerminalNode AMP(int i) {
			return getToken(PowerQueryParser.AMP, i);
		}
		public Additive_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additive_expression; }
	}

	public final Additive_expressionContext additive_expression() throws RecognitionException {
		Additive_expressionContext _localctx = new Additive_expressionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_additive_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(299);
			multiplicative_expression();
			setState(304);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 55)) & ~0x3f) == 0 && ((1L << (_la - 55)) & 515L) != 0)) {
				{
				{
				setState(300);
				_la = _input.LA(1);
				if ( !(((((_la - 55)) & ~0x3f) == 0 && ((1L << (_la - 55)) & 515L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(301);
				multiplicative_expression();
				}
				}
				setState(306);
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
	public static class Multiplicative_expressionContext extends ParserRuleContext {
		public List<Metadata_expressionContext> metadata_expression() {
			return getRuleContexts(Metadata_expressionContext.class);
		}
		public Metadata_expressionContext metadata_expression(int i) {
			return getRuleContext(Metadata_expressionContext.class,i);
		}
		public List<TerminalNode> STAR() { return getTokens(PowerQueryParser.STAR); }
		public TerminalNode STAR(int i) {
			return getToken(PowerQueryParser.STAR, i);
		}
		public List<TerminalNode> SLASH() { return getTokens(PowerQueryParser.SLASH); }
		public TerminalNode SLASH(int i) {
			return getToken(PowerQueryParser.SLASH, i);
		}
		public Multiplicative_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicative_expression; }
	}

	public final Multiplicative_expressionContext multiplicative_expression() throws RecognitionException {
		Multiplicative_expressionContext _localctx = new Multiplicative_expressionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_multiplicative_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(307);
			metadata_expression();
			setState(312);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SLASH || _la==STAR) {
				{
				{
				setState(308);
				_la = _input.LA(1);
				if ( !(_la==SLASH || _la==STAR) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(309);
				metadata_expression();
				}
				}
				setState(314);
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
	public static class Metadata_expressionContext extends ParserRuleContext {
		public List<Unary_expressionContext> unary_expression() {
			return getRuleContexts(Unary_expressionContext.class);
		}
		public Unary_expressionContext unary_expression(int i) {
			return getRuleContext(Unary_expressionContext.class,i);
		}
		public List<TerminalNode> META() { return getTokens(PowerQueryParser.META); }
		public TerminalNode META(int i) {
			return getToken(PowerQueryParser.META, i);
		}
		public Metadata_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_metadata_expression; }
	}

	public final Metadata_expressionContext metadata_expression() throws RecognitionException {
		Metadata_expressionContext _localctx = new Metadata_expressionContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_metadata_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(315);
			unary_expression();
			setState(320);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==META) {
				{
				{
				setState(316);
				match(META);
				setState(317);
				unary_expression();
				}
				}
				setState(322);
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
	public static class Unary_expressionContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(PowerQueryParser.PLUS, 0); }
		public Unary_expressionContext unary_expression() {
			return getRuleContext(Unary_expressionContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(PowerQueryParser.MINUS, 0); }
		public TerminalNode NOT() { return getToken(PowerQueryParser.NOT, 0); }
		public Type_expressionContext type_expression() {
			return getRuleContext(Type_expressionContext.class,0);
		}
		public Unary_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unary_expression; }
	}

	public final Unary_expressionContext unary_expression() throws RecognitionException {
		Unary_expressionContext _localctx = new Unary_expressionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_unary_expression);
		try {
			setState(330);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(323);
				match(PLUS);
				setState(324);
				unary_expression();
				}
				break;
			case MINUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(325);
				match(MINUS);
				setState(326);
				unary_expression();
				}
				break;
			case NOT:
				enterOuterAlt(_localctx, 3);
				{
				setState(327);
				match(NOT);
				setState(328);
				unary_expression();
				}
				break;
			case OPEN_BRACKET:
			case OPEN_BRACE:
			case OPEN_PAREN:
			case ELLIPSES:
			case TYPE:
			case AT:
			case LITERAL:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 4);
				{
				setState(329);
				type_expression();
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
	public static class Primary_expressionContext extends ParserRuleContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public List<Field_selectorContext> field_selector() {
			return getRuleContexts(Field_selectorContext.class);
		}
		public Field_selectorContext field_selector(int i) {
			return getRuleContext(Field_selectorContext.class,i);
		}
		public List<Required_projectionContext> required_projection() {
			return getRuleContexts(Required_projectionContext.class);
		}
		public Required_projectionContext required_projection(int i) {
			return getRuleContext(Required_projectionContext.class,i);
		}
		public List<Optional_projectionContext> optional_projection() {
			return getRuleContexts(Optional_projectionContext.class);
		}
		public Optional_projectionContext optional_projection(int i) {
			return getRuleContext(Optional_projectionContext.class,i);
		}
		public List<TerminalNode> OPEN_BRACE() { return getTokens(PowerQueryParser.OPEN_BRACE); }
		public TerminalNode OPEN_BRACE(int i) {
			return getToken(PowerQueryParser.OPEN_BRACE, i);
		}
		public List<Item_selectorContext> item_selector() {
			return getRuleContexts(Item_selectorContext.class);
		}
		public Item_selectorContext item_selector(int i) {
			return getRuleContext(Item_selectorContext.class,i);
		}
		public List<TerminalNode> CLOSE_BRACE() { return getTokens(PowerQueryParser.CLOSE_BRACE); }
		public TerminalNode CLOSE_BRACE(int i) {
			return getToken(PowerQueryParser.CLOSE_BRACE, i);
		}
		public List<TerminalNode> OPEN_PAREN() { return getTokens(PowerQueryParser.OPEN_PAREN); }
		public TerminalNode OPEN_PAREN(int i) {
			return getToken(PowerQueryParser.OPEN_PAREN, i);
		}
		public List<TerminalNode> CLOSE_PAREN() { return getTokens(PowerQueryParser.CLOSE_PAREN); }
		public TerminalNode CLOSE_PAREN(int i) {
			return getToken(PowerQueryParser.CLOSE_PAREN, i);
		}
		public List<TerminalNode> OPTIONAL() { return getTokens(PowerQueryParser.OPTIONAL); }
		public TerminalNode OPTIONAL(int i) {
			return getToken(PowerQueryParser.OPTIONAL, i);
		}
		public List<Argument_listContext> argument_list() {
			return getRuleContexts(Argument_listContext.class);
		}
		public Argument_listContext argument_list(int i) {
			return getRuleContext(Argument_listContext.class,i);
		}
		public Implicit_target_field_selectionContext implicit_target_field_selection() {
			return getRuleContext(Implicit_target_field_selectionContext.class,0);
		}
		public Implicit_target_projectionContext implicit_target_projection() {
			return getRuleContext(Implicit_target_projectionContext.class,0);
		}
		public Not_implemented_expressionContext not_implemented_expression() {
			return getRuleContext(Not_implemented_expressionContext.class,0);
		}
		public Primary_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary_expression; }
	}

	public final Primary_expressionContext primary_expression() throws RecognitionException {
		Primary_expressionContext _localctx = new Primary_expressionContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_primary_expression);
		int _la;
		try {
			setState(355);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(332);
				atom();
				setState(349);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 5376L) != 0)) {
					{
					setState(347);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
					case 1:
						{
						setState(333);
						field_selector();
						}
						break;
					case 2:
						{
						setState(334);
						required_projection();
						}
						break;
					case 3:
						{
						setState(335);
						optional_projection();
						}
						break;
					case 4:
						{
						setState(336);
						match(OPEN_BRACE);
						setState(337);
						item_selector();
						setState(338);
						match(CLOSE_BRACE);
						setState(340);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==OPTIONAL) {
							{
							setState(339);
							match(OPTIONAL);
							}
						}

						}
						break;
					case 5:
						{
						setState(342);
						match(OPEN_PAREN);
						setState(344);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & 2882798541774454805L) != 0)) {
							{
							setState(343);
							argument_list();
							}
						}

						setState(346);
						match(CLOSE_PAREN);
						}
						break;
					}
					}
					setState(351);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(352);
				implicit_target_field_selection();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(353);
				implicit_target_projection();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(354);
				not_implemented_expression();
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
	public static class AtomContext extends ParserRuleContext {
		public Literal_expressionContext literal_expression() {
			return getRuleContext(Literal_expressionContext.class,0);
		}
		public List_expressionContext list_expression() {
			return getRuleContext(List_expressionContext.class,0);
		}
		public Record_expressionContext record_expression() {
			return getRuleContext(Record_expressionContext.class,0);
		}
		public Identifier_expressionContext identifier_expression() {
			return getRuleContext(Identifier_expressionContext.class,0);
		}
		public Section_access_expressionContext section_access_expression() {
			return getRuleContext(Section_access_expressionContext.class,0);
		}
		public Parenthesized_expressionContext parenthesized_expression() {
			return getRuleContext(Parenthesized_expressionContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_atom);
		try {
			setState(363);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(357);
				literal_expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(358);
				list_expression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(359);
				record_expression();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(360);
				identifier_expression();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(361);
				section_access_expression();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(362);
				parenthesized_expression();
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
		enterRule(_localctx, 44, RULE_literal_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(365);
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
	public static class Identifier_expressionContext extends ParserRuleContext {
		public Identifier_referenceContext identifier_reference() {
			return getRuleContext(Identifier_referenceContext.class,0);
		}
		public Identifier_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier_expression; }
	}

	public final Identifier_expressionContext identifier_expression() throws RecognitionException {
		Identifier_expressionContext _localctx = new Identifier_expressionContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_identifier_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(367);
			identifier_reference();
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
	public static class Identifier_referenceContext extends ParserRuleContext {
		public Exclusive_identifier_referenceContext exclusive_identifier_reference() {
			return getRuleContext(Exclusive_identifier_referenceContext.class,0);
		}
		public Inclusive_identifier_referenceContext inclusive_identifier_reference() {
			return getRuleContext(Inclusive_identifier_referenceContext.class,0);
		}
		public Identifier_referenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier_reference; }
	}

	public final Identifier_referenceContext identifier_reference() throws RecognitionException {
		Identifier_referenceContext _localctx = new Identifier_referenceContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_identifier_reference);
		try {
			setState(371);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(369);
				exclusive_identifier_reference();
				}
				break;
			case AT:
				enterOuterAlt(_localctx, 2);
				{
				setState(370);
				inclusive_identifier_reference();
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
	public static class Exclusive_identifier_referenceContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(PowerQueryParser.IDENTIFIER, 0); }
		public Exclusive_identifier_referenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exclusive_identifier_reference; }
	}

	public final Exclusive_identifier_referenceContext exclusive_identifier_reference() throws RecognitionException {
		Exclusive_identifier_referenceContext _localctx = new Exclusive_identifier_referenceContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_exclusive_identifier_reference);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(373);
			match(IDENTIFIER);
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
	public static class Inclusive_identifier_referenceContext extends ParserRuleContext {
		public TerminalNode AT() { return getToken(PowerQueryParser.AT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(PowerQueryParser.IDENTIFIER, 0); }
		public Inclusive_identifier_referenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inclusive_identifier_reference; }
	}

	public final Inclusive_identifier_referenceContext inclusive_identifier_reference() throws RecognitionException {
		Inclusive_identifier_referenceContext _localctx = new Inclusive_identifier_referenceContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_inclusive_identifier_reference);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(375);
			match(AT);
			setState(376);
			match(IDENTIFIER);
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
	public static class Section_access_expressionContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(PowerQueryParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(PowerQueryParser.IDENTIFIER, i);
		}
		public TerminalNode BANG() { return getToken(PowerQueryParser.BANG, 0); }
		public Section_access_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_section_access_expression; }
	}

	public final Section_access_expressionContext section_access_expression() throws RecognitionException {
		Section_access_expressionContext _localctx = new Section_access_expressionContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_section_access_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(378);
			match(IDENTIFIER);
			setState(379);
			match(BANG);
			setState(380);
			match(IDENTIFIER);
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
		enterRule(_localctx, 56, RULE_parenthesized_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(382);
			match(OPEN_PAREN);
			setState(383);
			expression();
			setState(384);
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
	public static class Not_implemented_expressionContext extends ParserRuleContext {
		public TerminalNode ELLIPSES() { return getToken(PowerQueryParser.ELLIPSES, 0); }
		public Not_implemented_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_not_implemented_expression; }
	}

	public final Not_implemented_expressionContext not_implemented_expression() throws RecognitionException {
		Not_implemented_expressionContext _localctx = new Not_implemented_expressionContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_not_implemented_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(386);
			match(ELLIPSES);
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
	public static class Argument_listContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Argument_listContext argument_list() {
			return getRuleContext(Argument_listContext.class,0);
		}
		public Argument_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument_list; }
	}

	public final Argument_listContext argument_list() throws RecognitionException {
		Argument_listContext _localctx = new Argument_listContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_argument_list);
		try {
			setState(393);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(388);
				expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(389);
				expression();
				setState(390);
				match(COMMA);
				setState(391);
				argument_list();
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
	public static class List_expressionContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACE() { return getToken(PowerQueryParser.OPEN_BRACE, 0); }
		public TerminalNode CLOSE_BRACE() { return getToken(PowerQueryParser.CLOSE_BRACE, 0); }
		public Item_listContext item_list() {
			return getRuleContext(Item_listContext.class,0);
		}
		public List_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_expression; }
	}

	public final List_expressionContext list_expression() throws RecognitionException {
		List_expressionContext _localctx = new List_expressionContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_list_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(395);
			match(OPEN_BRACE);
			setState(397);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & 2882798541774454805L) != 0)) {
				{
				setState(396);
				item_list();
				}
			}

			setState(399);
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
	public static class Item_listContext extends ParserRuleContext {
		public ItemContext item() {
			return getRuleContext(ItemContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Item_listContext item_list() {
			return getRuleContext(Item_listContext.class,0);
		}
		public Item_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item_list; }
	}

	public final Item_listContext item_list() throws RecognitionException {
		Item_listContext _localctx = new Item_listContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_item_list);
		try {
			setState(406);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(401);
				item();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(402);
				item();
				setState(403);
				match(COMMA);
				setState(404);
				item_list();
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
	public static class ItemContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode DOTDOT() { return getToken(PowerQueryParser.DOTDOT, 0); }
		public ItemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item; }
	}

	public final ItemContext item() throws RecognitionException {
		ItemContext _localctx = new ItemContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_item);
		try {
			setState(413);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(408);
				expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(409);
				expression();
				setState(410);
				match(DOTDOT);
				setState(411);
				expression();
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
	public static class Record_expressionContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACKET() { return getToken(PowerQueryParser.OPEN_BRACKET, 0); }
		public TerminalNode CLOSE_BRACKET() { return getToken(PowerQueryParser.CLOSE_BRACKET, 0); }
		public Field_listContext field_list() {
			return getRuleContext(Field_listContext.class,0);
		}
		public Record_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_record_expression; }
	}

	public final Record_expressionContext record_expression() throws RecognitionException {
		Record_expressionContext _localctx = new Record_expressionContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_record_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(415);
			match(OPEN_BRACKET);
			setState(417);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(416);
				field_list();
				}
			}

			setState(419);
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
	public static class Field_listContext extends ParserRuleContext {
		public FieldContext field() {
			return getRuleContext(FieldContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Field_listContext field_list() {
			return getRuleContext(Field_listContext.class,0);
		}
		public Field_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_list; }
	}

	public final Field_listContext field_list() throws RecognitionException {
		Field_listContext _localctx = new Field_listContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_field_list);
		try {
			setState(426);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(421);
				field();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(422);
				field();
				setState(423);
				match(COMMA);
				setState(424);
				field_list();
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
	public static class FieldContext extends ParserRuleContext {
		public Field_nameContext field_name() {
			return getRuleContext(Field_nameContext.class,0);
		}
		public TerminalNode EQUALS() { return getToken(PowerQueryParser.EQUALS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public FieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field; }
	}

	public final FieldContext field() throws RecognitionException {
		FieldContext _localctx = new FieldContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_field);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(428);
			field_name();
			setState(429);
			match(EQUALS);
			setState(430);
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
	public static class Field_nameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(PowerQueryParser.IDENTIFIER, 0); }
		public Field_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_name; }
	}

	public final Field_nameContext field_name() throws RecognitionException {
		Field_nameContext _localctx = new Field_nameContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_field_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(432);
			match(IDENTIFIER);
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
	public static class Item_selectorContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Item_selectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item_selector; }
	}

	public final Item_selectorContext item_selector() throws RecognitionException {
		Item_selectorContext _localctx = new Item_selectorContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_item_selector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(434);
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
	public static class Field_selectorContext extends ParserRuleContext {
		public Required_field_selectorContext required_field_selector() {
			return getRuleContext(Required_field_selectorContext.class,0);
		}
		public Optional_field_selectorContext optional_field_selector() {
			return getRuleContext(Optional_field_selectorContext.class,0);
		}
		public Field_selectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_selector; }
	}

	public final Field_selectorContext field_selector() throws RecognitionException {
		Field_selectorContext _localctx = new Field_selectorContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_field_selector);
		try {
			setState(438);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(436);
				required_field_selector();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(437);
				optional_field_selector();
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
	public static class Required_field_selectorContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACKET() { return getToken(PowerQueryParser.OPEN_BRACKET, 0); }
		public Field_nameContext field_name() {
			return getRuleContext(Field_nameContext.class,0);
		}
		public TerminalNode CLOSE_BRACKET() { return getToken(PowerQueryParser.CLOSE_BRACKET, 0); }
		public Required_field_selectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_required_field_selector; }
	}

	public final Required_field_selectorContext required_field_selector() throws RecognitionException {
		Required_field_selectorContext _localctx = new Required_field_selectorContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_required_field_selector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(440);
			match(OPEN_BRACKET);
			setState(441);
			field_name();
			setState(442);
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
	public static class Optional_field_selectorContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACKET() { return getToken(PowerQueryParser.OPEN_BRACKET, 0); }
		public Field_nameContext field_name() {
			return getRuleContext(Field_nameContext.class,0);
		}
		public TerminalNode CLOSE_BRACKET() { return getToken(PowerQueryParser.CLOSE_BRACKET, 0); }
		public TerminalNode OPTIONAL() { return getToken(PowerQueryParser.OPTIONAL, 0); }
		public Optional_field_selectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_optional_field_selector; }
	}

	public final Optional_field_selectorContext optional_field_selector() throws RecognitionException {
		Optional_field_selectorContext _localctx = new Optional_field_selectorContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_optional_field_selector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(444);
			match(OPEN_BRACKET);
			setState(445);
			field_name();
			setState(446);
			match(CLOSE_BRACKET);
			setState(447);
			match(OPTIONAL);
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
	public static class Implicit_target_field_selectionContext extends ParserRuleContext {
		public Field_selectorContext field_selector() {
			return getRuleContext(Field_selectorContext.class,0);
		}
		public Implicit_target_field_selectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_implicit_target_field_selection; }
	}

	public final Implicit_target_field_selectionContext implicit_target_field_selection() throws RecognitionException {
		Implicit_target_field_selectionContext _localctx = new Implicit_target_field_selectionContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_implicit_target_field_selection);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(449);
			field_selector();
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
	public static class Required_projectionContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACKET() { return getToken(PowerQueryParser.OPEN_BRACKET, 0); }
		public Required_selector_listContext required_selector_list() {
			return getRuleContext(Required_selector_listContext.class,0);
		}
		public TerminalNode CLOSE_BRACKET() { return getToken(PowerQueryParser.CLOSE_BRACKET, 0); }
		public Required_projectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_required_projection; }
	}

	public final Required_projectionContext required_projection() throws RecognitionException {
		Required_projectionContext _localctx = new Required_projectionContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_required_projection);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(451);
			match(OPEN_BRACKET);
			setState(452);
			required_selector_list();
			setState(453);
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
	public static class Optional_projectionContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACKET() { return getToken(PowerQueryParser.OPEN_BRACKET, 0); }
		public Required_selector_listContext required_selector_list() {
			return getRuleContext(Required_selector_listContext.class,0);
		}
		public TerminalNode CLOSE_BRACKET() { return getToken(PowerQueryParser.CLOSE_BRACKET, 0); }
		public TerminalNode OPTIONAL() { return getToken(PowerQueryParser.OPTIONAL, 0); }
		public Optional_projectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_optional_projection; }
	}

	public final Optional_projectionContext optional_projection() throws RecognitionException {
		Optional_projectionContext _localctx = new Optional_projectionContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_optional_projection);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(455);
			match(OPEN_BRACKET);
			setState(456);
			required_selector_list();
			setState(457);
			match(CLOSE_BRACKET);
			setState(458);
			match(OPTIONAL);
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
	public static class Required_selector_listContext extends ParserRuleContext {
		public Required_field_selectorContext required_field_selector() {
			return getRuleContext(Required_field_selectorContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Required_selector_listContext required_selector_list() {
			return getRuleContext(Required_selector_listContext.class,0);
		}
		public Required_selector_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_required_selector_list; }
	}

	public final Required_selector_listContext required_selector_list() throws RecognitionException {
		Required_selector_listContext _localctx = new Required_selector_listContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_required_selector_list);
		try {
			setState(465);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(460);
				required_field_selector();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(461);
				required_field_selector();
				setState(462);
				match(COMMA);
				setState(463);
				required_selector_list();
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
	public static class Implicit_target_projectionContext extends ParserRuleContext {
		public Required_projectionContext required_projection() {
			return getRuleContext(Required_projectionContext.class,0);
		}
		public Optional_projectionContext optional_projection() {
			return getRuleContext(Optional_projectionContext.class,0);
		}
		public Implicit_target_projectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_implicit_target_projection; }
	}

	public final Implicit_target_projectionContext implicit_target_projection() throws RecognitionException {
		Implicit_target_projectionContext _localctx = new Implicit_target_projectionContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_implicit_target_projection);
		try {
			setState(469);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(467);
				required_projection();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(468);
				optional_projection();
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
	public static class Function_expressionContext extends ParserRuleContext {
		public TerminalNode OPEN_PAREN() { return getToken(PowerQueryParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(PowerQueryParser.CLOSE_PAREN, 0); }
		public TerminalNode ARROW() { return getToken(PowerQueryParser.ARROW, 0); }
		public Function_bodyContext function_body() {
			return getRuleContext(Function_bodyContext.class,0);
		}
		public Parameter_listContext parameter_list() {
			return getRuleContext(Parameter_listContext.class,0);
		}
		public Return_typeContext return_type() {
			return getRuleContext(Return_typeContext.class,0);
		}
		public Function_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_expression; }
	}

	public final Function_expressionContext function_expression() throws RecognitionException {
		Function_expressionContext _localctx = new Function_expressionContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_function_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(471);
			match(OPEN_PAREN);
			setState(473);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(472);
				parameter_list();
				}
			}

			setState(475);
			match(CLOSE_PAREN);
			setState(477);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(476);
				return_type();
				}
			}

			setState(479);
			match(ARROW);
			setState(480);
			function_body();
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
	public static class Function_bodyContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Function_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_body; }
	}

	public final Function_bodyContext function_body() throws RecognitionException {
		Function_bodyContext _localctx = new Function_bodyContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_function_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(482);
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
	public static class Parameter_listContext extends ParserRuleContext {
		public Fixed_parameter_listContext fixed_parameter_list() {
			return getRuleContext(Fixed_parameter_listContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Optional_parameter_listContext optional_parameter_list() {
			return getRuleContext(Optional_parameter_listContext.class,0);
		}
		public Parameter_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_list; }
	}

	public final Parameter_listContext parameter_list() throws RecognitionException {
		Parameter_listContext _localctx = new Parameter_listContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_parameter_list);
		try {
			setState(489);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(484);
				fixed_parameter_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(485);
				fixed_parameter_list();
				setState(486);
				match(COMMA);
				setState(487);
				optional_parameter_list();
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
	public static class Fixed_parameter_listContext extends ParserRuleContext {
		public ParameterContext parameter() {
			return getRuleContext(ParameterContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Fixed_parameter_listContext fixed_parameter_list() {
			return getRuleContext(Fixed_parameter_listContext.class,0);
		}
		public Fixed_parameter_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fixed_parameter_list; }
	}

	public final Fixed_parameter_listContext fixed_parameter_list() throws RecognitionException {
		Fixed_parameter_listContext _localctx = new Fixed_parameter_listContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_fixed_parameter_list);
		try {
			setState(496);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(491);
				parameter();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(492);
				parameter();
				setState(493);
				match(COMMA);
				setState(494);
				fixed_parameter_list();
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
	public static class ParameterContext extends ParserRuleContext {
		public Parameter_nameContext parameter_name() {
			return getRuleContext(Parameter_nameContext.class,0);
		}
		public Parameter_typeContext parameter_type() {
			return getRuleContext(Parameter_typeContext.class,0);
		}
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_parameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(498);
			parameter_name();
			setState(500);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(499);
				parameter_type();
				}
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
	public static class Parameter_nameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(PowerQueryParser.IDENTIFIER, 0); }
		public Parameter_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_name; }
	}

	public final Parameter_nameContext parameter_name() throws RecognitionException {
		Parameter_nameContext _localctx = new Parameter_nameContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_parameter_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(502);
			match(IDENTIFIER);
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
	public static class Parameter_typeContext extends ParserRuleContext {
		public AssertionContext assertion() {
			return getRuleContext(AssertionContext.class,0);
		}
		public Parameter_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_type; }
	}

	public final Parameter_typeContext parameter_type() throws RecognitionException {
		Parameter_typeContext _localctx = new Parameter_typeContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_parameter_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(504);
			assertion();
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
	public static class Return_typeContext extends ParserRuleContext {
		public AssertionContext assertion() {
			return getRuleContext(AssertionContext.class,0);
		}
		public Return_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_type; }
	}

	public final Return_typeContext return_type() throws RecognitionException {
		Return_typeContext _localctx = new Return_typeContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_return_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(506);
			assertion();
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
	public static class AssertionContext extends ParserRuleContext {
		public TerminalNode AS() { return getToken(PowerQueryParser.AS, 0); }
		public Nullable_primitive_typeContext nullable_primitive_type() {
			return getRuleContext(Nullable_primitive_typeContext.class,0);
		}
		public AssertionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assertion; }
	}

	public final AssertionContext assertion() throws RecognitionException {
		AssertionContext _localctx = new AssertionContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_assertion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(508);
			match(AS);
			setState(509);
			nullable_primitive_type();
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
	public static class Optional_parameter_listContext extends ParserRuleContext {
		public Optional_parameterContext optional_parameter() {
			return getRuleContext(Optional_parameterContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Optional_parameter_listContext optional_parameter_list() {
			return getRuleContext(Optional_parameter_listContext.class,0);
		}
		public Optional_parameter_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_optional_parameter_list; }
	}

	public final Optional_parameter_listContext optional_parameter_list() throws RecognitionException {
		Optional_parameter_listContext _localctx = new Optional_parameter_listContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_optional_parameter_list);
		try {
			setState(516);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(511);
				optional_parameter();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(512);
				optional_parameter();
				setState(513);
				match(COMMA);
				setState(514);
				optional_parameter_list();
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
	public static class Optional_parameterContext extends ParserRuleContext {
		public TerminalNode OPTIONAL_TEXT() { return getToken(PowerQueryParser.OPTIONAL_TEXT, 0); }
		public ParameterContext parameter() {
			return getRuleContext(ParameterContext.class,0);
		}
		public Optional_parameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_optional_parameter; }
	}

	public final Optional_parameterContext optional_parameter() throws RecognitionException {
		Optional_parameterContext _localctx = new Optional_parameterContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_optional_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(518);
			match(OPTIONAL_TEXT);
			setState(519);
			parameter();
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
		public Each_expression_bodyContext each_expression_body() {
			return getRuleContext(Each_expression_bodyContext.class,0);
		}
		public Each_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_each_expression; }
	}

	public final Each_expressionContext each_expression() throws RecognitionException {
		Each_expressionContext _localctx = new Each_expressionContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_each_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(521);
			match(EACH);
			setState(522);
			each_expression_body();
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
	public static class Each_expression_bodyContext extends ParserRuleContext {
		public Function_bodyContext function_body() {
			return getRuleContext(Function_bodyContext.class,0);
		}
		public Each_expression_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_each_expression_body; }
	}

	public final Each_expression_bodyContext each_expression_body() throws RecognitionException {
		Each_expression_bodyContext _localctx = new Each_expression_bodyContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_each_expression_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(524);
			function_body();
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
	public static class Let_expressionContext extends ParserRuleContext {
		public TerminalNode LET() { return getToken(PowerQueryParser.LET, 0); }
		public Variable_listContext variable_list() {
			return getRuleContext(Variable_listContext.class,0);
		}
		public TerminalNode IN() { return getToken(PowerQueryParser.IN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Let_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_let_expression; }
	}

	public final Let_expressionContext let_expression() throws RecognitionException {
		Let_expressionContext _localctx = new Let_expressionContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_let_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(526);
			match(LET);
			setState(527);
			variable_list();
			setState(528);
			match(IN);
			setState(529);
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
	public static class Variable_listContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Variable_listContext variable_list() {
			return getRuleContext(Variable_listContext.class,0);
		}
		public Variable_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_list; }
	}

	public final Variable_listContext variable_list() throws RecognitionException {
		Variable_listContext _localctx = new Variable_listContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_variable_list);
		try {
			setState(536);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,40,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(531);
				variable();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(532);
				variable();
				setState(533);
				match(COMMA);
				setState(534);
				variable_list();
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
	public static class VariableContext extends ParserRuleContext {
		public Variable_nameContext variable_name() {
			return getRuleContext(Variable_nameContext.class,0);
		}
		public TerminalNode EQUALS() { return getToken(PowerQueryParser.EQUALS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 124, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(538);
			variable_name();
			setState(539);
			match(EQUALS);
			setState(540);
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
	public static class Variable_nameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(PowerQueryParser.IDENTIFIER, 0); }
		public Variable_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_name; }
	}

	public final Variable_nameContext variable_name() throws RecognitionException {
		Variable_nameContext _localctx = new Variable_nameContext(_ctx, getState());
		enterRule(_localctx, 126, RULE_variable_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(542);
			match(IDENTIFIER);
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
	public static class If_expressionContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(PowerQueryParser.IF, 0); }
		public If_conditionContext if_condition() {
			return getRuleContext(If_conditionContext.class,0);
		}
		public TerminalNode THEN() { return getToken(PowerQueryParser.THEN, 0); }
		public True_expressionContext true_expression() {
			return getRuleContext(True_expressionContext.class,0);
		}
		public TerminalNode ELSE() { return getToken(PowerQueryParser.ELSE, 0); }
		public False_expressionContext false_expression() {
			return getRuleContext(False_expressionContext.class,0);
		}
		public If_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_expression; }
	}

	public final If_expressionContext if_expression() throws RecognitionException {
		If_expressionContext _localctx = new If_expressionContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_if_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(544);
			match(IF);
			setState(545);
			if_condition();
			setState(546);
			match(THEN);
			setState(547);
			true_expression();
			setState(548);
			match(ELSE);
			setState(549);
			false_expression();
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
	public static class If_conditionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public If_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_condition; }
	}

	public final If_conditionContext if_condition() throws RecognitionException {
		If_conditionContext _localctx = new If_conditionContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_if_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(551);
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
	public static class True_expressionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public True_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_true_expression; }
	}

	public final True_expressionContext true_expression() throws RecognitionException {
		True_expressionContext _localctx = new True_expressionContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_true_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(553);
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
	public static class False_expressionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public False_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_false_expression; }
	}

	public final False_expressionContext false_expression() throws RecognitionException {
		False_expressionContext _localctx = new False_expressionContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_false_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(555);
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
	public static class Type_expressionContext extends ParserRuleContext {
		public Primary_expressionContext primary_expression() {
			return getRuleContext(Primary_expressionContext.class,0);
		}
		public TerminalNode TYPE() { return getToken(PowerQueryParser.TYPE, 0); }
		public Primary_typeContext primary_type() {
			return getRuleContext(Primary_typeContext.class,0);
		}
		public Type_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_expression; }
	}

	public final Type_expressionContext type_expression() throws RecognitionException {
		Type_expressionContext _localctx = new Type_expressionContext(_ctx, getState());
		enterRule(_localctx, 136, RULE_type_expression);
		try {
			setState(560);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_BRACKET:
			case OPEN_BRACE:
			case OPEN_PAREN:
			case ELLIPSES:
			case AT:
			case LITERAL:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(557);
				primary_expression();
				}
				break;
			case TYPE:
				enterOuterAlt(_localctx, 2);
				{
				setState(558);
				match(TYPE);
				setState(559);
				primary_type();
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
	public static class Type_exprContext extends ParserRuleContext {
		public Parenthesized_expressionContext parenthesized_expression() {
			return getRuleContext(Parenthesized_expressionContext.class,0);
		}
		public Primary_typeContext primary_type() {
			return getRuleContext(Primary_typeContext.class,0);
		}
		public Type_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_expr; }
	}

	public final Type_exprContext type_expr() throws RecognitionException {
		Type_exprContext _localctx = new Type_exprContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_type_expr);
		try {
			setState(564);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(562);
				parenthesized_expression();
				}
				break;
			case OPEN_BRACKET:
			case OPEN_BRACE:
			case TABLE:
			case NULLABLE:
			case FUNCTION_START:
			case TYPE:
			case TEXT:
			case RECORD:
			case NUMBER:
			case NONE:
			case LOGICAL:
			case LIST:
			case FUNCTION:
			case DURATION:
			case DATETIMEZONE:
			case ANY:
			case ANYNONNULL:
			case BINARY:
			case DATE:
			case DATETIME:
			case LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(563);
				primary_type();
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
	public static class Primary_typeContext extends ParserRuleContext {
		public Primitive_typeContext primitive_type() {
			return getRuleContext(Primitive_typeContext.class,0);
		}
		public Record_typeContext record_type() {
			return getRuleContext(Record_typeContext.class,0);
		}
		public List_typeContext list_type() {
			return getRuleContext(List_typeContext.class,0);
		}
		public Function_typeContext function_type() {
			return getRuleContext(Function_typeContext.class,0);
		}
		public Table_typeContext table_type() {
			return getRuleContext(Table_typeContext.class,0);
		}
		public Nullable_typeContext nullable_type() {
			return getRuleContext(Nullable_typeContext.class,0);
		}
		public Primary_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary_type; }
	}

	public final Primary_typeContext primary_type() throws RecognitionException {
		Primary_typeContext _localctx = new Primary_typeContext(_ctx, getState());
		enterRule(_localctx, 140, RULE_primary_type);
		try {
			setState(572);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,43,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(566);
				primitive_type();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(567);
				record_type();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(568);
				list_type();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(569);
				function_type();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(570);
				table_type();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(571);
				nullable_type();
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
	public static class Primitive_typeContext extends ParserRuleContext {
		public TerminalNode ANY() { return getToken(PowerQueryParser.ANY, 0); }
		public TerminalNode ANYNONNULL() { return getToken(PowerQueryParser.ANYNONNULL, 0); }
		public TerminalNode BINARY() { return getToken(PowerQueryParser.BINARY, 0); }
		public TerminalNode DATE() { return getToken(PowerQueryParser.DATE, 0); }
		public TerminalNode DATETIME() { return getToken(PowerQueryParser.DATETIME, 0); }
		public TerminalNode DATETIMEZONE() { return getToken(PowerQueryParser.DATETIMEZONE, 0); }
		public TerminalNode DURATION() { return getToken(PowerQueryParser.DURATION, 0); }
		public TerminalNode FUNCTION() { return getToken(PowerQueryParser.FUNCTION, 0); }
		public TerminalNode LIST() { return getToken(PowerQueryParser.LIST, 0); }
		public TerminalNode LOGICAL() { return getToken(PowerQueryParser.LOGICAL, 0); }
		public TerminalNode NONE() { return getToken(PowerQueryParser.NONE, 0); }
		public TerminalNode NUMBER() { return getToken(PowerQueryParser.NUMBER, 0); }
		public TerminalNode RECORD() { return getToken(PowerQueryParser.RECORD, 0); }
		public TerminalNode TABLE() { return getToken(PowerQueryParser.TABLE, 0); }
		public TerminalNode TEXT() { return getToken(PowerQueryParser.TEXT, 0); }
		public TerminalNode TYPE() { return getToken(PowerQueryParser.TYPE, 0); }
		public TerminalNode LITERAL() { return getToken(PowerQueryParser.LITERAL, 0); }
		public Primitive_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive_type; }
	}

	public final Primitive_typeContext primitive_type() throws RecognitionException {
		Primitive_typeContext _localctx = new Primitive_typeContext(_ctx, getState());
		enterRule(_localctx, 142, RULE_primitive_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(574);
			_la = _input.LA(1);
			if ( !(((((_la - 16)) & ~0x3f) == 0 && ((1L << (_la - 16)) & 2251808403099649L) != 0)) ) {
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
	public static class Record_typeContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACKET() { return getToken(PowerQueryParser.OPEN_BRACKET, 0); }
		public Open_record_markerContext open_record_marker() {
			return getRuleContext(Open_record_markerContext.class,0);
		}
		public TerminalNode CLOSE_BRACKET() { return getToken(PowerQueryParser.CLOSE_BRACKET, 0); }
		public Field_specification_listContext field_specification_list() {
			return getRuleContext(Field_specification_listContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Record_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_record_type; }
	}

	public final Record_typeContext record_type() throws RecognitionException {
		Record_typeContext _localctx = new Record_typeContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_record_type);
		int _la;
		try {
			setState(591);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(576);
				match(OPEN_BRACKET);
				setState(577);
				open_record_marker();
				setState(578);
				match(CLOSE_BRACKET);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(580);
				match(OPEN_BRACKET);
				setState(582);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==OPTIONAL_TEXT || _la==IDENTIFIER) {
					{
					setState(581);
					field_specification_list();
					}
				}

				setState(584);
				match(CLOSE_BRACKET);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(585);
				match(OPEN_BRACKET);
				setState(586);
				field_specification_list();
				setState(587);
				match(COMMA);
				setState(588);
				open_record_marker();
				setState(589);
				match(CLOSE_BRACKET);
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
	public static class Field_specification_listContext extends ParserRuleContext {
		public Field_specificationContext field_specification() {
			return getRuleContext(Field_specificationContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Field_specification_listContext field_specification_list() {
			return getRuleContext(Field_specification_listContext.class,0);
		}
		public Field_specification_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_specification_list; }
	}

	public final Field_specification_listContext field_specification_list() throws RecognitionException {
		Field_specification_listContext _localctx = new Field_specification_listContext(_ctx, getState());
		enterRule(_localctx, 146, RULE_field_specification_list);
		try {
			setState(598);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(593);
				field_specification();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(594);
				field_specification();
				setState(595);
				match(COMMA);
				setState(596);
				field_specification_list();
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
	public static class Field_specificationContext extends ParserRuleContext {
		public Field_nameContext field_name() {
			return getRuleContext(Field_nameContext.class,0);
		}
		public TerminalNode OPTIONAL_TEXT() { return getToken(PowerQueryParser.OPTIONAL_TEXT, 0); }
		public Field_type_specificationContext field_type_specification() {
			return getRuleContext(Field_type_specificationContext.class,0);
		}
		public Field_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_specification; }
	}

	public final Field_specificationContext field_specification() throws RecognitionException {
		Field_specificationContext _localctx = new Field_specificationContext(_ctx, getState());
		enterRule(_localctx, 148, RULE_field_specification);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(601);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPTIONAL_TEXT) {
				{
				setState(600);
				match(OPTIONAL_TEXT);
				}
			}

			setState(603);
			field_name();
			setState(605);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUALS) {
				{
				setState(604);
				field_type_specification();
				}
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
	public static class Field_type_specificationContext extends ParserRuleContext {
		public TerminalNode EQUALS() { return getToken(PowerQueryParser.EQUALS, 0); }
		public Field_typeContext field_type() {
			return getRuleContext(Field_typeContext.class,0);
		}
		public Field_type_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_type_specification; }
	}

	public final Field_type_specificationContext field_type_specification() throws RecognitionException {
		Field_type_specificationContext _localctx = new Field_type_specificationContext(_ctx, getState());
		enterRule(_localctx, 150, RULE_field_type_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(607);
			match(EQUALS);
			setState(608);
			field_type();
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
	public static class Field_typeContext extends ParserRuleContext {
		public Type_exprContext type_expr() {
			return getRuleContext(Type_exprContext.class,0);
		}
		public Field_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_type; }
	}

	public final Field_typeContext field_type() throws RecognitionException {
		Field_typeContext _localctx = new Field_typeContext(_ctx, getState());
		enterRule(_localctx, 152, RULE_field_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(610);
			type_expr();
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
	public static class Open_record_markerContext extends ParserRuleContext {
		public TerminalNode ELLIPSES() { return getToken(PowerQueryParser.ELLIPSES, 0); }
		public Open_record_markerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_open_record_marker; }
	}

	public final Open_record_markerContext open_record_marker() throws RecognitionException {
		Open_record_markerContext _localctx = new Open_record_markerContext(_ctx, getState());
		enterRule(_localctx, 154, RULE_open_record_marker);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(612);
			match(ELLIPSES);
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
	public static class List_typeContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACE() { return getToken(PowerQueryParser.OPEN_BRACE, 0); }
		public Item_typeContext item_type() {
			return getRuleContext(Item_typeContext.class,0);
		}
		public TerminalNode CLOSE_BRACE() { return getToken(PowerQueryParser.CLOSE_BRACE, 0); }
		public List_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_type; }
	}

	public final List_typeContext list_type() throws RecognitionException {
		List_typeContext _localctx = new List_typeContext(_ctx, getState());
		enterRule(_localctx, 156, RULE_list_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(614);
			match(OPEN_BRACE);
			setState(615);
			item_type();
			setState(616);
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
	public static class Item_typeContext extends ParserRuleContext {
		public Type_exprContext type_expr() {
			return getRuleContext(Type_exprContext.class,0);
		}
		public Item_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item_type; }
	}

	public final Item_typeContext item_type() throws RecognitionException {
		Item_typeContext _localctx = new Item_typeContext(_ctx, getState());
		enterRule(_localctx, 158, RULE_item_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(618);
			type_expr();
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
	public static class Function_typeContext extends ParserRuleContext {
		public TerminalNode FUNCTION_START() { return getToken(PowerQueryParser.FUNCTION_START, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(PowerQueryParser.CLOSE_PAREN, 0); }
		public Return_typeContext return_type() {
			return getRuleContext(Return_typeContext.class,0);
		}
		public Parameter_specification_listContext parameter_specification_list() {
			return getRuleContext(Parameter_specification_listContext.class,0);
		}
		public Function_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_type; }
	}

	public final Function_typeContext function_type() throws RecognitionException {
		Function_typeContext _localctx = new Function_typeContext(_ctx, getState());
		enterRule(_localctx, 160, RULE_function_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(620);
			match(FUNCTION_START);
			setState(622);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPTIONAL_TEXT || _la==IDENTIFIER) {
				{
				setState(621);
				parameter_specification_list();
				}
			}

			setState(624);
			match(CLOSE_PAREN);
			setState(625);
			return_type();
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
	public static class Parameter_specification_listContext extends ParserRuleContext {
		public Required_parameter_specification_listContext required_parameter_specification_list() {
			return getRuleContext(Required_parameter_specification_listContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Optional_parameter_specification_listContext optional_parameter_specification_list() {
			return getRuleContext(Optional_parameter_specification_listContext.class,0);
		}
		public Parameter_specification_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_specification_list; }
	}

	public final Parameter_specification_listContext parameter_specification_list() throws RecognitionException {
		Parameter_specification_listContext _localctx = new Parameter_specification_listContext(_ctx, getState());
		enterRule(_localctx, 162, RULE_parameter_specification_list);
		try {
			setState(633);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,50,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(627);
				required_parameter_specification_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(628);
				required_parameter_specification_list();
				setState(629);
				match(COMMA);
				setState(630);
				optional_parameter_specification_list();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(632);
				optional_parameter_specification_list();
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
	public static class Required_parameter_specification_listContext extends ParserRuleContext {
		public Required_parameter_specificationContext required_parameter_specification() {
			return getRuleContext(Required_parameter_specificationContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Required_parameter_specification_listContext required_parameter_specification_list() {
			return getRuleContext(Required_parameter_specification_listContext.class,0);
		}
		public Required_parameter_specification_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_required_parameter_specification_list; }
	}

	public final Required_parameter_specification_listContext required_parameter_specification_list() throws RecognitionException {
		Required_parameter_specification_listContext _localctx = new Required_parameter_specification_listContext(_ctx, getState());
		enterRule(_localctx, 164, RULE_required_parameter_specification_list);
		try {
			setState(640);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,51,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(635);
				required_parameter_specification();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(636);
				required_parameter_specification();
				setState(637);
				match(COMMA);
				setState(638);
				required_parameter_specification_list();
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
	public static class Required_parameter_specificationContext extends ParserRuleContext {
		public Parameter_specificationContext parameter_specification() {
			return getRuleContext(Parameter_specificationContext.class,0);
		}
		public Required_parameter_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_required_parameter_specification; }
	}

	public final Required_parameter_specificationContext required_parameter_specification() throws RecognitionException {
		Required_parameter_specificationContext _localctx = new Required_parameter_specificationContext(_ctx, getState());
		enterRule(_localctx, 166, RULE_required_parameter_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(642);
			parameter_specification();
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
	public static class Optional_parameter_specification_listContext extends ParserRuleContext {
		public Optional_parameter_specificationContext optional_parameter_specification() {
			return getRuleContext(Optional_parameter_specificationContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Optional_parameter_specification_listContext optional_parameter_specification_list() {
			return getRuleContext(Optional_parameter_specification_listContext.class,0);
		}
		public Optional_parameter_specification_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_optional_parameter_specification_list; }
	}

	public final Optional_parameter_specification_listContext optional_parameter_specification_list() throws RecognitionException {
		Optional_parameter_specification_listContext _localctx = new Optional_parameter_specification_listContext(_ctx, getState());
		enterRule(_localctx, 168, RULE_optional_parameter_specification_list);
		try {
			setState(649);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,52,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(644);
				optional_parameter_specification();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(645);
				optional_parameter_specification();
				setState(646);
				match(COMMA);
				setState(647);
				optional_parameter_specification_list();
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
	public static class Optional_parameter_specificationContext extends ParserRuleContext {
		public TerminalNode OPTIONAL_TEXT() { return getToken(PowerQueryParser.OPTIONAL_TEXT, 0); }
		public Parameter_specificationContext parameter_specification() {
			return getRuleContext(Parameter_specificationContext.class,0);
		}
		public Optional_parameter_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_optional_parameter_specification; }
	}

	public final Optional_parameter_specificationContext optional_parameter_specification() throws RecognitionException {
		Optional_parameter_specificationContext _localctx = new Optional_parameter_specificationContext(_ctx, getState());
		enterRule(_localctx, 170, RULE_optional_parameter_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(651);
			match(OPTIONAL_TEXT);
			setState(652);
			parameter_specification();
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
	public static class Parameter_specificationContext extends ParserRuleContext {
		public Parameter_nameContext parameter_name() {
			return getRuleContext(Parameter_nameContext.class,0);
		}
		public Parameter_typeContext parameter_type() {
			return getRuleContext(Parameter_typeContext.class,0);
		}
		public Parameter_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_specification; }
	}

	public final Parameter_specificationContext parameter_specification() throws RecognitionException {
		Parameter_specificationContext _localctx = new Parameter_specificationContext(_ctx, getState());
		enterRule(_localctx, 172, RULE_parameter_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(654);
			parameter_name();
			setState(655);
			parameter_type();
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
	public static class Table_typeContext extends ParserRuleContext {
		public TerminalNode TABLE() { return getToken(PowerQueryParser.TABLE, 0); }
		public Row_typeContext row_type() {
			return getRuleContext(Row_typeContext.class,0);
		}
		public Table_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_table_type; }
	}

	public final Table_typeContext table_type() throws RecognitionException {
		Table_typeContext _localctx = new Table_typeContext(_ctx, getState());
		enterRule(_localctx, 174, RULE_table_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(657);
			match(TABLE);
			setState(658);
			row_type();
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
	public static class Row_typeContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACKET() { return getToken(PowerQueryParser.OPEN_BRACKET, 0); }
		public Field_specification_listContext field_specification_list() {
			return getRuleContext(Field_specification_listContext.class,0);
		}
		public TerminalNode CLOSE_BRACKET() { return getToken(PowerQueryParser.CLOSE_BRACKET, 0); }
		public Row_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_row_type; }
	}

	public final Row_typeContext row_type() throws RecognitionException {
		Row_typeContext _localctx = new Row_typeContext(_ctx, getState());
		enterRule(_localctx, 176, RULE_row_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(660);
			match(OPEN_BRACKET);
			setState(661);
			field_specification_list();
			setState(662);
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
	public static class Nullable_typeContext extends ParserRuleContext {
		public TerminalNode NULLABLE() { return getToken(PowerQueryParser.NULLABLE, 0); }
		public Type_exprContext type_expr() {
			return getRuleContext(Type_exprContext.class,0);
		}
		public Nullable_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nullable_type; }
	}

	public final Nullable_typeContext nullable_type() throws RecognitionException {
		Nullable_typeContext _localctx = new Nullable_typeContext(_ctx, getState());
		enterRule(_localctx, 178, RULE_nullable_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(664);
			match(NULLABLE);
			setState(665);
			type_expr();
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
	public static class Error_raising_expressionContext extends ParserRuleContext {
		public TerminalNode ERROR() { return getToken(PowerQueryParser.ERROR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Error_raising_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_error_raising_expression; }
	}

	public final Error_raising_expressionContext error_raising_expression() throws RecognitionException {
		Error_raising_expressionContext _localctx = new Error_raising_expressionContext(_ctx, getState());
		enterRule(_localctx, 180, RULE_error_raising_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(667);
			match(ERROR);
			setState(668);
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
	public static class Error_handling_expressionContext extends ParserRuleContext {
		public TerminalNode TRY() { return getToken(PowerQueryParser.TRY, 0); }
		public Protected_expressionContext protected_expression() {
			return getRuleContext(Protected_expressionContext.class,0);
		}
		public Otherwise_clauseContext otherwise_clause() {
			return getRuleContext(Otherwise_clauseContext.class,0);
		}
		public Error_handling_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_error_handling_expression; }
	}

	public final Error_handling_expressionContext error_handling_expression() throws RecognitionException {
		Error_handling_expressionContext _localctx = new Error_handling_expressionContext(_ctx, getState());
		enterRule(_localctx, 182, RULE_error_handling_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(670);
			match(TRY);
			setState(671);
			protected_expression();
			setState(673);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,53,_ctx) ) {
			case 1:
				{
				setState(672);
				otherwise_clause();
				}
				break;
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
	public static class Protected_expressionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Protected_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_protected_expression; }
	}

	public final Protected_expressionContext protected_expression() throws RecognitionException {
		Protected_expressionContext _localctx = new Protected_expressionContext(_ctx, getState());
		enterRule(_localctx, 184, RULE_protected_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(675);
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
	public static class Otherwise_clauseContext extends ParserRuleContext {
		public TerminalNode OTHERWISE() { return getToken(PowerQueryParser.OTHERWISE, 0); }
		public Default_expressionContext default_expression() {
			return getRuleContext(Default_expressionContext.class,0);
		}
		public Otherwise_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_otherwise_clause; }
	}

	public final Otherwise_clauseContext otherwise_clause() throws RecognitionException {
		Otherwise_clauseContext _localctx = new Otherwise_clauseContext(_ctx, getState());
		enterRule(_localctx, 186, RULE_otherwise_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(677);
			match(OTHERWISE);
			setState(678);
			default_expression();
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
	public static class Default_expressionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Default_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_default_expression; }
	}

	public final Default_expressionContext default_expression() throws RecognitionException {
		Default_expressionContext _localctx = new Default_expressionContext(_ctx, getState());
		enterRule(_localctx, 188, RULE_default_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(680);
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
	public static class Literal_attribsContext extends ParserRuleContext {
		public Record_literalContext record_literal() {
			return getRuleContext(Record_literalContext.class,0);
		}
		public Literal_attribsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal_attribs; }
	}

	public final Literal_attribsContext literal_attribs() throws RecognitionException {
		Literal_attribsContext _localctx = new Literal_attribsContext(_ctx, getState());
		enterRule(_localctx, 190, RULE_literal_attribs);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(682);
			record_literal();
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
	public static class Record_literalContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACKET() { return getToken(PowerQueryParser.OPEN_BRACKET, 0); }
		public TerminalNode CLOSE_BRACKET() { return getToken(PowerQueryParser.CLOSE_BRACKET, 0); }
		public Literal_field_listContext literal_field_list() {
			return getRuleContext(Literal_field_listContext.class,0);
		}
		public Record_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_record_literal; }
	}

	public final Record_literalContext record_literal() throws RecognitionException {
		Record_literalContext _localctx = new Record_literalContext(_ctx, getState());
		enterRule(_localctx, 192, RULE_record_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(684);
			match(OPEN_BRACKET);
			setState(686);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(685);
				literal_field_list();
				}
			}

			setState(688);
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
	public static class Literal_field_listContext extends ParserRuleContext {
		public Literal_fieldContext literal_field() {
			return getRuleContext(Literal_fieldContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Literal_field_listContext literal_field_list() {
			return getRuleContext(Literal_field_listContext.class,0);
		}
		public Literal_field_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal_field_list; }
	}

	public final Literal_field_listContext literal_field_list() throws RecognitionException {
		Literal_field_listContext _localctx = new Literal_field_listContext(_ctx, getState());
		enterRule(_localctx, 194, RULE_literal_field_list);
		try {
			setState(695);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,55,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(690);
				literal_field();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(691);
				literal_field();
				setState(692);
				match(COMMA);
				setState(693);
				literal_field_list();
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
	public static class Literal_fieldContext extends ParserRuleContext {
		public Field_nameContext field_name() {
			return getRuleContext(Field_nameContext.class,0);
		}
		public TerminalNode EQUALS() { return getToken(PowerQueryParser.EQUALS, 0); }
		public Any_literalContext any_literal() {
			return getRuleContext(Any_literalContext.class,0);
		}
		public Literal_fieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal_field; }
	}

	public final Literal_fieldContext literal_field() throws RecognitionException {
		Literal_fieldContext _localctx = new Literal_fieldContext(_ctx, getState());
		enterRule(_localctx, 196, RULE_literal_field);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(697);
			field_name();
			setState(698);
			match(EQUALS);
			setState(699);
			any_literal();
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
	public static class List_literalContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACE() { return getToken(PowerQueryParser.OPEN_BRACE, 0); }
		public TerminalNode CLOSE_BRACE() { return getToken(PowerQueryParser.CLOSE_BRACE, 0); }
		public Literal_item_listContext literal_item_list() {
			return getRuleContext(Literal_item_listContext.class,0);
		}
		public List_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_literal; }
	}

	public final List_literalContext list_literal() throws RecognitionException {
		List_literalContext _localctx = new List_literalContext(_ctx, getState());
		enterRule(_localctx, 198, RULE_list_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(701);
			match(OPEN_BRACE);
			setState(703);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & 576460752303423493L) != 0)) {
				{
				setState(702);
				literal_item_list();
				}
			}

			setState(705);
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
	public static class Literal_item_listContext extends ParserRuleContext {
		public Any_literalContext any_literal() {
			return getRuleContext(Any_literalContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PowerQueryParser.COMMA, 0); }
		public Literal_item_listContext literal_item_list() {
			return getRuleContext(Literal_item_listContext.class,0);
		}
		public Literal_item_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal_item_list; }
	}

	public final Literal_item_listContext literal_item_list() throws RecognitionException {
		Literal_item_listContext _localctx = new Literal_item_listContext(_ctx, getState());
		enterRule(_localctx, 200, RULE_literal_item_list);
		try {
			setState(712);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,57,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(707);
				any_literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(708);
				any_literal();
				setState(709);
				match(COMMA);
				setState(710);
				literal_item_list();
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
	public static class Any_literalContext extends ParserRuleContext {
		public Record_literalContext record_literal() {
			return getRuleContext(Record_literalContext.class,0);
		}
		public List_literalContext list_literal() {
			return getRuleContext(List_literalContext.class,0);
		}
		public TerminalNode LITERAL() { return getToken(PowerQueryParser.LITERAL, 0); }
		public Any_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_any_literal; }
	}

	public final Any_literalContext any_literal() throws RecognitionException {
		Any_literalContext _localctx = new Any_literalContext(_ctx, getState());
		enterRule(_localctx, 202, RULE_any_literal);
		try {
			setState(717);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_BRACKET:
				enterOuterAlt(_localctx, 1);
				{
				setState(714);
				record_literal();
				}
				break;
			case OPEN_BRACE:
				enterOuterAlt(_localctx, 2);
				{
				setState(715);
				list_literal();
				}
				break;
			case LITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(716);
				match(LITERAL);
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

	public static final String _serializedATN =
		"\u0004\u0001H\u02d0\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002"+
		"-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u00070\u00021\u00071\u0002"+
		"2\u00072\u00023\u00073\u00024\u00074\u00025\u00075\u00026\u00076\u0002"+
		"7\u00077\u00028\u00078\u00029\u00079\u0002:\u0007:\u0002;\u0007;\u0002"+
		"<\u0007<\u0002=\u0007=\u0002>\u0007>\u0002?\u0007?\u0002@\u0007@\u0002"+
		"A\u0007A\u0002B\u0007B\u0002C\u0007C\u0002D\u0007D\u0002E\u0007E\u0002"+
		"F\u0007F\u0002G\u0007G\u0002H\u0007H\u0002I\u0007I\u0002J\u0007J\u0002"+
		"K\u0007K\u0002L\u0007L\u0002M\u0007M\u0002N\u0007N\u0002O\u0007O\u0002"+
		"P\u0007P\u0002Q\u0007Q\u0002R\u0007R\u0002S\u0007S\u0002T\u0007T\u0002"+
		"U\u0007U\u0002V\u0007V\u0002W\u0007W\u0002X\u0007X\u0002Y\u0007Y\u0002"+
		"Z\u0007Z\u0002[\u0007[\u0002\\\u0007\\\u0002]\u0007]\u0002^\u0007^\u0002"+
		"_\u0007_\u0002`\u0007`\u0002a\u0007a\u0002b\u0007b\u0002c\u0007c\u0002"+
		"d\u0007d\u0002e\u0007e\u0001\u0000\u0001\u0000\u0003\u0000\u00cf\b\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0003\u0002\u00d4\b\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002\u00da\b\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0003\u0004\u00e0\b\u0004\u0001\u0005"+
		"\u0003\u0005\u00e3\b\u0005\u0001\u0005\u0003\u0005\u00e6\b\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0003\b\u00f8\b\b\u0001\t\u0001\t\u0001\t\u0005\t\u00fd"+
		"\b\t\n\t\f\t\u0100\t\t\u0001\n\u0001\n\u0001\n\u0005\n\u0105\b\n\n\n\f"+
		"\n\u0108\t\n\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u010d\b\u000b"+
		"\u0001\f\u0003\f\u0110\b\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0005"+
		"\r\u0117\b\r\n\r\f\r\u011a\t\r\u0001\u000e\u0001\u000e\u0001\u000e\u0005"+
		"\u000e\u011f\b\u000e\n\u000e\f\u000e\u0122\t\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0005\u000f\u0127\b\u000f\n\u000f\f\u000f\u012a\t\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u012f\b\u0010\n\u0010\f\u0010"+
		"\u0132\t\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011\u0137\b"+
		"\u0011\n\u0011\f\u0011\u013a\t\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0005\u0012\u013f\b\u0012\n\u0012\f\u0012\u0142\t\u0012\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003"+
		"\u0013\u014b\b\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u0155\b\u0014\u0001"+
		"\u0014\u0001\u0014\u0003\u0014\u0159\b\u0014\u0001\u0014\u0005\u0014\u015c"+
		"\b\u0014\n\u0014\f\u0014\u015f\t\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0003\u0014\u0164\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0003\u0015\u016c\b\u0015\u0001\u0016\u0001\u0016"+
		"\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0003\u0018\u0174\b\u0018"+
		"\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0003\u001e\u018a\b\u001e\u0001\u001f\u0001\u001f"+
		"\u0003\u001f\u018e\b\u001f\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001"+
		" \u0001 \u0001 \u0003 \u0197\b \u0001!\u0001!\u0001!\u0001!\u0001!\u0003"+
		"!\u019e\b!\u0001\"\u0001\"\u0003\"\u01a2\b\"\u0001\"\u0001\"\u0001#\u0001"+
		"#\u0001#\u0001#\u0001#\u0003#\u01ab\b#\u0001$\u0001$\u0001$\u0001$\u0001"+
		"%\u0001%\u0001&\u0001&\u0001\'\u0001\'\u0003\'\u01b7\b\'\u0001(\u0001"+
		"(\u0001(\u0001(\u0001)\u0001)\u0001)\u0001)\u0001)\u0001*\u0001*\u0001"+
		"+\u0001+\u0001+\u0001+\u0001,\u0001,\u0001,\u0001,\u0001,\u0001-\u0001"+
		"-\u0001-\u0001-\u0001-\u0003-\u01d2\b-\u0001.\u0001.\u0003.\u01d6\b.\u0001"+
		"/\u0001/\u0003/\u01da\b/\u0001/\u0001/\u0003/\u01de\b/\u0001/\u0001/\u0001"+
		"/\u00010\u00010\u00011\u00011\u00011\u00011\u00011\u00031\u01ea\b1\u0001"+
		"2\u00012\u00012\u00012\u00012\u00032\u01f1\b2\u00013\u00013\u00033\u01f5"+
		"\b3\u00014\u00014\u00015\u00015\u00016\u00016\u00017\u00017\u00017\u0001"+
		"8\u00018\u00018\u00018\u00018\u00038\u0205\b8\u00019\u00019\u00019\u0001"+
		":\u0001:\u0001:\u0001;\u0001;\u0001<\u0001<\u0001<\u0001<\u0001<\u0001"+
		"=\u0001=\u0001=\u0001=\u0001=\u0003=\u0219\b=\u0001>\u0001>\u0001>\u0001"+
		">\u0001?\u0001?\u0001@\u0001@\u0001@\u0001@\u0001@\u0001@\u0001@\u0001"+
		"A\u0001A\u0001B\u0001B\u0001C\u0001C\u0001D\u0001D\u0001D\u0003D\u0231"+
		"\bD\u0001E\u0001E\u0003E\u0235\bE\u0001F\u0001F\u0001F\u0001F\u0001F\u0001"+
		"F\u0003F\u023d\bF\u0001G\u0001G\u0001H\u0001H\u0001H\u0001H\u0001H\u0001"+
		"H\u0003H\u0247\bH\u0001H\u0001H\u0001H\u0001H\u0001H\u0001H\u0001H\u0003"+
		"H\u0250\bH\u0001I\u0001I\u0001I\u0001I\u0001I\u0003I\u0257\bI\u0001J\u0003"+
		"J\u025a\bJ\u0001J\u0001J\u0003J\u025e\bJ\u0001K\u0001K\u0001K\u0001L\u0001"+
		"L\u0001M\u0001M\u0001N\u0001N\u0001N\u0001N\u0001O\u0001O\u0001P\u0001"+
		"P\u0003P\u026f\bP\u0001P\u0001P\u0001P\u0001Q\u0001Q\u0001Q\u0001Q\u0001"+
		"Q\u0001Q\u0003Q\u027a\bQ\u0001R\u0001R\u0001R\u0001R\u0001R\u0003R\u0281"+
		"\bR\u0001S\u0001S\u0001T\u0001T\u0001T\u0001T\u0001T\u0003T\u028a\bT\u0001"+
		"U\u0001U\u0001U\u0001V\u0001V\u0001V\u0001W\u0001W\u0001W\u0001X\u0001"+
		"X\u0001X\u0001X\u0001Y\u0001Y\u0001Y\u0001Z\u0001Z\u0001Z\u0001[\u0001"+
		"[\u0001[\u0003[\u02a2\b[\u0001\\\u0001\\\u0001]\u0001]\u0001]\u0001^\u0001"+
		"^\u0001_\u0001_\u0001`\u0001`\u0003`\u02af\b`\u0001`\u0001`\u0001a\u0001"+
		"a\u0001a\u0001a\u0001a\u0003a\u02b8\ba\u0001b\u0001b\u0001b\u0001b\u0001"+
		"c\u0001c\u0003c\u02c0\bc\u0001c\u0001c\u0001d\u0001d\u0001d\u0001d\u0001"+
		"d\u0003d\u02c9\bd\u0001e\u0001e\u0001e\u0003e\u02ce\be\u0001e\u0000\u0000"+
		"f\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a"+
		"\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082"+
		"\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a"+
		"\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2"+
		"\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca"+
		"\u0000\u0005\u0002\u0000\u0006\u0006;;\u0002\u0000<=AB\u0002\u000078@"+
		"@\u0001\u0000>?\u0004\u0000\u0010\u0010\u001c\u001c#0CC\u02bb\u0000\u00ce"+
		"\u0001\u0000\u0000\u0000\u0002\u00d0\u0001\u0000\u0000\u0000\u0004\u00d3"+
		"\u0001\u0000\u0000\u0000\u0006\u00db\u0001\u0000\u0000\u0000\b\u00dd\u0001"+
		"\u0000\u0000\u0000\n\u00e2\u0001\u0000\u0000\u0000\f\u00ec\u0001\u0000"+
		"\u0000\u0000\u000e\u00ee\u0001\u0000\u0000\u0000\u0010\u00f7\u0001\u0000"+
		"\u0000\u0000\u0012\u00f9\u0001\u0000\u0000\u0000\u0014\u0101\u0001\u0000"+
		"\u0000\u0000\u0016\u0109\u0001\u0000\u0000\u0000\u0018\u010f\u0001\u0000"+
		"\u0000\u0000\u001a\u0113\u0001\u0000\u0000\u0000\u001c\u011b\u0001\u0000"+
		"\u0000\u0000\u001e\u0123\u0001\u0000\u0000\u0000 \u012b\u0001\u0000\u0000"+
		"\u0000\"\u0133\u0001\u0000\u0000\u0000$\u013b\u0001\u0000\u0000\u0000"+
		"&\u014a\u0001\u0000\u0000\u0000(\u0163\u0001\u0000\u0000\u0000*\u016b"+
		"\u0001\u0000\u0000\u0000,\u016d\u0001\u0000\u0000\u0000.\u016f\u0001\u0000"+
		"\u0000\u00000\u0173\u0001\u0000\u0000\u00002\u0175\u0001\u0000\u0000\u0000"+
		"4\u0177\u0001\u0000\u0000\u00006\u017a\u0001\u0000\u0000\u00008\u017e"+
		"\u0001\u0000\u0000\u0000:\u0182\u0001\u0000\u0000\u0000<\u0189\u0001\u0000"+
		"\u0000\u0000>\u018b\u0001\u0000\u0000\u0000@\u0196\u0001\u0000\u0000\u0000"+
		"B\u019d\u0001\u0000\u0000\u0000D\u019f\u0001\u0000\u0000\u0000F\u01aa"+
		"\u0001\u0000\u0000\u0000H\u01ac\u0001\u0000\u0000\u0000J\u01b0\u0001\u0000"+
		"\u0000\u0000L\u01b2\u0001\u0000\u0000\u0000N\u01b6\u0001\u0000\u0000\u0000"+
		"P\u01b8\u0001\u0000\u0000\u0000R\u01bc\u0001\u0000\u0000\u0000T\u01c1"+
		"\u0001\u0000\u0000\u0000V\u01c3\u0001\u0000\u0000\u0000X\u01c7\u0001\u0000"+
		"\u0000\u0000Z\u01d1\u0001\u0000\u0000\u0000\\\u01d5\u0001\u0000\u0000"+
		"\u0000^\u01d7\u0001\u0000\u0000\u0000`\u01e2\u0001\u0000\u0000\u0000b"+
		"\u01e9\u0001\u0000\u0000\u0000d\u01f0\u0001\u0000\u0000\u0000f\u01f2\u0001"+
		"\u0000\u0000\u0000h\u01f6\u0001\u0000\u0000\u0000j\u01f8\u0001\u0000\u0000"+
		"\u0000l\u01fa\u0001\u0000\u0000\u0000n\u01fc\u0001\u0000\u0000\u0000p"+
		"\u0204\u0001\u0000\u0000\u0000r\u0206\u0001\u0000\u0000\u0000t\u0209\u0001"+
		"\u0000\u0000\u0000v\u020c\u0001\u0000\u0000\u0000x\u020e\u0001\u0000\u0000"+
		"\u0000z\u0218\u0001\u0000\u0000\u0000|\u021a\u0001\u0000\u0000\u0000~"+
		"\u021e\u0001\u0000\u0000\u0000\u0080\u0220\u0001\u0000\u0000\u0000\u0082"+
		"\u0227\u0001\u0000\u0000\u0000\u0084\u0229\u0001\u0000\u0000\u0000\u0086"+
		"\u022b\u0001\u0000\u0000\u0000\u0088\u0230\u0001\u0000\u0000\u0000\u008a"+
		"\u0234\u0001\u0000\u0000\u0000\u008c\u023c\u0001\u0000\u0000\u0000\u008e"+
		"\u023e\u0001\u0000\u0000\u0000\u0090\u024f\u0001\u0000\u0000\u0000\u0092"+
		"\u0256\u0001\u0000\u0000\u0000\u0094\u0259\u0001\u0000\u0000\u0000\u0096"+
		"\u025f\u0001\u0000\u0000\u0000\u0098\u0262\u0001\u0000\u0000\u0000\u009a"+
		"\u0264\u0001\u0000\u0000\u0000\u009c\u0266\u0001\u0000\u0000\u0000\u009e"+
		"\u026a\u0001\u0000\u0000\u0000\u00a0\u026c\u0001\u0000\u0000\u0000\u00a2"+
		"\u0279\u0001\u0000\u0000\u0000\u00a4\u0280\u0001\u0000\u0000\u0000\u00a6"+
		"\u0282\u0001\u0000\u0000\u0000\u00a8\u0289\u0001\u0000\u0000\u0000\u00aa"+
		"\u028b\u0001\u0000\u0000\u0000\u00ac\u028e\u0001\u0000\u0000\u0000\u00ae"+
		"\u0291\u0001\u0000\u0000\u0000\u00b0\u0294\u0001\u0000\u0000\u0000\u00b2"+
		"\u0298\u0001\u0000\u0000\u0000\u00b4\u029b\u0001\u0000\u0000\u0000\u00b6"+
		"\u029e\u0001\u0000\u0000\u0000\u00b8\u02a3\u0001\u0000\u0000\u0000\u00ba"+
		"\u02a5\u0001\u0000\u0000\u0000\u00bc\u02a8\u0001\u0000\u0000\u0000\u00be"+
		"\u02aa\u0001\u0000\u0000\u0000\u00c0\u02ac\u0001\u0000\u0000\u0000\u00c2"+
		"\u02b7\u0001\u0000\u0000\u0000\u00c4\u02b9\u0001\u0000\u0000\u0000\u00c6"+
		"\u02bd\u0001\u0000\u0000\u0000\u00c8\u02c8\u0001\u0000\u0000\u0000\u00ca"+
		"\u02cd\u0001\u0000\u0000\u0000\u00cc\u00cf\u0003\u0002\u0001\u0000\u00cd"+
		"\u00cf\u0003\u000e\u0007\u0000\u00ce\u00cc\u0001\u0000\u0000\u0000\u00ce"+
		"\u00cd\u0001\u0000\u0000\u0000\u00cf\u0001\u0001\u0000\u0000\u0000\u00d0"+
		"\u00d1\u0003\u0004\u0002\u0000\u00d1\u0003\u0001\u0000\u0000\u0000\u00d2"+
		"\u00d4\u0003\u00be_\u0000\u00d3\u00d2\u0001\u0000\u0000\u0000\u00d3\u00d4"+
		"\u0001\u0000\u0000\u0000\u00d4\u00d5\u0001\u0000\u0000\u0000\u00d5\u00d6"+
		"\u0005\u0013\u0000\u0000\u00d6\u00d7\u0003\u0006\u0003\u0000\u00d7\u00d9"+
		"\u0005\u0012\u0000\u0000\u00d8\u00da\u0003\b\u0004\u0000\u00d9\u00d8\u0001"+
		"\u0000\u0000\u0000\u00d9\u00da\u0001\u0000\u0000\u0000\u00da\u0005\u0001"+
		"\u0000\u0000\u0000\u00db\u00dc\u0005E\u0000\u0000\u00dc\u0007\u0001\u0000"+
		"\u0000\u0000\u00dd\u00df\u0003\n\u0005\u0000\u00de\u00e0\u0003\b\u0004"+
		"\u0000\u00df\u00de\u0001\u0000\u0000\u0000\u00df\u00e0\u0001\u0000\u0000"+
		"\u0000\u00e0\t\u0001\u0000\u0000\u0000\u00e1\u00e3\u0003\u00be_\u0000"+
		"\u00e2\u00e1\u0001\u0000\u0000\u0000\u00e2\u00e3\u0001\u0000\u0000\u0000"+
		"\u00e3\u00e5\u0001\u0000\u0000\u0000\u00e4\u00e6\u0005\u0014\u0000\u0000"+
		"\u00e5\u00e4\u0001\u0000\u0000\u0000\u00e5\u00e6\u0001\u0000\u0000\u0000"+
		"\u00e6\u00e7\u0001\u0000\u0000\u0000\u00e7\u00e8\u0003\f\u0006\u0000\u00e8"+
		"\u00e9\u0005\u0006\u0000\u0000\u00e9\u00ea\u0003\u0010\b\u0000\u00ea\u00eb"+
		"\u0005\u0012\u0000\u0000\u00eb\u000b\u0001\u0000\u0000\u0000\u00ec\u00ed"+
		"\u0005E\u0000\u0000\u00ed\r\u0001\u0000\u0000\u0000\u00ee\u00ef\u0003"+
		"\u0010\b\u0000\u00ef\u000f\u0001\u0000\u0000\u0000\u00f0\u00f8\u0003t"+
		":\u0000\u00f1\u00f8\u0003^/\u0000\u00f2\u00f8\u0003x<\u0000\u00f3\u00f8"+
		"\u0003\u0080@\u0000\u00f4\u00f8\u0003\u00b4Z\u0000\u00f5\u00f8\u0003\u00b6"+
		"[\u0000\u00f6\u00f8\u0003\u0012\t\u0000\u00f7\u00f0\u0001\u0000\u0000"+
		"\u0000\u00f7\u00f1\u0001\u0000\u0000\u0000\u00f7\u00f2\u0001\u0000\u0000"+
		"\u0000\u00f7\u00f3\u0001\u0000\u0000\u0000\u00f7\u00f4\u0001\u0000\u0000"+
		"\u0000\u00f7\u00f5\u0001\u0000\u0000\u0000\u00f7\u00f6\u0001\u0000\u0000"+
		"\u0000\u00f8\u0011\u0001\u0000\u0000\u0000\u00f9\u00fe\u0003\u0014\n\u0000"+
		"\u00fa\u00fb\u0005\u0016\u0000\u0000\u00fb\u00fd\u0003\u0014\n\u0000\u00fc"+
		"\u00fa\u0001\u0000\u0000\u0000\u00fd\u0100\u0001\u0000\u0000\u0000\u00fe"+
		"\u00fc\u0001\u0000\u0000\u0000\u00fe\u00ff\u0001\u0000\u0000\u0000\u00ff"+
		"\u0013\u0001\u0000\u0000\u0000\u0100\u00fe\u0001\u0000\u0000\u0000\u0101"+
		"\u0106\u0003\u0016\u000b\u0000\u0102\u0103\u0005\u0015\u0000\u0000\u0103"+
		"\u0105\u0003\u0016\u000b\u0000\u0104\u0102\u0001\u0000\u0000\u0000\u0105"+
		"\u0108\u0001\u0000\u0000\u0000\u0106\u0104\u0001\u0000\u0000\u0000\u0106"+
		"\u0107\u0001\u0000\u0000\u0000\u0107\u0015\u0001\u0000\u0000\u0000\u0108"+
		"\u0106\u0001\u0000\u0000\u0000\u0109\u010c\u0003\u001a\r\u0000\u010a\u010b"+
		"\u0005:\u0000\u0000\u010b\u010d\u0003\u0018\f\u0000\u010c\u010a\u0001"+
		"\u0000\u0000\u0000\u010c\u010d\u0001\u0000\u0000\u0000\u010d\u0017\u0001"+
		"\u0000\u0000\u0000\u010e\u0110\u0005\u0011\u0000\u0000\u010f\u010e\u0001"+
		"\u0000\u0000\u0000\u010f\u0110\u0001\u0000\u0000\u0000\u0110\u0111\u0001"+
		"\u0000\u0000\u0000\u0111\u0112\u0003\u008eG\u0000\u0112\u0019\u0001\u0000"+
		"\u0000\u0000\u0113\u0118\u0003\u001c\u000e\u0000\u0114\u0115\u00052\u0000"+
		"\u0000\u0115\u0117\u0003\u0018\f\u0000\u0116\u0114\u0001\u0000\u0000\u0000"+
		"\u0117\u011a\u0001\u0000\u0000\u0000\u0118\u0116\u0001\u0000\u0000\u0000"+
		"\u0118\u0119\u0001\u0000\u0000\u0000\u0119\u001b\u0001\u0000\u0000\u0000"+
		"\u011a\u0118\u0001\u0000\u0000\u0000\u011b\u0120\u0003\u001e\u000f\u0000"+
		"\u011c\u011d\u0007\u0000\u0000\u0000\u011d\u011f\u0003\u001e\u000f\u0000"+
		"\u011e\u011c\u0001\u0000\u0000\u0000\u011f\u0122\u0001\u0000\u0000\u0000"+
		"\u0120\u011e\u0001\u0000\u0000\u0000\u0120\u0121\u0001\u0000\u0000\u0000"+
		"\u0121\u001d\u0001\u0000\u0000\u0000\u0122\u0120\u0001\u0000\u0000\u0000"+
		"\u0123\u0128\u0003 \u0010\u0000\u0124\u0125\u0007\u0001\u0000\u0000\u0125"+
		"\u0127\u0003 \u0010\u0000\u0126\u0124\u0001\u0000\u0000\u0000\u0127\u012a"+
		"\u0001\u0000\u0000\u0000\u0128\u0126\u0001\u0000\u0000\u0000\u0128\u0129"+
		"\u0001\u0000\u0000\u0000\u0129\u001f\u0001\u0000\u0000\u0000\u012a\u0128"+
		"\u0001\u0000\u0000\u0000\u012b\u0130\u0003\"\u0011\u0000\u012c\u012d\u0007"+
		"\u0002\u0000\u0000\u012d\u012f\u0003\"\u0011\u0000\u012e\u012c\u0001\u0000"+
		"\u0000\u0000\u012f\u0132\u0001\u0000\u0000\u0000\u0130\u012e\u0001\u0000"+
		"\u0000\u0000\u0130\u0131\u0001\u0000\u0000\u0000\u0131!\u0001\u0000\u0000"+
		"\u0000\u0132\u0130\u0001\u0000\u0000\u0000\u0133\u0138\u0003$\u0012\u0000"+
		"\u0134\u0135\u0007\u0003\u0000\u0000\u0135\u0137\u0003$\u0012\u0000\u0136"+
		"\u0134\u0001\u0000\u0000\u0000\u0137\u013a\u0001\u0000\u0000\u0000\u0138"+
		"\u0136\u0001\u0000\u0000\u0000\u0138\u0139\u0001\u0000\u0000\u0000\u0139"+
		"#\u0001\u0000\u0000\u0000\u013a\u0138\u0001\u0000\u0000\u0000\u013b\u0140"+
		"\u0003&\u0013\u0000\u013c\u013d\u00059\u0000\u0000\u013d\u013f\u0003&"+
		"\u0013\u0000\u013e\u013c\u0001\u0000\u0000\u0000\u013f\u0142\u0001\u0000"+
		"\u0000\u0000\u0140\u013e\u0001\u0000\u0000\u0000\u0140\u0141\u0001\u0000"+
		"\u0000\u0000\u0141%\u0001\u0000\u0000\u0000\u0142\u0140\u0001\u0000\u0000"+
		"\u0000\u0143\u0144\u00057\u0000\u0000\u0144\u014b\u0003&\u0013\u0000\u0145"+
		"\u0146\u00058\u0000\u0000\u0146\u014b\u0003&\u0013\u0000\u0147\u0148\u0005"+
		"6\u0000\u0000\u0148\u014b\u0003&\u0013\u0000\u0149\u014b\u0003\u0088D"+
		"\u0000\u014a\u0143\u0001\u0000\u0000\u0000\u014a\u0145\u0001\u0000\u0000"+
		"\u0000\u014a\u0147\u0001\u0000\u0000\u0000\u014a\u0149\u0001\u0000\u0000"+
		"\u0000\u014b\'\u0001\u0000\u0000\u0000\u014c\u015d\u0003*\u0015\u0000"+
		"\u014d\u015c\u0003N\'\u0000\u014e\u015c\u0003V+\u0000\u014f\u015c\u0003"+
		"X,\u0000\u0150\u0151\u0005\n\u0000\u0000\u0151\u0152\u0003L&\u0000\u0152"+
		"\u0154\u0005\u000b\u0000\u0000\u0153\u0155\u0005\u000e\u0000\u0000\u0154"+
		"\u0153\u0001\u0000\u0000\u0000\u0154\u0155\u0001\u0000\u0000\u0000\u0155"+
		"\u015c\u0001\u0000\u0000\u0000\u0156\u0158\u0005\f\u0000\u0000\u0157\u0159"+
		"\u0003<\u001e\u0000\u0158\u0157\u0001\u0000\u0000\u0000\u0158\u0159\u0001"+
		"\u0000\u0000\u0000\u0159\u015a\u0001\u0000\u0000\u0000\u015a\u015c\u0005"+
		"\r\u0000\u0000\u015b\u014d\u0001\u0000\u0000\u0000\u015b\u014e\u0001\u0000"+
		"\u0000\u0000\u015b\u014f\u0001\u0000\u0000\u0000\u015b\u0150\u0001\u0000"+
		"\u0000\u0000\u015b\u0156\u0001\u0000\u0000\u0000\u015c\u015f\u0001\u0000"+
		"\u0000\u0000\u015d\u015b\u0001\u0000\u0000\u0000\u015d\u015e\u0001\u0000"+
		"\u0000\u0000\u015e\u0164\u0001\u0000\u0000\u0000\u015f\u015d\u0001\u0000"+
		"\u0000\u0000\u0160\u0164\u0003T*\u0000\u0161\u0164\u0003\\.\u0000\u0162"+
		"\u0164\u0003:\u001d\u0000\u0163\u014c\u0001\u0000\u0000\u0000\u0163\u0160"+
		"\u0001\u0000\u0000\u0000\u0163\u0161\u0001\u0000\u0000\u0000\u0163\u0162"+
		"\u0001\u0000\u0000\u0000\u0164)\u0001\u0000\u0000\u0000\u0165\u016c\u0003"+
		",\u0016\u0000\u0166\u016c\u0003>\u001f\u0000\u0167\u016c\u0003D\"\u0000"+
		"\u0168\u016c\u0003.\u0017\u0000\u0169\u016c\u00036\u001b\u0000\u016a\u016c"+
		"\u00038\u001c\u0000\u016b\u0165\u0001\u0000\u0000\u0000\u016b\u0166\u0001"+
		"\u0000\u0000\u0000\u016b\u0167\u0001\u0000\u0000\u0000\u016b\u0168\u0001"+
		"\u0000\u0000\u0000\u016b\u0169\u0001\u0000\u0000\u0000\u016b\u016a\u0001"+
		"\u0000\u0000\u0000\u016c+\u0001\u0000\u0000\u0000\u016d\u016e\u0005C\u0000"+
		"\u0000\u016e-\u0001\u0000\u0000\u0000\u016f\u0170\u00030\u0018\u0000\u0170"+
		"/\u0001\u0000\u0000\u0000\u0171\u0174\u00032\u0019\u0000\u0172\u0174\u0003"+
		"4\u001a\u0000\u0173\u0171\u0001\u0000\u0000\u0000\u0173\u0172\u0001\u0000"+
		"\u0000\u0000\u01741\u0001\u0000\u0000\u0000\u0175\u0176\u0005E\u0000\u0000"+
		"\u01763\u0001\u0000\u0000\u0000\u0177\u0178\u00051\u0000\u0000\u0178\u0179"+
		"\u0005E\u0000\u0000\u01795\u0001\u0000\u0000\u0000\u017a\u017b\u0005E"+
		"\u0000\u0000\u017b\u017c\u00055\u0000\u0000\u017c\u017d\u0005E\u0000\u0000"+
		"\u017d7\u0001\u0000\u0000\u0000\u017e\u017f\u0005\f\u0000\u0000\u017f"+
		"\u0180\u0003\u0010\b\u0000\u0180\u0181\u0005\r\u0000\u0000\u01819\u0001"+
		"\u0000\u0000\u0000\u0182\u0183\u0005\u001b\u0000\u0000\u0183;\u0001\u0000"+
		"\u0000\u0000\u0184\u018a\u0003\u0010\b\u0000\u0185\u0186\u0003\u0010\b"+
		"\u0000\u0186\u0187\u0005\u0007\u0000\u0000\u0187\u0188\u0003<\u001e\u0000"+
		"\u0188\u018a\u0001\u0000\u0000\u0000\u0189\u0184\u0001\u0000\u0000\u0000"+
		"\u0189\u0185\u0001\u0000\u0000\u0000\u018a=\u0001\u0000\u0000\u0000\u018b"+
		"\u018d\u0005\n\u0000\u0000\u018c\u018e\u0003@ \u0000\u018d\u018c\u0001"+
		"\u0000\u0000\u0000\u018d\u018e\u0001\u0000\u0000\u0000\u018e\u018f\u0001"+
		"\u0000\u0000\u0000\u018f\u0190\u0005\u000b\u0000\u0000\u0190?\u0001\u0000"+
		"\u0000\u0000\u0191\u0197\u0003B!\u0000\u0192\u0193\u0003B!\u0000\u0193"+
		"\u0194\u0005\u0007\u0000\u0000\u0194\u0195\u0003@ \u0000\u0195\u0197\u0001"+
		"\u0000\u0000\u0000\u0196\u0191\u0001\u0000\u0000\u0000\u0196\u0192\u0001"+
		"\u0000\u0000\u0000\u0197A\u0001\u0000\u0000\u0000\u0198\u019e\u0003\u0010"+
		"\b\u0000\u0199\u019a\u0003\u0010\b\u0000\u019a\u019b\u00054\u0000\u0000"+
		"\u019b\u019c\u0003\u0010\b\u0000\u019c\u019e\u0001\u0000\u0000\u0000\u019d"+
		"\u0198\u0001\u0000\u0000\u0000\u019d\u0199\u0001\u0000\u0000\u0000\u019e"+
		"C\u0001\u0000\u0000\u0000\u019f\u01a1\u0005\b\u0000\u0000\u01a0\u01a2"+
		"\u0003F#\u0000\u01a1\u01a0\u0001\u0000\u0000\u0000\u01a1\u01a2\u0001\u0000"+
		"\u0000\u0000\u01a2\u01a3\u0001\u0000\u0000\u0000\u01a3\u01a4\u0005\t\u0000"+
		"\u0000\u01a4E\u0001\u0000\u0000\u0000\u01a5\u01ab\u0003H$\u0000\u01a6"+
		"\u01a7\u0003H$\u0000\u01a7\u01a8\u0005\u0007\u0000\u0000\u01a8\u01a9\u0003"+
		"F#\u0000\u01a9\u01ab\u0001\u0000\u0000\u0000\u01aa\u01a5\u0001\u0000\u0000"+
		"\u0000\u01aa\u01a6\u0001\u0000\u0000\u0000\u01abG\u0001\u0000\u0000\u0000"+
		"\u01ac\u01ad\u0003J%\u0000\u01ad\u01ae\u0005\u0006\u0000\u0000\u01ae\u01af"+
		"\u0003\u0010\b\u0000\u01afI\u0001\u0000\u0000\u0000\u01b0\u01b1\u0005"+
		"E\u0000\u0000\u01b1K\u0001\u0000\u0000\u0000\u01b2\u01b3\u0003\u0010\b"+
		"\u0000\u01b3M\u0001\u0000\u0000\u0000\u01b4\u01b7\u0003P(\u0000\u01b5"+
		"\u01b7\u0003R)\u0000\u01b6\u01b4\u0001\u0000\u0000\u0000\u01b6\u01b5\u0001"+
		"\u0000\u0000\u0000\u01b7O\u0001\u0000\u0000\u0000\u01b8\u01b9\u0005\b"+
		"\u0000\u0000\u01b9\u01ba\u0003J%\u0000\u01ba\u01bb\u0005\t\u0000\u0000"+
		"\u01bbQ\u0001\u0000\u0000\u0000\u01bc\u01bd\u0005\b\u0000\u0000\u01bd"+
		"\u01be\u0003J%\u0000\u01be\u01bf\u0005\t\u0000\u0000\u01bf\u01c0\u0005"+
		"\u000e\u0000\u0000\u01c0S\u0001\u0000\u0000\u0000\u01c1\u01c2\u0003N\'"+
		"\u0000\u01c2U\u0001\u0000\u0000\u0000\u01c3\u01c4\u0005\b\u0000\u0000"+
		"\u01c4\u01c5\u0003Z-\u0000\u01c5\u01c6\u0005\t\u0000\u0000\u01c6W\u0001"+
		"\u0000\u0000\u0000\u01c7\u01c8\u0005\b\u0000\u0000\u01c8\u01c9\u0003Z"+
		"-\u0000\u01c9\u01ca\u0005\t\u0000\u0000\u01ca\u01cb\u0005\u000e\u0000"+
		"\u0000\u01cbY\u0001\u0000\u0000\u0000\u01cc\u01d2\u0003P(\u0000\u01cd"+
		"\u01ce\u0003P(\u0000\u01ce\u01cf\u0005\u0007\u0000\u0000\u01cf\u01d0\u0003"+
		"Z-\u0000\u01d0\u01d2\u0001\u0000\u0000\u0000\u01d1\u01cc\u0001\u0000\u0000"+
		"\u0000\u01d1\u01cd\u0001\u0000\u0000\u0000\u01d2[\u0001\u0000\u0000\u0000"+
		"\u01d3\u01d6\u0003V+\u0000\u01d4\u01d6\u0003X,\u0000\u01d5\u01d3\u0001"+
		"\u0000\u0000\u0000\u01d5\u01d4\u0001\u0000\u0000\u0000\u01d6]\u0001\u0000"+
		"\u0000\u0000\u01d7\u01d9\u0005\f\u0000\u0000\u01d8\u01da\u0003b1\u0000"+
		"\u01d9\u01d8\u0001\u0000\u0000\u0000\u01d9\u01da\u0001\u0000\u0000\u0000"+
		"\u01da\u01db\u0001\u0000\u0000\u0000\u01db\u01dd\u0005\r\u0000\u0000\u01dc"+
		"\u01de\u0003l6\u0000\u01dd\u01dc\u0001\u0000\u0000\u0000\u01dd\u01de\u0001"+
		"\u0000\u0000\u0000\u01de\u01df\u0001\u0000\u0000\u0000\u01df\u01e0\u0005"+
		"3\u0000\u0000\u01e0\u01e1\u0003`0\u0000\u01e1_\u0001\u0000\u0000\u0000"+
		"\u01e2\u01e3\u0003\u0010\b\u0000\u01e3a\u0001\u0000\u0000\u0000\u01e4"+
		"\u01ea\u0003d2\u0000\u01e5\u01e6\u0003d2\u0000\u01e6\u01e7\u0005\u0007"+
		"\u0000\u0000\u01e7\u01e8\u0003p8\u0000\u01e8\u01ea\u0001\u0000\u0000\u0000"+
		"\u01e9\u01e4\u0001\u0000\u0000\u0000\u01e9\u01e5\u0001\u0000\u0000\u0000"+
		"\u01eac\u0001\u0000\u0000\u0000\u01eb\u01f1\u0003f3\u0000\u01ec\u01ed"+
		"\u0003f3\u0000\u01ed\u01ee\u0005\u0007\u0000\u0000\u01ee\u01ef\u0003d"+
		"2\u0000\u01ef\u01f1\u0001\u0000\u0000\u0000\u01f0\u01eb\u0001\u0000\u0000"+
		"\u0000\u01f0\u01ec\u0001\u0000\u0000\u0000\u01f1e\u0001\u0000\u0000\u0000"+
		"\u01f2\u01f4\u0003h4\u0000\u01f3\u01f5\u0003j5\u0000\u01f4\u01f3\u0001"+
		"\u0000\u0000\u0000\u01f4\u01f5\u0001\u0000\u0000\u0000\u01f5g\u0001\u0000"+
		"\u0000\u0000\u01f6\u01f7\u0005E\u0000\u0000\u01f7i\u0001\u0000\u0000\u0000"+
		"\u01f8\u01f9\u0003n7\u0000\u01f9k\u0001\u0000\u0000\u0000\u01fa\u01fb"+
		"\u0003n7\u0000\u01fbm\u0001\u0000\u0000\u0000\u01fc\u01fd\u00052\u0000"+
		"\u0000\u01fd\u01fe\u0003\u0018\f\u0000\u01feo\u0001\u0000\u0000\u0000"+
		"\u01ff\u0205\u0003r9\u0000\u0200\u0201\u0003r9\u0000\u0201\u0202\u0005"+
		"\u0007\u0000\u0000\u0202\u0203\u0003p8\u0000\u0203\u0205\u0001\u0000\u0000"+
		"\u0000\u0204\u01ff\u0001\u0000\u0000\u0000\u0204\u0200\u0001\u0000\u0000"+
		"\u0000\u0205q\u0001\u0000\u0000\u0000\u0206\u0207\u0005\u000f\u0000\u0000"+
		"\u0207\u0208\u0003f3\u0000\u0208s\u0001\u0000\u0000\u0000\u0209\u020a"+
		"\u0005\u001d\u0000\u0000\u020a\u020b\u0003v;\u0000\u020bu\u0001\u0000"+
		"\u0000\u0000\u020c\u020d\u0003`0\u0000\u020dw\u0001\u0000\u0000\u0000"+
		"\u020e\u020f\u0005\u001e\u0000\u0000\u020f\u0210\u0003z=\u0000\u0210\u0211"+
		"\u0005\u001f\u0000\u0000\u0211\u0212\u0003\u0010\b\u0000\u0212y\u0001"+
		"\u0000\u0000\u0000\u0213\u0219\u0003|>\u0000\u0214\u0215\u0003|>\u0000"+
		"\u0215\u0216\u0005\u0007\u0000\u0000\u0216\u0217\u0003z=\u0000\u0217\u0219"+
		"\u0001\u0000\u0000\u0000\u0218\u0213\u0001\u0000\u0000\u0000\u0218\u0214"+
		"\u0001\u0000\u0000\u0000\u0219{\u0001\u0000\u0000\u0000\u021a\u021b\u0003"+
		"~?\u0000\u021b\u021c\u0005\u0006\u0000\u0000\u021c\u021d\u0003\u0010\b"+
		"\u0000\u021d}\u0001\u0000\u0000\u0000\u021e\u021f\u0005E\u0000\u0000\u021f"+
		"\u007f\u0001\u0000\u0000\u0000\u0220\u0221\u0005 \u0000\u0000\u0221\u0222"+
		"\u0003\u0082A\u0000\u0222\u0223\u0005!\u0000\u0000\u0223\u0224\u0003\u0084"+
		"B\u0000\u0224\u0225\u0005\"\u0000\u0000\u0225\u0226\u0003\u0086C\u0000"+
		"\u0226\u0081\u0001\u0000\u0000\u0000\u0227\u0228\u0003\u0010\b\u0000\u0228"+
		"\u0083\u0001\u0000\u0000\u0000\u0229\u022a\u0003\u0010\b\u0000\u022a\u0085"+
		"\u0001\u0000\u0000\u0000\u022b\u022c\u0003\u0010\b\u0000\u022c\u0087\u0001"+
		"\u0000\u0000\u0000\u022d\u0231\u0003(\u0014\u0000\u022e\u022f\u0005\u001c"+
		"\u0000\u0000\u022f\u0231\u0003\u008cF\u0000\u0230\u022d\u0001\u0000\u0000"+
		"\u0000\u0230\u022e\u0001\u0000\u0000\u0000\u0231\u0089\u0001\u0000\u0000"+
		"\u0000\u0232\u0235\u00038\u001c\u0000\u0233\u0235\u0003\u008cF\u0000\u0234"+
		"\u0232\u0001\u0000\u0000\u0000\u0234\u0233\u0001\u0000\u0000\u0000\u0235"+
		"\u008b\u0001\u0000\u0000\u0000\u0236\u023d\u0003\u008eG\u0000\u0237\u023d"+
		"\u0003\u0090H\u0000\u0238\u023d\u0003\u009cN\u0000\u0239\u023d\u0003\u00a0"+
		"P\u0000\u023a\u023d\u0003\u00aeW\u0000\u023b\u023d\u0003\u00b2Y\u0000"+
		"\u023c\u0236\u0001\u0000\u0000\u0000\u023c\u0237\u0001\u0000\u0000\u0000"+
		"\u023c\u0238\u0001\u0000\u0000\u0000\u023c\u0239\u0001\u0000\u0000\u0000"+
		"\u023c\u023a\u0001\u0000\u0000\u0000\u023c\u023b\u0001\u0000\u0000\u0000"+
		"\u023d\u008d\u0001\u0000\u0000\u0000\u023e\u023f\u0007\u0004\u0000\u0000"+
		"\u023f\u008f\u0001\u0000\u0000\u0000\u0240\u0241\u0005\b\u0000\u0000\u0241"+
		"\u0242\u0003\u009aM\u0000\u0242\u0243\u0005\t\u0000\u0000\u0243\u0250"+
		"\u0001\u0000\u0000\u0000\u0244\u0246\u0005\b\u0000\u0000\u0245\u0247\u0003"+
		"\u0092I\u0000\u0246\u0245\u0001\u0000\u0000\u0000\u0246\u0247\u0001\u0000"+
		"\u0000\u0000\u0247\u0248\u0001\u0000\u0000\u0000\u0248\u0250\u0005\t\u0000"+
		"\u0000\u0249\u024a\u0005\b\u0000\u0000\u024a\u024b\u0003\u0092I\u0000"+
		"\u024b\u024c\u0005\u0007\u0000\u0000\u024c\u024d\u0003\u009aM\u0000\u024d"+
		"\u024e\u0005\t\u0000\u0000\u024e\u0250\u0001\u0000\u0000\u0000\u024f\u0240"+
		"\u0001\u0000\u0000\u0000\u024f\u0244\u0001\u0000\u0000\u0000\u024f\u0249"+
		"\u0001\u0000\u0000\u0000\u0250\u0091\u0001\u0000\u0000\u0000\u0251\u0257"+
		"\u0003\u0094J\u0000\u0252\u0253\u0003\u0094J\u0000\u0253\u0254\u0005\u0007"+
		"\u0000\u0000\u0254\u0255\u0003\u0092I\u0000\u0255\u0257\u0001\u0000\u0000"+
		"\u0000\u0256\u0251\u0001\u0000\u0000\u0000\u0256\u0252\u0001\u0000\u0000"+
		"\u0000\u0257\u0093\u0001\u0000\u0000\u0000\u0258\u025a\u0005\u000f\u0000"+
		"\u0000\u0259\u0258\u0001\u0000\u0000\u0000\u0259\u025a\u0001\u0000\u0000"+
		"\u0000\u025a\u025b\u0001\u0000\u0000\u0000\u025b\u025d\u0003J%\u0000\u025c"+
		"\u025e\u0003\u0096K\u0000\u025d\u025c\u0001\u0000\u0000\u0000\u025d\u025e"+
		"\u0001\u0000\u0000\u0000\u025e\u0095\u0001\u0000\u0000\u0000\u025f\u0260"+
		"\u0005\u0006\u0000\u0000\u0260\u0261\u0003\u0098L\u0000\u0261\u0097\u0001"+
		"\u0000\u0000\u0000\u0262\u0263\u0003\u008aE\u0000\u0263\u0099\u0001\u0000"+
		"\u0000\u0000\u0264\u0265\u0005\u001b\u0000\u0000\u0265\u009b\u0001\u0000"+
		"\u0000\u0000\u0266\u0267\u0005\n\u0000\u0000\u0267\u0268\u0003\u009eO"+
		"\u0000\u0268\u0269\u0005\u000b\u0000\u0000\u0269\u009d\u0001\u0000\u0000"+
		"\u0000\u026a\u026b\u0003\u008aE\u0000\u026b\u009f\u0001\u0000\u0000\u0000"+
		"\u026c\u026e\u0005\u001a\u0000\u0000\u026d\u026f\u0003\u00a2Q\u0000\u026e"+
		"\u026d\u0001\u0000\u0000\u0000\u026e\u026f\u0001\u0000\u0000\u0000\u026f"+
		"\u0270\u0001\u0000\u0000\u0000\u0270\u0271\u0005\r\u0000\u0000\u0271\u0272"+
		"\u0003l6\u0000\u0272\u00a1\u0001\u0000\u0000\u0000\u0273\u027a\u0003\u00a4"+
		"R\u0000\u0274\u0275\u0003\u00a4R\u0000\u0275\u0276\u0005\u0007\u0000\u0000"+
		"\u0276\u0277\u0003\u00a8T\u0000\u0277\u027a\u0001\u0000\u0000\u0000\u0278"+
		"\u027a\u0003\u00a8T\u0000\u0279\u0273\u0001\u0000\u0000\u0000\u0279\u0274"+
		"\u0001\u0000\u0000\u0000\u0279\u0278\u0001\u0000\u0000\u0000\u027a\u00a3"+
		"\u0001\u0000\u0000\u0000\u027b\u0281\u0003\u00a6S\u0000\u027c\u027d\u0003"+
		"\u00a6S\u0000\u027d\u027e\u0005\u0007\u0000\u0000\u027e\u027f\u0003\u00a4"+
		"R\u0000\u027f\u0281\u0001\u0000\u0000\u0000\u0280\u027b\u0001\u0000\u0000"+
		"\u0000\u0280\u027c\u0001\u0000\u0000\u0000\u0281\u00a5\u0001\u0000\u0000"+
		"\u0000\u0282\u0283\u0003\u00acV\u0000\u0283\u00a7\u0001\u0000\u0000\u0000"+
		"\u0284\u028a\u0003\u00aaU\u0000\u0285\u0286\u0003\u00aaU\u0000\u0286\u0287"+
		"\u0005\u0007\u0000\u0000\u0287\u0288\u0003\u00a8T\u0000\u0288\u028a\u0001"+
		"\u0000\u0000\u0000\u0289\u0284\u0001\u0000\u0000\u0000\u0289\u0285\u0001"+
		"\u0000\u0000\u0000\u028a\u00a9\u0001\u0000\u0000\u0000\u028b\u028c\u0005"+
		"\u000f\u0000\u0000\u028c\u028d\u0003\u00acV\u0000\u028d\u00ab\u0001\u0000"+
		"\u0000\u0000\u028e\u028f\u0003h4\u0000\u028f\u0290\u0003j5\u0000\u0290"+
		"\u00ad\u0001\u0000\u0000\u0000\u0291\u0292\u0005\u0010\u0000\u0000\u0292"+
		"\u0293\u0003\u00b0X\u0000\u0293\u00af\u0001\u0000\u0000\u0000\u0294\u0295"+
		"\u0005\b\u0000\u0000\u0295\u0296\u0003\u0092I\u0000\u0296\u0297\u0005"+
		"\t\u0000\u0000\u0297\u00b1\u0001\u0000\u0000\u0000\u0298\u0299\u0005\u0011"+
		"\u0000\u0000\u0299\u029a\u0003\u008aE\u0000\u029a\u00b3\u0001\u0000\u0000"+
		"\u0000\u029b\u029c\u0005\u0019\u0000\u0000\u029c\u029d\u0003\u0010\b\u0000"+
		"\u029d\u00b5\u0001\u0000\u0000\u0000\u029e\u029f\u0005\u0018\u0000\u0000"+
		"\u029f\u02a1\u0003\u00b8\\\u0000\u02a0\u02a2\u0003\u00ba]\u0000\u02a1"+
		"\u02a0\u0001\u0000\u0000\u0000\u02a1\u02a2\u0001\u0000\u0000\u0000\u02a2"+
		"\u00b7\u0001\u0000\u0000\u0000\u02a3\u02a4\u0003\u0010\b\u0000\u02a4\u00b9"+
		"\u0001\u0000\u0000\u0000\u02a5\u02a6\u0005\u0017\u0000\u0000\u02a6\u02a7"+
		"\u0003\u00bc^\u0000\u02a7\u00bb\u0001\u0000\u0000\u0000\u02a8\u02a9\u0003"+
		"\u0010\b\u0000\u02a9\u00bd\u0001\u0000\u0000\u0000\u02aa\u02ab\u0003\u00c0"+
		"`\u0000\u02ab\u00bf\u0001\u0000\u0000\u0000\u02ac\u02ae\u0005\b\u0000"+
		"\u0000\u02ad\u02af\u0003\u00c2a\u0000\u02ae\u02ad\u0001\u0000\u0000\u0000"+
		"\u02ae\u02af\u0001\u0000\u0000\u0000\u02af\u02b0\u0001\u0000\u0000\u0000"+
		"\u02b0\u02b1\u0005\t\u0000\u0000\u02b1\u00c1\u0001\u0000\u0000\u0000\u02b2"+
		"\u02b8\u0003\u00c4b\u0000\u02b3\u02b4\u0003\u00c4b\u0000\u02b4\u02b5\u0005"+
		"\u0007\u0000\u0000\u02b5\u02b6\u0003\u00c2a\u0000\u02b6\u02b8\u0001\u0000"+
		"\u0000\u0000\u02b7\u02b2\u0001\u0000\u0000\u0000\u02b7\u02b3\u0001\u0000"+
		"\u0000\u0000\u02b8\u00c3\u0001\u0000\u0000\u0000\u02b9\u02ba\u0003J%\u0000"+
		"\u02ba\u02bb\u0005\u0006\u0000\u0000\u02bb\u02bc\u0003\u00cae\u0000\u02bc"+
		"\u00c5\u0001\u0000\u0000\u0000\u02bd\u02bf\u0005\n\u0000\u0000\u02be\u02c0"+
		"\u0003\u00c8d\u0000\u02bf\u02be\u0001\u0000\u0000\u0000\u02bf\u02c0\u0001"+
		"\u0000\u0000\u0000\u02c0\u02c1\u0001\u0000\u0000\u0000\u02c1\u02c2\u0005"+
		"\u000b\u0000\u0000\u02c2\u00c7\u0001\u0000\u0000\u0000\u02c3\u02c9\u0003"+
		"\u00cae\u0000\u02c4\u02c5\u0003\u00cae\u0000\u02c5\u02c6\u0005\u0007\u0000"+
		"\u0000\u02c6\u02c7\u0003\u00c8d\u0000\u02c7\u02c9\u0001\u0000\u0000\u0000"+
		"\u02c8\u02c3\u0001\u0000\u0000\u0000\u02c8\u02c4\u0001\u0000\u0000\u0000"+
		"\u02c9\u00c9\u0001\u0000\u0000\u0000\u02ca\u02ce\u0003\u00c0`\u0000\u02cb"+
		"\u02ce\u0003\u00c6c\u0000\u02cc\u02ce\u0005C\u0000\u0000\u02cd\u02ca\u0001"+
		"\u0000\u0000\u0000\u02cd\u02cb\u0001\u0000\u0000\u0000\u02cd\u02cc\u0001"+
		"\u0000\u0000\u0000\u02ce\u00cb\u0001\u0000\u0000\u0000;\u00ce\u00d3\u00d9"+
		"\u00df\u00e2\u00e5\u00f7\u00fe\u0106\u010c\u010f\u0118\u0120\u0128\u0130"+
		"\u0138\u0140\u014a\u0154\u0158\u015b\u015d\u0163\u016b\u0173\u0189\u018d"+
		"\u0196\u019d\u01a1\u01aa\u01b6\u01d1\u01d5\u01d9\u01dd\u01e9\u01f0\u01f4"+
		"\u0204\u0218\u0230\u0234\u023c\u0246\u024f\u0256\u0259\u025d\u026e\u0279"+
		"\u0280\u0289\u02a1\u02ae\u02b7\u02bf\u02c8\u02cd";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}