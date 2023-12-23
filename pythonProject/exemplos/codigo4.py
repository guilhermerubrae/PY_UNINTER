# Código 4 Menu de Frutas e Cálculo de Preços:
option = ['maçãs', 'maça', 'maças', 'laranjas', 'laranja', 'banana', 'bananas']
menu = ('Menu das frutas em promoção: maçãs, laranjas, bananas')
print(menu)
escolha = input('Escolha uma das opções acima: ').lower()
if escolha in ['maçãs', 'maça', 'maças']:
    unidades = int(input('Quantas unidades? '))
    preco = 2.30
    total = unidades * preco
    print('Total: {:.2f}'.format(total))
elif escolha in ['laranjas', 'laranja']:
    unidades = int(input('Quantas unidades? '))
    preco = 3.60
    total = unidades * preco
    print('Total: {:.2f}'.format(total))
elif escolha in ['banana', 'bananas']:
    unidades = int(input('Quantas unidades? '))
    preco = 1.85
    total = unidades * preco
    print('Total: {:.2f}'.format(total))
else:
    print('Opção inválida')
