import re

TOKEN_SPEC = [
    ('FLOAT',    r'\d+\.\d+'),                        # Float
    ('INT',      r'\d+'),                             # Integer
    ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),          # Identifiers
    ('ASSIGN',   r'='),                               # Assignment
    ('END',      r';'),                               # End statement
    ('OP',       r'[+\-*/]'),                         # Arithmetic operators
    ('LBRACE',   r'\{'),                              # Left brace
    ('RBRACE',   r'\}'),                              # Right brace
    ('LPAREN',   r'\('),                              # Left paren
    ('RPAREN',   r'\)'),                              # Right paren
    ('STRING',   r'"[^"]*"'),                         # String literals
    ('SKIP',     r'[ \t]+'),                          # Skip spaces/tabs
    ('NEWLINE',  r'\n'),                              # Newlines
    ('MISMATCH', r'.'),                               # Anything else
]

KEYWORDS = {'int', 'float', 'bool', 'string', 'print'}

def tokenize(code):
    tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPEC)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'ID' and value in KEYWORDS:
            yield ('KEYWORD', value)
        elif kind == 'SKIP' or kind == 'NEWLINE':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected token: {value}')
        else:
            yield (kind, value)
