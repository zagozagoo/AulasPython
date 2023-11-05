import csv

class Tamagotchi:
    def __init__(self, nome, fome=10, saude=0, idade=0):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @property
    def fome(self):
        return self._fome
    
    @fome.setter
    def fome(self, value):
        self._fome = max(0, min(10, value))

    @property
    def saude(self):
        return self._saude
    
    @saude.setter
    def saude(self, value):
        self._saude = max(0, min(10, value))

    @property
    def idade(self):
        return self._idade
    
    @property
    def humor(self):
        if self._fome < 6 and self._saude >= 6:
            return "com fome"
        elif self._fome >= 6 and self._saude < 6:
            return "doente"
        elif self._fome < 6 and self._saude < 6:
            return "doente e com fome"
        else:
            return "feliz"
        
    @property
    def status(self):
        if self._fome == 10 or self._saude == 0:
            return "falecido"
        else:
            return "vivo"
        
    def salvar(self):
        try:
            with open('saves.csv', mode='a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)                           
                csv_writer.writerow([self._nome, self._fome, self._saude, self._idade])
        except Exception as e:
            print(f"Ocorreu um erro ao salvar os dados do Tamagotchi: {e}")

    @staticmethod
    def verificar(nome):
        try:
            with open('saves.csv', mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if row[0] == nome:
                        return True
        except FileNotFoundError:
            print("O arquivo 'saves.csv' não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao verificar o nome do Tamagotchi: {e}")
        return False

    def recuperar(self):
        try:
            if self.status == "falecido":
                print(f"{self._nome} faleceu e não pode ser recuperado.")
                return
            
            if not Tamagotchi.verificar(self._nome):
                print(f"Não foi possível encontrar {self._nome} no arquivo de saves.")
                return

            with open('saves.csv', mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if row[0] == self._nome:
                        self._fome = int(row[1])
                        self._saude = int(row[2])
                        self._idade = int(row[3])
                        break
        except FileNotFoundError:
            print("O arquivo 'saves.csv' não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao recuperar os dados do Tamagotchi: {e}")

def renomear_tamagotchi(tamagotchi):
    novo_nome = input("Insira um novo nome para o Tamagotchi: ")
    if not Tamagotchi.verificar(novo_nome):
        tamagotchi.nome = novo_nome
    else:
        print("Esse nome já existe. Escolha outro nome.")

def alimentar_tamagotchi(tamagotchi):
    tamagotchi.fome -= 2

def medicar_tamagotchi(tamagotchi):
    tamagotchi.saude += 2

def banhar_tamagotchi(tamagotchi):
    if tamagotchi.idade < 10:
        tamagotchi.saude += 5
        tamagotchi.idade += 1
    else:
        print("Seu Tamagotchi está muito velho para tomar banho.")

def verificar_humor_tamagotchi(tamagotchi):
    print(f"Humor do Tamagotchi: {tamagotchi.humor}")

def verificar_idade_tamagotchi(tamagotchi):
    print(f"Idade do Tamagotchi: {tamagotchi.idade}")

def salvar_e_sair(tamagotchi):
    confirmacao = input("Deseja salvar o seu save? (s/n): ")
    if confirmacao.lower() == "s":
        tamagotchi.salvar()
    exit()

def menu_principal():
    nome = input("Insira o nome do seu Tamagotchi: ")
    tamagotchi = Tamagotchi(nome)

    if Tamagotchi.verificar(nome):
        tamagotchi.recuperar()

    opcoes = {
        "1": renomear_tamagotchi,
        "2": alimentar_tamagotchi,
        "3": medicar_tamagotchi,
        "4": banhar_tamagotchi,
        "5": verificar_humor_tamagotchi,
        "6": verificar_idade_tamagotchi,
        "7": salvar_e_sair
    }

    while tamagotchi.status == "vivo":
        print("\nOpções:")
        print("1. Renomear")
        print("2. Alimentar")
        print("3. Medicar")
        print("4. Banhar")
        print("5. Verificar humor")
        print("6. Verificar Idade")
        print("7. Sair")

        escolha = input("Escolha uma opção (1-7): ")

        if escolha in opcoes:
            opcoes[escolha](tamagotchi)
        else:
            print("Escolha uma opção válida.")

if __name__ == "__main__":
    menu_principal()
