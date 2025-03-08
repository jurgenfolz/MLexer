# Generated from src/PyM/PowerQueryParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PowerQueryParser import PowerQueryParser
else:
    from PowerQueryParser import PowerQueryParser

# This class defines a complete listener for a parse tree produced by PowerQueryParser.
class PowerQueryParserListener(ParseTreeListener):

    # Enter a parse tree produced by PowerQueryParser#program.
    def enterProgram(self, ctx:PowerQueryParser.ProgramContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#program.
    def exitProgram(self, ctx:PowerQueryParser.ProgramContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#statement.
    def enterStatement(self, ctx:PowerQueryParser.StatementContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#statement.
    def exitStatement(self, ctx:PowerQueryParser.StatementContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#letExpression.
    def enterLetExpression(self, ctx:PowerQueryParser.LetExpressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#letExpression.
    def exitLetExpression(self, ctx:PowerQueryParser.LetExpressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#assignmentList.
    def enterAssignmentList(self, ctx:PowerQueryParser.AssignmentListContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#assignmentList.
    def exitAssignmentList(self, ctx:PowerQueryParser.AssignmentListContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#assignment.
    def enterAssignment(self, ctx:PowerQueryParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#assignment.
    def exitAssignment(self, ctx:PowerQueryParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#expression.
    def enterExpression(self, ctx:PowerQueryParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#expression.
    def exitExpression(self, ctx:PowerQueryParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#literal_expression.
    def enterLiteral_expression(self, ctx:PowerQueryParser.Literal_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#literal_expression.
    def exitLiteral_expression(self, ctx:PowerQueryParser.Literal_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#parenthesized_expression.
    def enterParenthesized_expression(self, ctx:PowerQueryParser.Parenthesized_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#parenthesized_expression.
    def exitParenthesized_expression(self, ctx:PowerQueryParser.Parenthesized_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#each_expression.
    def enterEach_expression(self, ctx:PowerQueryParser.Each_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#each_expression.
    def exitEach_expression(self, ctx:PowerQueryParser.Each_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#meta_expression.
    def enterMeta_expression(self, ctx:PowerQueryParser.Meta_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#meta_expression.
    def exitMeta_expression(self, ctx:PowerQueryParser.Meta_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#type_expression.
    def enterType_expression(self, ctx:PowerQueryParser.Type_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#type_expression.
    def exitType_expression(self, ctx:PowerQueryParser.Type_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#type_body.
    def enterType_body(self, ctx:PowerQueryParser.Type_bodyContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#type_body.
    def exitType_body(self, ctx:PowerQueryParser.Type_bodyContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#dottedTypeName.
    def enterDottedTypeName(self, ctx:PowerQueryParser.DottedTypeNameContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#dottedTypeName.
    def exitDottedTypeName(self, ctx:PowerQueryParser.DottedTypeNameContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#functionCall.
    def enterFunctionCall(self, ctx:PowerQueryParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#functionCall.
    def exitFunctionCall(self, ctx:PowerQueryParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#argumentList.
    def enterArgumentList(self, ctx:PowerQueryParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#argumentList.
    def exitArgumentList(self, ctx:PowerQueryParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#tableNestedJoinFunction.
    def enterTableNestedJoinFunction(self, ctx:PowerQueryParser.TableNestedJoinFunctionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#tableNestedJoinFunction.
    def exitTableNestedJoinFunction(self, ctx:PowerQueryParser.TableNestedJoinFunctionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#tableExpandTableColumnFunction.
    def enterTableExpandTableColumnFunction(self, ctx:PowerQueryParser.TableExpandTableColumnFunctionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#tableExpandTableColumnFunction.
    def exitTableExpandTableColumnFunction(self, ctx:PowerQueryParser.TableExpandTableColumnFunctionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#dottedIdentifier.
    def enterDottedIdentifier(self, ctx:PowerQueryParser.DottedIdentifierContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#dottedIdentifier.
    def exitDottedIdentifier(self, ctx:PowerQueryParser.DottedIdentifierContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#literalList.
    def enterLiteralList(self, ctx:PowerQueryParser.LiteralListContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#literalList.
    def exitLiteralList(self, ctx:PowerQueryParser.LiteralListContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#list_expression.
    def enterList_expression(self, ctx:PowerQueryParser.List_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#list_expression.
    def exitList_expression(self, ctx:PowerQueryParser.List_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#record_expression.
    def enterRecord_expression(self, ctx:PowerQueryParser.Record_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#record_expression.
    def exitRecord_expression(self, ctx:PowerQueryParser.Record_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#record_field.
    def enterRecord_field(self, ctx:PowerQueryParser.Record_fieldContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#record_field.
    def exitRecord_field(self, ctx:PowerQueryParser.Record_fieldContext):
        pass



del PowerQueryParser