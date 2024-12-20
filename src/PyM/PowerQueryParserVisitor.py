# Generated from src/PyM/PowerQueryParser.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
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


    # Visit a parse tree produced by PowerQueryParser#tableNestedJoinFunction.
    def visitTableNestedJoinFunction(self, ctx:PowerQueryParser.TableNestedJoinFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#tableExpandTableColumnFunction.
    def visitTableExpandTableColumnFunction(self, ctx:PowerQueryParser.TableExpandTableColumnFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#literalList.
    def visitLiteralList(self, ctx:PowerQueryParser.LiteralListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#functionCall.
    def visitFunctionCall(self, ctx:PowerQueryParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#argumentList.
    def visitArgumentList(self, ctx:PowerQueryParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PowerQueryParser#otherExpression.
    def visitOtherExpression(self, ctx:PowerQueryParser.OtherExpressionContext):
        return self.visitChildren(ctx)



del PowerQueryParser