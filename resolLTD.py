# Criando a lista de livros
lista_de_livros = [
    {"Título": "Dom Casmurro", "Autor": "Machado de Assis", "Ano de Publicação": 1899, "Gênero": "Romance"},
    {"Título": "1984", "Autor": "George Orwell", "Ano de Publicação": 1949, "Gênero": "Ficção Científica"},
    {"Título": "Orgulho e Preconceito", "Autor": "Jane Austen", "Ano de Publicação": 1813, "Gênero": "Romance"},
    {"Título": "Hamlet", "Autor": "William Shakespeare", "Ano de Publicação": 1603, "Gênero": "Drama"},
    {"Título": "O Senhor dos Anéis", "Autor": "J.R.R. Tolkien", "Ano de Publicação": 1954, "Gênero": "Fantasia"}
]

# Criando a tupla de autores
autores_famosos = ("Shakespeare", "Jane Austen", "George Orwell")

# Criando o dicionário do livro favorito
livro_favorito = {"Título": "A Revolução dos Bichos", "Autor": "George Orwell", "Ano de Publicação": 1945, "Gênero": "Ficção Política"}

# Imprimindo os detalhes do livro favorito
print("Detalhes do livro favorito:")
for chave, valor in livro_favorito.items():
    print(f"{chave}: {valor}")

# Imprimindo o título do primeiro livro na lista de livros
print("\nTítulo do primeiro livro na lista de livros:", lista_de_livros[0]["Título"])

# Adicionando um novo livro à lista de livros
novo_livro = {"Título": "O Pequeno Príncipe", "Autor": "Antoine de Saint-Exupéry", "Ano de Publicação": 1943, "Gênero": "Conto"}
lista_de_livros.append(novo_livro)

# Imprimindo todos os livros disponíveis na biblioteca
print("\nLista de todos os livros disponíveis na biblioteca:")
for livro in lista_de_livros:
    print(f"Título: {livro['Título']}, Autor: {livro['Autor']}")

# Imprimindo os nomes dos autores da tupla
print("\nAutores famosos:")
for autor in autores_famosos:
    print(autor)

# Alterando o gênero do livro favorito no dicionário
livro_favorito["Gênero"] = "Alegoria Política"

# Removendo o livro que foi adicionado anteriormente à lista de livros
lista_de_livros.pop()

# Imprimindo a lista de livros atualizada
print("\nLista de livros após a remoção:")
for livro in lista_de_livros:
    print(f"Título: {livro['Título']}, Autor: {livro['Autor']}")
