class Animal:
    def __init__(self, especie, emitir_som):
        self.especie = especie
        self.emitir_som = emitir_som
       

    def comer(self):
        print(f'{self.especie} está comendo.')
    
    def dormir(self):
        print(f'Silêncio! {self.especie} está dormindo.')
        
class Cachorro(Animal):
    def __init__(self, especie, emitir_som, interacao):
        
        super().__init__(especie, emitir_som)
        self.interacao = interacao
        
    def latir(self):
        print(f'O {self.especie} está latindo. ')
        
    def brincar(self):
        print(f'Joque uma bolinha para o {self.especie}.')

class Gato(Animal):
    def __init__(self, especie, emitir_som, carinho):
        
        super().__init__(especie, emitir_som)
        self.carinho = carinho
        
    def miar(self):
        print(f'O {self.especie} está miando.')
        
    def ronronar(self):
        print(f'Ele está feliz e está ronronando.')
        
class Papagaio(Animal):
    def __init__(self, especie, emitir_som, interagir):
        
        super().__init__(especie, emitir_som)
        self.interagir = interagir
        
    def falar(self):
        print(f'{self.especie} está falando.')
        
    def dancar(self):
        print(f'O {self.especie} está dançando.')
        
cachorro1 = Cachorro('Bob', 'latir', 'brincar')
gato1 = Gato('Tom', 'miar', 'ronronar')
papagaio1 = Papagaio('Louro', 'falar', 'dançar')

cachorro1.latir()
cachorro1.comer()
cachorro1.latir()
cachorro1.brincar()
cachorro1.dormir()

gato1.miar()
gato1.comer()
gato1.ronronar()
gato1.dormir()

papagaio1.falar()
papagaio1.comer()
papagaio1.dancar()
papagaio1.dormir()