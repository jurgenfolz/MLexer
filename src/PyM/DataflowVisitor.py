# BuildDataFlowVisitor.py
from .PowerQueryParser import PowerQueryParser
from .PowerQueryParserVisitor import PowerQueryParserVisitor
from .StepNode import StepNode  # your custom data structure

class BuildDataFlowVisitor(PowerQueryParserVisitor):
    def __init__(self):
        super().__init__()  # not strictly required, but good practice
        self.steps_map = {}  # e.g. step_name -> StepNode

    # Example override for letExpression
    def visitLetExpression(self, ctx: PowerQueryParser.LetExpressionContext):
        """
        letExpression
            : LET assignmentList IN expression
        """
        # Possibly just visit children, or do something special here
        # We definitely want to visit assignmentList so we can collect step definitions
        return self.visitChildren(ctx)

    # Example override for assignment
    def visitAssignment(self, ctx: PowerQueryParser.AssignmentContext):
        """
        assignment
            : IDENTIFIER EQUALS expression
        """
        step_name = ctx.IDENTIFIER().getText()
        expression_ctx = ctx.expression()

        function_name, depends_on, used_columns, produced_columns = self._analyzeExpression(expression_ctx)

        # Create and store a StepNode
        node = StepNode(
            step_name=step_name,
            function_name=function_name,
            depends_on_steps=depends_on,
            used_columns=used_columns,
            produced_columns=produced_columns
        )
        self.steps_map[step_name] = node

        return None  # or return self.visitChildren(ctx) if you want to continue

    def _analyzeExpression(self, expression_ctx):
        """
        Inspect which rule matched. 
        For example:
            - tableNestedJoinFunction
            - tableExpandTableColumnFunction
            - functionCall
            - or a fallback
        """
        # Check if it matched tableNestedJoinFunction, etc.
        if isinstance(expression_ctx, PowerQueryParser.TableNestedJoinFunctionContext):
            return self._analyzeTableNestedJoin(expression_ctx)
        elif isinstance(expression_ctx, PowerQueryParser.TableExpandTableColumnFunctionContext):
            return self._analyzeExpandTableColumn(expression_ctx)
        elif isinstance(expression_ctx, PowerQueryParser.FunctionCallContext):
            return self._analyzeGenericFunctionCall(expression_ctx)
        else:
            return ("<unknown_expr>", [], [], [])

    def _analyzeTableNestedJoin(self, ctx: PowerQueryParser.TableNestedJoinFunctionContext):
        """
        example: Table.NestedJoin(
            #\"Changed Type\", {"Kanton"}, dimKantone, {"Kanton"}, "dimKantone", JoinKind.LeftOuter
        )
        """
        function_name = "Table.NestedJoin"
        depends_on = []
        used_columns = []
        produced_columns = []
        
        first_table = ctx.firstTable.getText()
        depends_on.append(first_table)

        
        for f_column in ctx.firstKeyColumns:
            used_columns.append(f_column.getText())
        
        for s_column in ctx.secondKeyColumns:
            used_columns.append(s_column.getText())
        
    
        return (function_name, depends_on, used_columns, produced_columns)

    def _analyzeExpandTableColumn(self, ctx: PowerQueryParser.TableExpandTableColumnFunctionContext):
        function_name = "Table.ExpandTableColumn"
        depends_on = []
        used_columns = []
        produced_columns = []

        table = ctx.table.getText()
        depends_on.append(table)

        return (function_name, depends_on, used_columns, produced_columns)

    def _analyzeGenericFunctionCall(self, ctx: PowerQueryParser.FunctionCallContext):
        function_name = ctx.IDENTIFIER().getText()
        depends_on = []
        used_columns = []
        produced_columns = []

        return (function_name, depends_on, used_columns, produced_columns)
