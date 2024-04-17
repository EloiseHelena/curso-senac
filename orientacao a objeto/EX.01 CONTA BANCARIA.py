import random
import string
import time

contas = []

class Banco:
 for palavra in range(1):
     
    def __init__(self, titular):
        self.titular = titular   
        self.saldo = 0
            
    #Realizar consulta de saldo
    def consultar(self):
        print(f"Saldo atual: R${self.saldo}")

    #Realizar depósito
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso. novo saldo: R$[self.saldo ")

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
     print('\n ------------  MENU  ------------')
     print('1 - Consultar Saldo')
     print('2 - Depositar')
     print('3 - Sacar')
     print('4 - Sair')
     opcao = input('Digite a opção desejada: ')

     if opcao == '1':
      conta.consultar()
      
     elif opcao == '2':
        valor = float(input('Digite valor a ser depositado: R$'))
        conta.depositar(valor)
        
     elif opcao == '3':
        valor = float(input('Digite o valor a ser sacado: R$'))
        conta.sacar(valor)
     
     elif opcao == '4':
        print()
        print('Você saiu do programa...  \n')
        return
     else:
        print('Opção inválida!')
        
if __name__ == '__main__':
    login()