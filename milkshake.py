from datetime import datetime

class Milkshake:
    def __init__(self, sabor, tamanho, preco=7.99, adicionais=None):
        self._sabor = sabor
        self._tamanho = tamanho
        self._preco = preco
        self._adicionais = adicionais if adicionais is not None else []
        
        if tamanho not in ["pequeno", "medio", "grande"]:
            raise ValueError("Tamanho deve ser pequeno, medio ou grande")
    
    @property
    def sabor(self):
        return self._sabor
    
    @sabor.setter
    def sabor(self, value):
        self._sabor = value

    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self, value):
        if value in ["pequeno", "medio", "grande"]:
            self._tamanho = value
        else:
            raise ValueError("Tamanho deve ser 'pequeno', 'medio' ou 'grande'")
    
    @property
    def preco(self):
        if self._tamanho == "pequeno":
            return self._preco
        elif self._tamanho == "medio":
            return self._preco * 1.5
        elif self._tamanho == "grande":
            return self._preco * 1.7
    
    def add_toppings(self, topping):
        self._adicionais.append(topping)
    
    def get_cost(self):
        return self.preco + len(self._adicionais) * 3.99
    
    def __str__(self):
        return f"Sabor: {self.sabor}, tamanho: {self.tamanho}, preco: R${self.get_cost():.2f}, adicionais: {', '.join(self._adicionais)}"


class Compra:
    def __init__(self, data=None, milkshakes=None):
        self._data = data if data is not None else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._milkshakes = milkshakes if milkshakes is not None else []

    @property
    def data(self):
        return self._data
    
    @property
    def milkshakes(self):
        return self._milkshakes
    
    def add_milkshake(self):
        sabor = input("Insira o sabor do milkshake: ")
        tamanho = input("Insira o tamanho (pequeno, medio ou grande): ")
        milkshake = Milkshake(sabor, tamanho)
        self._milkshakes.append(milkshake)
        print("Milkshake adicionado")
    
    def remove_milkshake(self):
        if not self._milkshakes:
            print("Nenhum milkshake para remover.")
            return
        
        print("Milkshakes na compra:")
        for i, milkshake in enumerate(self._milkshakes):
            print(f"{i + 1}: {milkshake}")
        
        try:
            choice = int(input("informe o numero do milkshake a ser removido: ")) - 1
            if 0 <= choice < len(self._milkshakes):
                removed_milkshake = self._milkshakes.pop(choice)
                print(f"Milkshake {removed_milkshake.sabor} removido com sucesso")
            else:
                print("Escolha invalida.")
        except ValueError:
            print("Invalido, informe o numero do milkshake a ser removido")
    
    def get_totalcost(self):
        total_cost = sum(milkshake.get_cost() for milkshake in self._milkshakes)
        return total_cost
    
    def __str__(self):
        milkshake_info = "\n".join([str(milkshake) for milkshake in self._milkshakes]) #Join all items into a string
        return f"Data da Compra: {self.data}\nMilkshakes:\n{milkshake_info}\nCusto Total: R${self.get_totalcost():.2f}"
def main():
    compras = []
    
    while True:
        print("\nMenu principal")
        print("1. Nova compra")
        print("2. Visualizar compras")
        print("3.Sair")
        
        choice = input("Escolha a opcao: ")
        
        if choice == "1":
            compra = Compra()
            while True:
                print("\nMenu nova compra:")
                print("1. Adicionar Milkshake")
                print("2. Remover Milkshake")
                print("3. Confirmar Compra")
                print("4. Cancelar Compra")
                
                new_choice = input("Escolha a opção: ")
                
                if new_choice == "1":
                    compra.add_milkshake()
                elif new_choice == "2":
                    compra.remove_milkshake()
                elif new_choice == "3":
                    compras.append(compra)
                    print("Compra salva.")
                    break
                elif new_choice == "4":
                    print("Compra cancelada")
                    break
                else:
                    print("Opcao invalida")
        elif choice == "2":
            print("\nCompras Salvas:")
            for i, compra in enumerate(compras, 1):
                print(f"{i}: {compra.data}")
            view_choice = input("Escolha o numero da compra para visualizar ou '0' para voltar: ")
            if view_choice == "0":
                continue
            try:
                index = int(view_choice) - 1
                if 0 <= index < len(compras):
                    print(compras[index])
                    delete_choice = input("Deseja excluir esta compra? (S/N): ").lower()
                    if delete_choice == "s":
                        del compras[index]
                        print("Compra excluida.")
                else:
                    print("Escolha invalida.")
            except ValueError:
                print("Escolha invalida.")
        elif choice == "3":
            confirmation = input("Tem certeza de que deseja sair? (S/N): ").lower()
            if confirmation == "s":
                break
        else:
            print("Opção invalida. Escolha uma opcao valida")
        

if __name__ == "__main__":
    main()
