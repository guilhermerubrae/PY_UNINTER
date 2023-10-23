#preco = float(input('Preço do produto:'))
#p = float(input('Percentual de desconto(0-50)%:'))

#desconto = preco * (p / 100)
#final = preco - desconto
#print('O preço do produto é {}. Desconto {}%.'.format(preco, p))
#print('Valor calculado de desconto: {}. Valor final do produto {}'.format(desconto, final))

#km = int(input('Quantos km foram percorridos?:'))
#dias = int(input('Quantos dias o selta foi usado?:'))

#preco  = 60 * dias + 0.15 * km
#print('O carro percorreu {}. por {}%. dias'.format(km, dias))
#print('Valor calculado de: {}'.format(preco))

frase1 = input('Digite uma frase:')
tam = len(frase1)
frase2 = frase1[:int(tam/2)]
print(frase2[-2:])
print(frase1[24:34])

tam = len(frase1)
print('Exemplo: ', tam)

letra1 = 44
letra = 'você tirou %.4s na prova de letramento' % (frase1)
print('Exemplo: ', letra)