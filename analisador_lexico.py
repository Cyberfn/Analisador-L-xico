import re
import tkinter as tk
from tkinter import scrolledtext
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

def lexer(code):
    tokens = Counter()
    result = []
    for match in re.finditer(token_regex, code.rstrip()):
        token_type = match.lastgroup
        token_value = match.group(0)
        tokens[token_type] += 1
        if token_type != 'espacos':
            result.append(f'{token_type}: {token_value}')
    return tokens, result

def analisar_codigo():
    tokens_contagem, tokens_resultado = lexer(text_input.get("1.0", tk.END))
    resultado_texto = "\n".join(tokens_resultado) + "\n\nContagem de tokens:\n" + "\n".join(f'{t}: {c}' for t, c in tokens_contagem.items())
    result_label.config(text=resultado_texto)

root = tk.Tk()
root.title("Analisador Léxico")
tk.Label(root, text="Código:").pack()
text_input = scrolledtext.ScrolledText(root, width=80, height=15)
text_input.pack()
tk.Button(root, text="Analisar", command=analisar_codigo).pack()
result_label = tk.Label(root, text="", justify=tk.LEFT, anchor="w")
result_label.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
root.mainloop()