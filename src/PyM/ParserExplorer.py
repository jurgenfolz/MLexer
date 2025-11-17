from __future__ import annotations
from antlr4 import (
    InputStream,
    CommonTokenStream,
    ParserRuleContext,
    TerminalNode,
)
from antlr4.error.ErrorStrategy import BailErrorStrategy, DefaultErrorStrategy
from antlr4.atn.PredictionMode import PredictionMode
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Tree import ParseTree
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import ParseTreeVisitor
from antlr4 import ParseTreeWalker

# Import the generated lexer and parser so we can build the parse tree
from .PowerQueryLexer import PowerQueryLexer
from .PowerQueryParser import PowerQueryParser


class ParserExplorer:
    """High level wrapper around the PowerQuery parser."""

    def __init__(self, text: str) -> None:
        #Keep the original expressions for debugging and toStringTree usage
        self.text: str = text or ""
        
        self.input_stream = InputStream(self.text) #* Input stream is the stream of characters that the lexer will read from
        self.lexer = PowerQueryLexer(self.input_stream) #* The lexer takes the input stream and breaks it into tokens

        #Create the token stream consumed by the parser
        self.tokens = CommonTokenStream(self.lexer)

        #Create the parser instance
        self.parser = PowerQueryParser(self.tokens)

        # Suppress default console error messages; collect them quietly instead
        self._quiet_errors: list[dict] = []
        self._quiet_listener = _QuietErrorListener(self._quiet_errors)
        try:
            self.lexer.removeErrorListeners()
        except Exception:
            pass
        self.lexer.addErrorListener(self._quiet_listener)
        try:
            self.parser.removeErrorListeners()
        except Exception:
            pass
        self.parser.addErrorListener(self._quiet_listener)

        #rule names are useful when exploring the tree
        self.rule_names = list(getattr(self.parser, "ruleNames", []))

        # We'll populate these after calling parse
        self.tree: ParserRuleContext | None = None
        self.start_rule_name: str | None = None

    def parse(self, candidates: tuple[str, ...] = ("document", "expression_document", "expression")) -> ParserRuleContext:
        """Parse the input with a 2 strategies? for speed and robustness.

        1 - First try SLL prediction with a BailErrorStrategy (very fast, but aborts on ambiguity). 
        2 - If SLL fails, we reset the stream and retry with full LL prediction + default error recovery (slower, but robust).
        """
        
        # Choose the first start rule that exists in this parser
        self.start_rule_name = next((n for n in candidates if hasattr(self.parser, n)), None)
        if not self.start_rule_name:
            #! If the code hit this, it means the grammar changed rule names
            raise AttributeError(f"No expected start rule found. Available rules: {self.rule_names}")

        # FAST SLL + bail on error
        #* Basically: "Try to recognize this query as fast as possible, without thinking too hard about ambiguous cases.”
        self.parser._interp.predictionMode = PredictionMode.SLL #* very fast, but aborts on ambiguity
        self.parser._errHandler = BailErrorStrategy()
        self.parser.buildParseTrees = True

        try:
            self.tree = getattr(self.parser, self.start_rule_name)()
        except Exception:
            self.tokens.seek(0)
            self.parser.reset()
            self.parser._interp.predictionMode = PredictionMode.LL
            self.parser._errHandler = DefaultErrorStrategy()
            self.tree = getattr(self.parser, self.start_rule_name)()

        return self.tree

    # region #! Tree visualizers
    def to_string_tree(self) -> str:
        """Return ANTLR's compact Lisp-style string for the parse tree."""
        if not self.tree:
            raise RuntimeError("Call parse() first")
        return Trees.toStringTree(self.tree, ruleNames=self.rule_names, recog=self.parser)

    def pretty_tree(self, max_len: int = 48) -> str:
        """Return a human-friendly, indented tree with rule names and leaves.

        max_len truncates long leaf texts to keep it readable.
        """
        if not self.tree:
            raise RuntimeError("Call parse() first")

        lines: list[str] = []

        def _recurse(node: ParseTree, depth: int) -> None:
            indent = "  " * depth
            if isinstance(node, ParserRuleContext):
                rule = self.rule_names[node.getRuleIndex()] if self.rule_names else str(node.getRuleIndex())
                lines.append(f"{indent}{rule}")
                for i in range(node.getChildCount()):
                    _recurse(node.getChild(i), depth + 1)
            elif isinstance(node, TerminalNode):
                t = node.getSymbol()
                # Clean up and maybe truncate the token text for display
                text = t.text.replace("\n", "\\n").replace("\r", "\\r") if t.text is not None else ""
                if len(text) > max_len:
                    text = text[: max_len - 1] + "…"
                token_name = self.lexer.symbolicNames[t.type] if t.type < len(self.lexer.symbolicNames) else str(t.type)
                lines.append(f"{indent}{token_name}: '{text}' @({t.line},{t.column})")
            else:
                # Fallback for any other parse tree node types
                lines.append(f"{indent}{type(node).__name__}")

        _recurse(self.tree, 0)
        return "\n".join(lines)

    # endregion #! Tree visualizers
    
    
    def collect_summary(self) -> dict:
        """Walk the tree and collect identifiers, field selectors, section access etc...

        Returns a dict with simple lists to inspect.
        """
        if not self.tree:
            raise RuntimeError("Call parse() first")

        walker = ParseTreeWalker()
        listener = _SummaryListener(self.parser, self.lexer)
        walker.walk(listener, self.tree)
        return listener.as_dict()


    def find_all(self, rule_name: str) -> list[ParserRuleContext]:
        """Find all subtrees based on the `rule_name`."""
        if not self.tree:
            raise RuntimeError("Call parse() first")
        try:
            target_index = self.rule_names.index(rule_name)
        except ValueError:
            raise ValueError(f"Unknown rule '{rule_name}'. Known rules: {', '.join(self.rule_names)}")

        matches: list[ParserRuleContext] = []

        def _walk(node: ParseTree) -> None:
            if isinstance(node, ParserRuleContext) and node.getRuleIndex() == target_index:
                matches.append(node)
            if isinstance(node, ParserRuleContext):
                for i in range(node.getChildCount()):
                    _walk(node.getChild(i))

        _walk(self.tree)
        return matches

    def get_errors(self) -> list[dict]:
        """Return collected lexer/parser errors without printing to the terminal."""
        return list(self._quiet_errors)


