from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from .PowerQueryLexer import PowerQueryLexer
from .PowerQueryParser import PowerQueryParser
from .visitors import Visitors


class MExpression:
    def __init__(self, m_code: str):
        
        input_stream = InputStream(m_code)
        lexer = PowerQueryLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = PowerQueryParser(token_stream)
        self.tree = parser.program()
        

    
    def visit_table_nested_join(self):
        visitor = Visitors.TableNestedJoinVisitor()
        visitor.visit(self.tree)
        
    
        print("Tables used:")
        for table in visitor.tables:
            print(f" - {table}")

        print("\nColumns used:")
        for column in visitor.columns:
            print(f" - {column}")

        print("\nOther Identifiers:")
        for identifier in visitor.other_identifiers:
            print(f" - {identifier}")