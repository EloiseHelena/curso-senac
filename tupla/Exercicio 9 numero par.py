valores = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numero_impar = list(valores)
impar = []

for valor in numero_impar:
    if valor % 2 != 0:
        impar.append(valor)

tupla_impar = tuple(impar)
print(f'O valores pares da tupla são {tupla_impar}')