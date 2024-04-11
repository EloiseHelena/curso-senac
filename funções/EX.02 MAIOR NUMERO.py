numero = 0
lista = []

print('__________CRIE SUA LISTA E SAIBA O MAIOR NÚMERO__________')

for numero in range(5):
  escolher_numero = int(input('Insira sua lista de números:'))
  lista.append(escolher_numero)
  print(f'Sua lista ficou assim: {lista} ')
 

def maior_numero(lista):
    if not lista:
        return None
    else:
        return max(lista)

print(f'O maior número da lista é {(maior_numero(lista))}.')



