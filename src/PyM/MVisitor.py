from .PowerQueryParserVisitor import PowerQueryParserVisitor
from .PowerQueryParser import PowerQueryParser

class MVisitor(PowerQueryParserVisitor):
    def __init__(self):
        super().__init__()
        self.steps_map = {}

    # Top-level entry point
    def visitProgram(self, ctx: PowerQueryParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.steps_map

    def visitStatement(self, ctx: PowerQueryParser.StatementContext):
        return self.visitChildren(ctx)

    def visitLetExpression(self, ctx: PowerQueryParser.LetExpressionContext):
        # Loop through assignments
        assignments = ctx.assignmentList().assignment()
        for assign in assignments:
            self.visit(assign)

        # Visit final expression after "in"
        self.visit(ctx.expression())
        return None

    def visitAssignment(self, ctx: PowerQueryParser.AssignmentContext):
        step_name = ctx.IDENTIFIER().getText()
        expr_ctx = ctx.expression()

        depends_on, used_columns, produced_columns = self.analyzeExpression(expr_ctx)

        # Store analysis results
        self.steps_map[step_name] = {
            "depends_on_steps": depends_on,
            "used_columns": used_columns,
            "produced_columns": produced_columns
        }

    def analyzeExpression(self, expr_ctx):
        depends_on = []
        used_columns = []
        produced_columns = []

        # Determine the exact type of expression and process accordingly
        if isinstance(expr_ctx, PowerQueryParser.TableNestedJoinFunctionContext):
            
            
            first_cols = [col.getText().strip('"') for col in expr_ctx.firstKeyColumns.literalList().LITERAL()]
            second_cols = [col.getText().strip('"') for col in expr_ctx.secondKeyColumns.literalList().LITERAL()]
            new_col = expr_ctx.newColumnName.getText().strip('"')
            first_table = expr_ctx.firstTable.getText()
            second_table = expr_ctx.secondTable.getText()
            
            depends_on.extend([first_table, second_table])
            used_columns = first_cols + second_cols
            produced_columns.append(new_col)

        elif isinstance(expr_ctx, PowerQueryParser.TableExpandTableColumnFunctionContext):
            table = expr_ctx.table.getText()
            column = expr_ctx.column.getText().strip('"')
            cols_list = [col.getText().strip('"') for col in expr_ctx.columnsList.literalList().LITERAL()]
            depends_on = [table]
            used_columns = [column]
            produced_columns.extend(cols_list)

        elif isinstance(expr_ctx, PowerQueryParser.FunctionCallContext):
            # Generic function call
            function_name = expr_ctx.IDENTIFIER().getText()
            args = expr_ctx.argumentList().expression() if expr_ctx.argumentList() else []
            depends_on = []
            used_columns = []
            for arg in args:
                # Further recursion might be needed here
                arg_depends, arg_used, _ = self.analyzeExpression(arg)
                depends_on.extend(arg_used)

        else:
            # Other expressions, literals, etc.
            depends_on = []
            used_columns = []
            produced_columns = []

        return depends_on, used_columns, produced_columns



#For debugging porpuses
class TreePrinterVisitor(PowerQueryParserVisitor):
    def __init__(self):
        super().__init__()

    def visit(self, ctx):
        # Print current node's rule name (if available) and its text.
        if hasattr(ctx, "getRuleIndex"):
            rule_index = ctx.getRuleIndex()
            rule_name = PowerQueryParser.ruleNames[rule_index]
            print(f"Visiting rule: {rule_name} -> {ctx.getText()}")
        else:
            # For terminal nodes
            print("Visiting terminal: " + ctx.getText())
        return self.visitChildren(ctx)