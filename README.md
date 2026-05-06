# 📚 BookBot — Analisador de Livros em Python

BookBot é uma aplicação de linha de comando desenvolvida em **Python** que analisa livros e arquivos `.txt`, gerando relatórios detalhados sobre o conteúdo do texto.

O projeto foi criado com foco em aprendizado de:

- Manipulação de arquivos
- Processamento de texto
- Estruturas de dados
- Organização modular de código
- Uso de argumentos via terminal

> 🚀 BookBot é meu primeiro projeto desenvolvido durante os estudos na plataforma Boot.dev.

---

# ✨ Funcionalidades

- 📖 Contagem total de palavras
- 🔠 Frequência de caracteres alfabéticos
- 📊 Relatório ordenado por frequência
- 🧩 Código modular e organizado
- 💻 Execução via linha de comando
- ⚡ Utilização apenas de bibliotecas nativas do Python

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| Python 3 | Linguagem principal |
| sys | Manipulação de argumentos CLI |
| Arquivos `.txt` | Fonte de dados para análise |

---

# 📦 Requisitos

- Python **3.6+**
- Nenhuma biblioteca externa necessária

---

# 📁 Estrutura do Projeto

```bash
bookbot/
│
├── books/
│   └── frankenstein.txt
│
├── main.py
├── stats.py
└── README.md
```

---

# ▶️ Como Executar

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/thiagodraken/bookbot.git
```

## 2️⃣ Acesse a pasta do projeto

```bash
cd bookbot
```

## 3️⃣ Execute o programa

```bash
python3 main.py <caminho_para_o_livro>
```

---

# 📚 Exemplos de Uso

## Analisar o livro Frankenstein

```bash
python3 main.py books/frankenstein.txt
```

---

# ⚠️ Tratamento de Erros

Caso o programa seja executado sem informar o caminho do arquivo:

```bash
python3 main.py
```

O retorno será:

```bash
Usage: python3 main.py <path_to_book>
```

---

# 📄 Exemplo de Saída

```bash
--- Begin report of books/frankenstein.txt ---

77986 words found in the document

The 'e' character was found 46003 times
The 't' character was found 30234 times
The 'a' character was found 26516 times
The 'o' character was found 25118 times
The 'n' character was found 24395 times

...

--- End report ---
```

---

# 🧠 Arquitetura do Projeto

## `main.py`

Responsável por:

- Ler argumentos da linha de comando
- Validar entradas do usuário
- Carregar o conteúdo do livro
- Executar a análise
- Exibir o relatório final

---

## `stats.py`

Contém toda a lógica de processamento:

| Função | Descrição |
|---|---|
| `words_counter(text)` | Conta o número total de palavras |
| `count_characters(text)` | Conta a frequência dos caracteres |
| `sort_characters(dict)` | Ordena os caracteres por frequência |

---

# 📚 Conceitos Praticados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Manipulação de arquivos
- Funções em Python
- Dicionários e listas
- Ordenação de dados
- Processamento de strings
- Estruturação de projetos
- Programação modular
- CLI (Command Line Interface)

---

# 🚧 Melhorias Futuras

- 📊 Exportação de relatórios em JSON/CSV
- 🌎 Suporte a múltiplos idiomas
- 📈 Estatísticas avançadas
- 🔍 Contagem de palavras mais frequentes
- 🖥️ Interface gráfica
- ⚡ Melhorias de performance para arquivos grandes

---

# 🤝 Contribuição

Contribuições são bem-vindas!

Sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

# 📄 Licença

Este projeto está sob a licença MIT.

---

# 👨‍💻 Autor

Desenvolvido por **Thiago Henrique Vital de Oliveira**

🔗 GitHub: https://github.com/thiagodraken
