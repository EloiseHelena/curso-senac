class ContaBancaria:
    def __init__(self, titular, saldo, taxa_juros):
        self.titular = titular
        self.saldo = saldo
        self.taxa_juros = taxa_juros
        
    def titular_conta(self):
        print(f'Nome do titular: {self.titular}')
        
    def apresentar_saldo(self):
       print(f'Saldo em conta: {self.saldo}') 
       
    def depositar(self, valor):
        if valor <= 0:
         print('Valor inválido!')
        else:
         self.saldo += valor
         print(f"Depósito de R${valor} realizado com sucesso. Novo saldo: R${self.saldo} ") 
    
    def sacar(self, valor):
        if self.saldo >= valor:
         self.saldo -= valor
         print(f"Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}")
        else:
         print("Saldo insuficiente.")
         
        
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo, taxa_juros, rendimento_mensal):
        
       super().__init__(titular, saldo, taxa_juros)
       self.rendimento_mensal = rendimento_mensal
      
       
    def calcular_rendimento(self):
        self.rendimento_mensal = self.saldo * self.taxa_juros / 100
        return self.rendimento_mensal
    
    
conta1 = ContaBancaria('TITULAR', 50.00, 0.5)
poupanca1 = ContaPoupanca('MARIA', 50.00, 0.5, 1)

def login():
    while True:
        print('__________MENU__________')
        print('1 - CONTA CORRENTE\n2 - CONTA POUPANÇA\n3 - SAIR')
        menu = input('Digite que opção desejada:')
        
        if menu == '1':
            while True:
                print('__________CONTA CORRENTE__________')
                print('1 - Consultar Titular')
                print('2 - Consultar Saldo')
                print('3 - Depositar')
                print('4 - Sacar')
                print('5 - Sair')
                menu2= input('Digite a opção desejada: ')
                
                if menu2 == '1':
                    conta1.titular_conta()
                    
                elif menu2 == '2':
                    conta1.apresentar_saldo()
                
                elif menu2 == '3':
                    valor = int(input('Digite o valor a ser depositado na CC:'))
                    conta1.depositar(valor)
                    
                elif menu2 == '4':
                    valor = int(input('Digite o valor a ser sacado da CC: '))
                    conta1.sacar(valor)
                
                elif menu2 == '5':
                    print()
                    print('Saindo de Conta Corrente...')
                    return
                else:
                    print('Opção inválida!')
                    
        if menu == '2':
            while True:
                print('__________CONTA POUPANÇA_________')
                print('1 - Consultar Saldo')
                print('2 - Depositar')
                print('3 - Sacar')
                print('4 - Calcular Rendimento')
                print('5 - Sair')
                menu3 = input('Digite a opção desejada: ')
                
                if menu3 == '1':
                    poupanca1.apresentar_saldo()
                    
                elif menu3 == '2':
                    valor = int(input('Digite o valor a ser depositado na Poupança:'))
                    poupanca1.depositar(valor)
                    
                elif menu3 == '3':
                    valor = int(input('Digite o valor a ser sacado da Poupança: '))
                    poupanca1.sacar(valor)
                    
                elif menu3 == '4':
                    print('A taxa Selic está em alta! Sua Poupança está rendendo 0.5%.')
                    print(f'Seu rendimento mensal está em R$ {poupanca1.calcular_rendimento()}')
                
                elif menu3 == '5':
                    print()
                    print(f'Saindo de Conta Poupança...')
                    return
                else:
                    print('Opção inválida!')
        
        if menu == '3':
            print('Saindo da aplicação...')
            quit()
            
        else:
            print('Opção inválida!')
            
if __name__ == '__main__':
    login()
                    
                    
                
                    



        
    
    
            
        
        
 
        