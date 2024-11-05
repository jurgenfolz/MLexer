
from ..PowerQueryParser import PowerQueryParser
from ._AbstractVisitor import AbstractVisitor
from ..PowerQueryParserVisitor import PowerQueryParserVisitor

    

class TableNestedJoinVisitor(PowerQueryParserVisitor):
    def __init__(self):
        self.tables: list[str] = []
        self.columns:list[str] = []
        self.other_identifiers: list[str] = []

    
    def visitTableNestedJoinFunction(self, ctx: PowerQueryParser.TableNestedJoinFunctionContext):
        # Tables
        table1: str = ctx.firstTable.text
        table2: str = ctx.secondTable.text
        self.tables.extend([table1, table2])

        # Column lists
        columns1: list[str] = [literal.getText().strip('"') for literal in ctx.firstKeyColumns.LITERAL()]
        columns2:list[str] = [literal.getText().strip('"') for literal in ctx.secondKeyColumns.LITERAL()]
        self.columns.extend([columns1, columns2])

        # New column name
        newColumnName = ctx.newColumnName.text.strip('"')
        self.other_identifiers.append(newColumnName)

        #! Optional parameters
        
        if ctx.joinKind:
            joinKind = ctx.joinKind.text
            self.other_identifiers.append(joinKind)
        
        if ctx.keyEqualityComparer:
            keyEqualityComparer = ctx.keyEqualityComparer.getText()
            self.other_identifiers.append(keyEqualityComparer)

        return self.visitChildren(ctx)


class TableExpandTableColumnVisitor(PowerQueryParserVisitor):
    def __init__(self):
        self.tables: list[str] = []
        self.columns:list[str] = []
        self.other_identifiers: list[str] = []

    def visitTableExpandTableColumnFunction(self, ctx: PowerQueryParser.TableExpandTableColumnFunctionContext):
        
        self.tables.append(ctx.table.text)
        self.columns.extend([literal.getText().strip('"') for literal in ctx.columnsList.LITERAL()])        
