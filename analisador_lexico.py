import re

token_patterns = [
    ('palavra_chave', r'\b(if|else|while|return|function)\b'),
    ('identificador', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('numero', r'\b\d+\b'),
    ('string', r'"[^"]*"|\'[^\']*\''),
    ('delimitador', r'[\'"\(\)\[\]\{\},;]'),
    ('operador', r'[+\-*/=<>!]+'),
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

codigo = input("Digite o código a ser analisado: ")

tokens = tokenize(codigo)
contagem, total = contar_tokens(tokens)

print("Tokens encontrados:")
for token in tokens:
    print(token)

print("\nContagem de tokens:")
for tipo_token, quantidade in contagem.items():
    print(f"{tipo_token}: {quantidade}")

print(f"\nTotal de tokens: {total}\n")
