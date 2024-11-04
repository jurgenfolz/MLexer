parser grammar PowerQueryParser;

options {
    tokenVocab=PowerQueryLexer;
}

tableNestedJoinFunction
    : TABLE_NESTED_JOIN '(' IDENTIFIER ',' '{' IDENTIFIER '}' ',' IDENTIFIER ',' '{' IDENTIFIER '}' ',' IDENTIFIER (',' IDENTIFIER)? ')'
    ;
