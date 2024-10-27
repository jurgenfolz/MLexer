from antlr4 import *
from src.PyM.PowerQueryLexer import PowerQueryLexer
from src.PyM.PowerQueryParser import PowerQueryParser
from src.PyM.PowerQueryParserListener import PowerQueryParserListener

class PowerQueryListener(PowerQueryParserListener):
    def enterLet_expression(self, ctx):
        print("Entering a 'let' expression")

    def exitLet_expression(self, ctx):
        print("Exiting a 'let' expression")

    def enterVariable(self, ctx):
        var_name_ctx = ctx.variable_name()
        if var_name_ctx:
            var_name = var_name_ctx.getText()
            print(f"Variable declared: {var_name}")

    def enterFunction_expression(self, ctx):
        print("Entering a function expression")
        # You can extract more information here

class ColumnExtractorListener(PowerQueryParserListener):
    def __init__(self):
        self.columns = set()

    # Override methods to capture column names
    def enterField_selector(self, ctx):
        # field_selector: required_field_selector | optional_field_selector;
        required_selector = ctx.required_field_selector()
        optional_selector = ctx.optional_field_selector()
        if required_selector:
            field_name_ctx = required_selector.field_name()
        elif optional_selector:
            field_name_ctx = optional_selector.field_name()
        else:
            return

        if field_name_ctx:
            column_name = field_name_ctx.getText()
            self.columns.add(column_name)

    def enterField(self, ctx):
        # field: field_name EQUALS expression;
        field_name_ctx = ctx.field_name()
        if field_name_ctx:
            field_name = field_name_ctx.getText()
            self.columns.add(field_name)
            
    def enterLiteral_expression(self, ctx):
        # literal_expression: LITERAL;
        literal = ctx.LITERAL()
        if literal:
            # Remove quotes if necessary
            text = literal.getText().strip('"\'')
            self.columns.add(text)




def main():
    with open('query.txt', 'r', encoding='utf-8') as file:
        query = file.read()

    input_stream = InputStream(query)

    lexer = PowerQueryLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = PowerQueryParser(token_stream)

    parse_tree = parser.document()

    listener = ColumnExtractorListener()
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)

    print("Columns referenced in the script:")
    for column in listener.columns:
        print(column)

if __name__ == '__main__':
    main()
