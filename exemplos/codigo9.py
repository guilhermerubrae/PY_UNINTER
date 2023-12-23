
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

