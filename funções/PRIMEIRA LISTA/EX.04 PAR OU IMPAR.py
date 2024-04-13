numero = 0


print('__________PAR OU ÌMPAR?__________')

for numero in range(1):
  escolher_numero = int(input('Insira o número:'))
  
  
def par_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'
    
    
resultado = par_impar(escolher_numero)
print(f'O número {escolher_numero} é {resultado}.')
    
