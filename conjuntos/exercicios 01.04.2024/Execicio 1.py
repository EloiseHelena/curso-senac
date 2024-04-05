amigos = {'Fernando', 'Tuany', 'Kamila', 'Matheus', 'Carol', 'Tayane', 'Lari', 'Júlia'}
verificar = str(input('Verifique se seu nome está na lista: '))
if verificar in amigos:
    print('Amigo, você é um amigo! Bora tomar uma???')
else:
    print('Acho que não conheço você, vamos deixar para próxima.')