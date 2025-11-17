# Contributing to MLexer / PyM

Thanks for your interest in improving this project! This guide describes how to set up your environment, make changes, and submit pull requests that are easy to review.

## Prerequisites

- Python 3.11.8
- Optional (only needed when editing the grammars):
  - Java 8+ and the ANTLR jar in repo root (`antlr-4.13.2-complete.jar`)
  - `antlr4-python3-runtime` for running generated parsers in Python

## Getting started

1. Create and activate a virtual environment.
2. Install dependencies:
   - Runtime is intentionally minimal. If you plan to regenerate grammars:
     - `pip install antlr4-python3-runtime`
3. Run the sample harness to verify things work:
   - `python .\main.py` (writes `summary.json`)

## Project layout

- `src/PyM/*.g4` – source grammars (edit these when changing the language)
- `src/PyM/*Parser.py`, `*Lexer.py` – generated; keep in sync with grammars
- `src/PyM/MExpression.py` – lexer helpers
- `src/PyM/ParserExplorer.py` – parser helpers
- `src/PyM/DataflowQuerySplitter.py` – dataflow query split utility
- `queries/` – sample M scripts used for manual testing/development
- `tests/` – add automated tests here (pytest)

## Regenerating grammar artifacts

When you change `PowerQueryLexer.g4` or `PowerQueryParser.g4`, regenerate:

```powershell
# From repo root (Windows PowerShell)
java -Xmx500M -cp .\antlr-4.13.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 .\src\PyM\PowerQueryLexer.g4
java -Xmx500M -cp .\antlr-4.13.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 .\src\PyM\PowerQueryParser.g4
```

Commit the updated `*.py`, `*.tokens`, and `*.interp` files.

## Code style

- Follow the repository’s STYLE.md.
- Prefer clear, explanatory comments for parser work; it helps future readers.
- Add type hints to new code.
- Keep changes small and focused.

## Testing

- Add unit tests under `tests/` for new features or bug fixes.
- Use small examples from `queries/` or add new ones if necessary.
- Keep test runtime fast; parsing large scripts should still complete quickly.

## Performance

- Use the SLL→LL fallback parse strategy in new parser utilities.
- Avoid grammar changes that introduce ambiguity or exponential prediction.
- If you see significant slowdowns on a sample query, capture a minimal repro and open an issue.

## Pull requests

- Describe the problem and the approach.
- Call out any grammar changes explicitly and note effects on prediction.
- Include before/after timings if you changed parsing behavior.

## Questions

Open an issue with a minimal code sample and steps to reproduce. Contributions and ideas are very welcome!