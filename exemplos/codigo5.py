# Código 5 Saudação com Base no Nome e Verificação de Idade:
nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
if nome == 'Guilherme':
    print('Welcome, Guilherme!')
else:
    print('Welcome, {}!'.format(nome))

if idade < 18:
    print('Você é menor de idade!')
elif idade > 100:
    print('Esta pessoa possivelmente não existe!')
else:
    print('Você é maior de idade!')
