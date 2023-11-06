#  Neste simulador, você terá que cuidar das plantas do seu jardim.
#  As plantas terão atributos como saúde, sede, idade e você precisará realizar ações para cuidar delas.
#  As ações disponíveis incluem regar as plantas, adubar, podar,
#  verificar o estado das plantas, verificar a idade das plantas e sair do simulador.

class Planta:
    def __init__(self, nome, saude=10, sede=0, idade=0)
    self.nome = nome
    self.saude = saude
    self.sede = sede
    self.idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def saude(self):
        return self._saude

    @saude.setter
    def saude(self, value):
        self._saude = max(0, min(10, value))

    @property
    def sede(self):
        return self._sede

    @sede.setter
    def sede(self, value):
        self._sede = max(0, min(10, value))

    @property
    def idade(self):
        return self._idade

    @property
    def estado(self):
        if self._sede >= 6 and self._saude >= 6:
            return "saudavel"
        elif self._sede < 6 and self._saude >= 6:
            return "com sede"
        elif self._sede >= 6 and self._saude < 6:
            return "doente"
        else:
            return "doente e com sede"

    @property
    def status(self):
        if self._sede == 10 or self._saude == 0:
            return "murcha"
        else:
            return "viva"

    def regar(self):
        self._sede -= 2
    
    def adubar(self):
        self._saude += 2
    
    def podar(self):
        self._idade +=1

    def verificar_estado(self):
        print(f"{self._nome} esta {self.estado}")

    def verificar_idade(self):
        print(f"{self._nome} tem {self._idade} dias de vida")

def criar_planta():
    nome = input("Insira um nome para a sua planta: ")
    return Planta(nome)

def menu_principal():
    jardim = []

    while True:
        print("\nOpcoes:")
        print("1. Adicionar planta")
        print("2. Cuidar das plantas")
        print("3. Verificar estado das plantas")
        print("4. Verificar idade das plantas")
        print("5. Sair")

        escolha = input("Escolha uma opcao (1-5): ")

        if escolha == "1":
            planta = criar_planta()
            jardim.append(planta)
            print(f"{planta.nome} foi adicionada ao seu jardim.")
        elif escolha == "2":
            print("Escolha uma planta para cuidar:")
            for i, planta in enumerate(jardim):
                print(f"{i + 1}. {planta.nome}")

            escolha_planta = input("Escolha uma planta (1-{}): ".format(len(jardim)))
            try:
                escolha_planta = int(escolha_planta)
                if 1 <= escolha_planta <= len(jardim):
                    planta = jardim[escolha_planta - 1]
                    print("\nOpções de cuidados:")
                    print("1. Regar")
                    print("2. Adubar")
                    print("3. Podar")

                    escolha_cuidado = input("Escolha um cuidado (1-3): ")

                    if escolha_cuidado == "1":
                        planta.regar()
                        print(f"Você regou {planta.nome}.")
                    elif escolha_cuidado == "2":
                        planta.adubar()
                        print(f"Você adubou {planta.nome}.")
                    elif escolha_cuidado == "3":
                        planta.podar()
                        print(f"Você podou {planta.nome}.")
                    else:
                        print("Escolha um cuidado válido.")
                else:
                    print("Escolha uma planta válida.")
            except ValueError:
                print("Escolha inválida. Digite um número.")
        elif escolha == "3":
            for planta in jardim:
                planta.verificar_estado()
        elif escolha == "4":
            for planta in jardim:
                planta.verificar_idade()
        elif escolha == "5":
            break
        else:
            print("Escolha uma opção válida.")

if __name__ == "__main__":
    menu_principal()