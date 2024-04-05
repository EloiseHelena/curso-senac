livros_lidos = {'Coraline', 'A marca de uma lágrima', 'Capitães da Areia', 'Gato preto', 'A Droga da Obediencia', 'Estatutos do homem', 'Os Miseráveis', 'O homem que calculava'}
livros_ler = {'O Vazio', 'Código Limpo', 'Will', 'A Arte da Guerra', 'A Metamorfose', 'O Príncipe'}

conjunto_ler = livros_ler.difference(livros_lidos)
print(f'Ler depois: {conjunto_ler}')