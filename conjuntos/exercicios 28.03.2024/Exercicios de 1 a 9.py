
numero = 0
meu_conjunto = set()
segundo_conjunto = set()
intersecao = set()
diferenca = set()
uniao = set()
ordenar_crescente = int
ordenar_decrescente = int
remover_duplicados = set()
conjunto_jogo = {8, 9, 1, 3, 5}
conjunto_chutes = set()

print('**********EXERCÍCIOS DO DIA 28/03/03 - CONJUNTOS********** \n')
print('01 = Verificação de um elemento em um conjunto.\n02 = Interseção de conjunto.\n03 = Diferença de conjuntos.\n04 = União de conjuntos.\n05 = Subconjuntos.\n06 = Ordenação de elementos em um conjunto.\n07 = Remoção de elementos duplicados.\n08 = Jogo de adivinhação com conjuntos.\n09 = Cálculo de média, mediana e moda de um conjunto.\n10 = Sair.\n')

while True: 
    exercicio = (input('Digite o número do exercício que deseja verificar: '))
     
    if exercicio == '01':
        print('**********EXERCÍCIO 01 - VERIFICAÇÃO DE ELEMENTO EM CONJUNTO*********')
        for numero in range(6):
    
         criar_conjunto = int(input('Insira os números desejados do conjunto:'))
         meu_conjunto.add(criar_conjunto)
         print('Número adicionando com sucesso!\n')
        while True:
            verificar = int(input('Verifique se um número está no conjunto: '))
            if verificar in meu_conjunto:
                print('Esse número está no conjunto.\n')
                break
            else:
                print('Esse número não está no conjunto.\n')
      
        
        
    elif exercicio == '02': 
        print('**********EXERCÍCIO 02 - INTERSEÇÃO DE CONJUNTO*********')
        
        for numero in range(3):
    
         criar_conjunto = int(input('Insira os números desejados do primeiro conjunto:'))
         meu_conjunto.add(criar_conjunto)
         print(f'Número adicionando com sucesso! Seu primeiro conjunto possui esses valores:\n {meu_conjunto}\n')
         
        for numero in range(3):
         criar_segundo_conjunto = int(input('Insira os números desejados para um segundo conjunto:'))
         segundo_conjunto.add(criar_segundo_conjunto)
         print(f'Número adicionando com sucesso! Seu segundo conjunto possui esses valores:\n {segundo_conjunto}\n')
         
        while True:
            intersecao = meu_conjunto.intersection(segundo_conjunto)
            if intersecao != set():
                print(f'Os valores de interseção dos seus conjuntos são: {intersecao}')
                break
            else:
                 print('Não há interseções nos conjuntos.')
                 break
                     
         
         
    elif exercicio == '03':
        print('**********EXERCÍCIO 03 - DIFERENÇA DE CONJUNTOS*********')
        
        for numero in range(6):
    
         criar_conjunto = int(input('Insira os números desejados do primeiro conjunto:'))
         meu_conjunto.add(criar_conjunto)
         print(f'Número adicionando com sucesso! Seu primeiro conjunto possui esses valores:\n {meu_conjunto}\n')
         
        for numero in range(6):
         criar_segundo_conjunto = int(input('Insira os números desejados para um segundo conjunto:'))
         segundo_conjunto.add(criar_segundo_conjunto)
         print(f'Número adicionando com sucesso! Seu segundo conjunto possui esses valores:\n {segundo_conjunto}\n')
        
        while True:
         for numero in meu_conjunto:
          if numero not in segundo_conjunto or numero in meu_conjunto and numero not in segundo_conjunto:
           diferenca.add(numero)

         for numero in segundo_conjunto:
          if numero not in meu_conjunto or numero in segundo_conjunto and numero not in meu_conjunto:
           diferenca.add(numero)
         if diferenca != set():
             print(f'A diferença simétrica é: {diferenca}.')
             break
         else:
            print('Não há diferença simétrica.')
            break
         
        
        
    elif exercicio == '04':
        print('**********EXERCÍCIO 04 - UNIÃO DE CONJUNTOS*********')
        
        for numero in range(6):
    
         criar_conjunto = int(input('Insira os números desejados do primeiro conjunto:'))
         meu_conjunto.add(criar_conjunto)
         print(f'Número adicionando com sucesso! Seu primeiro conjunto possui esses valores:\n {meu_conjunto}\n')
         
        for numero in range(6):
         criar_segundo_conjunto = int(input('Insira os números desejados para um segundo conjunto:'))
         segundo_conjunto.add(criar_segundo_conjunto)
         print(f'Número adicionando com sucesso! Seu segundo conjunto possui esses valores:\n {segundo_conjunto}\n')
        
        while True:
         for numero in meu_conjunto:
             if numero in segundo_conjunto or numero in meu_conjunto and numero not in segundo_conjunto: 
                uniao.add(numero)
                
         for numero in segundo_conjunto:
             if numero in meu_conjunto or numero in segundo_conjunto and numero not in meu_conjunto:
                 uniao.add(numero)

         print(f'A união do conjunto é: {uniao}.')
         break
         
        
        
    elif exercicio == '05':
        print('**********EXERCÍCIO 05 - SUBCONJUNTOS*********')
        
      
        
        

    elif exercicio == '06':
        print('**********EXERCÍCIO 06 - ORDENAÇÃO DE ELEMENTOS EM UM CONJUNTO*********')
        
        for numero in range(6):
    
         criar_conjunto = int(input('Insira os números desejados do conjunto:'))
         meu_conjunto.add(criar_conjunto)
         print('Número adicionando com sucesso!\n')
     
        print('Escolha de que forma o ordenamento será realizado:\n01 = CRESCENTE\n02 = DESCRESCENTE\n')
        while True:
         escolha = (input('Digite o modo desejado:  ')) 
         
         if escolha == '01':
          ordenar_crescente = sorted(meu_conjunto)
          print(f'Este é seu conjunto em ordem crescente: {ordenar_crescente}')
          break
         
         elif escolha == '02':
             ordenar_decrescente = sorted(meu_conjunto, reverse=True)
             print(f'Este é seu conjunto em ordem decrescente: {ordenar_decrescente}')
             break
         else:
             print('Opção inválida, digite as opções entre 01 - Ordem Crescente ou 02 - Ordem Decrescente! ')
             break
            
       
   
    elif exercicio == '07':
        print('**********EXERCÍCIO 07 - REMOÇÃO DE ELEMENTOS DUPLICADOS*********')
        for numero in range(4):
    
         criar_conjunto = int(input('Insira os números ou itens desejados do conjunto:'))
         meu_conjunto.add(criar_conjunto)
         print(f'Item adicionando com sucesso! Seu primeiro conjunto possui esses valores:\n {meu_conjunto}\n')
         
        while True: 
         for numero in meu_conjunto:
            remover_duplicados.add(numero)
            
         print(f'Foram removidas as duplicatas, seu conjunto ficou assim: {remover_duplicados}')
         break
       
         
          
    elif exercicio == '08':
        print('**********EXERCÍCIO 08 - JOGO DE ADIVINHAÇÃO COM CONJUNTOS*********')
       
        for numero in range(5):
         adivinhar = int(input('Tente adivinhar os números entre 1 e 10 do conjunto: '))
         conjunto_chutes.add(numero)
         while True:
            if adivinhar in conjunto_jogo:
                print('Esse número está no conjunto.\n')
                break
            else:
             print('Esse número não está no conjunto.\n')
             break
            
        print(f'Seu conjunto é {conjunto_chutes}')
        print(f'O conjunto secreto é: {conjunto_jogo}')
             
         
         
    elif exercicio == '09':
        print('**********EXERCÍCIO 09 - CÁLCULO DE MÉDIA, MEDIANA E MODA EM CONJUNTO*********')
        for numero in range(6):
    
         criar_conjunto = int(input('Insira os números desejados do conjunto:'))
         meu_conjunto.add(criar_conjunto)
         print(f'Número adicionando com sucesso! Seu primeiro conjunto possui esses valores:\n {meu_conjunto}\n')
         
         
    
    elif exercicio == '10':
        print('SAINDO...')
        break
    else:
        print('Opção inválida, digite as opções de 01 a 10 do Menu!')