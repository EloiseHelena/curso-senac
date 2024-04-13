numero = 0

print('__________FATORIAL DE UM NÚMERO__________')
     
for numero in range(1):
  escolher_numero = int(input('Insira o número:'))
  
def fatorial(escolher_numero):
    if escolher_numero == 0:
        return 1
    else:
        return escolher_numero * fatorial(escolher_numero - 1)
print(f'O fatorial de {escolher_numero}!, é {fatorial(escolher_numero)}.')