class _SummaryListener:
    """A simple listener that collects:
    - all IDENTIFIER tokens (names)
    - field selectors ([Name] and [Name]?)
    - section access expressions (Section!Name)
    """

    def __init__(self, parser: PowerQueryParser, lexer: PowerQueryLexer) -> None:
        # Keep references for rule names and token types
        self.parser = parser
        self.lexer = lexer
        self.rule_names = list(getattr(parser, "ruleNames", []))

        # Track our current rule path as we enter/exit rules
        self._rule_stack: list[int] = []

        # Collected data:
        self.identifiers: list[dict] = []
        self.field_selectors: list[dict] = []
        self.section_access: list[dict] = []


    def enterEveryRule(self, ctx: ParserRuleContext):
        self._rule_stack.append(ctx.getRuleIndex())

    def exitEveryRule(self, ctx: ParserRuleContext):
        # Pop once per enter; safe even with errors
        if self._rule_stack:
            self._rule_stack.pop()


    def visitTerminal(self, node: TerminalNode):
        t = node.getSymbol()
        ttype = t.type

        # Collect IDENTIFIER tokens with coordinates.
        if ttype == PowerQueryLexer.IDENTIFIER:
            self.identifiers.append({
                "text": t.text,
                "line": t.line,
                "col": t.column,
                "path": self._debug_path(),  # which rules we're inside
            })

        #! Detect [Field] and [Field]? by checking current rule context path.
        if self._in_rule("required_field_selector") or self._in_rule("optional_field_selector"):
            # In these rules, the IDENTIFIER is the field name; 'OPTIONAL' token indicates the '?' suffix
            if ttype == PowerQueryLexer.IDENTIFIER:
                self.field_selectors.append({
                    "name": t.text,
                    "optional": self._in_rule("optional_field_selector"),
                    "line": t.line,
                    "col": t.column,
                })

        # While inside section_access_expression, remember IDENTIFIER tokens so
        # exitSection_access_expression can consolidate them into one record.
        if self._in_rule("section_access_expression") and ttype == PowerQueryLexer.IDENTIFIER:
            if not hasattr(self, "_sec_ids"):
                self._sec_ids = []
            # Store the terminal node itself so we can access text and coords
            self._sec_ids.append(node)

        """Section access expressions are parsed as a dedicated rule; we can grab
        the text when we leave that rule, but a simple approach is to watch
        for a path that includes 'section_access_expression' and capture both
        sides around '!'. Here we just collect IDENTIFIERs under that rule and
        finalize in exitEveryRule if two are seen."""

    def _in_rule(self, name: str) -> bool:
        """Return True if the current path includes a rule named `name`."""
        try:
            idx = self.rule_names.index(name)
        except ValueError:
            return False
        return idx in self._rule_stack

    def _debug_path(self) -> list[str]:
        """A human-friendly copy of the current rule stack for diagnostics."""
        return [self.rule_names[i] for i in self._rule_stack]

    # We override enter/exit specifically for section_access_expression so we
    # can accumulate the two identifiers and store a single record for it.
    def enterSection_access_expression(self, ctx: ParserRuleContext):
        # Temporary storage for this rule instance
        self._sec_ids: list[TerminalNode] = []

    def exitSection_access_expression(self, ctx: ParserRuleContext): 
        # If we collected two identifiers, save them as a single record
        ids: list[TerminalNode] = getattr(self, "_sec_ids", [])  # type: ignore[assignment]
        if len(ids) == 2:
            a, b = ids
            self.section_access.append({
                "section": a.getText(),
                "name": b.getText(),
                "line": a.getSymbol().line,
                "col": a.getSymbol().column,
            })
        # Clear temporary storage for safety
        self._sec_ids = [] 

    # While inside section_access_expression, gather IDENTIFIER terminals
    def visitErrorNode(self, node):  #not used, but present for completeness
        pass

    # Hook visitTerminal to collect identifiers under section_access_expression
    def enterEveryRule_collect_for_section(self, node):
        pass  # kept for illustration

    def visitTerminal_collect_section(self, node: TerminalNode):
        pass  # kept for illustration

    # Provide a stable dict output for consumers
    def as_dict(self) -> dict:
        return {
            "identifiers": self.identifiers,
            "field_selectors": self.field_selectors,
            "section_access": self.section_access,
        }


class _QuietErrorListener(ErrorListener):
    """An error listener that records errors instead of printing to stderr."""

    def __init__(self, bucket: list[dict]):
        super().__init__()
        self._bucket = bucket

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  # noqa: N802
        self._bucket.append({
            "line": line,
            "column": column,
            "message": msg,
            "symbol": getattr(offendingSymbol, "text", None),
            "exception": type(e).__name__ if e else None,
        })
