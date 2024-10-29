from antlr4 import *
from src.PyM.PowerQueryLexer import PowerQueryLexer

def main():
    with open('query.txt', 'r', encoding='utf-8') as file:
        query = file.read()

    input_stream = InputStream(query)
    lexer = PowerQueryLexer(input_stream)
    
    lexer.reset()  # Reset the lexer to start from the beginning
    token: Token = lexer.nextToken() 
    while token.type != Token.EOF:
        if token.type == PowerQueryLexer.COLUMN_REFERENCE:
            print(f"COLUMN_REFERENCE: {token.text}")
        if token.type == PowerQueryLexer.IDENTIFIER:
            print(f"IDENTIFIER: {token.text}")
        if token.type == PowerQueryLexer.REGULAR_IDENTIFIER:
            print(f"REGULAR_IDENTIFIER: {token.text}")
        if token.type == PowerQueryLexer.AVAILABLE_IDENTIFIER:
            print(f"AVAILABLE_IDENTIFIER: {token.text}")
        if token.type == PowerQueryLexer.KEYWORD_OR_IDENTIFIER:
            print(f"KEYWORD_OR_IDENTIFIER: {token.text}")
        
        token: Token = lexer.nextToken() 
    

if __name__ == '__main__':
    main()
