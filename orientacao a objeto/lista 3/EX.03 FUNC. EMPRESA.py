class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def apresentar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Salário: R${self.salario}')
        

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        
        super().__init__(nome, salario)
        self.bonus = bonus
        
    def apresentar_dados(self):
        super().apresentar_dados()
        print(f'Bônus: R${self.bonus * vendas_totais:.2f}\n')
        
    def calcular_pagamento(self):
        print(f'Ganhos Totais: R${self.bonus * vendas_totais + self.salario}')
             
    def adicionar_funcionario(self, funcionario, lista_funcionarios):
        lista_funcionarios.append(funcionario)
        
class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao):
        
        super().__init__(nome, salario)
        self.comissao = comissao
        
    def apresentar_dados(self):
        super().apresentar_dados()
        print(f'Comissão: R${self.comissao * vendas_vendedor1:.2f}')
        
    def calcular_pagamento(self):
        print(f'Ganhos Totais: R${self.comissao * vendas_vendedor1 + self.salario:.2f}\n')
        
    
    
    
gerente1 = Gerente('Júlia', 5000, 0.1)
vendedor1 = Vendedor('Bruna', 2500, 0.05)

vendas_totais = 20000
vendas_vendedor1 = 2000


lista_funcionarios = [gerente1, vendedor1]


print('__________Lista de funcionários_________')
gerente1.apresentar_dados()
gerente1.calcular_pagamento()

vendedor1.apresentar_dados()
vendedor1.calcular_pagamento()



novo_funcionario = Funcionario("Cauã", 2500)
gerente1.adicionar_funcionario(novo_funcionario, lista_funcionarios)

print('\n__________Lista de funcionários atualizada:__________')
for funcionario in lista_funcionarios:
    print(f'Nome: {funcionario.nome}')
    print(f'Salário: R${funcionario.salario:.2f}\n')


    
        