#gerenciamento de contas bancárias, ContaPoupanca herda da classe ContaBancaria
class ContaBancaria:
    _numero_contas = 0

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        ContaBancaria._numero_contas += 1

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, novo_titular):
        if isinstance(novo_titular, str):
            self._titular = novo_titular
        else:
            raise ValueError("O titular deve ser uma string.")

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            raise ValueError("O valor deve ser maior que zero.")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
        else:
            raise ValueError("Saldo insuficiente ou valor inválido.")

    def get_saldo(self):
        return self._saldo

    @staticmethod
    def get_numero_contas():
        return ContaBancaria._numero_contas

    def __str__(self):
        return f"Titular: {self._titular}, Saldo: {self._saldo}"


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo, juros):
        super().__init__(titular, saldo)
        self._juros = juros

    def calcular_juros(self):
        self._saldo += self._saldo * (self._juros / 100)

    def __str__(self):
        return super().__str__() + f", Juros: {self._juros}%"

# Exemplo de uso:
conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaPoupanca("Bob", 2000, 5)

print(conta1)
print(conta2)

conta1.depositar(500)
conta2.sacar(300)

print(f"Saldo conta1: {conta1.get_saldo()}")
print(f"Saldo conta2: {conta2.get_saldo()}")

conta2.calcular_juros()
print(f"Saldo conta2 com juros: {conta2.get_saldo()}")

print(f"Número de contas: {ContaBancaria.get_numero_contas()}")
