from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from .PowerQueryLexer import PowerQueryLexer
from .PowerQueryParser import PowerQueryParser
from .PowerQueryParserListener import PowerQueryParserListener  # Import if you generated a listener


class MExpression:
    def __init__(self, query_m_code: str):
        pass