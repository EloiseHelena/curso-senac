from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area (self):
        pass
    
    @abstractmethod
    def descrever (self):
        pass
    
class Quadrado(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
       
    def calcular_area(self):
        return self.base * self.altura
    
    def descrever(self):
        print('Figura: quadrado')
        print(f'Base = {self.base}')
        print(f'Altura = {self.altura}')
        
class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
       
    def calcular_area(self):
        return self.base * self.altura
    
    def descrever(self):
        print('Figura: retângulo')
        print(f'Base = {self.base}')
        print(f'Altura = {self.altura}')
        
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.1415 * self.raio ** 2
    
    def descrever(self):
        print('Figura: círculo')
        print(f'Raio: {self.raio}')
        
quadrado1 = Quadrado(5, 5)
quadrado1.descrever()
print(f'Área do quadrado: {quadrado1.calcular_area()}\n')

retangulo1 = Retangulo(5, 10)
retangulo1.descrever()
print(f'Área do retângulo: {retangulo1.calcular_area()}\n')

circulo1 = Circulo(8)
circulo1.descrever()
print(f'Área do círculo: {circulo1.calcular_area()}')
    
        