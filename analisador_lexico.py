import re
import tkinter as tk
from tkinter import scrolledtext, messagebox

token_patterns = [
    ('palavra_chave', r'\b(print|if|else|while|return|function|def|for|break|continue|class|try|except|finally|import|from|as|with|pass|yield|lambda|assert|raise|del|global|nonlocal|True|False|None|and|or|not|is|in)\b'),
    ('identificador', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('numero', r'\b\d+\b'),
    ('string', r'"[^"]*"|\'[^\']*\''),
    ('delimitador', r'[\'"\(\)\[\]\{\},;:.]'),
    ('operador', r'[+\-*/%&|^~<>!=]=?|//|<<|>>|\*\*'),
    ('espacos', r'\s+'),
    ('desconhecido', r'.')
]

def tokenize(codigo):
    tokens = []
    posicao_atual = 0
    while posicao_atual < len(codigo):
        encontrou_match = None
        for tipo_token, padrao in token_patterns:
            regex = re.compile(padrao)
            encontrou_match = regex.match(codigo, posicao_atual)
            if encontrou_match:
                texto_encontrado = encontrou_match.group(0)
                if tipo_token != 'espacos':
                    tokens.append((tipo_token, texto_encontrado))
                posicao_atual = encontrou_match.end(0)
                break
        if not encontrou_match:
            raise RuntimeError(f"Caractere inesperado: {codigo[posicao_atual]}")
    return tokens

def contar_tokens(tokens):
    contagem = {}
    for tipo_token, _ in tokens:
        if tipo_token in contagem:
            contagem[tipo_token] += 1
        else:
            contagem[tipo_token] = 1
    contagem_total = sum(contagem.values())
    return contagem, contagem_total

def analisar_codigo():
    codigo = text_input.get("1.0", tk.END)
    try:
        tokens = tokenize(codigo)
        contagem, total = contar_tokens(tokens)
        
        resultado_texto = "Tokens encontrados:\n"
        resultado_texto += "\n".join(f"{token}" for token in tokens)
        resultado_texto += "\n\nContagem de tokens:\n"
        resultado_texto += "\n".join(f"{tipo_token}: {quantidade}" for tipo_token, quantidade in contagem.items())
        resultado_texto += f"\n\nTotal de tokens: {total}"
        
        result_label.config(text=resultado_texto)
        
    except RuntimeError as e:
        messagebox.showerror("Erro", str(e))

root = tk.Tk()
root.title("Analisador Léxico")

# Widgets
tk.Label(root, text="Código:").pack()

text_input = scrolledtext.ScrolledText(root, width=80, height=15)
text_input.pack()

tk.Button(root, text="Analisar", command=analisar_codigo).pack()

result_label = tk.Label(root, text="", justify=tk.LEFT, anchor="w")
result_label.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()
