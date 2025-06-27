# src/PyM/MQuerySplitter.py
from antlr4 import InputStream, Token
from .PowerQueryLexer import PowerQueryLexer


# src/PyM/MQuerySplitter.py
from antlr4 import InputStream, Token
from .PowerQueryLexer import PowerQueryLexer


def dataflow_split_queries(m_expression: str) -> dict[str, str]:
    """
    Return {query_name: query_text}
    """
    
    lexer = PowerQueryLexer(InputStream(m_expression))
    lexer.reset()

    IRR = getattr(PowerQueryLexer, "IRRELEVANTCHARS", -1)
    CMT = getattr(PowerQueryLexer, "COMMENTCHANNEL", -2)

    queries: dict[str, str] = {}
    current_name: str | None = None
    buffer: list[str] = []

    expecting_name = False
    capturing = False

    tok: Token = lexer.nextToken()
    while tok.type != Token.EOF:

        #'shared' starts a new query
        if tok.type == PowerQueryLexer.SHARED:
            # flush previous
            if current_name and buffer:                     
                queries[current_name] = "".join(buffer).rstrip()
            current_name = None
            buffer.clear()
            capturing = False
            expecting_name = True
            tok = lexer.nextToken()
            continue

        #identifier after 'shared' becomes the key
        if expecting_name and tok.type == PowerQueryLexer.IDENTIFIER:
            current_name = tok.text
            expecting_name = False
            tok = lexer.nextToken()
            continue  #don't include the query name itself

        # start buffering at first 'let'
        if not capturing and tok.type == PowerQueryLexer.LET:
            capturing = True
            buffer.append(tok.text)
            tok = lexer.nextToken()
            continue

        # append tokens once capturing
        if capturing and tok.channel in (Token.DEFAULT_CHANNEL, IRR, CMT):
            buffer.append(tok.text)

        tok = lexer.nextToken()

    # flush last query
    if current_name and buffer:
        queries[current_name] = "".join(buffer).rstrip()

    return queries

