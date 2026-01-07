import html

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
    
    def __getstate__(self):
        state = self.__dict__.copy()
        # Handle attributes that can't be pickled
        state["input_stream"] = None 
        state["lexer"] = None
        return state
    
    def __setstate__(self, state):
        self.__dict__.update(state)
        # Reinitialize attributes that were set to None
        self.input_stream = InputStream(self.m_expression)
        self.lexer = PowerQueryLexer(self.input_stream)
        self.lexer.removeErrorListeners()
        self._kind = self._classify()
        
    
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
    
    def _get_original_token_text(self, token: Token) -> str:
        """Return the exact slice from the original expression when possible."""
        expr = self.m_expression or ""
        fallback = getattr(token, "text", "") or ""
        if not expr:
            return fallback

        try:
            start = getattr(token, "start", None)
            stop = getattr(token, "stop", None)
            if isinstance(start, int) and isinstance(stop, int):
                if stop < start:
                    start, stop = stop, start
                if start >= len(expr) or stop < 0:
                    return fallback
                start = max(0, start)
                stop = min(len(expr) - 1, stop)
                if start <= stop:
                    return expr[start: stop + 1]
        except Exception:
            return fallback

        return fallback

    def generate_html(self, light: bool = True) -> str:
        dark_palette = {
            "bg":        "#1e1e1e",
            "text":      "#d4d4d4",
            "keyword":   "#569cd6",
            "operator":  "#d4d4d4",
            "identifier": "#dcdcaa",
            "number":    "#b5cea8",
            "string":    "#ce9178",
            "comment":   "#6a9955",
        }
        light_palette = {
            "bg":        "#ffffff",
            "text":      "#000000",
            "keyword":   "#0000ff",
            "operator":  "#333333",
            "identifier": "#795e26",
            "number":    "#008000",
            "string":    "#a31515",
            "comment":   "#008000",
        }
        palette = light_palette if light else dark_palette

        html_parts: list[str] = [
            f'<pre style="font-family: Consolas, monospace; '
            f'background:{palette["bg"]}; color:{palette["text"]}; padding:8px;">'
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

        irr_channel = getattr(PowerQueryLexer, "IRRELEVANTCHARS", -1)
        comment_channel = getattr(PowerQueryLexer, "COMMENTCHANNEL", -2)
        self.lexer.reset()
        tok: Token = self.lexer.nextToken()
        while tok.type != Token.EOF:

            # keep whitespace / EOL exactly as they are
            if tok.channel == irr_channel:
                safe_text = html.escape(self._get_original_token_text(tok), quote=False)
                html_parts.append(safe_text)
                tok = self.lexer.nextToken()
                continue

            # comments
            if tok.channel == comment_channel:
                safe_text = html.escape(self._get_original_token_text(tok), quote=False)
                html_parts.append(f'<span style="color:{palette["comment"]};">{safe_text}</span>')
                tok = self.lexer.nextToken()
                continue

            safe_text = html.escape(self._get_original_token_text(tok), quote=False)
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

            html_parts.append(f'<span style="color:{palette[style]};">{safe_text}</span>')
            tok = self.lexer.nextToken()

        html_parts.append("</pre>")
        return "".join(html_parts)
    
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

        # standalone function definition
        if tok.type == PowerQueryLexer.OPEN_PAREN:
            if self._has_arrow_before((Token.EOF,), tok):
                return "function"
            return "query"

        # identifier assignment without let/in
        if tok.type == PowerQueryLexer.IDENTIFIER:
            ahead = self._next_sig()
            if ahead.type == PowerQueryLexer.EQUALS:
                after_equals = self._next_sig()
                if after_equals.type == PowerQueryLexer.OPEN_PAREN and self._has_arrow_before((Token.EOF,), after_equals):
                    return "function"
                return "query"
            return "parameter"

        # parameter: literal or identifier at top level #*Easy peasy
        if tok.type not in (PowerQueryLexer.LET,):
            return "parameter"

        # we are inside outer let-block
        # Identifier for functions =  (stuff)  => function
        # otherwise query
        # skip after LET
        tok = self._next_sig(tok)
        if tok.type != PowerQueryLexer.IDENTIFIER:
            return "query"
        tok = self._next_sig()
        if tok.type != PowerQueryLexer.EQUALS:
            return "query"
        tok = self._next_sig()
        if tok.type == PowerQueryLexer.OPEN_PAREN and self._has_arrow_before((Token.EOF, PowerQueryLexer.IN), tok):
            return "function"
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

    def _has_arrow_before(self, stop_tokens: tuple[int, ...], current: Token | None = None) -> bool:
        tok = self._next_sig(current)
        while tok.type not in stop_tokens:
            if tok.type == PowerQueryLexer.ARROW:
                return True
            tok = self._next_sig()
        return False
    
    #enregion #*Classification Methods






