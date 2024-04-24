from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area (self):
        pass
    
    @abstractmethod
    def descrever (self):
        pass
    
class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.1415 * self.raio ** 2
    
    def descrever(self):
        print('Figura: círculo')
        print(f'Raio: {self.raio}')

circulo1 = Circulo(8)

print(f'Área do círculo: {circulo1.calcular_area()}')

circulo1.descrever()

   