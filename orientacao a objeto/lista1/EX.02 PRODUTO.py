class Produto:
     
   def __init__(self, nome, preco):
       self.nome = nome
       self.preco = preco
       
   def get_nome(self):
    return self.nome   
       
   def get_preco(self):
    return self.preco

   def set_nome(self, novo_nome):
     self.nome = novo_nome
     
   def set_preco(self, novo_preco):
     self.preco = novo_preco


#Imprime produto e preço
produto1 = Produto("arroz", 5.00)
print(f"Produto: {produto1.get_nome()}")

preco_original = Produto("arroz", 5.00)
print(f"Preço do produto: {preco_original.get_preco()}\n")

# Nome e preço alterados
produto1.set_nome("arroz integral")
print(f"Nome do produto alterado: {produto1.get_nome()}")

preco_original.set_preco("3.50")
print(f"Novo preço, após o desconto: {preco_original.get_preco()}")
