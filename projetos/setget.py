class Exemplo:
    def __init__(self):
        self._valor = 0

    @property
    def propriedade(self):
        print("Obtendo o valor da propriedade")
        return self._valor

    @propriedade.setter
    def propriedade(self, value):
        print("Configurando o valor da propriedade")
        self._valor = value

objeto = Exemplo()
print(objeto.propriedade)  # Isso chama o getter, que usa o valor atual da propriedade
objeto.propriedade = 42   # Isso chama o setter e atribui 42 à propriedade
