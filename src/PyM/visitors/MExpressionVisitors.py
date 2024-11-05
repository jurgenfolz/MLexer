from .TableNestedJoin import TableNestedJoinVisitor, TableExpandTableColumnVisitor
from ._AbstractVisitor import AbstractVisitor
from ..PowerQueryParser import PowerQueryParser

class MExpressionVisitor:
    VISITORS: dict = {
        "TableNestedJoin": TableNestedJoinVisitor,
        "TableExpandTableColumn": TableExpandTableColumnVisitor
    }
    
    

    
    def __init__(self,program_context: PowerQueryParser.ProgramContext) -> None:
        self.program_context:PowerQueryParser.ProgramContext = program_context
        
    
    def visit(self):
        for visitor_name, visitor_class in self.VISITORS.items():
            visitor = visitor_class()
            visitor.visit(self.program_context)
            
            print(f"\n{visitor_name}:\n")
            print("Tables used:")
            for table in visitor.tables:
                print(f" - {table}")

            print("\nColumns used:")
            for column in visitor.columns:
                print(f" - {column}")

            print("\nOther Identifiers:")
            for identifier in visitor.other_identifiers:
                print(f" - {identifier}")