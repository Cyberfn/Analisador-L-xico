# Analisador Léxico em Python

Este projeto é um **Analisador Léxico** simples, implementado em Python usando a biblioteca Tkinter para uma interface gráfica. O analisador identifica e conta diferentes tipos de tokens em um código fonte, como palavras-chave, identificadores, números, strings, operadores, delimitadores e espaços em branco.

## Funcionalidades

- **Identificação de Tokens**: O analisador pode identificar e categorizar os seguintes tipos de tokens:
  - Palavras-chave do Python
  - Identificadores
  - Números
  - Strings
  - Delimitadores
  - Operadores
  - Espaços em branco
- **Contagem de Tokens**: Além de identificar tokens, o programa também conta quantas vezes cada tipo de token aparece no código fornecido.
- **Interface Gráfica**: A aplicação possui uma interface gráfica simples para entrada de código e visualização dos resultados.

## Como Usar

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu_usuario/analisador-lexico.git
   cd analisador-lexico
   ```

2. **Instale as Dependências**:
   Este projeto utiliza apenas a biblioteca padrão do Python. Portanto, você não precisa instalar dependências adicionais.

3. **Execute o Programa**:
   Você pode executar o programa diretamente com Python:
   ```bash
   python analisador_lexico.py
   ```

4. **Entrada de Código**:
   - Cole o código que deseja analisar na área de texto.
   - Clique no botão "Analisar" para processar o código.

5. **Resultados**:
   - Os resultados da análise aparecerão abaixo do botão, mostrando cada tipo de token encontrado, a contagem de cada um, e o total de tokens analisados.

## Exemplo de Uso

Aqui está um exemplo simples de código Python que pode ser analisado:

```python
def hello_world():
    print("Hello, world!")
```

## Estrutura do Código

- **Especificação dos Tokens**: Definido no início do script, onde cada tipo de token é descrito com uma expressão regular.
- **Função `lexer`**: Função principal que realiza a análise léxica e retorna os tokens encontrados.
- **Interface Gráfica**: Criada usando Tkinter, que permite a entrada do código e exibe os resultados da análise.

## Contribuições

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, por favor, abra uma issue ou faça um fork do repositório.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).