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
		RULE_unary_expression = 19, RULE_primary_expression = 20, RULE_literal_expression = 21, 
		RULE_identifier_expression = 22, RULE_identifier_reference = 23, RULE_exclusive_identifier_reference = 24, 
		RULE_inclusive_identifier_reference = 25, RULE_section_access_expression = 26, 
		RULE_parenthesized_expression = 27, RULE_not_implemented_expression = 28, 
		RULE_argument_list = 29, RULE_list_expression = 30, RULE_item_list = 31, 
		RULE_item = 32, RULE_record_expression = 33, RULE_field_list = 34, RULE_field = 35, 
		RULE_field_name = 36, RULE_item_selector = 37, RULE_field_selector = 38, 
		RULE_required_field_selector = 39, RULE_optional_field_selector = 40, 
		RULE_implicit_target_field_selection = 41, RULE_required_projection = 42, 
		RULE_optional_projection = 43, RULE_required_selector_list = 44, RULE_implicit_target_projection = 45, 
		RULE_function_expression = 46, RULE_function_body = 47, RULE_parameter_list = 48, 
		RULE_fixed_parameter_list = 49, RULE_parameter = 50, RULE_parameter_name = 51, 
		RULE_parameter_type = 52, RULE_return_type = 53, RULE_assertion = 54, 
		RULE_optional_parameter_list = 55, RULE_optional_parameter = 56, RULE_each_expression = 57, 
		RULE_each_expression_body = 58, RULE_let_expression = 59, RULE_variable_list = 60, 
		RULE_variable = 61, RULE_variable_name = 62, RULE_if_expression = 63, 
		RULE_if_condition = 64, RULE_true_expression = 65, RULE_false_expression = 66, 
		RULE_type_expression = 67, RULE_type_expr = 68, RULE_primary_type = 69, 
		RULE_primitive_type = 70, RULE_record_type = 71, RULE_field_specification_list = 72, 
		RULE_field_specification = 73, RULE_field_type_specification = 74, RULE_field_type = 75, 
		RULE_open_record_marker = 76, RULE_list_type = 77, RULE_item_type = 78, 
		RULE_function_type = 79, RULE_parameter_specification_list = 80, RULE_required_parameter_specification_list = 81, 
		RULE_required_parameter_specification = 82, RULE_optional_parameter_specification_list = 83, 
		RULE_optional_parameter_specification = 84, RULE_parameter_specification = 85, 
		RULE_table_type = 86, RULE_row_type = 87, RULE_nullable_type = 88, RULE_error_raising_expression = 89, 
		RULE_error_handling_expression = 90, RULE_protected_expression = 91, RULE_otherwise_clause = 92, 
		RULE_default_expression = 93, RULE_literal_attribs = 94, RULE_record_literal = 95, 
		RULE_literal_field_list = 96, RULE_literal_field = 97, RULE_list_literal = 98, 
		RULE_literal_item_list = 99, RULE_any_literal = 100;
	private static String[] makeRuleNames() {
		return new String[] {
			"document", "section_document", "section", "section_name", "section_members", 
			"section_member", "section_member_name", "expression_document", "expression", 
			"logical_or_expression", "logical_and_expression", "is_expression", "nullable_primitive_type", 
			"as_expression", "equality_expression", "relational_expression", "additive_expression", 
			"multiplicative_expression", "metadata_expression", "unary_expression", 
			"primary_expression", "literal_expression", "identifier_expression", 
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
			setState(204);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(202);
				section_document();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(203);
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
			setState(206);
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
			setState(209);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPEN_BRACKET) {
				{
				setState(208);
				literal_attribs();
				}
			}

			setState(211);
			match(SECTION);
			setState(212);
			section_name();
			setState(213);
			match(SEMICOLON);
			setState(215);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & 2305843009213698049L) != 0)) {
				{
				setState(214);
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
			setState(217);
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
			setState(219);
			section_member();
			setState(221);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & 2305843009213698049L) != 0)) {
				{
				setState(220);
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
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPEN_BRACKET) {
				{
				setState(223);
				literal_attribs();
				}
			}

			setState(227);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SHARED) {
				{
				setState(226);
				match(SHARED);
				}
			}

			setState(229);
			section_member_name();
			setState(230);
			match(EQUALS);
			setState(231);
			expression();
			setState(232);
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
			setState(234);
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
			setState(236);
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
		public Logical_or_expressionContext logical_or_expression() {
			return getRuleContext(Logical_or_expressionContext.class,0);
		}
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
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expression);
		try {
			setState(246);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(238);
				logical_or_expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(239);
				each_expression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(240);
				function_expression();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(241);
				let_expression();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(242);
				if_expression();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(243);
				let_expression();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(244);
				error_raising_expression();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(245);
				error_handling_expression();
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
		public Logical_and_expressionContext logical_and_expression() {
			return getRuleContext(Logical_and_expressionContext.class,0);
		}
		public TerminalNode OR() { return getToken(PowerQueryParser.OR, 0); }
		public Logical_or_expressionContext logical_or_expression() {
			return getRuleContext(Logical_or_expressionContext.class,0);
		}
		public Logical_or_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_or_expression; }
	}

	public final Logical_or_expressionContext logical_or_expression() throws RecognitionException {
		Logical_or_expressionContext _localctx = new Logical_or_expressionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_logical_or_expression);
		try {
			setState(253);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(248);
				logical_and_expression(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(249);
				logical_and_expression(0);
				setState(250);
				match(OR);
				setState(251);
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
	public static class Logical_and_expressionContext extends ParserRuleContext {
		public Is_expressionContext is_expression() {
			return getRuleContext(Is_expressionContext.class,0);
		}
		public Logical_and_expressionContext logical_and_expression() {
			return getRuleContext(Logical_and_expressionContext.class,0);
		}
		public TerminalNode AND() { return getToken(PowerQueryParser.AND, 0); }
		public Logical_and_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_and_expression; }
	}

	public final Logical_and_expressionContext logical_and_expression() throws RecognitionException {
		return logical_and_expression(0);
	}

	private Logical_and_expressionContext logical_and_expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Logical_and_expressionContext _localctx = new Logical_and_expressionContext(_ctx, _parentState);
		Logical_and_expressionContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_logical_and_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(256);
			is_expression(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(263);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Logical_and_expressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_logical_and_expression);
					setState(258);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(259);
					match(AND);
					setState(260);
					is_expression(0);
					}
					} 
				}
				setState(265);
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
	public static class Is_expressionContext extends ParserRuleContext {
		public As_expressionContext as_expression() {
			return getRuleContext(As_expressionContext.class,0);
		}
		public Is_expressionContext is_expression() {
			return getRuleContext(Is_expressionContext.class,0);
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
		return is_expression(0);
	}

	private Is_expressionContext is_expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Is_expressionContext _localctx = new Is_expressionContext(_ctx, _parentState);
		Is_expressionContext _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_is_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(267);
			as_expression(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(274);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Is_expressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_is_expression);
					setState(269);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(270);
					match(IS);
					setState(271);
					nullable_primitive_type();
					}
					} 
				}
				setState(276);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
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
			setState(278);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NULLABLE) {
				{
				setState(277);
				match(NULLABLE);
				}
			}

			setState(280);
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
		public As_expressionContext as_expression() {
			return getRuleContext(As_expressionContext.class,0);
		}
		public TerminalNode AS() { return getToken(PowerQueryParser.AS, 0); }
		public Nullable_primitive_typeContext nullable_primitive_type() {
			return getRuleContext(Nullable_primitive_typeContext.class,0);
		}
		public As_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_as_expression; }
	}

	public final As_expressionContext as_expression() throws RecognitionException {
		return as_expression(0);
	}

	private As_expressionContext as_expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		As_expressionContext _localctx = new As_expressionContext(_ctx, _parentState);
		As_expressionContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_as_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(283);
			equality_expression();
			}
			_ctx.stop = _input.LT(-1);
			setState(290);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new As_expressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_as_expression);
					setState(285);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(286);
					match(AS);
					setState(287);
					nullable_primitive_type();
					}
					} 
				}
				setState(292);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
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
	public static class Equality_expressionContext extends ParserRuleContext {
		public Relational_expressionContext relational_expression() {
			return getRuleContext(Relational_expressionContext.class,0);
		}
		public TerminalNode EQUALS() { return getToken(PowerQueryParser.EQUALS, 0); }
		public Equality_expressionContext equality_expression() {
			return getRuleContext(Equality_expressionContext.class,0);
		}
		public TerminalNode NEQ() { return getToken(PowerQueryParser.NEQ, 0); }
		public Equality_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equality_expression; }
	}

	public final Equality_expressionContext equality_expression() throws RecognitionException {
		Equality_expressionContext _localctx = new Equality_expressionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_equality_expression);
		try {
			setState(302);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(293);
				relational_expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(294);
				relational_expression();
				setState(295);
				match(EQUALS);
				setState(296);
				equality_expression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(298);
				relational_expression();
				setState(299);
				match(NEQ);
				setState(300);
				equality_expression();
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
	public static class Relational_expressionContext extends ParserRuleContext {
		public List<Additive_expressionContext> additive_expression() {
			return getRuleContexts(Additive_expressionContext.class);
		}
		public Additive_expressionContext additive_expression(int i) {
			return getRuleContext(Additive_expressionContext.class,i);
		}
		public TerminalNode LE() { return getToken(PowerQueryParser.LE, 0); }
		public Relational_expressionContext relational_expression() {
			return getRuleContext(Relational_expressionContext.class,0);
		}
		public TerminalNode GE() { return getToken(PowerQueryParser.GE, 0); }
		public TerminalNode LEQ() { return getToken(PowerQueryParser.LEQ, 0); }
		public TerminalNode GEQ() { return getToken(PowerQueryParser.GEQ, 0); }
		public Relational_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relational_expression; }
	}

	public final Relational_expressionContext relational_expression() throws RecognitionException {
		Relational_expressionContext _localctx = new Relational_expressionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_relational_expression);
		try {
			setState(321);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(304);
				additive_expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(305);
				additive_expression();
				setState(306);
				match(LE);
				setState(307);
				relational_expression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(309);
				additive_expression();
				setState(310);
				match(GE);
				setState(311);
				relational_expression();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(313);
				additive_expression();
				setState(314);
				match(LEQ);
				setState(315);
				additive_expression();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(317);
				additive_expression();
				setState(318);
				match(GEQ);
				setState(319);
				relational_expression();
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
	public static class Additive_expressionContext extends ParserRuleContext {
		public Multiplicative_expressionContext multiplicative_expression() {
			return getRuleContext(Multiplicative_expressionContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(PowerQueryParser.PLUS, 0); }
		public Additive_expressionContext additive_expression() {
			return getRuleContext(Additive_expressionContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(PowerQueryParser.MINUS, 0); }
		public TerminalNode AMP() { return getToken(PowerQueryParser.AMP, 0); }
		public Additive_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additive_expression; }
	}

	public final Additive_expressionContext additive_expression() throws RecognitionException {
		Additive_expressionContext _localctx = new Additive_expressionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_additive_expression);
		try {
			setState(336);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(323);
				multiplicative_expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(324);
				multiplicative_expression();
				setState(325);
				match(PLUS);
				setState(326);
				additive_expression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(328);
				multiplicative_expression();
				setState(329);
				match(MINUS);
				setState(330);
				additive_expression();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(332);
				multiplicative_expression();
				setState(333);
				match(AMP);
				setState(334);
				additive_expression();
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
	public static class Multiplicative_expressionContext extends ParserRuleContext {
		public Metadata_expressionContext metadata_expression() {
			return getRuleContext(Metadata_expressionContext.class,0);
		}
		public TerminalNode STAR() { return getToken(PowerQueryParser.STAR, 0); }
		public Multiplicative_expressionContext multiplicative_expression() {
			return getRuleContext(Multiplicative_expressionContext.class,0);
		}
		public TerminalNode SLASH() { return getToken(PowerQueryParser.SLASH, 0); }
		public Multiplicative_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicative_expression; }
	}

	public final Multiplicative_expressionContext multiplicative_expression() throws RecognitionException {
		Multiplicative_expressionContext _localctx = new Multiplicative_expressionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_multiplicative_expression);
		try {
			setState(347);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(338);
				metadata_expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(339);
				metadata_expression();
				setState(340);
				match(STAR);
				setState(341);
				multiplicative_expression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(343);
				metadata_expression();
				setState(344);
				match(SLASH);
				setState(345);
				multiplicative_expression();
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
	public static class Metadata_expressionContext extends ParserRuleContext {
		public List<Unary_expressionContext> unary_expression() {
			return getRuleContexts(Unary_expressionContext.class);
		}
		public Unary_expressionContext unary_expression(int i) {
			return getRuleContext(Unary_expressionContext.class,i);
		}
		public TerminalNode META() { return getToken(PowerQueryParser.META, 0); }
		public Metadata_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_metadata_expression; }
	}

	public final Metadata_expressionContext metadata_expression() throws RecognitionException {
		Metadata_expressionContext _localctx = new Metadata_expressionContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_metadata_expression);
		try {
			setState(354);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(349);
				unary_expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(350);
				unary_expression();
				setState(351);
				match(META);
				setState(352);
				unary_expression();
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
	public static class Unary_expressionContext extends ParserRuleContext {
		public Type_expressionContext type_expression() {
			return getRuleContext(Type_expressionContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(PowerQueryParser.PLUS, 0); }
		public Unary_expressionContext unary_expression() {
			return getRuleContext(Unary_expressionContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(PowerQueryParser.MINUS, 0); }
		public TerminalNode NOT() { return getToken(PowerQueryParser.NOT, 0); }
		public Unary_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unary_expression; }
	}

	public final Unary_expressionContext unary_expression() throws RecognitionException {
		Unary_expressionContext _localctx = new Unary_expressionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_unary_expression);
		try {
			setState(363);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_BRACKET:
			case OPEN_BRACE:
			case OPEN_PAREN:
			case ELLIPSES:
			case TYPE:
			case AT:
			case LITERAL:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(356);
				type_expression();
				}
				break;
			case PLUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(357);
				match(PLUS);
				setState(358);
				unary_expression();
				}
				break;
			case MINUS:
				enterOuterAlt(_localctx, 3);
				{
				setState(359);
				match(MINUS);
				setState(360);
				unary_expression();
				}
				break;
			case NOT:
				enterOuterAlt(_localctx, 4);
				{
				setState(361);
				match(NOT);
				setState(362);
				unary_expression();
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
		public Implicit_target_field_selectionContext implicit_target_field_selection() {
			return getRuleContext(Implicit_target_field_selectionContext.class,0);
		}
		public Implicit_target_projectionContext implicit_target_projection() {
			return getRuleContext(Implicit_target_projectionContext.class,0);
		}
		public Not_implemented_expressionContext not_implemented_expression() {
			return getRuleContext(Not_implemented_expressionContext.class,0);
		}
		public Primary_expressionContext primary_expression() {
			return getRuleContext(Primary_expressionContext.class,0);
		}
		public Field_selectorContext field_selector() {
			return getRuleContext(Field_selectorContext.class,0);
		}
		public Required_projectionContext required_projection() {
			return getRuleContext(Required_projectionContext.class,0);
		}
		public Optional_projectionContext optional_projection() {
			return getRuleContext(Optional_projectionContext.class,0);
		}
		public TerminalNode OPEN_BRACE() { return getToken(PowerQueryParser.OPEN_BRACE, 0); }
		public Item_selectorContext item_selector() {
			return getRuleContext(Item_selectorContext.class,0);
		}
		public TerminalNode CLOSE_BRACE() { return getToken(PowerQueryParser.CLOSE_BRACE, 0); }
		public TerminalNode OPTIONAL() { return getToken(PowerQueryParser.OPTIONAL, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(PowerQueryParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(PowerQueryParser.CLOSE_PAREN, 0); }
		public Argument_listContext argument_list() {
			return getRuleContext(Argument_listContext.class,0);
		}
		public Primary_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary_expression; }
	}

	public final Primary_expressionContext primary_expression() throws RecognitionException {
		return primary_expression(0);
	}

	private Primary_expressionContext primary_expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Primary_expressionContext _localctx = new Primary_expressionContext(_ctx, _parentState);
		Primary_expressionContext _prevctx = _localctx;
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_primary_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(375);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(366);
				literal_expression();
				}
				break;
			case 2:
				{
				setState(367);
				list_expression();
				}
				break;
			case 3:
				{
				setState(368);
				record_expression();
				}
				break;
			case 4:
				{
				setState(369);
				identifier_expression();
				}
				break;
			case 5:
				{
				setState(370);
				section_access_expression();
				}
				break;
			case 6:
				{
				setState(371);
				parenthesized_expression();
				}
				break;
			case 7:
				{
				setState(372);
				implicit_target_field_selection();
				}
				break;
			case 8:
				{
				setState(373);
				implicit_target_projection();
				}
				break;
			case 9:
				{
				setState(374);
				not_implemented_expression();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(402);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(400);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
					case 1:
						{
						_localctx = new Primary_expressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primary_expression);
						setState(377);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(378);
						field_selector();
						}
						break;
					case 2:
						{
						_localctx = new Primary_expressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primary_expression);
						setState(379);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(380);
						required_projection();
						}
						break;
					case 3:
						{
						_localctx = new Primary_expressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primary_expression);
						setState(381);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(382);
						optional_projection();
						}
						break;
					case 4:
						{
						_localctx = new Primary_expressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primary_expression);
						setState(383);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(384);
						match(OPEN_BRACE);
						setState(385);
						item_selector();
						setState(386);
						match(CLOSE_BRACE);
						}
						break;
					case 5:
						{
						_localctx = new Primary_expressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primary_expression);
						setState(388);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(389);
						match(OPEN_BRACE);
						setState(390);
						item_selector();
						setState(391);
						match(CLOSE_BRACE);
						setState(392);
						match(OPTIONAL);
						}
						break;
					case 6:
						{
						_localctx = new Primary_expressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primary_expression);
						setState(394);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(395);
						match(OPEN_PAREN);
						setState(397);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & 2882798541774454805L) != 0)) {
							{
							setState(396);
							argument_list();
							}
						}

						setState(399);
						match(CLOSE_PAREN);
						}
						break;
					}
					} 
				}
				setState(404);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
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
	public static class Literal_expressionContext extends ParserRuleContext {
		public TerminalNode LITERAL() { return getToken(PowerQueryParser.LITERAL, 0); }
		public Literal_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal_expression; }
	}

	public final Literal_expressionContext literal_expression() throws RecognitionException {
		Literal_expressionContext _localctx = new Literal_expressionContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_literal_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(405);
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
		enterRule(_localctx, 44, RULE_identifier_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(407);
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
		enterRule(_localctx, 46, RULE_identifier_reference);
		try {
			setState(411);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(409);
				exclusive_identifier_reference();
				}
				break;
			case AT:
				enterOuterAlt(_localctx, 2);
				{
				setState(410);
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
		enterRule(_localctx, 48, RULE_exclusive_identifier_reference);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(413);
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
		enterRule(_localctx, 50, RULE_inclusive_identifier_reference);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(415);
			match(AT);
			setState(416);
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
		enterRule(_localctx, 52, RULE_section_access_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(418);
			match(IDENTIFIER);
			setState(419);
			match(BANG);
			setState(420);
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
		enterRule(_localctx, 54, RULE_parenthesized_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(422);
			match(OPEN_PAREN);
			setState(423);
			expression();
			setState(424);
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
		enterRule(_localctx, 56, RULE_not_implemented_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(426);
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
		enterRule(_localctx, 58, RULE_argument_list);
		try {
			setState(433);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(428);
				expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(429);
				expression();
				setState(430);
				match(COMMA);
				setState(431);
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
		enterRule(_localctx, 60, RULE_list_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(435);
			match(OPEN_BRACE);
			setState(437);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & 2882798541774454805L) != 0)) {
				{
				setState(436);
				item_list();
				}
			}

			setState(439);
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
		enterRule(_localctx, 62, RULE_item_list);
		try {
			setState(446);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(441);
				item();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(442);
				item();
				setState(443);
				match(COMMA);
				setState(444);
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
		enterRule(_localctx, 64, RULE_item);
		try {
			setState(453);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(448);
				expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(449);
				expression();
				setState(450);
				match(DOTDOT);
				setState(451);
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
		enterRule(_localctx, 66, RULE_record_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(455);
			match(OPEN_BRACKET);
			setState(457);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(456);
				field_list();
				}
			}

			setState(459);
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
		enterRule(_localctx, 68, RULE_field_list);
		try {
			setState(466);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(461);
				field();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(462);
				field();
				setState(463);
				match(COMMA);
				setState(464);
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
		enterRule(_localctx, 70, RULE_field);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(468);
			field_name();
			setState(469);
			match(EQUALS);
			setState(470);
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
		enterRule(_localctx, 72, RULE_field_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(472);
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
		enterRule(_localctx, 74, RULE_item_selector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(474);
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
		enterRule(_localctx, 76, RULE_field_selector);
		try {
			setState(478);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(476);
				required_field_selector();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(477);
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
		enterRule(_localctx, 78, RULE_required_field_selector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(480);
			match(OPEN_BRACKET);
			setState(481);
			field_name();
			setState(482);
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
		enterRule(_localctx, 80, RULE_optional_field_selector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(484);
			match(OPEN_BRACKET);
			setState(485);
			field_name();
			setState(486);
			match(CLOSE_BRACKET);
			setState(487);
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
		enterRule(_localctx, 82, RULE_implicit_target_field_selection);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(489);
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
		enterRule(_localctx, 84, RULE_required_projection);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(491);
			match(OPEN_BRACKET);
			setState(492);
			required_selector_list();
			setState(493);
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
		enterRule(_localctx, 86, RULE_optional_projection);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(495);
			match(OPEN_BRACKET);
			setState(496);
			required_selector_list();
			setState(497);
			match(CLOSE_BRACKET);
			setState(498);
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
		enterRule(_localctx, 88, RULE_required_selector_list);
		try {
			setState(505);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(500);
				required_field_selector();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(501);
				required_field_selector();
				setState(502);
				match(COMMA);
				setState(503);
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
		enterRule(_localctx, 90, RULE_implicit_target_projection);
		try {
			setState(509);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(507);
				required_projection();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(508);
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
		enterRule(_localctx, 92, RULE_function_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(511);
			match(OPEN_PAREN);
			setState(513);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(512);
				parameter_list();
				}
			}

			setState(515);
			match(CLOSE_PAREN);
			setState(517);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(516);
				return_type();
				}
			}

			setState(519);
			match(ARROW);
			setState(520);
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
		enterRule(_localctx, 94, RULE_function_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(522);
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
		enterRule(_localctx, 96, RULE_parameter_list);
		try {
			setState(529);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(524);
				fixed_parameter_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(525);
				fixed_parameter_list();
				setState(526);
				match(COMMA);
				setState(527);
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
		enterRule(_localctx, 98, RULE_fixed_parameter_list);
		try {
			setState(536);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(531);
				parameter();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(532);
				parameter();
				setState(533);
				match(COMMA);
				setState(534);
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
		enterRule(_localctx, 100, RULE_parameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(538);
			parameter_name();
			setState(540);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(539);
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
		enterRule(_localctx, 102, RULE_parameter_name);
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
		enterRule(_localctx, 104, RULE_parameter_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(544);
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
		enterRule(_localctx, 106, RULE_return_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(546);
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
		enterRule(_localctx, 108, RULE_assertion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(548);
			match(AS);
			setState(549);
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
		enterRule(_localctx, 110, RULE_optional_parameter_list);
		try {
			setState(556);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(551);
				optional_parameter();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(552);
				optional_parameter();
				setState(553);
				match(COMMA);
				setState(554);
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
		enterRule(_localctx, 112, RULE_optional_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(558);
			match(OPTIONAL_TEXT);
			setState(559);
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
		enterRule(_localctx, 114, RULE_each_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(561);
			match(EACH);
			setState(562);
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
		enterRule(_localctx, 116, RULE_each_expression_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(564);
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
		enterRule(_localctx, 118, RULE_let_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(566);
			match(LET);
			setState(567);
			variable_list();
			setState(568);
			match(IN);
			setState(569);
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
		enterRule(_localctx, 120, RULE_variable_list);
		try {
			setState(576);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(571);
				variable();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(572);
				variable();
				setState(573);
				match(COMMA);
				setState(574);
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
		enterRule(_localctx, 122, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(578);
			variable_name();
			setState(579);
			match(EQUALS);
			setState(580);
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
		enterRule(_localctx, 124, RULE_variable_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(582);
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
		enterRule(_localctx, 126, RULE_if_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(584);
			match(IF);
			setState(585);
			if_condition();
			setState(586);
			match(THEN);
			setState(587);
			true_expression();
			setState(588);
			match(ELSE);
			setState(589);
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
		enterRule(_localctx, 128, RULE_if_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(591);
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
		enterRule(_localctx, 130, RULE_true_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(593);
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
		enterRule(_localctx, 132, RULE_false_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(595);
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
		enterRule(_localctx, 134, RULE_type_expression);
		try {
			setState(600);
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
				setState(597);
				primary_expression(0);
				}
				break;
			case TYPE:
				enterOuterAlt(_localctx, 2);
				{
				setState(598);
				match(TYPE);
				setState(599);
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
		enterRule(_localctx, 136, RULE_type_expr);
		try {
			setState(604);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(602);
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
				setState(603);
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
		enterRule(_localctx, 138, RULE_primary_type);
		try {
			setState(612);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,41,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(606);
				primitive_type();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(607);
				record_type();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(608);
				list_type();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(609);
				function_type();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(610);
				table_type();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(611);
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
		enterRule(_localctx, 140, RULE_primitive_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(614);
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
		enterRule(_localctx, 142, RULE_record_type);
		int _la;
		try {
			setState(631);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,43,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(616);
				match(OPEN_BRACKET);
				setState(617);
				open_record_marker();
				setState(618);
				match(CLOSE_BRACKET);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(620);
				match(OPEN_BRACKET);
				setState(622);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==OPTIONAL_TEXT || _la==IDENTIFIER) {
					{
					setState(621);
					field_specification_list();
					}
				}

				setState(624);
				match(CLOSE_BRACKET);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(625);
				match(OPEN_BRACKET);
				setState(626);
				field_specification_list();
				setState(627);
				match(COMMA);
				setState(628);
				open_record_marker();
				setState(629);
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
		enterRule(_localctx, 144, RULE_field_specification_list);
		try {
			setState(638);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,44,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(633);
				field_specification();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(634);
				field_specification();
				setState(635);
				match(COMMA);
				setState(636);
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
		enterRule(_localctx, 146, RULE_field_specification);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(641);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPTIONAL_TEXT) {
				{
				setState(640);
				match(OPTIONAL_TEXT);
				}
			}

			setState(643);
			field_name();
			setState(645);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUALS) {
				{
				setState(644);
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
		enterRule(_localctx, 148, RULE_field_type_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(647);
			match(EQUALS);
			setState(648);
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
		enterRule(_localctx, 150, RULE_field_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(650);
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
		enterRule(_localctx, 152, RULE_open_record_marker);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(652);
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
		enterRule(_localctx, 154, RULE_list_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(654);
			match(OPEN_BRACE);
			setState(655);
			item_type();
			setState(656);
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
		enterRule(_localctx, 156, RULE_item_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(658);
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
		enterRule(_localctx, 158, RULE_function_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(660);
			match(FUNCTION_START);
			setState(662);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPTIONAL_TEXT || _la==IDENTIFIER) {
				{
				setState(661);
				parameter_specification_list();
				}
			}

			setState(664);
			match(CLOSE_PAREN);
			setState(665);
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
		enterRule(_localctx, 160, RULE_parameter_specification_list);
		try {
			setState(673);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,48,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(667);
				required_parameter_specification_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(668);
				required_parameter_specification_list();
				setState(669);
				match(COMMA);
				setState(670);
				optional_parameter_specification_list();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(672);
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
		enterRule(_localctx, 162, RULE_required_parameter_specification_list);
		try {
			setState(680);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,49,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(675);
				required_parameter_specification();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(676);
				required_parameter_specification();
				setState(677);
				match(COMMA);
				setState(678);
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
		enterRule(_localctx, 164, RULE_required_parameter_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(682);
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
		enterRule(_localctx, 166, RULE_optional_parameter_specification_list);
		try {
			setState(689);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,50,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(684);
				optional_parameter_specification();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(685);
				optional_parameter_specification();
				setState(686);
				match(COMMA);
				setState(687);
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
		enterRule(_localctx, 168, RULE_optional_parameter_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(691);
			match(OPTIONAL_TEXT);
			setState(692);
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
		enterRule(_localctx, 170, RULE_parameter_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(694);
			parameter_name();
			setState(695);
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
		enterRule(_localctx, 172, RULE_table_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(697);
			match(TABLE);
			setState(698);
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
		enterRule(_localctx, 174, RULE_row_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(700);
			match(OPEN_BRACKET);
			setState(701);
			field_specification_list();
			setState(702);
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
		enterRule(_localctx, 176, RULE_nullable_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(704);
			match(NULLABLE);
			setState(705);
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
		enterRule(_localctx, 178, RULE_error_raising_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(707);
			match(ERROR);
			setState(708);
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
		enterRule(_localctx, 180, RULE_error_handling_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(710);
			match(TRY);
			setState(711);
			protected_expression();
			setState(713);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,51,_ctx) ) {
			case 1:
				{
				setState(712);
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
		enterRule(_localctx, 182, RULE_protected_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(715);
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
		enterRule(_localctx, 184, RULE_otherwise_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(717);
			match(OTHERWISE);
			setState(718);
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
		enterRule(_localctx, 186, RULE_default_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(720);
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
		enterRule(_localctx, 188, RULE_literal_attribs);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(722);
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
		enterRule(_localctx, 190, RULE_record_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(724);
			match(OPEN_BRACKET);
			setState(726);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(725);
				literal_field_list();
				}
			}

			setState(728);
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
		enterRule(_localctx, 192, RULE_literal_field_list);
		try {
			setState(735);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,53,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(730);
				literal_field();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(731);
				literal_field();
				setState(732);
				match(COMMA);
				setState(733);
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
		enterRule(_localctx, 194, RULE_literal_field);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(737);
			field_name();
			setState(738);
			match(EQUALS);
			setState(739);
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
		enterRule(_localctx, 196, RULE_list_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(741);
			match(OPEN_BRACE);
			setState(743);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & 576460752303423493L) != 0)) {
				{
				setState(742);
				literal_item_list();
				}
			}

			setState(745);
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
		enterRule(_localctx, 198, RULE_literal_item_list);
		try {
			setState(752);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,55,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(747);
				any_literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(748);
				any_literal();
				setState(749);
				match(COMMA);
				setState(750);
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
		enterRule(_localctx, 200, RULE_any_literal);
		try {
			setState(757);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_BRACKET:
				enterOuterAlt(_localctx, 1);
				{
				setState(754);
				record_literal();
				}
				break;
			case OPEN_BRACE:
				enterOuterAlt(_localctx, 2);
				{
				setState(755);
				list_literal();
				}
				break;
			case LITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(756);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 10:
			return logical_and_expression_sempred((Logical_and_expressionContext)_localctx, predIndex);
		case 11:
			return is_expression_sempred((Is_expressionContext)_localctx, predIndex);
		case 13:
			return as_expression_sempred((As_expressionContext)_localctx, predIndex);
		case 20:
			return primary_expression_sempred((Primary_expressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean logical_and_expression_sempred(Logical_and_expressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean is_expression_sempred(Is_expressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean as_expression_sempred(As_expressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean primary_expression_sempred(Primary_expressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 9);
		case 4:
			return precpred(_ctx, 7);
		case 5:
			return precpred(_ctx, 6);
		case 6:
			return precpred(_ctx, 4);
		case 7:
			return precpred(_ctx, 3);
		case 8:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001H\u02f8\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"d\u0007d\u0001\u0000\u0001\u0000\u0003\u0000\u00cd\b\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0003\u0002\u00d2\b\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u0002\u00d8\b\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0003\u0004\u00de\b\u0004\u0001\u0005\u0003\u0005"+
		"\u00e1\b\u0005\u0001\u0005\u0003\u0005\u00e4\b\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0003\b\u00f7\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003"+
		"\t\u00fe\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0005\n\u0106"+
		"\b\n\n\n\f\n\u0109\t\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0005\u000b\u0111\b\u000b\n\u000b\f\u000b\u0114"+
		"\t\u000b\u0001\f\u0003\f\u0117\b\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0005\r\u0121\b\r\n\r\f\r\u0124\t\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0003\u000e\u012f\b\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u0142\b\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0003\u0010\u0151\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011"+
		"\u015c\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0003\u0012\u0163\b\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u016c\b\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u0178\b\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0003\u0014\u018e\b\u0014\u0001\u0014\u0005\u0014\u0191\b"+
		"\u0014\n\u0014\f\u0014\u0194\t\u0014\u0001\u0015\u0001\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0017\u0001\u0017\u0003\u0017\u019c\b\u0017\u0001\u0018"+
		"\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0003\u001d\u01b2\b\u001d\u0001\u001e\u0001\u001e\u0003\u001e"+
		"\u01b6\b\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f"+
		"\u0001\u001f\u0001\u001f\u0003\u001f\u01bf\b\u001f\u0001 \u0001 \u0001"+
		" \u0001 \u0001 \u0003 \u01c6\b \u0001!\u0001!\u0003!\u01ca\b!\u0001!\u0001"+
		"!\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0003\"\u01d3\b\"\u0001#\u0001"+
		"#\u0001#\u0001#\u0001$\u0001$\u0001%\u0001%\u0001&\u0001&\u0003&\u01df"+
		"\b&\u0001\'\u0001\'\u0001\'\u0001\'\u0001(\u0001(\u0001(\u0001(\u0001"+
		"(\u0001)\u0001)\u0001*\u0001*\u0001*\u0001*\u0001+\u0001+\u0001+\u0001"+
		"+\u0001+\u0001,\u0001,\u0001,\u0001,\u0001,\u0003,\u01fa\b,\u0001-\u0001"+
		"-\u0003-\u01fe\b-\u0001.\u0001.\u0003.\u0202\b.\u0001.\u0001.\u0003.\u0206"+
		"\b.\u0001.\u0001.\u0001.\u0001/\u0001/\u00010\u00010\u00010\u00010\u0001"+
		"0\u00030\u0212\b0\u00011\u00011\u00011\u00011\u00011\u00031\u0219\b1\u0001"+
		"2\u00012\u00032\u021d\b2\u00013\u00013\u00014\u00014\u00015\u00015\u0001"+
		"6\u00016\u00016\u00017\u00017\u00017\u00017\u00017\u00037\u022d\b7\u0001"+
		"8\u00018\u00018\u00019\u00019\u00019\u0001:\u0001:\u0001;\u0001;\u0001"+
		";\u0001;\u0001;\u0001<\u0001<\u0001<\u0001<\u0001<\u0003<\u0241\b<\u0001"+
		"=\u0001=\u0001=\u0001=\u0001>\u0001>\u0001?\u0001?\u0001?\u0001?\u0001"+
		"?\u0001?\u0001?\u0001@\u0001@\u0001A\u0001A\u0001B\u0001B\u0001C\u0001"+
		"C\u0001C\u0003C\u0259\bC\u0001D\u0001D\u0003D\u025d\bD\u0001E\u0001E\u0001"+
		"E\u0001E\u0001E\u0001E\u0003E\u0265\bE\u0001F\u0001F\u0001G\u0001G\u0001"+
		"G\u0001G\u0001G\u0001G\u0003G\u026f\bG\u0001G\u0001G\u0001G\u0001G\u0001"+
		"G\u0001G\u0001G\u0003G\u0278\bG\u0001H\u0001H\u0001H\u0001H\u0001H\u0003"+
		"H\u027f\bH\u0001I\u0003I\u0282\bI\u0001I\u0001I\u0003I\u0286\bI\u0001"+
		"J\u0001J\u0001J\u0001K\u0001K\u0001L\u0001L\u0001M\u0001M\u0001M\u0001"+
		"M\u0001N\u0001N\u0001O\u0001O\u0003O\u0297\bO\u0001O\u0001O\u0001O\u0001"+
		"P\u0001P\u0001P\u0001P\u0001P\u0001P\u0003P\u02a2\bP\u0001Q\u0001Q\u0001"+
		"Q\u0001Q\u0001Q\u0003Q\u02a9\bQ\u0001R\u0001R\u0001S\u0001S\u0001S\u0001"+
		"S\u0001S\u0003S\u02b2\bS\u0001T\u0001T\u0001T\u0001U\u0001U\u0001U\u0001"+
		"V\u0001V\u0001V\u0001W\u0001W\u0001W\u0001W\u0001X\u0001X\u0001X\u0001"+
		"Y\u0001Y\u0001Y\u0001Z\u0001Z\u0001Z\u0003Z\u02ca\bZ\u0001[\u0001[\u0001"+
		"\\\u0001\\\u0001\\\u0001]\u0001]\u0001^\u0001^\u0001_\u0001_\u0003_\u02d7"+
		"\b_\u0001_\u0001_\u0001`\u0001`\u0001`\u0001`\u0001`\u0003`\u02e0\b`\u0001"+
		"a\u0001a\u0001a\u0001a\u0001b\u0001b\u0003b\u02e8\bb\u0001b\u0001b\u0001"+
		"c\u0001c\u0001c\u0001c\u0001c\u0003c\u02f1\bc\u0001d\u0001d\u0001d\u0003"+
		"d\u02f6\bd\u0001d\u0000\u0004\u0014\u0016\u001a(e\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,."+
		"02468:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088"+
		"\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0"+
		"\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8"+
		"\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u0000\u0001\u0004\u0000"+
		"\u0010\u0010\u001c\u001c#0CC\u02ec\u0000\u00cc\u0001\u0000\u0000\u0000"+
		"\u0002\u00ce\u0001\u0000\u0000\u0000\u0004\u00d1\u0001\u0000\u0000\u0000"+
		"\u0006\u00d9\u0001\u0000\u0000\u0000\b\u00db\u0001\u0000\u0000\u0000\n"+
		"\u00e0\u0001\u0000\u0000\u0000\f\u00ea\u0001\u0000\u0000\u0000\u000e\u00ec"+
		"\u0001\u0000\u0000\u0000\u0010\u00f6\u0001\u0000\u0000\u0000\u0012\u00fd"+
		"\u0001\u0000\u0000\u0000\u0014\u00ff\u0001\u0000\u0000\u0000\u0016\u010a"+
		"\u0001\u0000\u0000\u0000\u0018\u0116\u0001\u0000\u0000\u0000\u001a\u011a"+
		"\u0001\u0000\u0000\u0000\u001c\u012e\u0001\u0000\u0000\u0000\u001e\u0141"+
		"\u0001\u0000\u0000\u0000 \u0150\u0001\u0000\u0000\u0000\"\u015b\u0001"+
		"\u0000\u0000\u0000$\u0162\u0001\u0000\u0000\u0000&\u016b\u0001\u0000\u0000"+
		"\u0000(\u0177\u0001\u0000\u0000\u0000*\u0195\u0001\u0000\u0000\u0000,"+
		"\u0197\u0001\u0000\u0000\u0000.\u019b\u0001\u0000\u0000\u00000\u019d\u0001"+
		"\u0000\u0000\u00002\u019f\u0001\u0000\u0000\u00004\u01a2\u0001\u0000\u0000"+
		"\u00006\u01a6\u0001\u0000\u0000\u00008\u01aa\u0001\u0000\u0000\u0000:"+
		"\u01b1\u0001\u0000\u0000\u0000<\u01b3\u0001\u0000\u0000\u0000>\u01be\u0001"+
		"\u0000\u0000\u0000@\u01c5\u0001\u0000\u0000\u0000B\u01c7\u0001\u0000\u0000"+
		"\u0000D\u01d2\u0001\u0000\u0000\u0000F\u01d4\u0001\u0000\u0000\u0000H"+
		"\u01d8\u0001\u0000\u0000\u0000J\u01da\u0001\u0000\u0000\u0000L\u01de\u0001"+
		"\u0000\u0000\u0000N\u01e0\u0001\u0000\u0000\u0000P\u01e4\u0001\u0000\u0000"+
		"\u0000R\u01e9\u0001\u0000\u0000\u0000T\u01eb\u0001\u0000\u0000\u0000V"+
		"\u01ef\u0001\u0000\u0000\u0000X\u01f9\u0001\u0000\u0000\u0000Z\u01fd\u0001"+
		"\u0000\u0000\u0000\\\u01ff\u0001\u0000\u0000\u0000^\u020a\u0001\u0000"+
		"\u0000\u0000`\u0211\u0001\u0000\u0000\u0000b\u0218\u0001\u0000\u0000\u0000"+
		"d\u021a\u0001\u0000\u0000\u0000f\u021e\u0001\u0000\u0000\u0000h\u0220"+
		"\u0001\u0000\u0000\u0000j\u0222\u0001\u0000\u0000\u0000l\u0224\u0001\u0000"+
		"\u0000\u0000n\u022c\u0001\u0000\u0000\u0000p\u022e\u0001\u0000\u0000\u0000"+
		"r\u0231\u0001\u0000\u0000\u0000t\u0234\u0001\u0000\u0000\u0000v\u0236"+
		"\u0001\u0000\u0000\u0000x\u0240\u0001\u0000\u0000\u0000z\u0242\u0001\u0000"+
		"\u0000\u0000|\u0246\u0001\u0000\u0000\u0000~\u0248\u0001\u0000\u0000\u0000"+
		"\u0080\u024f\u0001\u0000\u0000\u0000\u0082\u0251\u0001\u0000\u0000\u0000"+
		"\u0084\u0253\u0001\u0000\u0000\u0000\u0086\u0258\u0001\u0000\u0000\u0000"+
		"\u0088\u025c\u0001\u0000\u0000\u0000\u008a\u0264\u0001\u0000\u0000\u0000"+
		"\u008c\u0266\u0001\u0000\u0000\u0000\u008e\u0277\u0001\u0000\u0000\u0000"+
		"\u0090\u027e\u0001\u0000\u0000\u0000\u0092\u0281\u0001\u0000\u0000\u0000"+
		"\u0094\u0287\u0001\u0000\u0000\u0000\u0096\u028a\u0001\u0000\u0000\u0000"+
		"\u0098\u028c\u0001\u0000\u0000\u0000\u009a\u028e\u0001\u0000\u0000\u0000"+
		"\u009c\u0292\u0001\u0000\u0000\u0000\u009e\u0294\u0001\u0000\u0000\u0000"+
		"\u00a0\u02a1\u0001\u0000\u0000\u0000\u00a2\u02a8\u0001\u0000\u0000\u0000"+
		"\u00a4\u02aa\u0001\u0000\u0000\u0000\u00a6\u02b1\u0001\u0000\u0000\u0000"+
		"\u00a8\u02b3\u0001\u0000\u0000\u0000\u00aa\u02b6\u0001\u0000\u0000\u0000"+
		"\u00ac\u02b9\u0001\u0000\u0000\u0000\u00ae\u02bc\u0001\u0000\u0000\u0000"+
		"\u00b0\u02c0\u0001\u0000\u0000\u0000\u00b2\u02c3\u0001\u0000\u0000\u0000"+
		"\u00b4\u02c6\u0001\u0000\u0000\u0000\u00b6\u02cb\u0001\u0000\u0000\u0000"+
		"\u00b8\u02cd\u0001\u0000\u0000\u0000\u00ba\u02d0\u0001\u0000\u0000\u0000"+
		"\u00bc\u02d2\u0001\u0000\u0000\u0000\u00be\u02d4\u0001\u0000\u0000\u0000"+
		"\u00c0\u02df\u0001\u0000\u0000\u0000\u00c2\u02e1\u0001\u0000\u0000\u0000"+
		"\u00c4\u02e5\u0001\u0000\u0000\u0000\u00c6\u02f0\u0001\u0000\u0000\u0000"+
		"\u00c8\u02f5\u0001\u0000\u0000\u0000\u00ca\u00cd\u0003\u0002\u0001\u0000"+
		"\u00cb\u00cd\u0003\u000e\u0007\u0000\u00cc\u00ca\u0001\u0000\u0000\u0000"+
		"\u00cc\u00cb\u0001\u0000\u0000\u0000\u00cd\u0001\u0001\u0000\u0000\u0000"+
		"\u00ce\u00cf\u0003\u0004\u0002\u0000\u00cf\u0003\u0001\u0000\u0000\u0000"+
		"\u00d0\u00d2\u0003\u00bc^\u0000\u00d1\u00d0\u0001\u0000\u0000\u0000\u00d1"+
		"\u00d2\u0001\u0000\u0000\u0000\u00d2\u00d3\u0001\u0000\u0000\u0000\u00d3"+
		"\u00d4\u0005\u0013\u0000\u0000\u00d4\u00d5\u0003\u0006\u0003\u0000\u00d5"+
		"\u00d7\u0005\u0012\u0000\u0000\u00d6\u00d8\u0003\b\u0004\u0000\u00d7\u00d6"+
		"\u0001\u0000\u0000\u0000\u00d7\u00d8\u0001\u0000\u0000\u0000\u00d8\u0005"+
		"\u0001\u0000\u0000\u0000\u00d9\u00da\u0005E\u0000\u0000\u00da\u0007\u0001"+
		"\u0000\u0000\u0000\u00db\u00dd\u0003\n\u0005\u0000\u00dc\u00de\u0003\b"+
		"\u0004\u0000\u00dd\u00dc\u0001\u0000\u0000\u0000\u00dd\u00de\u0001\u0000"+
		"\u0000\u0000\u00de\t\u0001\u0000\u0000\u0000\u00df\u00e1\u0003\u00bc^"+
		"\u0000\u00e0\u00df\u0001\u0000\u0000\u0000\u00e0\u00e1\u0001\u0000\u0000"+
		"\u0000\u00e1\u00e3\u0001\u0000\u0000\u0000\u00e2\u00e4\u0005\u0014\u0000"+
		"\u0000\u00e3\u00e2\u0001\u0000\u0000\u0000\u00e3\u00e4\u0001\u0000\u0000"+
		"\u0000\u00e4\u00e5\u0001\u0000\u0000\u0000\u00e5\u00e6\u0003\f\u0006\u0000"+
		"\u00e6\u00e7\u0005\u0006\u0000\u0000\u00e7\u00e8\u0003\u0010\b\u0000\u00e8"+
		"\u00e9\u0005\u0012\u0000\u0000\u00e9\u000b\u0001\u0000\u0000\u0000\u00ea"+
		"\u00eb\u0005E\u0000\u0000\u00eb\r\u0001\u0000\u0000\u0000\u00ec\u00ed"+
		"\u0003\u0010\b\u0000\u00ed\u000f\u0001\u0000\u0000\u0000\u00ee\u00f7\u0003"+
		"\u0012\t\u0000\u00ef\u00f7\u0003r9\u0000\u00f0\u00f7\u0003\\.\u0000\u00f1"+
		"\u00f7\u0003v;\u0000\u00f2\u00f7\u0003~?\u0000\u00f3\u00f7\u0003v;\u0000"+
		"\u00f4\u00f7\u0003\u00b2Y\u0000\u00f5\u00f7\u0003\u00b4Z\u0000\u00f6\u00ee"+
		"\u0001\u0000\u0000\u0000\u00f6\u00ef\u0001\u0000\u0000\u0000\u00f6\u00f0"+
		"\u0001\u0000\u0000\u0000\u00f6\u00f1\u0001\u0000\u0000\u0000\u00f6\u00f2"+
		"\u0001\u0000\u0000\u0000\u00f6\u00f3\u0001\u0000\u0000\u0000\u00f6\u00f4"+
		"\u0001\u0000\u0000\u0000\u00f6\u00f5\u0001\u0000\u0000\u0000\u00f7\u0011"+
		"\u0001\u0000\u0000\u0000\u00f8\u00fe\u0003\u0014\n\u0000\u00f9\u00fa\u0003"+
		"\u0014\n\u0000\u00fa\u00fb\u0005\u0016\u0000\u0000\u00fb\u00fc\u0003\u0012"+
		"\t\u0000\u00fc\u00fe\u0001\u0000\u0000\u0000\u00fd\u00f8\u0001\u0000\u0000"+
		"\u0000\u00fd\u00f9\u0001\u0000\u0000\u0000\u00fe\u0013\u0001\u0000\u0000"+
		"\u0000\u00ff\u0100\u0006\n\uffff\uffff\u0000\u0100\u0101\u0003\u0016\u000b"+
		"\u0000\u0101\u0107\u0001\u0000\u0000\u0000\u0102\u0103\n\u0001\u0000\u0000"+
		"\u0103\u0104\u0005\u0015\u0000\u0000\u0104\u0106\u0003\u0016\u000b\u0000"+
		"\u0105\u0102\u0001\u0000\u0000\u0000\u0106\u0109\u0001\u0000\u0000\u0000"+
		"\u0107\u0105\u0001\u0000\u0000\u0000\u0107\u0108\u0001\u0000\u0000\u0000"+
		"\u0108\u0015\u0001\u0000\u0000\u0000\u0109\u0107\u0001\u0000\u0000\u0000"+
		"\u010a\u010b\u0006\u000b\uffff\uffff\u0000\u010b\u010c\u0003\u001a\r\u0000"+
		"\u010c\u0112\u0001\u0000\u0000\u0000\u010d\u010e\n\u0001\u0000\u0000\u010e"+
		"\u010f\u0005:\u0000\u0000\u010f\u0111\u0003\u0018\f\u0000\u0110\u010d"+
		"\u0001\u0000\u0000\u0000\u0111\u0114\u0001\u0000\u0000\u0000\u0112\u0110"+
		"\u0001\u0000\u0000\u0000\u0112\u0113\u0001\u0000\u0000\u0000\u0113\u0017"+
		"\u0001\u0000\u0000\u0000\u0114\u0112\u0001\u0000\u0000\u0000\u0115\u0117"+
		"\u0005\u0011\u0000\u0000\u0116\u0115\u0001\u0000\u0000\u0000\u0116\u0117"+
		"\u0001\u0000\u0000\u0000\u0117\u0118\u0001\u0000\u0000\u0000\u0118\u0119"+
		"\u0003\u008cF\u0000\u0119\u0019\u0001\u0000\u0000\u0000\u011a\u011b\u0006"+
		"\r\uffff\uffff\u0000\u011b\u011c\u0003\u001c\u000e\u0000\u011c\u0122\u0001"+
		"\u0000\u0000\u0000\u011d\u011e\n\u0001\u0000\u0000\u011e\u011f\u00052"+
		"\u0000\u0000\u011f\u0121\u0003\u0018\f\u0000\u0120\u011d\u0001\u0000\u0000"+
		"\u0000\u0121\u0124\u0001\u0000\u0000\u0000\u0122\u0120\u0001\u0000\u0000"+
		"\u0000\u0122\u0123\u0001\u0000\u0000\u0000\u0123\u001b\u0001\u0000\u0000"+
		"\u0000\u0124\u0122\u0001\u0000\u0000\u0000\u0125\u012f\u0003\u001e\u000f"+
		"\u0000\u0126\u0127\u0003\u001e\u000f\u0000\u0127\u0128\u0005\u0006\u0000"+
		"\u0000\u0128\u0129\u0003\u001c\u000e\u0000\u0129\u012f\u0001\u0000\u0000"+
		"\u0000\u012a\u012b\u0003\u001e\u000f\u0000\u012b\u012c\u0005;\u0000\u0000"+
		"\u012c\u012d\u0003\u001c\u000e\u0000\u012d\u012f\u0001\u0000\u0000\u0000"+
		"\u012e\u0125\u0001\u0000\u0000\u0000\u012e\u0126\u0001\u0000\u0000\u0000"+
		"\u012e\u012a\u0001\u0000\u0000\u0000\u012f\u001d\u0001\u0000\u0000\u0000"+
		"\u0130\u0142\u0003 \u0010\u0000\u0131\u0132\u0003 \u0010\u0000\u0132\u0133"+
		"\u0005=\u0000\u0000\u0133\u0134\u0003\u001e\u000f\u0000\u0134\u0142\u0001"+
		"\u0000\u0000\u0000\u0135\u0136\u0003 \u0010\u0000\u0136\u0137\u0005<\u0000"+
		"\u0000\u0137\u0138\u0003\u001e\u000f\u0000\u0138\u0142\u0001\u0000\u0000"+
		"\u0000\u0139\u013a\u0003 \u0010\u0000\u013a\u013b\u0005A\u0000\u0000\u013b"+
		"\u013c\u0003 \u0010\u0000\u013c\u0142\u0001\u0000\u0000\u0000\u013d\u013e"+
		"\u0003 \u0010\u0000\u013e\u013f\u0005B\u0000\u0000\u013f\u0140\u0003\u001e"+
		"\u000f\u0000\u0140\u0142\u0001\u0000\u0000\u0000\u0141\u0130\u0001\u0000"+
		"\u0000\u0000\u0141\u0131\u0001\u0000\u0000\u0000\u0141\u0135\u0001\u0000"+
		"\u0000\u0000\u0141\u0139\u0001\u0000\u0000\u0000\u0141\u013d\u0001\u0000"+
		"\u0000\u0000\u0142\u001f\u0001\u0000\u0000\u0000\u0143\u0151\u0003\"\u0011"+
		"\u0000\u0144\u0145\u0003\"\u0011\u0000\u0145\u0146\u00057\u0000\u0000"+
		"\u0146\u0147\u0003 \u0010\u0000\u0147\u0151\u0001\u0000\u0000\u0000\u0148"+
		"\u0149\u0003\"\u0011\u0000\u0149\u014a\u00058\u0000\u0000\u014a\u014b"+
		"\u0003 \u0010\u0000\u014b\u0151\u0001\u0000\u0000\u0000\u014c\u014d\u0003"+
		"\"\u0011\u0000\u014d\u014e\u0005@\u0000\u0000\u014e\u014f\u0003 \u0010"+
		"\u0000\u014f\u0151\u0001\u0000\u0000\u0000\u0150\u0143\u0001\u0000\u0000"+
		"\u0000\u0150\u0144\u0001\u0000\u0000\u0000\u0150\u0148\u0001\u0000\u0000"+
		"\u0000\u0150\u014c\u0001\u0000\u0000\u0000\u0151!\u0001\u0000\u0000\u0000"+
		"\u0152\u015c\u0003$\u0012\u0000\u0153\u0154\u0003$\u0012\u0000\u0154\u0155"+
		"\u0005?\u0000\u0000\u0155\u0156\u0003\"\u0011\u0000\u0156\u015c\u0001"+
		"\u0000\u0000\u0000\u0157\u0158\u0003$\u0012\u0000\u0158\u0159\u0005>\u0000"+
		"\u0000\u0159\u015a\u0003\"\u0011\u0000\u015a\u015c\u0001\u0000\u0000\u0000"+
		"\u015b\u0152\u0001\u0000\u0000\u0000\u015b\u0153\u0001\u0000\u0000\u0000"+
		"\u015b\u0157\u0001\u0000\u0000\u0000\u015c#\u0001\u0000\u0000\u0000\u015d"+
		"\u0163\u0003&\u0013\u0000\u015e\u015f\u0003&\u0013\u0000\u015f\u0160\u0005"+
		"9\u0000\u0000\u0160\u0161\u0003&\u0013\u0000\u0161\u0163\u0001\u0000\u0000"+
		"\u0000\u0162\u015d\u0001\u0000\u0000\u0000\u0162\u015e\u0001\u0000\u0000"+
		"\u0000\u0163%\u0001\u0000\u0000\u0000\u0164\u016c\u0003\u0086C\u0000\u0165"+
		"\u0166\u00057\u0000\u0000\u0166\u016c\u0003&\u0013\u0000\u0167\u0168\u0005"+
		"8\u0000\u0000\u0168\u016c\u0003&\u0013\u0000\u0169\u016a\u00056\u0000"+
		"\u0000\u016a\u016c\u0003&\u0013\u0000\u016b\u0164\u0001\u0000\u0000\u0000"+
		"\u016b\u0165\u0001\u0000\u0000\u0000\u016b\u0167\u0001\u0000\u0000\u0000"+
		"\u016b\u0169\u0001\u0000\u0000\u0000\u016c\'\u0001\u0000\u0000\u0000\u016d"+
		"\u016e\u0006\u0014\uffff\uffff\u0000\u016e\u0178\u0003*\u0015\u0000\u016f"+
		"\u0178\u0003<\u001e\u0000\u0170\u0178\u0003B!\u0000\u0171\u0178\u0003"+
		",\u0016\u0000\u0172\u0178\u00034\u001a\u0000\u0173\u0178\u00036\u001b"+
		"\u0000\u0174\u0178\u0003R)\u0000\u0175\u0178\u0003Z-\u0000\u0176\u0178"+
		"\u00038\u001c\u0000\u0177\u016d\u0001\u0000\u0000\u0000\u0177\u016f\u0001"+
		"\u0000\u0000\u0000\u0177\u0170\u0001\u0000\u0000\u0000\u0177\u0171\u0001"+
		"\u0000\u0000\u0000\u0177\u0172\u0001\u0000\u0000\u0000\u0177\u0173\u0001"+
		"\u0000\u0000\u0000\u0177\u0174\u0001\u0000\u0000\u0000\u0177\u0175\u0001"+
		"\u0000\u0000\u0000\u0177\u0176\u0001\u0000\u0000\u0000\u0178\u0192\u0001"+
		"\u0000\u0000\u0000\u0179\u017a\n\t\u0000\u0000\u017a\u0191\u0003L&\u0000"+
		"\u017b\u017c\n\u0007\u0000\u0000\u017c\u0191\u0003T*\u0000\u017d\u017e"+
		"\n\u0006\u0000\u0000\u017e\u0191\u0003V+\u0000\u017f\u0180\n\u0004\u0000"+
		"\u0000\u0180\u0181\u0005\n\u0000\u0000\u0181\u0182\u0003J%\u0000\u0182"+
		"\u0183\u0005\u000b\u0000\u0000\u0183\u0191\u0001\u0000\u0000\u0000\u0184"+
		"\u0185\n\u0003\u0000\u0000\u0185\u0186\u0005\n\u0000\u0000\u0186\u0187"+
		"\u0003J%\u0000\u0187\u0188\u0005\u000b\u0000\u0000\u0188\u0189\u0005\u000e"+
		"\u0000\u0000\u0189\u0191\u0001\u0000\u0000\u0000\u018a\u018b\n\u0002\u0000"+
		"\u0000\u018b\u018d\u0005\f\u0000\u0000\u018c\u018e\u0003:\u001d\u0000"+
		"\u018d\u018c\u0001\u0000\u0000\u0000\u018d\u018e\u0001\u0000\u0000\u0000"+
		"\u018e\u018f\u0001\u0000\u0000\u0000\u018f\u0191\u0005\r\u0000\u0000\u0190"+
		"\u0179\u0001\u0000\u0000\u0000\u0190\u017b\u0001\u0000\u0000\u0000\u0190"+
		"\u017d\u0001\u0000\u0000\u0000\u0190\u017f\u0001\u0000\u0000\u0000\u0190"+
		"\u0184\u0001\u0000\u0000\u0000\u0190\u018a\u0001\u0000\u0000\u0000\u0191"+
		"\u0194\u0001\u0000\u0000\u0000\u0192\u0190\u0001\u0000\u0000\u0000\u0192"+
		"\u0193\u0001\u0000\u0000\u0000\u0193)\u0001\u0000\u0000\u0000\u0194\u0192"+
		"\u0001\u0000\u0000\u0000\u0195\u0196\u0005C\u0000\u0000\u0196+\u0001\u0000"+
		"\u0000\u0000\u0197\u0198\u0003.\u0017\u0000\u0198-\u0001\u0000\u0000\u0000"+
		"\u0199\u019c\u00030\u0018\u0000\u019a\u019c\u00032\u0019\u0000\u019b\u0199"+
		"\u0001\u0000\u0000\u0000\u019b\u019a\u0001\u0000\u0000\u0000\u019c/\u0001"+
		"\u0000\u0000\u0000\u019d\u019e\u0005E\u0000\u0000\u019e1\u0001\u0000\u0000"+
		"\u0000\u019f\u01a0\u00051\u0000\u0000\u01a0\u01a1\u0005E\u0000\u0000\u01a1"+
		"3\u0001\u0000\u0000\u0000\u01a2\u01a3\u0005E\u0000\u0000\u01a3\u01a4\u0005"+
		"5\u0000\u0000\u01a4\u01a5\u0005E\u0000\u0000\u01a55\u0001\u0000\u0000"+
		"\u0000\u01a6\u01a7\u0005\f\u0000\u0000\u01a7\u01a8\u0003\u0010\b\u0000"+
		"\u01a8\u01a9\u0005\r\u0000\u0000\u01a97\u0001\u0000\u0000\u0000\u01aa"+
		"\u01ab\u0005\u001b\u0000\u0000\u01ab9\u0001\u0000\u0000\u0000\u01ac\u01b2"+
		"\u0003\u0010\b\u0000\u01ad\u01ae\u0003\u0010\b\u0000\u01ae\u01af\u0005"+
		"\u0007\u0000\u0000\u01af\u01b0\u0003:\u001d\u0000\u01b0\u01b2\u0001\u0000"+
		"\u0000\u0000\u01b1\u01ac\u0001\u0000\u0000\u0000\u01b1\u01ad\u0001\u0000"+
		"\u0000\u0000\u01b2;\u0001\u0000\u0000\u0000\u01b3\u01b5\u0005\n\u0000"+
		"\u0000\u01b4\u01b6\u0003>\u001f\u0000\u01b5\u01b4\u0001\u0000\u0000\u0000"+
		"\u01b5\u01b6\u0001\u0000\u0000\u0000\u01b6\u01b7\u0001\u0000\u0000\u0000"+
		"\u01b7\u01b8\u0005\u000b\u0000\u0000\u01b8=\u0001\u0000\u0000\u0000\u01b9"+
		"\u01bf\u0003@ \u0000\u01ba\u01bb\u0003@ \u0000\u01bb\u01bc\u0005\u0007"+
		"\u0000\u0000\u01bc\u01bd\u0003>\u001f\u0000\u01bd\u01bf\u0001\u0000\u0000"+
		"\u0000\u01be\u01b9\u0001\u0000\u0000\u0000\u01be\u01ba\u0001\u0000\u0000"+
		"\u0000\u01bf?\u0001\u0000\u0000\u0000\u01c0\u01c6\u0003\u0010\b\u0000"+
		"\u01c1\u01c2\u0003\u0010\b\u0000\u01c2\u01c3\u00054\u0000\u0000\u01c3"+
		"\u01c4\u0003\u0010\b\u0000\u01c4\u01c6\u0001\u0000\u0000\u0000\u01c5\u01c0"+
		"\u0001\u0000\u0000\u0000\u01c5\u01c1\u0001\u0000\u0000\u0000\u01c6A\u0001"+
		"\u0000\u0000\u0000\u01c7\u01c9\u0005\b\u0000\u0000\u01c8\u01ca\u0003D"+
		"\"\u0000\u01c9\u01c8\u0001\u0000\u0000\u0000\u01c9\u01ca\u0001\u0000\u0000"+
		"\u0000\u01ca\u01cb\u0001\u0000\u0000\u0000\u01cb\u01cc\u0005\t\u0000\u0000"+
		"\u01ccC\u0001\u0000\u0000\u0000\u01cd\u01d3\u0003F#\u0000\u01ce\u01cf"+
		"\u0003F#\u0000\u01cf\u01d0\u0005\u0007\u0000\u0000\u01d0\u01d1\u0003D"+
		"\"\u0000\u01d1\u01d3\u0001\u0000\u0000\u0000\u01d2\u01cd\u0001\u0000\u0000"+
		"\u0000\u01d2\u01ce\u0001\u0000\u0000\u0000\u01d3E\u0001\u0000\u0000\u0000"+
		"\u01d4\u01d5\u0003H$\u0000\u01d5\u01d6\u0005\u0006\u0000\u0000\u01d6\u01d7"+
		"\u0003\u0010\b\u0000\u01d7G\u0001\u0000\u0000\u0000\u01d8\u01d9\u0005"+
		"E\u0000\u0000\u01d9I\u0001\u0000\u0000\u0000\u01da\u01db\u0003\u0010\b"+
		"\u0000\u01dbK\u0001\u0000\u0000\u0000\u01dc\u01df\u0003N\'\u0000\u01dd"+
		"\u01df\u0003P(\u0000\u01de\u01dc\u0001\u0000\u0000\u0000\u01de\u01dd\u0001"+
		"\u0000\u0000\u0000\u01dfM\u0001\u0000\u0000\u0000\u01e0\u01e1\u0005\b"+
		"\u0000\u0000\u01e1\u01e2\u0003H$\u0000\u01e2\u01e3\u0005\t\u0000\u0000"+
		"\u01e3O\u0001\u0000\u0000\u0000\u01e4\u01e5\u0005\b\u0000\u0000\u01e5"+
		"\u01e6\u0003H$\u0000\u01e6\u01e7\u0005\t\u0000\u0000\u01e7\u01e8\u0005"+
		"\u000e\u0000\u0000\u01e8Q\u0001\u0000\u0000\u0000\u01e9\u01ea\u0003L&"+
		"\u0000\u01eaS\u0001\u0000\u0000\u0000\u01eb\u01ec\u0005\b\u0000\u0000"+
		"\u01ec\u01ed\u0003X,\u0000\u01ed\u01ee\u0005\t\u0000\u0000\u01eeU\u0001"+
		"\u0000\u0000\u0000\u01ef\u01f0\u0005\b\u0000\u0000\u01f0\u01f1\u0003X"+
		",\u0000\u01f1\u01f2\u0005\t\u0000\u0000\u01f2\u01f3\u0005\u000e\u0000"+
		"\u0000\u01f3W\u0001\u0000\u0000\u0000\u01f4\u01fa\u0003N\'\u0000\u01f5"+
		"\u01f6\u0003N\'\u0000\u01f6\u01f7\u0005\u0007\u0000\u0000\u01f7\u01f8"+
		"\u0003X,\u0000\u01f8\u01fa\u0001\u0000\u0000\u0000\u01f9\u01f4\u0001\u0000"+
		"\u0000\u0000\u01f9\u01f5\u0001\u0000\u0000\u0000\u01faY\u0001\u0000\u0000"+
		"\u0000\u01fb\u01fe\u0003T*\u0000\u01fc\u01fe\u0003V+\u0000\u01fd\u01fb"+
		"\u0001\u0000\u0000\u0000\u01fd\u01fc\u0001\u0000\u0000\u0000\u01fe[\u0001"+
		"\u0000\u0000\u0000\u01ff\u0201\u0005\f\u0000\u0000\u0200\u0202\u0003`"+
		"0\u0000\u0201\u0200\u0001\u0000\u0000\u0000\u0201\u0202\u0001\u0000\u0000"+
		"\u0000\u0202\u0203\u0001\u0000\u0000\u0000\u0203\u0205\u0005\r\u0000\u0000"+
		"\u0204\u0206\u0003j5\u0000\u0205\u0204\u0001\u0000\u0000\u0000\u0205\u0206"+
		"\u0001\u0000\u0000\u0000\u0206\u0207\u0001\u0000\u0000\u0000\u0207\u0208"+
		"\u00053\u0000\u0000\u0208\u0209\u0003^/\u0000\u0209]\u0001\u0000\u0000"+
		"\u0000\u020a\u020b\u0003\u0010\b\u0000\u020b_\u0001\u0000\u0000\u0000"+
		"\u020c\u0212\u0003b1\u0000\u020d\u020e\u0003b1\u0000\u020e\u020f\u0005"+
		"\u0007\u0000\u0000\u020f\u0210\u0003n7\u0000\u0210\u0212\u0001\u0000\u0000"+
		"\u0000\u0211\u020c\u0001\u0000\u0000\u0000\u0211\u020d\u0001\u0000\u0000"+
		"\u0000\u0212a\u0001\u0000\u0000\u0000\u0213\u0219\u0003d2\u0000\u0214"+
		"\u0215\u0003d2\u0000\u0215\u0216\u0005\u0007\u0000\u0000\u0216\u0217\u0003"+
		"b1\u0000\u0217\u0219\u0001\u0000\u0000\u0000\u0218\u0213\u0001\u0000\u0000"+
		"\u0000\u0218\u0214\u0001\u0000\u0000\u0000\u0219c\u0001\u0000\u0000\u0000"+
		"\u021a\u021c\u0003f3\u0000\u021b\u021d\u0003h4\u0000\u021c\u021b\u0001"+
		"\u0000\u0000\u0000\u021c\u021d\u0001\u0000\u0000\u0000\u021de\u0001\u0000"+
		"\u0000\u0000\u021e\u021f\u0005E\u0000\u0000\u021fg\u0001\u0000\u0000\u0000"+
		"\u0220\u0221\u0003l6\u0000\u0221i\u0001\u0000\u0000\u0000\u0222\u0223"+
		"\u0003l6\u0000\u0223k\u0001\u0000\u0000\u0000\u0224\u0225\u00052\u0000"+
		"\u0000\u0225\u0226\u0003\u0018\f\u0000\u0226m\u0001\u0000\u0000\u0000"+
		"\u0227\u022d\u0003p8\u0000\u0228\u0229\u0003p8\u0000\u0229\u022a\u0005"+
		"\u0007\u0000\u0000\u022a\u022b\u0003n7\u0000\u022b\u022d\u0001\u0000\u0000"+
		"\u0000\u022c\u0227\u0001\u0000\u0000\u0000\u022c\u0228\u0001\u0000\u0000"+
		"\u0000\u022do\u0001\u0000\u0000\u0000\u022e\u022f\u0005\u000f\u0000\u0000"+
		"\u022f\u0230\u0003d2\u0000\u0230q\u0001\u0000\u0000\u0000\u0231\u0232"+
		"\u0005\u001d\u0000\u0000\u0232\u0233\u0003t:\u0000\u0233s\u0001\u0000"+
		"\u0000\u0000\u0234\u0235\u0003^/\u0000\u0235u\u0001\u0000\u0000\u0000"+
		"\u0236\u0237\u0005\u001e\u0000\u0000\u0237\u0238\u0003x<\u0000\u0238\u0239"+
		"\u0005\u001f\u0000\u0000\u0239\u023a\u0003\u0010\b\u0000\u023aw\u0001"+
		"\u0000\u0000\u0000\u023b\u0241\u0003z=\u0000\u023c\u023d\u0003z=\u0000"+
		"\u023d\u023e\u0005\u0007\u0000\u0000\u023e\u023f\u0003x<\u0000\u023f\u0241"+
		"\u0001\u0000\u0000\u0000\u0240\u023b\u0001\u0000\u0000\u0000\u0240\u023c"+
		"\u0001\u0000\u0000\u0000\u0241y\u0001\u0000\u0000\u0000\u0242\u0243\u0003"+
		"|>\u0000\u0243\u0244\u0005\u0006\u0000\u0000\u0244\u0245\u0003\u0010\b"+
		"\u0000\u0245{\u0001\u0000\u0000\u0000\u0246\u0247\u0005E\u0000\u0000\u0247"+
		"}\u0001\u0000\u0000\u0000\u0248\u0249\u0005 \u0000\u0000\u0249\u024a\u0003"+
		"\u0080@\u0000\u024a\u024b\u0005!\u0000\u0000\u024b\u024c\u0003\u0082A"+
		"\u0000\u024c\u024d\u0005\"\u0000\u0000\u024d\u024e\u0003\u0084B\u0000"+
		"\u024e\u007f\u0001\u0000\u0000\u0000\u024f\u0250\u0003\u0010\b\u0000\u0250"+
		"\u0081\u0001\u0000\u0000\u0000\u0251\u0252\u0003\u0010\b\u0000\u0252\u0083"+
		"\u0001\u0000\u0000\u0000\u0253\u0254\u0003\u0010\b\u0000\u0254\u0085\u0001"+
		"\u0000\u0000\u0000\u0255\u0259\u0003(\u0014\u0000\u0256\u0257\u0005\u001c"+
		"\u0000\u0000\u0257\u0259\u0003\u008aE\u0000\u0258\u0255\u0001\u0000\u0000"+
		"\u0000\u0258\u0256\u0001\u0000\u0000\u0000\u0259\u0087\u0001\u0000\u0000"+
		"\u0000\u025a\u025d\u00036\u001b\u0000\u025b\u025d\u0003\u008aE\u0000\u025c"+
		"\u025a\u0001\u0000\u0000\u0000\u025c\u025b\u0001\u0000\u0000\u0000\u025d"+
		"\u0089\u0001\u0000\u0000\u0000\u025e\u0265\u0003\u008cF\u0000\u025f\u0265"+
		"\u0003\u008eG\u0000\u0260\u0265\u0003\u009aM\u0000\u0261\u0265\u0003\u009e"+
		"O\u0000\u0262\u0265\u0003\u00acV\u0000\u0263\u0265\u0003\u00b0X\u0000"+
		"\u0264\u025e\u0001\u0000\u0000\u0000\u0264\u025f\u0001\u0000\u0000\u0000"+
		"\u0264\u0260\u0001\u0000\u0000\u0000\u0264\u0261\u0001\u0000\u0000\u0000"+
		"\u0264\u0262\u0001\u0000\u0000\u0000\u0264\u0263\u0001\u0000\u0000\u0000"+
		"\u0265\u008b\u0001\u0000\u0000\u0000\u0266\u0267\u0007\u0000\u0000\u0000"+
		"\u0267\u008d\u0001\u0000\u0000\u0000\u0268\u0269\u0005\b\u0000\u0000\u0269"+
		"\u026a\u0003\u0098L\u0000\u026a\u026b\u0005\t\u0000\u0000\u026b\u0278"+
		"\u0001\u0000\u0000\u0000\u026c\u026e\u0005\b\u0000\u0000\u026d\u026f\u0003"+
		"\u0090H\u0000\u026e\u026d\u0001\u0000\u0000\u0000\u026e\u026f\u0001\u0000"+
		"\u0000\u0000\u026f\u0270\u0001\u0000\u0000\u0000\u0270\u0278\u0005\t\u0000"+
		"\u0000\u0271\u0272\u0005\b\u0000\u0000\u0272\u0273\u0003\u0090H\u0000"+
		"\u0273\u0274\u0005\u0007\u0000\u0000\u0274\u0275\u0003\u0098L\u0000\u0275"+
		"\u0276\u0005\t\u0000\u0000\u0276\u0278\u0001\u0000\u0000\u0000\u0277\u0268"+
		"\u0001\u0000\u0000\u0000\u0277\u026c\u0001\u0000\u0000\u0000\u0277\u0271"+
		"\u0001\u0000\u0000\u0000\u0278\u008f\u0001\u0000\u0000\u0000\u0279\u027f"+
		"\u0003\u0092I\u0000\u027a\u027b\u0003\u0092I\u0000\u027b\u027c\u0005\u0007"+
		"\u0000\u0000\u027c\u027d\u0003\u0090H\u0000\u027d\u027f\u0001\u0000\u0000"+
		"\u0000\u027e\u0279\u0001\u0000\u0000\u0000\u027e\u027a\u0001\u0000\u0000"+
		"\u0000\u027f\u0091\u0001\u0000\u0000\u0000\u0280\u0282\u0005\u000f\u0000"+
		"\u0000\u0281\u0280\u0001\u0000\u0000\u0000\u0281\u0282\u0001\u0000\u0000"+
		"\u0000\u0282\u0283\u0001\u0000\u0000\u0000\u0283\u0285\u0003H$\u0000\u0284"+
		"\u0286\u0003\u0094J\u0000\u0285\u0284\u0001\u0000\u0000\u0000\u0285\u0286"+
		"\u0001\u0000\u0000\u0000\u0286\u0093\u0001\u0000\u0000\u0000\u0287\u0288"+
		"\u0005\u0006\u0000\u0000\u0288\u0289\u0003\u0096K\u0000\u0289\u0095\u0001"+
		"\u0000\u0000\u0000\u028a\u028b\u0003\u0088D\u0000\u028b\u0097\u0001\u0000"+
		"\u0000\u0000\u028c\u028d\u0005\u001b\u0000\u0000\u028d\u0099\u0001\u0000"+
		"\u0000\u0000\u028e\u028f\u0005\n\u0000\u0000\u028f\u0290\u0003\u009cN"+
		"\u0000\u0290\u0291\u0005\u000b\u0000\u0000\u0291\u009b\u0001\u0000\u0000"+
		"\u0000\u0292\u0293\u0003\u0088D\u0000\u0293\u009d\u0001\u0000\u0000\u0000"+
		"\u0294\u0296\u0005\u001a\u0000\u0000\u0295\u0297\u0003\u00a0P\u0000\u0296"+
		"\u0295\u0001\u0000\u0000\u0000\u0296\u0297\u0001\u0000\u0000\u0000\u0297"+
		"\u0298\u0001\u0000\u0000\u0000\u0298\u0299\u0005\r\u0000\u0000\u0299\u029a"+
		"\u0003j5\u0000\u029a\u009f\u0001\u0000\u0000\u0000\u029b\u02a2\u0003\u00a2"+
		"Q\u0000\u029c\u029d\u0003\u00a2Q\u0000\u029d\u029e\u0005\u0007\u0000\u0000"+
		"\u029e\u029f\u0003\u00a6S\u0000\u029f\u02a2\u0001\u0000\u0000\u0000\u02a0"+
		"\u02a2\u0003\u00a6S\u0000\u02a1\u029b\u0001\u0000\u0000\u0000\u02a1\u029c"+
		"\u0001\u0000\u0000\u0000\u02a1\u02a0\u0001\u0000\u0000\u0000\u02a2\u00a1"+
		"\u0001\u0000\u0000\u0000\u02a3\u02a9\u0003\u00a4R\u0000\u02a4\u02a5\u0003"+
		"\u00a4R\u0000\u02a5\u02a6\u0005\u0007\u0000\u0000\u02a6\u02a7\u0003\u00a2"+
		"Q\u0000\u02a7\u02a9\u0001\u0000\u0000\u0000\u02a8\u02a3\u0001\u0000\u0000"+
		"\u0000\u02a8\u02a4\u0001\u0000\u0000\u0000\u02a9\u00a3\u0001\u0000\u0000"+
		"\u0000\u02aa\u02ab\u0003\u00aaU\u0000\u02ab\u00a5\u0001\u0000\u0000\u0000"+
		"\u02ac\u02b2\u0003\u00a8T\u0000\u02ad\u02ae\u0003\u00a8T\u0000\u02ae\u02af"+
		"\u0005\u0007\u0000\u0000\u02af\u02b0\u0003\u00a6S\u0000\u02b0\u02b2\u0001"+
		"\u0000\u0000\u0000\u02b1\u02ac\u0001\u0000\u0000\u0000\u02b1\u02ad\u0001"+
		"\u0000\u0000\u0000\u02b2\u00a7\u0001\u0000\u0000\u0000\u02b3\u02b4\u0005"+
		"\u000f\u0000\u0000\u02b4\u02b5\u0003\u00aaU\u0000\u02b5\u00a9\u0001\u0000"+
		"\u0000\u0000\u02b6\u02b7\u0003f3\u0000\u02b7\u02b8\u0003h4\u0000\u02b8"+
		"\u00ab\u0001\u0000\u0000\u0000\u02b9\u02ba\u0005\u0010\u0000\u0000\u02ba"+
		"\u02bb\u0003\u00aeW\u0000\u02bb\u00ad\u0001\u0000\u0000\u0000\u02bc\u02bd"+
		"\u0005\b\u0000\u0000\u02bd\u02be\u0003\u0090H\u0000\u02be\u02bf\u0005"+
		"\t\u0000\u0000\u02bf\u00af\u0001\u0000\u0000\u0000\u02c0\u02c1\u0005\u0011"+
		"\u0000\u0000\u02c1\u02c2\u0003\u0088D\u0000\u02c2\u00b1\u0001\u0000\u0000"+
		"\u0000\u02c3\u02c4\u0005\u0019\u0000\u0000\u02c4\u02c5\u0003\u0010\b\u0000"+
		"\u02c5\u00b3\u0001\u0000\u0000\u0000\u02c6\u02c7\u0005\u0018\u0000\u0000"+
		"\u02c7\u02c9\u0003\u00b6[\u0000\u02c8\u02ca\u0003\u00b8\\\u0000\u02c9"+
		"\u02c8\u0001\u0000\u0000\u0000\u02c9\u02ca\u0001\u0000\u0000\u0000\u02ca"+
		"\u00b5\u0001\u0000\u0000\u0000\u02cb\u02cc\u0003\u0010\b\u0000\u02cc\u00b7"+
		"\u0001\u0000\u0000\u0000\u02cd\u02ce\u0005\u0017\u0000\u0000\u02ce\u02cf"+
		"\u0003\u00ba]\u0000\u02cf\u00b9\u0001\u0000\u0000\u0000\u02d0\u02d1\u0003"+
		"\u0010\b\u0000\u02d1\u00bb\u0001\u0000\u0000\u0000\u02d2\u02d3\u0003\u00be"+
		"_\u0000\u02d3\u00bd\u0001\u0000\u0000\u0000\u02d4\u02d6\u0005\b\u0000"+
		"\u0000\u02d5\u02d7\u0003\u00c0`\u0000\u02d6\u02d5\u0001\u0000\u0000\u0000"+
		"\u02d6\u02d7\u0001\u0000\u0000\u0000\u02d7\u02d8\u0001\u0000\u0000\u0000"+
		"\u02d8\u02d9\u0005\t\u0000\u0000\u02d9\u00bf\u0001\u0000\u0000\u0000\u02da"+
		"\u02e0\u0003\u00c2a\u0000\u02db\u02dc\u0003\u00c2a\u0000\u02dc\u02dd\u0005"+
		"\u0007\u0000\u0000\u02dd\u02de\u0003\u00c0`\u0000\u02de\u02e0\u0001\u0000"+
		"\u0000\u0000\u02df\u02da\u0001\u0000\u0000\u0000\u02df\u02db\u0001\u0000"+
		"\u0000\u0000\u02e0\u00c1\u0001\u0000\u0000\u0000\u02e1\u02e2\u0003H$\u0000"+
		"\u02e2\u02e3\u0005\u0006\u0000\u0000\u02e3\u02e4\u0003\u00c8d\u0000\u02e4"+
		"\u00c3\u0001\u0000\u0000\u0000\u02e5\u02e7\u0005\n\u0000\u0000\u02e6\u02e8"+
		"\u0003\u00c6c\u0000\u02e7\u02e6\u0001\u0000\u0000\u0000\u02e7\u02e8\u0001"+
		"\u0000\u0000\u0000\u02e8\u02e9\u0001\u0000\u0000\u0000\u02e9\u02ea\u0005"+
		"\u000b\u0000\u0000\u02ea\u00c5\u0001\u0000\u0000\u0000\u02eb\u02f1\u0003"+
		"\u00c8d\u0000\u02ec\u02ed\u0003\u00c8d\u0000\u02ed\u02ee\u0005\u0007\u0000"+
		"\u0000\u02ee\u02ef\u0003\u00c6c\u0000\u02ef\u02f1\u0001\u0000\u0000\u0000"+
		"\u02f0\u02eb\u0001\u0000\u0000\u0000\u02f0\u02ec\u0001\u0000\u0000\u0000"+
		"\u02f1\u00c7\u0001\u0000\u0000\u0000\u02f2\u02f6\u0003\u00be_\u0000\u02f3"+
		"\u02f6\u0003\u00c4b\u0000\u02f4\u02f6\u0005C\u0000\u0000\u02f5\u02f2\u0001"+
		"\u0000\u0000\u0000\u02f5\u02f3\u0001\u0000\u0000\u0000\u02f5\u02f4\u0001"+
		"\u0000\u0000\u0000\u02f6\u00c9\u0001\u0000\u0000\u00009\u00cc\u00d1\u00d7"+
		"\u00dd\u00e0\u00e3\u00f6\u00fd\u0107\u0112\u0116\u0122\u012e\u0141\u0150"+
		"\u015b\u0162\u016b\u0177\u018d\u0190\u0192\u019b\u01b1\u01b5\u01be\u01c5"+
		"\u01c9\u01d2\u01de\u01f9\u01fd\u0201\u0205\u0211\u0218\u021c\u022c\u0240"+
		"\u0258\u025c\u0264\u026e\u0277\u027e\u0281\u0285\u0296\u02a1\u02a8\u02b1"+
		"\u02c9\u02d6\u02df\u02e7\u02f0\u02f5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}