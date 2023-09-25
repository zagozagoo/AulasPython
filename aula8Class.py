#crie uma classe 'casa' com atributos de area, rua, cor, nome
#nome opcional na hora de instanciar;funcao mostrar para mostrar os atributos


"""
class Casa():
    def __init__(self, area= 150, rua= 'Carmesin', cor= "Vermelho", nome=''):
        self.area = area
        self.rua = rua
        self.cor = cor 
        self.nome = nome 
    
    def mostrar(self):
        print (f"Área: {self.area}")
        print (f"Rua: {self.rua}")
        print (f"Cor: {self.cor}")
        print (f"Nome: {self.nome}")
        
casa1 = Casa()
casa1.mostrar()
"""


'''
import.math
class Calculadora():

    def soma(self, a, b):
        return a+b

    def subtracao(self, a, b):
        return a-b

    def divisao(self, a, b):
        return a/b

    def multiplicacao(self, a, b):
        return a*b

class CalculadoraCientifica(Calculadora):

    def Potencia(self, a, b):
        return a**b

    def raiz(self, a ,b):
        return math.sqrt a

calc = CalculadoraCientifica()
print(calc.soma(5,2))
'''

class Conta():
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
        self.conta_corrente
        ContaCorrente(0)
        self.conta_poupanca = ContaPoupanca(0)
            

class ContaCorrente():
    def __init__(self, saldo):
        self.saldo = saldo

class ContaPoupanca():
     def __init__(self, saldo):
        self.saldo = saldo


nome =input("Digite seu nome: ") 
ano = input("Digite seu ano de nascimento: ")

minha_conta = Conta(nome, ano)

minha_conta.conta_corrente.saldo = 1000

print(minha_conta.conta_corrente.saldo)
print(minha_conta.conta_poupanca.saldo)