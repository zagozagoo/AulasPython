class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def __str__(self):
        return f"Funcionário: {self.nome}, CPF: {self.cpf}, Salário: R${self.salario:.2f}"


class Empresa:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)

    def encontrar_funcionario(self, cpf):
        for funcionario in self.funcionarios:
            if funcionario.cpf == cpf:
                return funcionario
        return None

# Exemplo de uso:
empresa = Empresa("Minha Empresa", "12345678901234")

funcionario1 = Funcionario("Alice", "123.456.789-00", 4500.00)
funcionario2 = Funcionario("Bob", "987.654.321-00", 5500.00)
empresa.adicionar_funcionario(funcionario1)
empresa.adicionar_funcionario(funcionario2)

empresa.listar_funcionarios()

funcionario_encontrado = empresa.encontrar_funcionario("123.456.789-00")
if funcionario_encontrado:
    print(f"Funcionário encontrado: {funcionario_encontrado}")
else:
    print("Funcionário não encontrado.")
