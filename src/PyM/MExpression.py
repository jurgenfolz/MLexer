from antlr4 import InputStream, Token
from src.PyM.PowerQueryLexer import PowerQueryLexer

class MExpression:
    def __init__(self, m_expression: str):
        m_expression = "" if not isinstance(m_expression, str) else m_expression
        self.m_expression: str = m_expression
        self.input_stream: InputStream = InputStream(m_expression)
        self.lexer: PowerQueryLexer = PowerQueryLexer(self.input_stream)
        self.lexer.removeErrorListeners()
        
        
    def remove_comments(self) -> str:
        """Removes comments from the M expression

        Returns:
            str: M expression without comments
        """
        self.lexer.reset()  # Reset the lexer to start from the beginning
        token: Token = self.lexer.nextToken()
        result: list = []

        while token.type != Token.EOF:
            if token.channel != PowerQueryLexer.COMMENT:
                result.append(token.text)
            token = self.lexer.nextToken()
        
        return ''.join(result)
    
    def print_tokens(self):
        """Prints the tokens of the M expression"""
        self.lexer.reset()
        token: Token = self.lexer.nextToken()
        while token.type != Token.EOF:
            print(f"Token: {token.text}, Type: {self.lexer.symbolicNames[token.type]}, Number: {token.type}")
            token = self.lexer.nextToken()
            