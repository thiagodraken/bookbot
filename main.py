# Importando as funções necessárias do arquivo stats.py
from stats import words_counter, count_characters, sort_characters
import sys

def get_book_text(filepath):
    """Lê o conteúdo de um arquivo de texto e o retorna como uma string."""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    # 1. Verifica se o número de argumentos da linha de comando é diferente de 2.
    # sys.argv[0] é o nome do script (ex: main.py)
    # sys.argv[1] é o primeiro argumento (ex: books/frankenstein.txt)
    if len(sys.argv) != 2:
        # Se não houver dois argumentos, mostra como usar o programa e sai.
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Sai do programa com um código de erro.

    # 2. Usa o segundo argumento da linha de comando como o caminho para o livro.
    book_path = sys.argv[1]

    """Ponto de entrada principal do programa."""
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = words_counter(text)
    char_counts = count_characters(text)
    sorted_char_list = sort_characters(char_counts)

    # Imprime o relatório formatado.
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Itera sobre a lista ordenada e imprime a contagem de cada caractere alfabético.
    for item in sorted_char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
            
    print("============= END ===============")


# Executa a função main quando o script é rodado.
main()
