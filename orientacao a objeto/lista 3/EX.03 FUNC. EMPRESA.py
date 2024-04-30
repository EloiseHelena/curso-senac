class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        
        super().__init__(nome, salario)
        self.bonus = bonus
        
    def bonificar(self, bonus):
        self.salario += bonus  
        self.bonus += bonus
        
    def calcular_pagamento(self):
        return self.salario + self.bonus
             
    def adicionar_funcionario(self, funcionario, lista_funcionarios):
        lista_funcionarios.append(funcionario)
        
class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao):
        
        super().__init__(nome, salario)
        self.comissao = comissao
        
    def calcular_comissao (self, vendas):
        return self.comissao * vendas
    
gerente1 = Gerente('Júlia', 5000, 500)
vendedor1 = Vendedor('Bruna', 2500, 0.5)

vendas_vendedor1 = 2000
comissao_vendedor1 = vendedor1.calcular_comissao(vendas_vendedor1)
comissao_gerente1 = gerente1.bonificar(200)

lista_funcionarios = [gerente1, vendedor1]

for funcionario in lista_funcionarios:
    print(f'Nome: {funcionario.nome}')
    print(f'Salário: R${funcionario.salario}')
if isinstance(funcionario, Gerente): 
    print(f'Bônus: {comissao_gerente1}\n')
elif isinstance(funcionario, Vendedor):
    print(f'Comissão: R${comissao_vendedor1}')
    print()


novo_funcionario = Funcionario("Cauã", 2500)
gerente1.adicionar_funcionario(novo_funcionario, lista_funcionarios)

print('__________Lista de funcionários atualizada:__________\n')
for funcionario in lista_funcionarios:
    print(f'Nome: {funcionario.nome}')
    print(f'Salário: R${funcionario.salario}\n')
if isinstance(funcionario, Gerente):
    print(f'Bônus: R${funcionario.bonus}')
elif isinstance(funcionario, Vendedor):
    print(f'Comissão: R${comissao_vendedor1}')
    print()
        