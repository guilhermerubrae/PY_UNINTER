# Cálculo de Preço com Base em Dias e Distância 
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