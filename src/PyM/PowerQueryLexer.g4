// $antlr-format alignTrailingComments true, columnLimit 150, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine true, allowShortBlocksOnASingleLine true, minEmptyLines 0, alignColons trailing, singleLineOverrulesHangingColon true, alignLexerCommands true, alignLabels true, alignTrailers true

lexer grammar PowerQueryLexer;

options {
    caseInsensitive = true;
}

// Comments are kept on their own channel so the parser ignores them but they
channels { COMMENTCHANNEL, IRRELEVANTCHARS }

fragment LEXICAL_UNIT     : LEXICAL_ELEMENTS;
fragment LEXICAL_ELEMENTS : LEXICAL_ELEMENT LEXICAL_ELEMENTS?;
fragment LEXICAL_ELEMENT  : WHITESPACE | TOKEN LINE_COMMENT | TOKEN BLOCK_COMMENT;

// Trivia that should completely disappear from the token stream
WHITESPACE    : ( [\p{White_Space}] | [\u0009\u000B\u000C] | [\u000D][\u000A] NEW_LINE_CHAR) -> channel(IRRELEVANTCHARS);
NEW_LINE_CHAR : [\u000D\u000A\u0085\u2028\u2029]                                             -> channel(IRRELEVANTCHARS);

// Comments – redirected to COMMENT channel
LINE_COMMENT
    : '//' ~[\r\n]*                       -> channel(COMMENTCHANNEL)
    ;

BLOCK_COMMENT
    : '/*' ( . | '\r' | '\n' )*? '*/'     -> channel(COMMENTCHANNEL)
    ;

// Keywords
fragment KEYWORD:
    AND | AS | EACH | ELSE | ERROR | IF | IN | IS | LET | META | NOT | OR | OTHERWISE | SECTION | SHARED | THEN | TRY | TYPE
    | '#binary' | '#date' | '#datetime' | '#datetimezone' | '#duration' | '#infinity' | '#nan' | '#sections' | '#shared' | '#table' | '#time'
;

// Main token dispatcher
fragment TOKEN : IDENTIFIER | KEYWORD | LITERAL | OPERATOR_OR_PUNCTUATOR;

// Escape sequences
CHARACHTER_ESCAPE_SEQUENCE : '#(' ESCAPE_SEQUENCE_LIST ')';
fragment ESCAPE_SEQUENCE_LIST : SINGLE_ESCAPE_SEQUENCE ( ',' SINGLE_ESCAPE_SEQUENCE )* ;
fragment SINGLE_ESCAPE_SEQUENCE : LONG_UNICODE_ESCAPE_SEQUENCE | SHORT_UNICODE_ESCAPE_SEQUENCE | CONTROL_CHAR_ESCAPE_SEQUENCE | ESCAPE_ESCAPE ;
fragment LONG_UNICODE_ESCAPE_SEQUENCE  : HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT ;
fragment SHORT_UNICODE_ESCAPE_SEQUENCE : HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT ;
fragment CONTROL_CHAR_ESCAPE_SEQUENCE  : CONTROL_CHAR ;
fragment CONTROL_CHAR                  : [\r\n\t];
fragment ESCAPE_ESCAPE                 : '#';

// Punctuation & operators
EQUALS           : '=';
COMMA            : ',';
OPEN_BRACKET     : '[';
CLOSE_BRACKET    : ']';
OPEN_BRACE       : '{';
CLOSE_BRACE      : '}';
OPEN_PAREN       : '(';
CLOSE_PAREN      : ')';
OPTIONAL         : '?';
OPTIONAL_TEXT    : 'optional';
TABLE            : 'table';
NULLABLE         : 'nullable';
SEMICOLON        : ';';
SECTION          : 'section';
SHARED           : 'shared';
AND              : 'and';
OR               : 'or';
OTHERWISE        : 'otherwise';
TRY              : 'try';
ERROR            : 'error';
FUNCTION_START   : 'function (';
ELLIPSES         : '...';
TYPE             : 'type';
EACH             : 'each';
LET              : 'let';
IN               : 'in';
IF               : 'if';
THEN             : 'then';
ELSE             : 'else';
TEXT             : 'text';
RECORD           : 'record';
NUMBER           : 'number';
NONE             : 'none';
LOGICAL          : 'logical';
LIST             : 'list';
FUNCTION         : 'fuction';
DURATION         : 'duration';
DATETIMEZONE     : 'datetimezone';
ANY              : 'any';
ANYNONNULL       : 'anynonnull';
BINARY           : 'binary';
DATE             : 'date';
DATETIME         : 'datetime';
AT               : '@';
AS               : 'as';
ARROW            : '=>';
DOTDOT           : '..';
BANG             : '!';
NOT              : 'not';
PLUS             : '+';
MINUS            : '-';
META             : 'meta';
IS               : 'is';
NEQ              : '<>';
GE               : '>';
LE               : '<';
SLASH            : '/';
STAR             : '*';
AMP              : '&';
LEQ              : '<=';
GEQ              : '>=';

