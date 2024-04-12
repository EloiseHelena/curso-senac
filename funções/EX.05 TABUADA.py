

print('__________TABUADA DE 1 A 10__________')
print('MENU:\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n5 - SAIR')



while True:
  operacao = (input('Escolha o tipo de operação: '))

  if operacao == '1':
      def tabuada():
       for i in range(1, 11):
         print(f'Tabuada do {i}')
         for j in range(1, 11):
            print(f'{i} + {j} = {i+j}')
         print()
      tabuada()
    
  elif operacao == '2':
      def tabuada():
       for i in range(1, 11):
         print(f'Tabuada do {i}')
         for j in range(1, 11):
            print(f'{i} - {j} = {i-j}')
         print()
      tabuada()
      
  elif operacao == '3':
      def tabuada():
       for i in range(1, 11):
         print(f'Tabuada do {i}')
         for j in range(1, 11):
            print(f'{i} - {j} = {i-j}')
         print()
      tabuada()
   
  elif operacao == '4':
      def tabuada():
       for i in range(1, 11):
         print(f'Tabuada do {i}')
         for j in range(1, 11):
            print(f'{i} / {j} = {i/j}')
         print()
      tabuada()
     
  elif operacao == '5':
        print('Saindo...')
        break
  else:
        print('Opção inválida')
        