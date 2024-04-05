receita_bolo = ('leite', 'farinha', 'ovos', 'fermento', 'açúcar', 'margarina')
ingredientes = list(receita_bolo)

item = str(input('Digite o item a ser verificado: \n'))
if item in ingredientes:
    print('O item se encontra na tupla.')
else:
    print('O item não está na tupla.')