// Literals & numbers
fragment TEXT_LITERAL_CHAR : SINGLE_TEXT_CHAR | CHARACHTER_ESCAPE_SEQUENCE | DOUBLE_QUOTE_ESACAPE_SEQUENCE ;
fragment NUMBER_LITERAL    : DECIMAL_NUMBER_LITERAL | HEX_NUMBER_LITERAL ;
LITERAL                    : LOGICAL_LITERAL | NUMBER_LITERAL | TEXT_LITERAL | NULL_LITERAL | VERBATIM_LITERAL ;
fragment LOGICAL_LITERAL   : 'true' | 'false' ;
fragment DECIMAL_DIGITS    : DECIMAL_DIGIT+ ;
fragment DECIMAL_DIGIT     : [0-9] ;
fragment HEX_NUMBER_LITERAL: '0x' HEX_DIGITS ;
fragment HEX_DIGITS        : HEX_DIGIT+ ;
fragment HEX_DIGIT         : [0-9a-f] ;
fragment DECIMAL_NUMBER_LITERAL :
      DECIMAL_DIGITS '.' DECIMAL_DIGITS EXPONENT_PART?
    | '.' DECIMAL_DIGITS EXPONENT_PART?
    | DECIMAL_DIGITS EXPONENT_PART?
;
fragment EXPONENT_PART : '[Ee]' SIGN? DECIMAL_DIGITS ;
fragment SIGN          : [+-] ;

TEXT_LITERAL                 : '"' TEXT_LITERAL_CHAR* '"' ;
fragment DOUBLE_QUOTE_ESACAPE_SEQUENCE : '""' ;
fragment NULL_LITERAL        : 'null' ;
fragment VERBATIM_LITERAL    : '#!' TEXT_LITERAL_CHAR* '"' ;

// Identifiers
IDENTIFIER                 : REGULAR_IDENTIFIER | QUOTED_IDENTIFIER ;
REGULAR_IDENTIFIER         : AVAILABLE_IDENTIFIER ( '.' REGULAR_IDENTIFIER )? ;
AVAILABLE_IDENTIFIER       : KEYWORD_OR_IDENTIFIER ;
fragment IDENTIFIER_START_CHAR : LETTER_CHAR | '_' ;
KEYWORD_OR_IDENTIFIER      : LETTER_CHAR | '_' | IDENTIFIER_START_CHAR IDENTIFIER_PART_CHARS ;
fragment IDENTIFIER_PART_CHARS : IDENTIFIER_PART_CHAR+ ;
fragment IDENTIFIER_PART_CHAR  : LETTER_CHAR | DECIMAL_DIGIT_CHAR | '_' | CONNECTING_CHAR | COMBINING_CHAR | FORMATTING_CHAR ;
fragment GENERALIZED_IDENTIFIER : GENERALIZED_IDENTIFIER_PART ( ' '+ GENERALIZED_IDENTIFIER_PART )* ;
fragment GENERALIZED_IDENTIFIER_PART : GENERALIZED_IDENTIFIER_SEGMENT | DECIMAL_DIGIT_CHAR GENERALIZED_IDENTIFIER_SEGMENT ;
fragment GENERALIZED_IDENTIFIER_SEGMENT : KEYWORD_OR_IDENTIFIER ( '.' KEYWORD_OR_IDENTIFIER )? ;
fragment LETTER_CHAR        : [\p{Lu}\p{Ll}\p{Lt}\p{Lm}\p{Lo}\p{Nl}] ;
fragment COMBINING_CHAR     : [\p{Mn}\p{Mc}] ;
fragment DECIMAL_DIGIT_CHAR : [\p{Nd}] ;
fragment CONNECTING_CHAR    : [\p{Pc}] ;
fragment FORMATTING_CHAR    : [\p{Cf}] ;
fragment QUOTED_IDENTIFIER  : '#"' TEXT_LITERAL_CHAR* '"' ;

// Operator & punctuator subset used by TOKEN
fragment OPERATOR_OR_PUNCTUATOR :
      COMMA | SEMICOLON | EQUALS | LE | LEQ | GE | GEQ | NEQ
    | PLUS | MINUS | STAR | SLASH | AMP
    | OPEN_PAREN | CLOSE_PAREN | OPEN_BRACKET | CLOSE_BRACKET | OPEN_BRACE | CLOSE_BRACE
    | OPTIONAL | AT | ARROW | DOTDOT | ELLIPSES | BANG
;

fragment SINGLE_TEXT_CHAR : ~'"' | '#' ~'(' ;
