parser grammar PowerQueryParser;

options {
    tokenVocab=PowerQueryLexer;
}

program
    : statement+ EOF
    ;

statement
    : letExpression
    | expression
    ;

letExpression
    : LET assignmentList IN expression
    ;

assignmentList
    : assignment (COMMA assignment)*
    ;

assignment
    : IDENTIFIER EQUALS expression
    ;

expression
    : tableNestedJoinFunction
    | functionCall
    //| otherExpression
    ;

tableNestedJoinFunction
    : TABLE_NESTED_JOIN '(' IDENTIFIER ',' '{' LITERAL '}' ',' IDENTIFIER ',' '{' LITERAL '}' ',' LITERAL (',' IDENTIFIER)? ')'
    ;

functionCall
    : IDENTIFIER OPEN_PAREN argumentList? CLOSE_PAREN
    ;

argumentList
    : expression (COMMA expression)*
    ;

otherExpression
    : /* other expressions */
    ;
