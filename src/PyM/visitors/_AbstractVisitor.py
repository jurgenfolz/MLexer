from ..PowerQueryParserVisitor import PowerQueryParserVisitor

class AbstractVisitor(PowerQueryParserVisitor):
    
    def __init__(self):
        self.tables: list[str] = []
        self.columns:list[str] = []
        self.other_identifiers: list[str] = []