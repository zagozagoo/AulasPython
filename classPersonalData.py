#Crie uma classe para representar uma pessoa, com os atributos privados de nome, data de nascimento e altura.
#Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos dados de uma pessoa. 
#Crie um método para calcular a idade da pessoa.

#A data de nascimento pode ser informada como uma String (no formato 05/10/1982, por exemplo) e, no cálculo da idade,
#considere apenas o ano da data de nascimento informada.

import datetime

class Pessoa():
    def __init__(self, nome, data, altura):
        self.__nome= nome
        self.__data= data
        self.__altura= altura

    def dados(self):
        print(f"\nNome: {self.__nome} ")
        print(f"\nData de nascimento: {self.__data} ")
        print(f"\nAltura: {self.__altura} ")


    
    def calcular_idade(self):
        ano_data_atual = datetime.date.today().year
        # obtendo o ano de nascimento
        partes_data_nascimento = self.__data.split("/")
        ano_nascimento = partes_data_nascimento[2] 
        # mostrando a idade
        anos = ano_data_atual - int(ano_nascimento)
        print("\nA pessoa tem", anos, "anos.\n")


    def set_nome(self, nome): 
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_data(self, data): 
        self.__data = data

    def get_data(self):
        return self.__data
    
    def set_altura(self, altura): 
        self.__altura = altura

    def get_altura(self):
        return self.__altura    
    

vitoria = Pessoa('Vitoria', '18/02/2006', 1.52)
vitoria.dados()
vitoria.calcular_idade()