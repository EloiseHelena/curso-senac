nome = 'nome'
idade = int
altura = float
peso = int
imc = float

print('Vamos calcular seu IMC? \n')

nome = input('Qual o seu nome? \n')
print('Olá', nome, '!')

idade = input('Qual a sua idade? \n')
print('Show!')

altura = float(input('Qual a sua altura? \n'))
print('Legal! Agora só mais uma pergunta...')

peso = int(input('Qual o seu peso? \n'))
print ('Vou calcular para você...')

imc =  peso/(altura * altura)
print('Seu IMC é', imc, '!')

