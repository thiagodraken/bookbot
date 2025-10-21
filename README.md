# Projeto 1 - Bookbot

# BookBot: Analisador de Livros

BookBot é um programa de linha de comando, desenvolvido em Python, que analisa o texto de um livro (ou qualquer ficheiro `.txt`) e gera um relatório detalhado sobre o seu conteúdo.

Este projeto foi criado com o objetivo de praticar a manipulação de ficheiros, o processamento de texto e a interação com o utilizador através da linha de comando.

## Funcionalidades

* **Contagem Total de Palavras**: Calcula o número total de palavras no texto fornecido.
* **Frequência de Caracteres**: Conta a ocorrência de cada caractere alfabético no livro.
* **Relatório Ordenado**: Apresenta um relatório limpo e ordenado da frequência dos caracteres, do mais comum ao menos comum.
* **Uso via Linha de Comando**: Permite analisar qualquer livro sem precisar alterar o código-fonte, bastando passar o caminho do ficheiro como argumento.

## Requisitos

* Python 3.6 ou superior.
* Não são necessárias bibliotecas externas. O projeto utiliza apenas módulos nativos do Python.

## Como Usar

Para executar o BookBot, siga os passos abaixo.

### 2. Execução do Programa

Abra o seu terminal, navegue até à pasta raiz do projeto (`bookbot/`) e execute o comando abaixo, substituindo `<caminho_para_o_livro>` pelo ficheiro que deseja analisar. A pasta books, contém alguns livros de exemplos para testes.

**Formato do Comando:**
python3 main.py <caminho_para_o_livro>

Exemplos Práticos:

Para analisar o livro "Frankenstein":
python3 main.py books/frankenstein.txt

### 3. Em Caso de Erro

Se executar o programa sem especificar o caminho do livro, ele exibirá uma mensagem de ajuda:
python3 main.py

Saída:
Usage: python3 main.py <path_to_book>

Exemplo de Saída
Ao executar a análise do livro "Frankenstein", a saída será semelhante a esta:

--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46003 times
The 't' character was found 30234 times
The 'a' character was found 26516 times
The 'o' character was found 25118 times
The 'n' character was found 24395 times
The 'i' character was found 24161 times
The 's' character was found 20875 times
...
--- End report ---


### O projeto está dividido em dois ficheiros principais para uma melhor organização:

## main.py: Este é o ponto de entrada do programa. 

É responsável por:

Verificar os argumentos da linha de comando com o módulo sys.
Ler o caminho do livro fornecido pelo utilizador.
Chamar as funções de análise do módulo stats.
Formatar e imprimir o relatório final no terminal.

## stats.py: Este ficheiro atua como uma "biblioteca" para o projeto, contendo a lógica principal da análise de texto:

words_counter(text): Conta as palavras.
count_characters(text): Cria um dicionário com a contagem de cada caractere.
sort_characters(dict): Ordena os caracteres pela sua frequência.

BookBot is my first [Boot.dev](https://www.boot.dev) project!
