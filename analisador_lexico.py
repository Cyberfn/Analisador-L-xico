import re
import tkinter as tk
from tkinter import scrolledtext
from collections import defaultdict

# Especificação dos tokens
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

# Compila os padrões de token
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

# Função de análise léxica
def lexer(code):
    tokens = defaultdict(int)
    result = []
    code = code.rstrip()  # Remove espaços em branco no final

    for match in re.finditer(token_regex, code):
        token_type = match.lastgroup
        token_value = match.group(0)

        tokens[token_type] += 1  # Conta o token
        if token_type != 'espacos':
            result.append(f'{token_type}: {token_value}')
        else:
            result.append(f'espacos: "{token_value}" ({len(token_value)} espaço(s))')

    total_tokens = sum(tokens.values())  # Total de tokens
    return tokens, result, total_tokens

# Função chamada ao pressionar "Analisar"
def analisar_codigo():
    codigo = text_input.get("1.0", tk.END)
    tokens_contagem, tokens_resultado, total_tokens = lexer(codigo)

    # Monta o resultado a ser exibido
    resultado_texto = "\n".join(tokens_resultado) + "\n\nContagem de tokens:\n"
    for token, count in tokens_contagem.items():
        resultado_texto += f'{token}: {count}\n'
    resultado_texto += f'\nTotal de tokens encontrados: {total_tokens}'

    result_label.config(text=resultado_texto)

# Interface gráfica
root = tk.Tk()
root.title("Analisador Léxico")
tk.Label(root, text="Código:").pack()
text_input = scrolledtext.ScrolledText(root, width=80, height=15)
text_input.pack()
tk.Button(root, text="Analisar", command=analisar_codigo).pack()
result_label = tk.Label(root, text="", justify=tk.LEFT, anchor="w")
result_label.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
root.mainloop()