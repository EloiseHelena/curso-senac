numero = 0


print('__________ÁREA DE UM TRIÂNGULO__________')
     
for numero in range(1):
  base = float(input('Insira o valor da base:'))
  altura = float(input('Insira o valor da altura:'))
  
def calcular_area_triangulo(base, altura):
  area = base * altura / 2
  return area

area = calcular_area_triangulo(base, altura)
print(f'A area do triângulo é: {area}')
  