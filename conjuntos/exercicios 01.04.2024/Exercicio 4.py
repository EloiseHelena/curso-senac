estados_brasil = {'Acre', 'Alagoas', 'Amazonas', 'Amapá', 'Bahia', 'Ceará', 'Rio Grande do Sul', 'Santa Catarina', 'São Paulo' 'Brasília', 'Roraima', 'Rio de Janeiro'}
estados_visitados = {'Amazonas', 'Roraima', 'Rio Grande do Sul', 'Santa Catarina', 'São Paulo', 'Brasília'}


while True:
 subconjunto = estados_brasil.issubset(estados_visitados)
 if subconjunto != set():
    print('O primeiro conjunto é um subconjunto do segundo conjunto')
    break
 else:
    print('O primeiro conjunto não é um subconjunto do segundo conjunto')
    break
