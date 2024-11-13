# Analisador Léxico em Python

Este projeto é um **Analisador Léxico** básico em Python com interface gráfica usando Tkinter. Ele identifica e conta diferentes tipos de tokens em códigos fonte, como palavras-chave, identificadores, números, strings, operadores, delimitadores e espaços em branco.

## Funcionalidades

- **Identificação de Tokens**: O analisador categoriza os seguintes tokens:
  - Palavras-chave do Python
  - Identificadores
  - Números
  - Strings
  - Delimitadores
  - Operadores
  - Espaços em branco
- **Contagem de Tokens**: Conta a quantidade de ocorrências de cada tipo de token no código fornecido.
- **Interface Gráfica**: Possui uma interface gráfica simples para entrada e visualização dos resultados da análise.

## Como Usar

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu_usuario/analisador-lexico.git
   cd analisador-lexico
   ```

2. **Instale as Dependências**:
   Não há dependências adicionais; o projeto usa apenas bibliotecas padrão do Python.

3. **Execute o Programa**:
   ```bash
   python analisador_lexico.py
   ```

4. **Entrada de Código**:
   - Cole o código a ser analisado na área de texto.
   - Clique em "Analisar" para processar o código.

5. **Resultados**:
   - Os resultados mostram os tipos de tokens encontrados, a contagem de cada tipo e o total de tokens.

## Estrutura do Código

- **Especificação dos Tokens**: Lista de tokens especificada com expressões regulares no início do script.
- **Função `tokenize`**: Realiza a análise léxica e retorna uma lista dos tokens identificados.
- **Interface Gráfica**: A interface criada com Tkinter permite a entrada e visualização dos resultados da análise.

## Contribuições

Contribuições são bem-vindas! Para contribuir, abra uma issue ou faça um fork do repositório.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).