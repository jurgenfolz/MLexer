
from ..PowerQueryParser import PowerQueryParser
from ..PowerQueryParserVisitor import PowerQueryParserVisitor



class AbstractVisitor(PowerQueryParserVisitor):
    
    def __init__(self):
        self.tables: list[str] = []
        self.columns:list[str] = []
        self.other_identifiers: list[str] = []
        


class TableNestedJoinVisitor(AbstractVisitor):
    def __init__(self):
        super().__init__() # Call the parent class constructor

    def visitTableNestedJoinFunction(self, ctx: PowerQueryParser.TableNestedJoinFunctionContext):
        # Tables
        table1 = ctx.firstTable.text
        table2 = ctx.secondTable.text
        self.tables.extend([table1, table2])

        # Column lists
        columns1 = [literal.getText().strip('"') for literal in ctx.firstKeyColumns.LITERAL()]
        columns2 = [literal.getText().strip('"') for literal in ctx.secondKeyColumns.LITERAL()]
        self.columns.extend([columns1, columns2])

        # New column name
        newColumnName = ctx.newColumnName.text.strip('"')
        self.other_identifiers.append(newColumnName)

        # Optional parameters
        if ctx.joinKind:
            joinKind = ctx.joinKind.text
            self.other_identifiers.append(joinKind)
        if ctx.keyEqualityComparer:
            keyEqualityComparer = ctx.keyEqualityComparer.getText()
            self.other_identifiers.append(keyEqualityComparer)

        return self.visitChildren(ctx)
