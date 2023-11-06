# Crie uma lista inicial com alguns nomes de cores
cores = ["vermelho", "azul", "verde", "amarelo"]

# Adicione a cor "roxo" no final da lista
cores.append("roxo")

# Insira a cor "laranja" na segunda posição da lista
cores.insert(1, "laranja")

# Remova a cor "verde" da lista
cores.remove("verde")

# Encontre o índice da cor "azul"
indice_azul = cores.index("azul")

# Imprima a lista resultante e o índice da cor "azul"
print("Lista de cores:", cores)
print("O índice da cor 'azul' é:", indice_azul)