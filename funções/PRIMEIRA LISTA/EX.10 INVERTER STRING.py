print('__________INVERTER PALAVRA__________')
     
for palavra in range(1):
  palavra= str(input('Insira a palavra a ser verificada:'))
  
def inverter_string(palavra):
    return palavra[:: -1]
palavra_invertida = inverter_string(palavra)
print(f'Sua palavra invertida é: {palavra_invertida}')