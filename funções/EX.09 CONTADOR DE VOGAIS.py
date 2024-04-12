print('__________CONTADOR DE VOGAIS__________')
     
for palavra in range(1):
  palavra= str(input('Insira a palavra a ser verificada:'))

def contar_vogais (palavra):
  vogais = 'aeiouAEIOU'
  num_vogais = 0
  
  for char in palavra:
     if char in vogais:
       num_vogais += 1
  return num_vogais
print(f'A palavra tem {contar_vogais(palavra)} vogais.')