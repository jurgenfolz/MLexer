from antlr4 import InputStream, Token
from .PowerQueryLexer import PowerQueryLexer

class MExpression:
    def __init__(self, m_expression: str):
        m_expression = "" if not isinstance(m_expression, str) else m_expression
        self.m_expression: str = m_expression
        self.input_stream: InputStream = InputStream(m_expression)
        self.lexer: PowerQueryLexer = PowerQueryLexer(self.input_stream)
        #self.lexer.removeErrorListeners()
    
    def __str__(self) -> str:
        """Returns the M expression as a string"""
        return self.m_expression
        
    def remove_comments(self) -> str:
        """Removes comments from the M expression

        Returns:
            str: M expression without comments
        """
        self.lexer.reset()  # Reset the lexer to start from the beginning
        token: Token = self.lexer.nextToken()
        result: list = []

        while token.type != Token.EOF:
            if token.channel != PowerQueryLexer.COMMENTCHANNEL:
                result.append(token.text)
            
            token = self.lexer.nextToken()
        
        return ''.join(result)
    
    def extract_comments(self) -> list[str]:
        """Extracts comments from the DAX expression

        Returns:
            list[str]: List of comments in the DAX expression
        """
        self.lexer.reset()  # Reset the lexer to start from the beginning
        comments: list[str] = []
        token: Token = self.lexer.nextToken()
        
        while token.type != Token.EOF:
            if token.channel == PowerQueryLexer.COMMENTCHANNEL:
                comments.append(token.text)
            
            token = self.lexer.nextToken()
        
        return comments
        
    
    def print_tokens(self, ignore_irrelevant_chars: bool = True) -> None: 
        """Prints the tokens of the M expression"""
        self.lexer.reset()
        token: Token = self.lexer.nextToken()
        while token.type != Token.EOF:
            
            if ignore_irrelevant_chars and token.channel == PowerQueryLexer.IRRELEVANTCHARS:
                token = self.lexer.nextToken()
                continue
            
            print(f"Token: {token.text}, Type: {self.lexer.symbolicNames[token.type]}, Number: {token.type}")
            token = self.lexer.nextToken()
    
    def write_tokens_to_txt(self, file_path: str) -> None:
        """Writes the tokens of the M expression to a text file

        Args:
            file_path (str): Path to the output text file
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            self.lexer.reset()
            token: Token = self.lexer.nextToken()
            while token.type != Token.EOF:
                file.write(f"Token: {token.text}, Type: {self.lexer.symbolicNames[token.type]}, Number: {token.type}\n")
                token = self.lexer.nextToken()
                
    