from antlr4 import *
from src.PyM.PowerQueryLexer import PowerQueryLexer
import time
def main():
    with open('query.txt', 'r', encoding='utf-8') as file:
        query = file.read()

    input_stream = InputStream(query)
    lexer = PowerQueryLexer(input_stream)
    
    lexer.reset()  # Reset the lexer to start from the beginning
    token: Token = lexer.nextToken() 
    while token.type != Token.EOF:
        if token.type ==lexer.TABLE_NESTED_JOIN:
            print(f"Token: {token.text}, Type: {lexer.symbolicNames[token.type]}")
        
        token: Token = lexer.nextToken() 
    

if __name__ == '__main__':
    main()
