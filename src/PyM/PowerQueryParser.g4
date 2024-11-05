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
    | tableExpandTableColumnFunction
    | functionCall
    //| unknownExpression
    ;

tableNestedJoinFunction
    : TABLE_NESTED_JOIN '('
        firstTable=IDENTIFIER ',' firstKeyColumns=literalList ',' secondTable=IDENTIFIER ',' secondKeyColumns=literalList ',' newColumnName=LITERAL
        (',' joinKind=IDENTIFIER)?
        (',' keyEqualityComparer=IDENTIFIER)?
      ')'
    ;

//Table.ExpandTableColumn(table as table, column as text, columnNames as list, optional newColumnNames as nullable list) as table
tableExpandTableColumnFunction
    : TABLE_EXPAND_TABLE_COLUMN '('
        table=IDENTIFIER ',' column=LITERAL ',' columnsList=literalList (',' NewColumnNamesList=literalList)? 
        ')'
    ;



literalList
    : '{' LITERAL (',' LITERAL)* '}'
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

/*unknownExpression
    : IDENTIFIER ( . )*? (COMMA | SEMICOLON | CLOSE_PAREN | CLOSE_BRACE | CLOSE_BRACKET | EOF)
    ;*/