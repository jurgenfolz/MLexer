// Generated from c:/Users/KlausFolz/Desktop/Repositories/MLexer/src/PyM/PowerQueryParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PowerQueryParser}.
 */
public interface PowerQueryParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PowerQueryParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(PowerQueryParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link PowerQueryParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(PowerQueryParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link PowerQueryParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(PowerQueryParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PowerQueryParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(PowerQueryParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PowerQueryParser#letExpression}.
	 * @param ctx the parse tree
	 */
	void enterLetExpression(PowerQueryParser.LetExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PowerQueryParser#letExpression}.
	 * @param ctx the parse tree
	 */
	void exitLetExpression(PowerQueryParser.LetExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PowerQueryParser#assignmentList}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentList(PowerQueryParser.AssignmentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link PowerQueryParser#assignmentList}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentList(PowerQueryParser.AssignmentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link PowerQueryParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(PowerQueryParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link PowerQueryParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(PowerQueryParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link PowerQueryParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(PowerQueryParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PowerQueryParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(PowerQueryParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PowerQueryParser#tableNestedJoinFunction}.
	 * @param ctx the parse tree
	 */
	void enterTableNestedJoinFunction(PowerQueryParser.TableNestedJoinFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PowerQueryParser#tableNestedJoinFunction}.
	 * @param ctx the parse tree
	 */
	void exitTableNestedJoinFunction(PowerQueryParser.TableNestedJoinFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PowerQueryParser#tableExpandTableColumnFunction}.
	 * @param ctx the parse tree
	 */
	void enterTableExpandTableColumnFunction(PowerQueryParser.TableExpandTableColumnFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PowerQueryParser#tableExpandTableColumnFunction}.
	 * @param ctx the parse tree
	 */
	void exitTableExpandTableColumnFunction(PowerQueryParser.TableExpandTableColumnFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PowerQueryParser#literalList}.
	 * @param ctx the parse tree
	 */
	void enterLiteralList(PowerQueryParser.LiteralListContext ctx);
	/**
	 * Exit a parse tree produced by {@link PowerQueryParser#literalList}.
	 * @param ctx the parse tree
	 */
	void exitLiteralList(PowerQueryParser.LiteralListContext ctx);
	/**
	 * Enter a parse tree produced by {@link PowerQueryParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(PowerQueryParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link PowerQueryParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(PowerQueryParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link PowerQueryParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(PowerQueryParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link PowerQueryParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(PowerQueryParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link PowerQueryParser#otherExpression}.
	 * @param ctx the parse tree
	 */
	void enterOtherExpression(PowerQueryParser.OtherExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PowerQueryParser#otherExpression}.
	 * @param ctx the parse tree
	 */
	void exitOtherExpression(PowerQueryParser.OtherExpressionContext ctx);
}