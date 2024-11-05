from antlr4 import InputStream, CommonTokenStream, Token
from .PowerQueryLexer import PowerQueryLexer
from .PowerQueryParser import PowerQueryParser
from .visitors.MExpressionVisitors import MExpressionVisitor


class MExpression:
    def __init__(self, m_code: str):
        
        self.input_stream = InputStream(m_code)
        self.lexer = PowerQueryLexer(self.input_stream)
        self.token_stream = CommonTokenStream(self.lexer)
        self.parser = PowerQueryParser(self.token_stream)
        
        """token: Token = self.lexer.nextToken()
        while token.type != Token.EOF:
            print(token.text, self.lexer.symbolicNames[token.type])
            token = self.lexer.nextToken()
        
        self.token_stream.fill()"""
        
        self.program_context: PowerQueryParser.ProgramContext = self.parser.program()
        self.visitor = MExpressionVisitor(self.program_context)    

    
    def _visit(self):
        self.visitor.visit()
        