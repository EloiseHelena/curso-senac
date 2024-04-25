class Funcionario:
    def __init__(self, nome, cargo, salario, data_admissao):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao
        
    def apresentar_dados(self):
        print(f'Dados do funcionário:\nNome: {self.nome}\nCargo: {self.cargo}\nData de admissão: {self.data_admissao}')   
        
    def calcular_pagamento(self):
        return self.salario
    
    
    
class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, data_admissao, bonus, area_gerenciada):
        super().__init__(nome, cargo, salario, data_admissao)
        self.bonus = bonus
        self.area_gerenciada = area_gerenciada
        
    def promover(self, novo_cargo):
        self.cargo = novo_cargo
        
    def bonificar(self, bonus):
        self.salario += bonus  
        self.bonus += bonus
    
    def calcular_pagamento(self):
        return self.salario + self.bonus
    
    def apresentar_dados(self):
        super().apresentar_dados()
        print(f'Bônus: {self.bonus}')
        print(f'Área Gerenciada: {self.area_gerenciada}')   
        
funcionario1 = ()
gerente1 = ()


        
        

        