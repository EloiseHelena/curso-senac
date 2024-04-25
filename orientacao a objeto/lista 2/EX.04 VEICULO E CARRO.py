from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def ligar(self):
        raise NotImplementedError
    
    def desligar(self):
        raise NotImplementedError
    
    def acelerar(self):
        raise NotImplementedError
    
    def freiar(self):
        raise NotImplementedError
    
    def descrever(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}')
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, numero_portas, tipo_cambio):
        super().__init__(marca, modelo, ano)
        self.cor = cor
        self.numero_portas = numero_portas
        self.tipo_cambio = tipo_cambio
        self.motor = False
        self.velocidade = 0    
        
    def ligar(self):
        if self.motor == True:
            print('O carro já está ligado!')
        else:
            self.motor = True
            print('O carro ligou.')
        
    def desligar(self):
        if self.motor == False:
            print('O carro já está desligado!')
        else:
            self.motor = False
            print('Desligando carro...')

    def acelerar(self):
        if self.motor == False:
            print('Ligue o carro primeiro.')
        else:
            self.velocidade += 10
            print(f'Acelerando: {self.velocidade}')
        
    def freiar(self):
        if self.velocidade < 0:
            print('O carro está parado.')
        else:
            self.velocidade -= 10
            print(f'Desacelerando: {self.velocidade}')
        
    def descrever(self):
        super().descrever()
        print(f'Cor: {self.cor}\nPortas: {self.numero_portas}\nCâmbio: {self.tipo_cambio}')
        
carro1 = Carro('Fiat', 'Uno', 1994, 'Preto', 2, 'Manual')

carro1.descrever()
carro1.ligar()
carro1.acelerar()
carro1.freiar()
carro1.desligar()

