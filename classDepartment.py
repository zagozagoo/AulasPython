class Pessoa:
    def __init__(self, nome, idade, genero):
        self.__nome = nome
        self.__idade = idade
        self.__genero = genero

    def set_nome(self, novonome):
        self.__nome = novonome

    def get_nome(self):
        return self.__nome
    
    def set_idade(self, novoidade):
        self.__idade = novoidade

    def get_idade(self):
        return self.__idade
    
    def set_genero(self, novogenero):
        self.__genero = novogenero

    def get_genero(self):
        return self.__genero
    
class Funcionario(Pessoa):
    def __init__(self, nome, idade, genero, cargo, salario, numero):
        super().__init__(nome, idade, genero)
        self.__cargo = cargo
        self.__salario = salario
        self.__numero = numero

    def calcular_bonificacao(self):
        return self.__salario * 0.1

    def set_cargo(self, novocargo):
        self.__cargo = novocargo

    def get_cargo(self):
        return self.__cargo
    
    def set_salario(self, novosalario):
        self.__salario = novosalario

    def get_salario(self):
        return self.__salario
    
    def set_numero(self, novonumero):
        self.__numero = novonumero

    def get_numero(self):
        return self.__numero

class Gerente(Funcionario):
    def __init__(self,nome, idade, genero, cargo, salario, numero, setor):
        super().__init__(nome, idade, genero, cargo, salario, numero)
        self.__setor = setor

    def calcular_bonificacao(self):
        return self.__salario * 0.15

    def set_setor(self, novosetor):
        self.__setor = novosetor

    def get_setor(self):
        return self.__setor

class Departamento:
    def __init__(self,nome_depart):
        self.__nome_depart= nome_depart
        self.__lista=[]
        
    def add_funcionario(self, f):
        self.__lista.append(f)

    def remov_funcionario(self, f):
        self.__lista.remove(f)

    def listar_funcionario(self):
        print('Departamento:', self.__lista)

        for i in range(len(self.__lista)):
            print(self.__lista[i].get_nome())



ets = Departamento("ETS")

f = Funcionario("Dom", 20, "masc", "aluno", 1000, 92896232)
f1 = Funcionario("Zago", 17, "fem", "aluno", 1000, 7)

g = Gerente("Fabio", 50, 'masc', 'gerente', 20000, 56, 'ETS')

ets.add_funcionario(f)
ets.add_funcionario(f1)
ets.add_funcionario(g)

ets.listar_funcionario()