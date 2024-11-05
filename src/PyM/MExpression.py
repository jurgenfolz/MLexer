from antlr4 import InputStream, CommonTokenStream
from .PowerQueryLexer import PowerQueryLexer
from .PowerQueryParser import PowerQueryParser
from .visitors.MExpressionVisitors import MExpressionVisitor


class MExpression:
    def __init__(self, m_code: str):
        
        self.input_stream = InputStream(m_code)
        self.lexer = PowerQueryLexer(self.input_stream)
        self.token_stream = CommonTokenStream(self.lexer)
        self.parser = PowerQueryParser(self.token_stream)
        self.program_context: PowerQueryParser.ProgramContext = self.parser.program()
        self.visitor = MExpressionVisitor(self.program_context)    

    
    def _visit(self):
        self.visitor.visit()
        