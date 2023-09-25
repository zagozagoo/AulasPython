cont = 1
tabuleiro = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]

def mostrar():
    print('    1    2    3')
    print('1', tabuleiro[0])
    print('2', tabuleiro[1])
    print('3', tabuleiro[2])

def menu():
    cont= int(input('1 - Jogar novamente\n'+
                "0 - Sair\n!"))
    if cont == 1:
        tabuleiro = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
        mostrar()
    else:
        print("Saindo")

def ganhou():
    print("Acabou!")


# === Game  === #
 
print('\n\n^^ Jogo da Velha ^^\n \n')
vez = 1
simbolo = ['X', 'O']

while True:
    
    mostrar()
    while True:
        coluna = int(input("\nDigite a coluna desejada: "))
        linha = int(input("\nDigite a linha desejada: "))
        
        if tabuleiro[linha-1][coluna-1] == '-':
            break
        else:
            print("Lugar ocupado!")
            pass
        
    tabuleiro[linha-1][coluna-1] = simbolo[vez]
    
    if vez == 1:
        vez = 0
    else:
        vez = 1
        
# primeiro [] significa linha e o segundo [] significa coluna
    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[2][2] != '-':
#verificar se os campos da lista são simbolos ou não, se forem, entao vc ganhou, se não, n acontece nada
        ganhou()
        cont= int(input('1 - Jogar novamente\n'+
                "0 - Sair\n!"))
        if cont == 1:
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = '-'
            pass
        else:
            break
        
    elif tabuleiro[0][0] == tabuleiro[0][1] and tabuleiro[0][1] == tabuleiro[0][2] and tabuleiro[0][2] != '-':
        ganhou()
        cont= int(input('1 - Jogar novamente\n'+
                "0 - Sair\n!"))
        if cont == 1:
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = '-'
            pass
        else:
            break
    elif tabuleiro[1][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[1][2] and tabuleiro[1][2] != '-':
        ganhou()
        cont= int(input('1 - Jogar novamente\n'+
                "0 - Sair\n!"))
        if cont == 1:
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = '-'
            pass
        else:
            break
    elif tabuleiro[2][0] == tabuleiro[2][1] and tabuleiro[2][1] == tabuleiro[2][2] and tabuleiro[2][2] != '-':
        ganhou()
        cont= int(input('1 - Jogar novamente\n'+
                "0 - Sair\n!"))
        if cont == 1:
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = '-'
            pass
        else:
            break
    elif tabuleiro[0][1] == tabuleiro[1][0] and tabuleiro[1][0] == tabuleiro[2][1] and tabuleiro[2][1] != '-':
        ganhou()
        cont= int(input('1 - Jogar novamente\n'+
                "0 - Sair\n!"))
        if cont == 1:
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = '-'
            pass
        else:
            break
    elif tabuleiro[0][1] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][1] and tabuleiro[2][1] != '-':
        ganhou()
        cont= int(input('1 - Jogar novamente\n'+
                "0 - Sair\n!"))
        if cont == 1:
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = '-'
            pass
        else:
            break
    elif tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[1][2] and tabuleiro[1][2] != '-':
        ganhou()
        cont= int(input('1 - Jogar novamente\n'+
                "0 - Sair\n!"))
        if cont == 1:
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = '-'
            pass
        else:
            break
    elif tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[2][0] != '-':
        ganhou()  
        cont= int(input('1 - Jogar novamente\n'+
                "0 - Sair\n!"))
        if cont == 1:
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = '-'
            pass
        else:
            break
