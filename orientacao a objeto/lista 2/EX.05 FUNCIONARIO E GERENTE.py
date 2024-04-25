class Funcionario:
    def __init__(self, nome, cargo, salario, data_admissao, bonus):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao
        self.bonus = bonus
        
    def apresentar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Cargo: {self.cargo}') 
        print(f'Data de admissão: {self.data_admissao}')
        print(f'Salário: R${self.salario}')
        print(f'Bônus: R${self.bonus}')
        
    def calcular_pagamento(self):
        return self.salario + self.bonus
    
    def promover(self, novo_cargo, novo_salario):
        self.cargo = novo_cargo
        self.salario = novo_salario
        
        
    def bonificar(self, bonus):
        self.salario += bonus  
        self.bonus += bonus
    
      
class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, data_admissao, bonus, area_gerenciada):
        
        super().__init__(nome, cargo, salario, data_admissao, bonus)
        self.area_gerenciada = area_gerenciada
        
    def bonificar(self, bonus):
        self.salario += bonus  
        self.bonus += bonus
    
    def calcular_pagamento(self):
        return self.salario + self.bonus
    
    def apresentar_dados(self):
        super().apresentar_dados()
        print(f'Área Gerenciada: {self.area_gerenciada}')  
        print(f'Bônus Adicional: R${self.bonus}\n')
        
funcionario1 = Funcionario('Eloise', 'Analista Junior', 3000,'01/04/2023', 250)
gerente1 = Gerente('Helena','Gerente de Setor', 5000, '01/01/2002', 500, 'TI')



print('_____Dados do Funcionário:_____\n')
funcionario1.apresentar_dados()

print('\n<<<< Promoção do funcionário: >>>>')
print('Data de promoção: 01/04/2024')
funcionario1.promover('Analista Pleno', 3500)
funcionario1.bonificar(500)
funcionario1.apresentar_dados()


print('\n_____Dados do Gerente:_____')
gerente1.apresentar_dados()
gerente1.bonificar(500)









        
        

        