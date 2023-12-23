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

9
kWh = float(input('Digite a quantidade de kWh: '))
print('Tipos de instalações: R, I, C')
instalação = input('Digite o tipo de instalação: ')

if instalação == 'R':
    if kWh <= 500:
       preco = 0.40 * kWh
    else:
         preco = 0.65 * kWh
         print('O preço calculado é de:{:.2f}'.format(preco))
elif instalação == 'C':
    if kWh <= 100:
       preco = 0.55 * kWh
    else:
         preco = 0.60 * kWh
         print('O preço calculado é de:{:.2f}'.format(preco))
elif instalação == 'I':
    if kWh <= 5000:
       preco = 0.55 * kWh
    else:
         preco = 0.60 * kWh
         print('O preço calculado é de:{:.2f}'.format(preco))


x = 1
while(x <= 5):
    print(x)
    x = x + 1

contagem
inicial = int(input('Qual valor deseja iniciar a contagem?: '))
final = int(input('Qual valor deseja encerrar a contagem?: '))
x= inicial
while (x<= final):
    if (x % 2 ==0):
        print(x)
    x = x + 1

acumuladores
soma = 0
cont = 1
while (cont <= 5):
    x = float(input('digite a {} nota: '.format(cont)))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print ('media final: {:.2f} '.format(media))

validar dados de entrada

x = int(input('Valor maior do que zero: '))
while (x <= 0):
    x = int(input('Valor maior do que zero: '))
print('Você digitou {}. Encerrando...'.format(x))

sair = input('Digite sair: ')
while (sair != 'sair'):
    sair = input('Digite sair: ')
print('Você digitou {}. Encerrando...'.format(sair))

break
print('Digite uma frase que irei repetir!')
print('Irei encerrar quando você digitar "sair".')
while True:
    texto = input('')
    print(texto)
    if (texto == 'sair'):
      break
print('Encerrando...')

while True:
    nome = input('Nome: ')
    if (nome != 'guilherme'):
        continue
    senha = input('Senha: ')
    if (senha == 'uninteR'):
        break
print('Acesso concedido.')

nome = ''
while not nome:
    nome = input('Nome: ')
valor = float(int(input('Digite um number: ')))
while (valor == 0 ):
    print('não aceitamos zero')
    valor = float(int(input('Digite um number: ')))
if valor:
    print('Ok {} Você digitou {}'.format(nome, valor))
else:
    print('não aceitamos zero')

for

for i in range(10, 20):
    # i var de controle do for
    # range função de intervalo
    if (i % 2 == 0):
      i += i / 3
      print('{:.2f}'.format(i))

for i in range(330, 10, -10):
    print(i)
soma = 0
qtd = 0
for i in range(1, 101):
     # i var de controle do for
     # range função de intervalo
    if (i % 2 == 0):
      soma += i
      qtd += 1
media = soma / qtd
print('média dos pares de 1 - 100 é: {:.2f}'.format(media))

estruturas aninhadas
tabuada = 1
while (tabuada <= 10):
    print('tabuada do {}'.format(tabuada))
    i =1
    while i <= 10:
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1

for tabuada in range(1,11,1):
1 inicial 11 final do iterador 1 passo adiciona ao inicial
    print('tabuada do {}'.format(tabuada))
    for i in range(1, 11, 1):
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))

tabuada = 1
while (tabuada <= 10):
    print('tabuada do {}'.format(tabuada))
    for i in range(1, 11, 1):
       print('{} x {} = {}'.format(tabuada, i, tabuada * i))
    tabuada += 1

inteiro = 3
while (inteiro <= 13):
     print(inteiro)
     inteiro += 1

     for i in range(3, 13):
        print(i)

inteiro = 0
while (inteiro <= 9):
    if (inteiro % 2 ==0):
      print(inteiro)
    inteiro += 1

for i in range (0,10, 2):
   print(i)

print('deseja sair? (digite sim):')
o = input('escolha um operador (+ ; - ; * ; /): ')
x = int(float(input('Digite: ')))
y = int(float(input('Digite: ')))

while True:
    o = input('Deseja sair? (digite sim): ')
    if o.lower() == 'sim':
        print('Encerrando...')
        break

    operador = input('Escolha um operador (+, -, *, /): ')
    if operador in ('+', '-', '*', '/'):
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))

        if operador == '+':
            resultado = x + y
        elif operador == '-':
            resultado = x - y
        elif operador == '*':
            resultado = x * y
        elif operador == '/':
            if y != 0:
                resultado = x / y
            else:
                print('Erro: divisão por zero!')
                continue

        print('Resultado:', resultado)
    else:
        print('Operador inválido. Escolha entre +, -, *, ou /')

