from antlr4 import InputStream, CommonTokenStream, Token
from .PowerQueryLexer import PowerQueryLexer 
from .PowerQueryParser import PowerQueryParser
from antlr4.tree.Tree import TerminalNodeImpl
from .MVisitor import MVisitor, TreePrinterVisitor
import json

class MExpression:
    def __init__(self, m_code: str):
        self.m_code = m_code

    def print_tokens(self):
        # Create an ANTLR input stream from the code string
        input_stream = InputStream(self.m_code)

        # Instantiate the lexer with that input stream
        lexer = PowerQueryLexer(input_stream)

        # Wrap the lexer in a token stream (though here we only need the raw tokens)
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()  # Force it to lex all tokens

        # Iterate over each token in the token stream
        for token in token_stream.tokens:
            if token.type == Token.EOF:
                # End-of-file token; skip printing
                continue

            line_number = token.line
            token_text = token.text
            # If token.type is within the symbolic names range, retrieve its name:
            token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else str(token.type)

            # Print the line number, token text, and token type name
            print(f"Line {line_number}: '{token_text}' => {token_name}")

    def build_dataflow(self):
        input_stream = InputStream(self.m_code)
        lexer = PowerQueryLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = PowerQueryParser(token_stream)
        
        tree = parser.program()
        visitor = MVisitor()
        steps_map = visitor.visit(tree)

        print('Steps Map:', steps_map)
        return steps_map

    def print_tree(self):
        input_stream = InputStream(self.m_code)
        lexer = PowerQueryLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = PowerQueryParser(token_stream)
        
        tree = parser.program()
        visitor = TreePrinterVisitor()
        visitor.visit(tree)
    
    #region printers
    def print_parse_tree(self):
        """
        Parses the M code using the generated parser and prints
        a textual (Lisp-like) representation of the parse tree.
        """
        input_stream = InputStream(self.m_code)
        lexer = PowerQueryLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        
        # Create the parser
        parser = PowerQueryParser(token_stream)
        
        # The top-level rule in your grammar is called 'program' (adjust if needed)
        tree = parser.program()
        
        # Convert the parse tree to a string (Lisp-style)
        parse_tree_str = tree.toStringTree(recog=parser)
        
        print("Parse Tree (Lisp-style):")
        print(parse_tree_str)
        
    def print_parse_tree_as_json(self, path):
        """
        Parses the M code, builds a JSON-like object of the parse tree,
        and prints it out with indentation.
        """
        input_stream = InputStream(self.m_code)
        lexer = PowerQueryLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = PowerQueryParser(token_stream)

        # Parse using your top-level rule (adjust if needed)
        tree = parser.program()

        # Convert the parse tree to a Python dict
        tree_dict = self._parse_tree_to_dict(tree, parser)

        # Serialize it to JSON and print
        with open(path, 'w') as file:
            json.dump(tree_dict, file, indent=4)
        
    def _parse_tree_to_dict(self, node, parser):
        """
        Recursively builds a dictionary from the ANTLR parse tree node.
        """
        if node is None:
            return None

        # If it's a terminal node (a token / leaf), return its text
        if isinstance(node, TerminalNodeImpl):
            token_text = node.getText()
            token_type = parser.symbolicNames[node.getSymbol().type] if node.getSymbol().type < len(parser.symbolicNames) else str(node.getSymbol().type)
            return {
                "type": "terminal",
                "tokenText": token_text,
                "tokenName": token_type
            }

        # Otherwise, it's a parser rule context
        rule_index = node.getRuleIndex()
        rule_name = parser.ruleNames[rule_index]

        # Collect children in a list
        children = []
        if node.children:
            for child in node.children:
                children.append(self._parse_tree_to_dict(child, parser))

        return {
            "type": "rule",
            "ruleName": rule_name,
            "children": children
        }
    #endregion