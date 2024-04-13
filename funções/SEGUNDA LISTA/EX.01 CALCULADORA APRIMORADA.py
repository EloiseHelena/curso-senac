

print('CALCULADORA APRIMORADA')

while True:
    print('MENU:\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n5 - POTÊNCIA\n6 - SAIR')
    operacao = (input('Escolha o tipo de operação: '))

    
    if operacao == '1': 
     def soma(n1, n2):
      return n1 + n2
     n1 = float (input('Insira o primeiro número: '))
     n2 = float(input('Insira o segundo número: '))
     resultado = (n1 + n2)
     print(f'O resultado da soma é: {resultado}')
    
    
    elif operacao == '2': 
     def subtracao(n1, n2):
        return n1 - n2
     n1 = float (input('Insira o primeiro número: '))
     n2 = float(input('Insira o segundo número: '))
     resultado = (n1 - n2)
     print(f'O resultado da subtração é: {resultado}')
     
    elif operacao == '3': 
     def multiplicacao(n1, n2):
       return n1 * n2
     n1 = float (input('Insira o primeiro número: '))
     n2 = float(input('Insira o segundo número: '))
     resultado = (n1*n2)
     print(f'O resultado da multiplicação é: {resultado}')  
      
    elif operacao == '4': 
     def divisao(n1, n2):
        return n1 / n2
     n1 = float (input('Insira o primeiro número: '))
     n2 = float(input('Insira o segundo número: '))
     resultado = (n1/n2)
     print(f'O resultado da divisão é: {resultado:.2f}') 
     
     
    elif operacao == '5': 
     def potencia(base, expoente):
         resultado = base ** expoente 
         return resultado
     base = float (input('Insira o valor da base: '))
     expoente = float(input('Insira o  valor do expoente: '))
     resultado = int(potencia(base, expoente))
     print(f'O resultado da divisão é: {resultado}')
 
 
    elif operacao == '6':
        print('Saindo...')
        break
    else:
        print('Opção inválida')
        

