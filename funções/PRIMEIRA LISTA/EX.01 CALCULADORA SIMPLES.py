print('CALCULADORA SIMPLES')
print('MENU:\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n5 - SAIR')

while True:
    operacao = (input('Escolha o tipo de operação: '))
    
    if operacao == '1': 
     def soma(n1, n2):
      return n1 + n2
     n1 = float (input('Insira o primeiro número: '))
     n2 = float(input('Insira o segundo número: '))
     print(f'O resultado da soma é: {(n1 + n2)}')
 
    
    elif operacao == '2': 
     def subtracao(n1, n2):
        return n1 - n2
     n1 = float (input('Insira o primeiro número: '))
     n2 = float(input('Insira o segundo número: '))
     print(f'O resultado da subtração é: {(n1 - n2)}')
     
    elif operacao == '3': 
     def multiplicacao(n1, n2):
       return n1 * n2
     n1 = float (input('Insira o primeiro número: '))
     n2 = float(input('Insira o segundo número: '))
     print(f'O resultado da multiplicação é: {(n1 * n2)}')  
      
    elif operacao == '4': 
     def divisao(n1, n2):
        return n1 / n2
     n1 = float (input('Insira o primeiro número: '))
     n2 = float(input('Insira o segundo número: '))
     print(f'O resultado da divisão é: {(n1 / n2)}')
 
    elif operacao == '5':
        print('Saindo...')
        break
    else:
        print('Opção inválida')
        








 

 

 