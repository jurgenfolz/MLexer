# MLexer / PyM – Architecture Overview

This repository provides a Python-friendly way to lex and parse Power Query M code using ANTLR-generated components, plus simple utilities to explore tokens and parse trees.

## Key modules

- `src/PyM/PowerQueryLexer.g4`
  - ANTLR lexer grammar for M. Channels split comments (`COMMENTCHANNEL`) and whitespace (`IRRELEVANTCHARS`) from the main token stream.
- `src/PyM/PowerQueryParser.g4`
  - ANTLR parser grammar for M. Structured to prefer predictive constructs first and avoid ambiguity (e.g., `primary_expression` is an atom with iterative suffixes).
- Generated artifacts
  - `src/PyM/PowerQueryLexer.py`, `src/PyM/PowerQueryParser.py`, `*.tokens`, `*.interp`, `.antlr/` files.
  - Checked in for convenience. Regenerate when grammars change.
- `src/PyM/MExpression.py`
  - Lexer-only helpers for comment removal, token printing, and simple searches.
- `src/PyM/ParserExplorer.py`
  - Parser helper with SLL→LL fallback, pretty tree printing, and a summary listener that collects identifiers, field selectors, and section access.
- `src/PyM/DataflowQuerySplitter.py`
  - Splits Dataflow text into named queries using the lexer's token channels; preserves formatting.
- `main.py`
  - Small harness demonstrating parse and summarization.

## Data flows

1. Input (M code) → `PowerQueryLexer` → token stream
   - Comments/whitespace go to side channels so they won't disturb the parser.
2. Token stream → `PowerQueryParser` → parse tree
   - Parser uses a 2-stage strategy:
     - SLL + `BailErrorStrategy()` (fast path)
     - On failure, reset and retry LL + `DefaultErrorStrategy()` (robust path)
3. Parse tree → listeners/visitors
   - `ParserExplorer.collect_summary()` walks the tree to extract identifiers and selectors with line/column metadata.

## Parsing strategy

- Start rule candidates: `document`, then `expression_document`, then `expression`.
- Grammar orders alternatives with distinct leading tokens first (e.g., `let`, `if`, `each`) to help SLL decide quickly.
- Ambiguous constructs (like identifier-based primary expressions) are shaped to reduce backtracking by using atom + suffix loops.

## Extensibility

- Add more listeners/visitors under `src/PyM/` for specific analyses:
  - Column lineage: detect `[Field]` selectors, `ExpandTableColumn`, `NestedJoin` patterns.
  - Function boundaries: map parameter types and return assertions.
  - Type expressions: identify `type table [..]` and capture schema.
- Keep utilities returning plain dicts/lists for easy JSON export.

## Regenerating grammar artifacts

- Prereqs: Java and ANTLR jar available at repo root.
- Typical regenerate commands (Windows PowerShell):

```powershell
# Lexer
java -Xmx500M -cp .\antlr-4.13.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 .\src\PyM\PowerQueryLexer.g4

# Parser (listener/visitor optional; enable if you need them)
java -Xmx500M -cp .\antlr-4.13.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 .\src\PyM\PowerQueryParser.g4
```

Commit both the `.py` and `.tokens/.interp` updates to keep the repo reproducible.

## Future goals (kept in mind)

- Identify columns and tables referenced in each step (lineage):
  - Extract field selectors and connect them to source tables via joins/expands.
  - Map step names on the left of `=` to the operations on the right.
- Performance guardrails:
  - Keep the SLL→LL fallback.
  - Avoid grammar patterns that cause exponential prediction.

## Constraints and assumptions

- Python 3.10+; no heavy runtime deps (antlr4-python3-runtime only when needed).
- Case-insensitive lexer is used; keyword/identifier rules reflect M semantics.
- We preserve comments/whitespace in some tools; parser ignores them by channel.

---
This document is a living map; update when the module layout or grammar structure changes.