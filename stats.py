def words_counter(file_contents):
    """Conta o número total de palavras em uma string."""
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    """Conta a ocorrência de cada caractere em uma string."""
    lower_text = file_contents.lower()
    char_counts = {}
    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(d):
    """Função auxiliar para obter o valor 'num' de um dicionário."""
    return d["num"]

def sort_characters(char_dict):
    """Converte um dicionário de contagem de caracteres em uma lista ordenada."""
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    
    # Ordena a lista de dicionários em ordem decrescente pela chave 'num'.
    char_list.sort(reverse=True, key=sort_on)
    return char_list
