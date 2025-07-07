from antlr4 import InputStream, Token
from typing import Literal

from .PowerQueryLexer import PowerQueryLexer

class MExpression:
    def __init__(self, m_expression: str):
        m_expression = "" if not isinstance(m_expression, str) else m_expression
        self.m_expression: str = m_expression
        self.input_stream: InputStream = InputStream(m_expression)
        self.lexer: PowerQueryLexer = PowerQueryLexer(self.input_stream)
        self.lexer.removeErrorListeners()
        
        self.m_expression_no_comments: str = self.remove_comments()
        self._kind: Literal["parameter", "query", "function"] = self._classify()
     
    def __str__(self) -> str:
        """Returns the M expression as a string"""
        return self.m_expression
    
    
    @property
    def is_parameter(self) -> bool:
        return self._kind == "parameter"

    @property
    def is_query(self) -> bool:
        return self._kind == "query"
    
    @property
    def is_function(self) -> bool:
        return self._kind == "function"
    
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
    
    def find_identifier_occurrences(self, identifier: str) -> list[tuple[int, int]]:
        """
        Finds all occurrences of a given identifier in the M expression.

        Args:
            identifier (str): The identifier to search for.

        Returns:
            list[tuple[int, int]]: A list of tuples where each tuple contains the line number and column number
        """
        
        id_lower = identifier.lower()
        matches: list[tuple[int, int]] = []
        self.lexer.reset()
        tok: Token = self.lexer.nextToken()
        while tok.type != Token.EOF:

            if tok.channel == Token.DEFAULT_CHANNEL and (tok.type == PowerQueryLexer.IDENTIFIER):
                
                if tok.text.lower() == id_lower:
                    matches.append((tok.line, tok.column + 1))

            tok = self.lexer.nextToken()

        return matches
    
    def find_literal_occurrences(self, identifier: str) -> list[tuple[int, int]]:
        """
        Finds all occurrences of a given literal in the M expression.

        Args:
            identifier (str): The identifier to search for.

        Returns:
            list[tuple[int, int]]: A list of tuples where each tuple contains the line number and column number
        """
        
        id_lower = identifier.lower()
        matches: list[tuple[int, int]] = []
        self.lexer.reset()
        tok: Token = self.lexer.nextToken()
        while tok.type != Token.EOF:

            if tok.channel == Token.DEFAULT_CHANNEL and (tok.type == PowerQueryLexer.LITERAL):
                
                if tok.text.lower() == id_lower:
                    matches.append((tok.line, tok.column + 1))
                elif id_lower in tok.text.lower():
                    # Literals will mostly contain the quotation marks, so we remove them for comparison
                    if tok.text.startswith('"') and tok.text.endswith('"') and id_lower in tok.text[1:-1].lower():
                        matches.append((tok.line, tok.column + 1))

            tok = self.lexer.nextToken()

        return matches
    
    def generate_html(self, light: bool = True) -> str:
        dark = {
            "bg":        "#1e1e1e",
            "text":      "#d4d4d4",
            "keyword":   "#569cd6",
            "operator":  "#d4d4d4",
            "identifier": "#dcdcaa",
            "number":    "#b5cea8",
            "string":    "#ce9178",
            "comment":   "#6a9955",
        }
        light = {
            "bg":        "#ffffff",
            "text":      "#000000",
            "keyword":   "#0000ff",
            "operator":  "#333333",
            "identifier": "#795e26",
            "number":    "#008000",
            "string":    "#a31515",
            "comment":   "#008000",
        }
        c = light if light else dark

        html: list[str] = [
            f'<pre style="font-family: Consolas, monospace; '
            f'background:{c["bg"]}; color:{c["text"]}; padding:8px;">'
        ]

        kw_tokens = {
            PowerQueryLexer.LET, PowerQueryLexer.IN, PowerQueryLexer.IF,
            PowerQueryLexer.THEN, PowerQueryLexer.ELSE, PowerQueryLexer.EACH,
            PowerQueryLexer.TRY, PowerQueryLexer.TYPE, PowerQueryLexer.META,
            PowerQueryLexer.SECTION, PowerQueryLexer.SHARED, PowerQueryLexer.AND,
            PowerQueryLexer.OR, PowerQueryLexer.NOT, PowerQueryLexer.OTHERWISE
        }
        op_tokens = {
            PowerQueryLexer.PLUS, PowerQueryLexer.MINUS, PowerQueryLexer.STAR,
            PowerQueryLexer.SLASH, PowerQueryLexer.AMP, PowerQueryLexer.LEQ,
            PowerQueryLexer.GEQ, PowerQueryLexer.GE, PowerQueryLexer.LE,
            PowerQueryLexer.NEQ, PowerQueryLexer.EQUALS, PowerQueryLexer.DOTDOT,
            PowerQueryLexer.ARROW, PowerQueryLexer.BANG, PowerQueryLexer.COMMA,
            PowerQueryLexer.SEMICOLON, PowerQueryLexer.OPEN_PAREN,
            PowerQueryLexer.CLOSE_PAREN, PowerQueryLexer.OPEN_BRACKET,
            PowerQueryLexer.CLOSE_BRACKET, PowerQueryLexer.OPEN_BRACE,
            PowerQueryLexer.CLOSE_BRACE
        }

        self.lexer.reset()
        tok: Token = self.lexer.nextToken()
        while tok.type != Token.EOF:

            # keep whitespace / EOL exactly as they are
            if tok.channel == getattr(PowerQueryLexer, "IRRELEVANTCHARS", -1):
                html.append(tok.text)
                tok = self.lexer.nextToken()
                continue

            # comments
            if tok.channel == getattr(PowerQueryLexer, "COMMENTCHANNEL", -2):
                html.append(f'<span style="color:{c["comment"]};">{tok.text}</span>')
                tok = self.lexer.nextToken()
                continue

            if tok.type in kw_tokens:
                style = "keyword"
            elif tok.type in op_tokens:
                style = "operator"
            elif tok.type == PowerQueryLexer.LITERAL:
                style = "string" if tok.text.startswith('"') or tok.text.startswith("#") else "number"
            elif tok.type == PowerQueryLexer.IDENTIFIER:
                style = "identifier"
            else:
                style = "text"

            html.append(f'<span style="color:{c[style]};">{tok.text}</span>')
            tok = self.lexer.nextToken()

        html.append("</pre>")
        return "".join(html)
    
    #region #*Classification Methods
    def _classify(self) -> str:
        self.lexer.reset()
        IRR = getattr(PowerQueryLexer, "IRRELEVANTCHARS", -1)
        CMT = getattr(PowerQueryLexer, "COMMENTCHANNEL", -2)

        tok: Token = self.lexer.nextToken()

        # optional “shared Name =”
        if tok.type == PowerQueryLexer.SHARED:
            while tok.type not in (PowerQueryLexer.EQUALS, Token.EOF):
                tok = self.lexer.nextToken()
            tok = self.lexer.nextToken()

        while tok.channel in (IRR, CMT):
            tok = self.lexer.nextToken()

        # parameter → literal or identifier at top level
        if tok.type not in (PowerQueryLexer.LET,):
            return "parameter"

        # we are inside outer let-block
        # seek: Identifier =  ( … )  => function
        # otherwise query
        # skip after LET
        tok = self._next_sig(tok)
        if tok.type != PowerQueryLexer.IDENTIFIER:
            return "query"
        tok = self._next_sig()
        if tok.type != PowerQueryLexer.EQUALS:
            return "query"
        tok = self._next_sig()
        if tok.type == PowerQueryLexer.OPEN_PAREN:
            # quick scan to confirm an ARROW appears before another LET/IN
            while tok.type not in (Token.EOF, PowerQueryLexer.IN):
                if tok.type == PowerQueryLexer.ARROW:
                    return "function"
                tok = self._next_sig()
        return "query"

    def _next_sig(self, current: Token | None = None) -> Token:
        IRR = getattr(PowerQueryLexer, "IRRELEVANTCHARS", -1)
        CMT = getattr(PowerQueryLexer, "COMMENTCHANNEL", -2)
        tok = current if current else self.lexer.nextToken()
        if current:  # start from already-fetched token
            tok = self.lexer.nextToken()
        while tok.channel in (IRR, CMT):
            tok = self.lexer.nextToken()
        return tok
    
    #enregion #*Classification Methods






