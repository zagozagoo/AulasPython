# Criar um arquivo de texto e escrever informações nele
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, este é um arquivo de exemplo.\n")
    arquivo.write("Python é uma linguagem de programação poderosa!\n")

# Ler o conteúdo do arquivo
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:\n" + conteudo)
