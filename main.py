from antlr4 import *
from src.PyM.PowerQueryLexer import PowerQueryLexer
from src.PyM.PowerQueryParser import PowerQueryParser
from src.PyM.PowerQueryParserVisitor import PowerQueryParserVisitor

class TableNestedJoinVisitor(PowerQueryParserVisitor):
    def __init__(self):
        self.tables = []
        self.columns = []
        self.other_identifiers = []

    def visitTableNestedJoinFunction(self, ctx:PowerQueryParser.TableNestedJoinFunctionContext):
        # Extract identifiers based on their positions in the parse tree
        identifiers = ctx.IDENTIFIER()
        if len(identifiers) >0:
           print(identifiers[0].getText())
        ctx.LITERAL()
        # Tables
        self.tables.append(identifiers[0].getText())
        self.tables.append(identifiers[2].getText())
        
        # Columns
        self.columns.append(identifiers[1].getText())
        self.columns.append(identifiers[3].getText())
        
        # Other Identifiers
        self.other_identifiers.extend(identifiers[4:])
        
        return self.visitChildren(ctx)

def main():

    with open('query.txt', 'r', encoding='utf-8') as file:
        query = file.read()

    input_stream = InputStream(query)
    lexer = PowerQueryLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PowerQueryParser(token_stream)
    tree = parser.program()
    
    # Optionally, print tokens
    token_stream.fill()
    #for token in token_stream.tokens:
        #rint(f"Token: {token.text}, Type: {lexer.symbolicNames[token.type]}")

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
        print(f" - {identifier.getText()}")

if __name__ == '__main__':
    main()


