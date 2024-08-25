# Analisador Léxico Simples

Este projeto implementa um analisador léxico simples em Python, capaz de identificar e contar diferentes tipos de tokens em um trecho de código. Ele reconhece palavras-chave, identificadores, números, strings, delimitadores, operadores, espaços em branco e caracteres desconhecidos.

## Funcionalidades

- **Tokenização**: Converte uma string de código em uma lista de tokens, identificando cada token pelo seu tipo.
- **Contagem de Tokens**: Conta a quantidade de cada tipo de token encontrado e o total de tokens.

## Padrões de Tokens

Os padrões de tokens utilizados pelo analisador são definidos como uma lista de tuplas, onde cada tupla contém o nome do tipo de token e a expressão regular correspondente:

- `palavra_chave`: Identifica palavras-chave como `if`, `else`, `while`, `return` e `function`.
- `identificador`: Reconhece variáveis e nomes de funções que seguem o padrão de um identificador em linguagens de programação.
- `numero`: Detecta números inteiros.
- `string`: Identifica strings delimitadas por aspas simples ou duplas.
- `delimitador`: Reconhece delimitadores como parênteses, colchetes, chaves, vírgulas e ponto e vírgula.
- `operador`: Detecta operadores matemáticos e lógicos.
- `espacos`: Ignora espaços em branco, incluindo tabulações e quebras de linha.
- `desconhecido`: Captura qualquer caractere que não corresponda aos padrões anteriores.

## Como Usar

1. **Entrada de Código**: O código a ser analisado é inserido como entrada pelo usuário.
2. **Tokenização**: O código é processado pela função `tokenize`, que retorna uma lista de tokens.
3. **Contagem de Tokens**: A função `contar_tokens` é usada para contar a quantidade de cada tipo de token.
4. **Saída**: O programa exibe a lista de tokens identificados, a contagem de cada tipo de token e o total de tokens.

## Como Executar
Para executar o analisador léxico, basta rodar o script Python e inserir o código a ser analisado quando solicitado.

```python
python analisador_lexico.py
```