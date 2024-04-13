
print('__________VERIFICA PALÍNDROMO__________')
     
for palavra in range(1):
  palavra= str(input('Insira a palavra a ser verificada:'))
  
def verificar_palindromo(palavra):
 palavra = palavra.replace(' ', ' ').lower()
 return palavra == palavra[::-1]

if verificar_palindromo(palavra):
    print(f'{palavra} é um palíndromo!')
else:
    print(f'{palavra} não é um palíndromo!')

    