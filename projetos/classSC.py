#classe simples
class NomeCompleto():
    def __init__(self, nome, sobrenome):
        self.nome = nome.title() #primeiras letras maiusculas
        self.sobrenome = sobrenome.title()

    def printNomeCompleto(self):
        nomesobrenome = self.nome + " " + self.sobrenome
        print(nomesobrenome)
        
#loop e manipulação de arquivo

specialchar = "!@#$%¨&*()^~´`[]{}?<>:/|.+-=_'"""
nomescorrigidos = []

file = open("nomes.txt", "r") #lendo arquivo
newfile = open("nomesCorretos.txt", "w") # criando arquivo que pode ser escrito

for line in file.readlines(): #para cada linha do arquivo
    for char in line: #para cada caracter da linha
        if not char.isdigit(): #se não for um dígito(número) 
            if char not in specialchar: #se o caracter não estiver dentro da "lista" de caracteres especiais
                newfile.write(char) #escreve no novo arquivo se atender todas as condições

file.close()
newfile.close() #fechando tudo

newfile = open("nomesCorretos.txt", "r") #abrindo novamente o arquivo, mas agora para leitura

for line in newfile.readlines():
    nomescorrigidos.append(line) #adicionando cada linha do arquivo à lista "nomesCorrigidos"
                                 #(as linhas vão manter o "\n" no final da string)

newfile.close()      

#atribuindo valores a classe e manipulando strings

for i in range(len(nomescorrigidos)): #equivalente em c: for(int i = 0; i < sizeof(nomescorrigidos); i++)
    nomescorrigidos[i] = nomescorrigidos[i].split(" ", 1) #vai separar o nome completo a partir do primeiro espaçamento 
                                                          #e atribuir a lista gerada pelo split ao mesmo índice
    
#depois do split, a lista vai seguir esse padrão: nomesCorrigidos = [["Joao", "Vitor"], ["Matheus", "Silva"], ["Carolina", "Meire"]]

nome1 = NomeCompleto(nomescorrigidos[0][0], nomescorrigidos[0][1]) #atribuindo os valores da lista a variávies utilizando a classe
nome2 = NomeCompleto(nomescorrigidos[1][0], nomescorrigidos[1][1])
nome3 = NomeCompleto(nomescorrigidos[2][0], nomescorrigidos[2][1])

print("Nome1:", nome1.nome)
print("Sobrenome1:", nome1.sobrenome)

nome2.printNomeCompleto() #usando a função da classe de printar o nome completo