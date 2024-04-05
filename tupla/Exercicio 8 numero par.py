valores = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numero_par = list(valores)
pares = []

for valor in numero_par:
    if valor % 2 == 0:
        pares.append(valor)

tupla_pares = tuple(pares)
print(f'O valores pares da tupla são {tupla_pares}')