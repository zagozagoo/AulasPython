#Crie uma classe base chamada FormaGeometrica com os seguintes métodos:

#calcular_area(): um método abstrato que deve ser implementado pelas classes derivadas.
#calcular_perimetro(): um método abstrato que deve ser implementado pelas classes derivadas.
#Em seguida, crie duas classes derivadas, Retangulo e Circulo, que herdam da classe FormaGeometrica.
#Implemente os métodos calcular_area() e calcular_perimetro() de acordo com as fórmulas apropriadas para cada forma.

#Por fim, crie objetos de ambas as classes e chame os métodos para calcular a área e o
#perímetro de cada forma. Imprima os resultados.
from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

# Exemplo de uso:
retangulo = Retangulo(5, 3)
circulo = Circulo(4)

print("Retângulo:")
print(f"Área: {retangulo.calcular_area()}")
print(f"Perímetro: {retangulo.calcular_perimetro()}")

print("\nCírculo:")
print(f"Área: {circulo.calcular_area()}")
print(f"Perímetro: {circulo.calcular_perimetro()}")
