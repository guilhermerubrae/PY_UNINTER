print('Bem-vindo a loja do Guilherme Abreu do Nascimento')
precos = {
    'CP': {'P': 10, 'M': 15, 'G': 19},
    'AC': {'P': 12, 'M': 17, 'G': 21},
}
print('Menu:')
print('Tamanho P de Cupuaçu (CP) custa', precos['CP']['P'], 'reais e o Açaí (AC) custa', precos['AC']['P'], 'reais')
print('Tamanho M de Cupuaçu (CP) custa', precos['CP']['M'], 'reais e o Açaí (AC) custa', precos['AC']['M'], 'reais')
print('Tamanho G de Cupuaçu (CP) custa', precos['CP']['G'], 'reais e o Açaí (AC) custa', precos['AC']['G'], 'reais')
#um dicionário que armazena os tamanhos e preços visualmente para o cliente.
#a variável preços recebe chaves para iniciar um dicionário.
#na saída do console colchetes para chamar os valores CP e AC que recebem outros valores.
total = 0
#total está acima de while para que calcule a soma sem interferência do while abaixo.
while True:
#while recebe True porque enquanto as condições continuem verdadeira o código reinicia a partir de sabor.
    sabor = input('Escolha o sabor desejado (CP/AC): ')
    while sabor not in ('CP', 'AC'):
#while pois se o sabor estiver incorreto o código reiniciar a entrada sabor
#not in pois se o valor colocado não for o descrito mandar uma saída de erro
        print("Sabor inválido. Tente novamente.")
        sabor = input('Escolha o sabor desejado (CP/AC): ')
        continue

    tamanho = input('Escolha o tamanho desejado (P/M/G): ')
    while tamanho not in ('P', 'M', 'G'):
# while pois se o tamanho estiver incorreto o código reiniciar a entrada sabor
# not in pois se o valor colocado não for o descrito mandar uma saída de erro
        print("Tamanho inválido. Tente novamente.")
        tamanho = input('Escolha o tamanho desejado (P/M/G): ')
        continue

    if sabor == 'CP' and tamanho == 'P':
        total += 10
    elif sabor == 'CP' and tamanho == 'M':
        total += 15
    elif sabor == 'CP' and tamanho == 'G':
        total += 17
    elif sabor == 'AC' and tamanho == 'P':
        total += 12
    elif sabor == 'AC' and tamanho == 'M':
        total += 17
    elif sabor == 'AC' and tamanho == 'G':
        total += 21
# os operadores += são análogos à: total = total + (algum valor) ou seja a mesma coisa e os operadores simplificam

    mais = input("Deseja pedir mais alguma coisa? (S/N) ")
    if mais != 'S':
        print("O total do seu pedido é R$ {:.2f}. Obrigado pela sua compra!".format(total))
        break
#break o código irá parar de rodar

