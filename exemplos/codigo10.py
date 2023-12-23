1
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
if(x >= y):
   print('resultado true')
else:
   print('resultado false')

2
y = float(input('Digite o segundo valor: '))
if(y %2 == 1):
   print('resultado IMPAR')
else:
   print('resultado PAR')

3
nota1 = float(input('digite a nota da 1 matéria: '))
nota2 = float(input('digite a nota da 2 matéria: '))
nota3 = float(input('digite a nota da 3 matéria: '))
minimo = 7
if nota1 >= minimo and nota2 >= minimo and nota3 >= minimo:
  print('passou')
else:
  print('reprovado')

4
option = ['maçãs', 'maça', 'maças', 'laranjas', 'laranja', 'banana', 'bananas']
menu = ('Menu das frutas em promoção: maçãs, laranjas, bananas')
print(menu)
escolha = input('Escolha uma das opções acima: ').lower()
if (escolha in ['maçãs', 'maça', 'maças']):
   unidades = int(input('Quantas unidades? '))
   preco = 2.30
   total = unidades * preco
   print('Total: {:.2f}'.format(total))
elif (escolha in ['laranjas', 'laranja']):
   unidades = int(input('Quantas unidades? '))
   preco = 3.60
   total = unidades * preco
   print('Total: {:.2f}'.format(total))
elif (escolha in ['banana', 'bananas']):
   unidades = int(input('Quantas unidades? '))
   preco = 1.85
   total = unidades * preco
   print('Total: {:.2f}'.format(total))
else:
    print('Opção inválida')

5
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

6
z = (2+2) < 4
print(z)
a = (7 // 3) == 1+1
print(a)
b = (3 ** 2 + 4 ** 2 == 25)
print(b)
zz = (2+4+6) > 12
print(zz)
print(1387 % 19 == 0)
print(31 % 2 == 1)
print(min(34, 29, 31) < 30)

7
idade = int(input('Digite sua idade: '))
if idade > 60:
    print('Você tem direito aos benefícios!')

dano = int(input('Digite: '))
escudo = int(input('Digite: '))
if dano > 10 and escudo == 0:
    print('Morreu')

if (n or s or l or o):
    print('Escapou')

if (2023 % 4):
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')

if ('cima' and 'baixo'):
    print('Decida-se')
else:
    print('Você escolheu um caminho')

8
A =int(input('Digite o 1 lado: '))
B =int(input('Digite o 2 lado: '))
C =int(input('Digite o 3 lado: '))

if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (C + B > A):
        if (A != B) and (A != C) and (C != B):
            print('Triângulo escaleno')
        else:
            if (A == B) and (A == C) and (C == B):
                print('Triângulo equilátero')
            else:
                print('Triângulo isósceles')
    else:
        print('erro')
else:
    print('erro')

9
print('CALCULADORA')
x = float(input('Digite o valor: '))
y = float(input('Digite o valor: '))
operacao = input('Digite a operação desejada (adição, subtração, multiplicação, divisão): ')

if operacao == 'adição':
    resultado = y + x
    print('O resultado deu:{}'.format(resultado))
elif operacao == 'subtração':
    resultado = y - x
    print('O resultado deu:{}'.format(resultado))
elif operacao == 'divisão':
    resultado = y / x
    print('O resultado deu:{}'.format(resultado))
elif operacao == 'multiplicação':
    resultado = y * x
    print('O resultado deu:{}'.format(resultado))
else:
    print('Operação inválida. Por favor, escolha uma operação válida.')
print('Encerrando')

