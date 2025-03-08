# Generated from src/PyM/PowerQueryParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PowerQueryParser import PowerQueryParser
else:
    from PowerQueryParser import PowerQueryParser

# This class defines a complete generic visitor for a parse tree produced by PowerQueryParser.

class PowerQueryParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PowerQueryParser#program.
    def visitProgram(self, ctx:PowerQueryParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#statement.
    def visitStatement(self, ctx:PowerQueryParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#letExpression.
    def visitLetExpression(self, ctx:PowerQueryParser.LetExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#assignmentList.
    def visitAssignmentList(self, ctx:PowerQueryParser.AssignmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#assignment.
    def visitAssignment(self, ctx:PowerQueryParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#expression.
    def visitExpression(self, ctx:PowerQueryParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#literal_expression.
    def visitLiteral_expression(self, ctx:PowerQueryParser.Literal_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#parenthesized_expression.
    def visitParenthesized_expression(self, ctx:PowerQueryParser.Parenthesized_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#each_expression.
    def visitEach_expression(self, ctx:PowerQueryParser.Each_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#meta_expression.
    def visitMeta_expression(self, ctx:PowerQueryParser.Meta_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#type_expression.
    def visitType_expression(self, ctx:PowerQueryParser.Type_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#type_body.
    def visitType_body(self, ctx:PowerQueryParser.Type_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#dottedTypeName.
    def visitDottedTypeName(self, ctx:PowerQueryParser.DottedTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#functionCall.
    def visitFunctionCall(self, ctx:PowerQueryParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#argumentList.
    def visitArgumentList(self, ctx:PowerQueryParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#tableNestedJoinFunction.
    def visitTableNestedJoinFunction(self, ctx:PowerQueryParser.TableNestedJoinFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#tableExpandTableColumnFunction.
    def visitTableExpandTableColumnFunction(self, ctx:PowerQueryParser.TableExpandTableColumnFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#dottedIdentifier.
    def visitDottedIdentifier(self, ctx:PowerQueryParser.DottedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#literalList.
    def visitLiteralList(self, ctx:PowerQueryParser.LiteralListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#list_expression.
    def visitList_expression(self, ctx:PowerQueryParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#record_expression.
    def visitRecord_expression(self, ctx:PowerQueryParser.Record_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#record_field.
    def visitRecord_field(self, ctx:PowerQueryParser.Record_fieldContext):
        return self.visitChildren(ctx)



del PowerQueryParser