class Carro:
     
   def __init__(self, marca, modelo, ano):
       self.marca = marca
       self.modelo = modelo
       self.ano = ano
       
   def get_marca(self):
    return self.marca   
       
   def get_modelo(self):
    return self.modelo

   def get_ano(self):
    return self.ano

   def set_marca(self, nova_marca):
     self.marca = nova_marca
     
   def set_modelo(self, novo_modelo):
     self.modelo = novo_modelo

   def set_ano(self, novo_ano):
     self.ano = novo_ano



#Imprime marca, modelo e ano
carro1 = Carro('Fiat', 'Uno', 1994)
print(f"Marca: {carro1.get_marca()}")

modelo = Carro('Fiat', 'Uno', 1994)
print(f"Modelo: {modelo.get_modelo()}")

ano = Carro('Fiat', 'Uno', 1994)
print(f"Ano: {ano.get_ano()}\n")

#Imprime nova marca, novo modelo e novo ano
carro1.set_marca("Ford")
print(f"Nova Marca: {carro1.get_marca()}")

modelo.set_modelo("Ka")
print(f"Novo Modelo: {modelo.get_modelo()}")

ano.set_ano(2001)
print(f"Novo Ano: {ano.get_ano()}")