# MLexer / PyM – Style Guide

This document captures the house style for this repository so contributors (and Copilot Chat with @workspace) can stay consistent.

Applies to:
- Python source in `src/PyM` and top-level helpers like `main.py`
- ANTLR grammar files in `src/PyM/*.g4`
- Tests under `tests/`

## Python style

- Python version: 3.11.8
- Types: Use typing everywhere in new/modified code.
  - Prefer precise types (e.g., `list[str]` over `List[str]`).
  - Mark attributes with explicit types in `__init__`.
- Docstrings and comments:
  - Keep public functions/classes documented with short, action oriented docstrings.
  - Use line comments liberally when code is educational (as in `ParserExplorer`).
  - Avoid redundant or stale comments.
- Imports:
  - Standard library, third-party, then local imports (blank line between groups).
  - Inside the package, prefer relative imports (e.g., `from .PowerQueryLexer import PowerQueryLexer`).
  - In examples and top-level scripts, you may use absolute imports (`from src.PyM import ...`).
- Naming:
  - Modules, packages: `snake_case`.
  - Classes: `PascalCase`.
  - Functions/methods/variables: `snake_case`.
  - Constants: `UPPER_SNAKE_CASE`.
- Errors and logging:
  - Keep exceptions descriptive; raise early for programmer errors.
  - Prefer returning rich data structures over printing; leave logging to callers.
- Collections and returns:
  - Return simple serializable dicts/lists from utilities (e.g., summaries) when helpful.
  - When returning tokens or parse nodes, include coordinates `(line, col)` if practical.
- Performance-sensitive parsing:
  - Use the SLL→LL fallback pattern when parsing: SLL with `BailErrorStrategy`, then retry LL with `DefaultErrorStrategy` on failure.
  - Only build parse trees when you need to analyze them (`parser.buildParseTrees = True`).

## ANTLR grammar style (`*.g4`)

- Keep token names UPPER_CASE and rule names `snake_case`.
- Put constructs with distinct leading tokens first to help prediction.
- Avoid left recursion in parser rules; prefer iterative suffix patterns (as done for `primary_expression`).
- Add comments at decision points that are known ambiguity hot-spots.
- When adding rules, ensure the lexer and parser agree on keywords vs identifiers; update tests accordingly.
- Regeneration target: Python3. Keep `-listener -visitor` enabled when you need them.

## File layout

- `src/PyM/MExpression.py`: Lexer-powered utilities (comments removal, tokens, simple searches).
- `src/PyM/ParserExplorer.py`: Educational parser utilities (parse tree, walkers, summaries).
- `src/PyM/DataflowQuerySplitter.py`: Splits Dataflow files using lexer channels.
- `src/PyM/PowerQueryLexer.g4`, `PowerQueryParser.g4`: Grammars (source of truth for generated files).
- Generated artifacts (`*.py`, `*.tokens`, `.interp`, `.antlr/`) are checked in for convenience; keep them in sync with grammars.

## Testing

- Use `pytest` for tests (lightweight and common).
- Keep tests small and fast; include at least one sample per query in `queries/`.
- Prefer golden outputs for summaries and token streams when practical.

## Formatting & linting

- Formatting: follow PEP 8; if using a formatter, Black defaults are fine.
- Linting: Ruff or flake8 are fine. Don’t introduce lints you can’t keep green.

## Git hygiene

- Small, focused commits with imperative messages: “Add ParserExplorer summary listener”.
- Branch per feature or fix.
- PRs should summarize problem, approach, and any grammar changes that affect prediction.

## Using with Copilot Chat (@workspace)

- Prompt example: `@workspace use our STYLE.md and ARCHITECTURE.md; add a visitor that collects all [field] selectors with coordinates.`
- Keep prompts concrete: mention the files or rules you want changed.

---
This style guide evolves with the codebase. Propose changes via PR when something becomes a standard pattern.