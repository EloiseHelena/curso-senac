import time


print('*************** CONTA BANCÁRIA **************')

class Banco:
     
   def __init__(self, titular):
       self.titular = titular   
       self.saldo = 0
    
   #Realizar consulta de nome
   def consultar_nome_titular(self):
       print(f'Nome do titular: {self.titular}')

   #Realizar consulta de saldo
   def consultar_saldo(self):
       print(f"Saldo atual: R${self.saldo}") 
   #Realizar depósito
   def depositar(self, valor):
      if valor <= 0:
         print('Valor inválido!')
      else:
         self.saldo += valor
         print(f"Depósito de R${valor} realizado com sucesso. novo saldo: R${self.saldo} ") 
   #Realizar saque
   def sacar(self, valor):
       if self.saldo >= valor:
          self.saldo -= valor
          print(f"Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}")
       else:
          print("Saldo insuficiente.")
           
conta = Banco('Eloise')
           

def login():  
   while True:
      print('\n ------------  INÍCIO  -------------')
      print('1 - Entrar na conta')
      print('2 - Sair')
      menu = input('Digite a opção desejada:  ')
   
      if menu == '1':
         while True:
            print('\n ------------  MENU  ------------')
            print('1 - Consultar Titular')
            print('2 - Consultar Saldo')
            print('3 - Depositar')
            print('4 - Sacar')
            print('5 - Sair')
            opcao = input('Digite a opção desejada: ')
      
            if opcao == '1':
               conta.consultar_nome_titular()
         
            elif opcao == '2':
               conta.consultar_saldo()
            
            elif opcao == '3':
               valor = float(input('Digite valor a ser depositado: R$'))
               conta.depositar(valor)
            
            elif opcao == '4':
               valor = float(input('Digite o valor a ser sacado: R$'))
               conta.sacar(valor)
         
            elif opcao == '5':
               print()
               print('Você saiu do programa...  \n')
               return
            else:
               print('Opção inválida!')
        
      if menu == '2':
         print('Você saiu do programa...  \n')
         for _ in tqdm(range(2)):
            time.sleep(1)
         quit()
      else:
         print('Opção inválida!')
        
if __name__ == '__main__':
    login()