import re
from collections import Counter

token_specification = [
    ('palavra_chave', r'\b(print|if|else|while|return|def|for|break|continue|class|try|except|finally|import|from|as|with|pass|yield|lambda|assert|raise|del|global|nonlocal|True|False|None|and|or|not|is|in)\b'),
    ('identificador', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('numero', r'\b\d+\b'),
    ('string', r'"[^"]*"|\'[^\']*\''), 
    ('delimitador', r'[\'"\(\)\[\]\{\},;:.]'),
    ('operador', r'[+\-*/%&|^~<>!=]=?|//|<<|>>|\*\*'),
    ('espacos', r'[ \t]+'),
    ('desconhecido', r'.'),
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

def tokenize(code):
    tokens = []
    
    for match in re.finditer(token_regex, code):
        tipo = match.lastgroup
        valor = match.group()
        tokens.append((tipo, valor))
    
    return tokens

code = input("Digite o código: ")
tokens = tokenize(code)
print(f"Total de tokens: {len(tokens)}")

for token_type, value in tokens:
    print(f"{token_type}: {value}")