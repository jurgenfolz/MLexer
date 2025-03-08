parser grammar PowerQueryParser;

options {
    tokenVocab = PowerQueryLexer;
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

// ----------------------
// Expression
// ----------------------
expression
    : tableNestedJoinFunction
    | tableExpandTableColumnFunction
    | functionCall
    | literal_expression
    | parenthesized_expression
    | meta_expression               // e.g. (type nullable text) meta [Foo=...]
    | type_expression               // e.g. type table [Foo=...], type nullable text
    | each_expression               // e.g. each [Column]
    | list_expression               // e.g. { expr, expr }
    | record_expression             // e.g. [ key = value ]
    ;

// For base-64 strings, numbers, booleans, etc.
literal_expression
    : LITERAL
    ;

// Parenthesized expression: ( expr )
parenthesized_expression
    : OPEN_PAREN expression CLOSE_PAREN
    ;

// e.g. each [Kanton], each 1
each_expression
    : EACH expression
    ;

// e.g. (someExpr) meta [Foo=...]
meta_expression
    : parenthesized_expression META record_expression
    ;

// e.g. type table [ ... ], type nullable text, type number, etc.
type_expression
    : TYPE (NULLABLE)? type_body
    ;

// The “body” of a type, e.g. table [..], or text, number, etc.
type_body
    // e.g. table [Stadt = ..., Kanton = ...]
    : TABLE record_expression
    // fallback to the built-in type name or dotted name (like Int64.Type)
    | dottedTypeName
    ;

// You can refine dottedTypeName if needed to match e.g. Int64.Type or MyLib.CustomType
dottedTypeName
    : (TEXT | NUMBER | DATETIME | DATETIMEZONE | LOGICAL | BINARY | DURATION)?  // optional built-in
      (DOT IDENTIFIER)*                    // support e.g. Int64.Type or MyCustom.Type
    ;

// A function call, e.g. Binary.FromText(...) or Table.AddColumn(...)
functionCall
    : dottedIdentifier OPEN_PAREN argumentList? CLOSE_PAREN
    ;

// argumentList: multiple expressions
argumentList
    : expression (COMMA expression)*
    ;

// Specialized M calls
tableNestedJoinFunction
    : TABLE_NESTED_JOIN '('
        firstTable=IDENTIFIER ',' firstKeyColumns=literalList ',' 
        secondTable=IDENTIFIER ',' secondKeyColumns=literalList ',' 
        newColumnName=LITERAL
        (',' joinKind=IDENTIFIER)?
        (',' keyEqualityComparer=IDENTIFIER)?
      ')'
    ;

tableExpandTableColumnFunction
    : TABLE_EXPAND_TABLE_COLUMN '('
        table=IDENTIFIER ',' column=LITERAL ',' columnsList=literalList (',' NewColumnNamesList=literalList)? 
        ')'
    ;

// “dottedIdentifier” for function calls, e.g. Binary.FromText or MyLib.Custom
dottedIdentifier
    : IDENTIFIER (DOT IDENTIFIER)*
    ;

// A list of literal strings: {"Kanton", "Bevölkerung"} 
// (Your original literalList used LITERAL only. That won't handle nested braces.)
literalList
    : OPEN_BRACE LITERAL (COMMA LITERAL)* CLOSE_BRACE
    ;

// More general curly-brace list: { expr, expr, ... }
list_expression
    : OPEN_BRACE (expression (COMMA expression)*)? CLOSE_BRACE
    ;

// A record: [ key = value, key2 = value2 ]
record_expression
    : OPEN_BRACKET (record_field (COMMA record_field)*)? CLOSE_BRACKET
    ;

record_field
    : expression EQUALS expression
    ;
