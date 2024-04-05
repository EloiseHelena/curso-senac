n = int(input("Digite a quantidade de células da sua lista: \n"))
numero = 0
lista_numeros= []
for numero in range(n):
    inserir_numero = input('Digite o {}° número da sua lista: \n' .format(numero))
    inserir_numero_formatado = int(inserir_numero)
    lista_numeros.append(inserir_numero_formatado)
print(f'Sua lista de números: {lista_numeros}\n')

#######################    Exercício 1 - Maior Valor  ###################################

maior_valor = max(lista_numeros)
print(f'O maior valor da sua lista é: {maior_valor} \n')

#######################    Exercício 2 - Soma  ###################################

soma = sum(lista_numeros)
print(f'Resultado da soma da sua lista: {soma} \n')

#########################  Exercício 3 - Média ################################### 

media = soma / (len(lista_numeros))

print(f'A média da sua lista é: {media} \n')

########################  Exercício 4 - Posição Menor Valor  #############################

menor_valor = min(lista_numeros)
posicao_menor = lista_numeros.index(menor_valor)
print(f'O menor valor da sua lista está na posição: {posicao_menor} \n')

########################  Exercício 5 - Posição Maior Valor  ##############################

maior_valor = max(lista_numeros)
posicao_maior = lista_numeros.index(maior_valor)
print(f'O maior valor da sua lista está na posição: {posicao_maior} \n \n')

########################  Exercício 6 - Encontrar o número de vezes  ########################

escolher_numero = int(input('Digite o número que você  quer contar as repetições: \n'))
quantidade = lista_numeros.count(escolher_numero)
print(f'O número {escolher_numero} aparece {quantidade} vezes na lista. \n \n')

########################  Exercício 7 - Verificar se um valor está presente em uma lista  ########################

valor = int(input('Digite o número a ser verificado: \n'))
if valor in lista_numeros:
    print(f'O número {valor} se encontra na lista.\n')
else:
    print(f'O número {valor} não se encontra na lista.\n')
    
########################  Exercício 8 - Gerar um lista com valores pares ########################

pares = []
for valor in lista_numeros:
    if valor % 2 == 0:
        pares.append(valor)

print(f'O valores pares da lista são {pares}')
 
########################  Exercício 9 - Gerar um lista com valores ímpares ########################   

impar = []
for valor in lista_numeros:
    if valor % 2 != 0:
        impar.append(valor)

print(f'O valores ímpares da lista são {impar}\n')

########################  Exercício 10 - Inverter as ordens dos elementos ########################
   
lista_numeros.reverse()
print(f'Sua lista invertida fica assim: {lista_numeros} \n \n')

########################  Exercício 11 - Concatenar duas listas ########################   

print('VAMOS MESCLAR A LISTA ANTERIOR COM UMA NOVA LISTA?\n')

p = int(input("Digite a quantidade de células da sua segunda lista: \n"))
numero = 0
segunda_lista = []
for numero in range(p):
    inserir_numero = input('Digite o {}° número da sua lista: \n' .format(numero))
    inserir_numero_formatado = int(inserir_numero)
    segunda_lista.append(inserir_numero_formatado)
print(f'Sua segunda lista de números é: {segunda_lista}\n')


concatenar_listas = lista_numeros + segunda_lista
print(f'Sua nova lista concatenada é: {concatenar_listas}\n')

########################  Exercício 12 - Dividir a lista em duas ######################## 

print('VAMOS DIVIDIR SUA LISTA?\n')
dividir = (len(concatenar_listas)) // 2
lista_um = concatenar_listas[:dividir]
lista_dois = concatenar_listas[dividir:]

print(f'Essa é sua primeira lista {lista_um}')
print(f'Essa é sua segunda lista {lista_dois}\n')

########################  Exercício 13 - Ordenar os elementos de uma lista ######################## 

concatenar_listas.sort()
print(f'Sua  nova lista  ordenada fica assim: {concatenar_listas} \n')

########################  Exercício 14 - Remover um elemento de uma lista ######################## 

remover_numero = int(input('Digite o número que você  quer remover: \n'))
remover = concatenar_listas.remove(remover_numero)
print(f'O número {remover_numero} foi removido da lista. \n \n')
print(f'Após a remoção sua lista ficou assim: {concatenar_listas}\n')

########################  Exercício 15 - Adicionar um elemento de uma lista ######################## 
print('AGORA VAMOS ADICIONAR UM NÚMERO:\n')
adicionar_numero = int(input('Digite o número que você  quer adicionar: \n'))
adicionar = concatenar_listas.append(adicionar_numero)
print(f'O número {adicionar_numero} foi adicionado na lista. \n \n')
print(f'Após a adição sua lista ficou assim: {concatenar_listas}\n')