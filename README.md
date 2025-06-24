PyM - Power Query M Lexer
=========================

`PyM` is a simple package that **tokenises** and **analyses** Microsoft **Power Query M** code. It builds an ANTLR-generated lexer and a class so you can work with M scripts straight from Python.

**Credits**: This package uses a Power Query M lexer grammar adapted from the excellent ANTLR grammars-v4 repository.
Original grammar authors deserve full credit for the work. Modifications were made for Python compatibility and additional token channel support.(https://github.com/antlr/grammars-v4/blob/master/powerquery/PowerQueryLexer.g4). 



Features
----------
- **Remove or collect comments** (single-line `//` and block `/* ... */`).
- **Iterate over every token**, keywords, literals, punctuation, whitespace.
- No ANTLR jar needed **at runtime**, only once when you regenerate the lexer.

Quick start
--------------
Optional, only install if you are going to change the PowerQueryLexer.G4 in the future\
`pip install antlr4-python3-runtime`

```python
from src.PyM.MExpression import MExpression

code = """
let
    // single-line comment
    source = 1 + 2,
/* multi
   line */
    result = source
in
    result
"""

expr = MExpression(code)

print(expr.remove_comments())
# let     source = 1 + 2,     result = source in     result

print(expr.extract_comments())
# ['// single-line comment', '/* multi\n   line */']

expr.print_tokens()                 # dump token stream
expr.write_tokens_to_txt("tokens.txt")`
```

Reminder to self
-------------------
Use this to regenerate the lexer
`java -Xmx500M -cp antlr-4.13.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 src\PyM\PowerQueryLexer.g4`

This creates/updates `src/PyM/PowerQueryLexer.py`.

Roadmap
-----------

Planned additions:
-   Automatic code formatter
-   Usage detection: references to columns 

Contributions and ideas are welcome!