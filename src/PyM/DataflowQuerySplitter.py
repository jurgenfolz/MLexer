# src/PyM/MQuerySplitter.py
from antlr4 import InputStream, Token
from .PowerQueryLexer import PowerQueryLexer


# src/PyM/MQuerySplitter.py
from antlr4 import InputStream, Token
from .PowerQueryLexer import PowerQueryLexer


def dataflow_split_queries(m_expression: str) -> dict[str, str]:
    """
    Return {query_name: query_text_without_shared_header},
    preserving whitespace and comments.
    """
    lexer = PowerQueryLexer(InputStream(m_expression))
    lexer.reset()

    IRR = getattr(PowerQueryLexer, "IRRELEVANTCHARS", -1)
    CMT = getattr(PowerQueryLexer, "COMMENTCHANNEL", -2)

    queries: dict[str, str] = {}
    current_name: str | None = None
    buffer: list[str] = []

    expecting_name = False
    expecting_equals = False
    capturing = False

    tok: Token = lexer.nextToken()
    while tok.type != Token.EOF:

        # new 'shared' starts a query header
        if tok.type == PowerQueryLexer.SHARED:
            if current_name and buffer:
                queries[current_name] = "".join(buffer).rstrip()
            current_name = None
            buffer.clear()
            capturing = False
            expecting_name = True
            expecting_equals = False
            tok = lexer.nextToken()
            continue

        # identifier after 'shared'
        if expecting_name and tok.type == PowerQueryLexer.IDENTIFIER:
            current_name = tok.text
            expecting_name = False
            expecting_equals = True
            tok = lexer.nextToken()
            continue

        # equal sign after identifier
        if expecting_equals and tok.type == PowerQueryLexer.EQUALS:
            expecting_equals = False
            capturing = True          # start capturing *after* '='
            tok = lexer.nextToken()
            continue  # skip the '=' itself

        # stop at top-level semicolon
        if capturing and tok.type == PowerQueryLexer.SEMICOLON:
            if current_name and buffer:
                queries[current_name] = "".join(buffer).rstrip()
            buffer.clear()
            capturing = False
            current_name = None
            tok = lexer.nextToken()
            continue

        # append tokens while capturing
        if capturing and tok.channel in (Token.DEFAULT_CHANNEL, IRR, CMT):
            buffer.append(tok.text)

        tok = lexer.nextToken()

    # last query
    if current_name and buffer:
        queries[current_name] = "".join(buffer).rstrip()

    return queries

