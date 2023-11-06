# 1. Crie uma lista vazia chamada "minha_lista".
minha_lista = []

# 2. Adicione os números de 1 a 5 à lista usando um loop for.
for i in range(1, 6):
    minha_lista.append(i)

# 3. Imprima a lista resultante.
print("Minha lista:", minha_lista)

# 4. Acesse o terceiro elemento da lista e armazene-o em uma variável.
terceiro_elemento = minha_lista[2]

# 5. Modifique o quarto elemento da lista para o valor 10.
minha_lista[3] = 10

# 6. Remova o primeiro elemento da lista.
minha_lista.pop(0)

# 7. Verifique se o número 7 está na lista e imprima o resultado.
if 7 in minha_lista:
    print("O número 7 está na lista.")
else:
    print("O número 7 não está na lista.")

# 8. Encontre o número de elementos na lista.
tamanho_da_lista = len(minha_lista)

# 9. Ordene a lista em ordem decrescente.
minha_lista.sort(reverse=True)

# 10. Crie uma cópia da lista original.
copia_da_lista = minha_lista.copy()

# 11. Limpe a lista original.
minha_lista.clear()

# 12. Imprima a lista ordenada em ordem decrescente, a cópia da lista e o tamanho da lista original.
print("Lista ordenada em ordem decrescente:", minha_lista)
print("Cópia da lista original:", copia_da_lista)
print("Tamanho da lista original:", tamanho_da_lista)