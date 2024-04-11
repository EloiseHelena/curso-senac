numero = 0
lista = []

print('__________CALCULE A MÉDIA DE 3 NÚMEROS__________')

for numero in range(3):
  escolher_numero = float(input('Insira os números:'))
  lista.append(escolher_numero)
  print(f'Sua lista ficou assim: {lista} ')
  
def media(lista):
    return sum(lista) / len(lista)

print(f'A média dos valores é {(media(lista))}.')