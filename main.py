from antlr4 import *
from src.PyM.PowerQueryLexer import PowerQueryLexer
from src.PyM.PowerQueryParser import PowerQueryParser
from src.PyM.visitors.TableNestedJoin import TableNestedJoinVisitor
import os

def main():

    file_path = os.path.join('queries', 'table_nested_join.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()

    input_stream = InputStream(query)
    lexer = PowerQueryLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PowerQueryParser(token_stream)
    tree = parser.program()
    
    # Optionally, print tokens
    token_stream.fill()
    #for token in token_stream.tokens:
    #    print(f"Token: {token.text}, Type: {lexer.symbolicNames[token.type]}")

    visitor = TableNestedJoinVisitor()
    visitor.visit(tree)
    print("Tables used:")
    for table in visitor.tables:
        print(f" - {table}")

    print("\nColumns used:")
    for column in visitor.columns:
        print(f" - {column}")

    print("\nOther Identifiers:")
    for identifier in visitor.other_identifiers:
        print(f" - {identifier}")

if __name__ == '__main__':
    main()


