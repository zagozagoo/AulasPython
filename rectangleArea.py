#exiba p o usuario qual é a area de um retangulo
class Retangulo():
    def __init__(self, base, altura):
        self.base= base
        self.altura= altura
        self.area= base*altura
        
    def mostrar(self):
        print(f"Base: {self.base}")
        print(f"Altura: {self.altura}")
        print(f"Área: {self.area}")

numB= float(input("\nInsira o valor da base: "))
numA= float(input("\nInsira o valor da altura: "))

forma= Retangulo(numB, numA)
forma.mostrar()