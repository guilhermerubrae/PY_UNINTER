# recapitulando a atividade 3 / exercício 3/4

#Ínicio Função volumeFeijoada()

def volumeFeijoada():
    print('--------------- Menu 1 de 3 - Volume Feijoada---------------')
    while True:
        try:
            volumeF = int(input('Digite a quantidade desejada em ml: '))
            if (volumeF >= 300) and (volumeF <= 5000): #if 300 <= volumeF <= 5000: cód enxuto que só funciona em py
                return volumeF * 0.08 #unica porta de saida para o programa principal
            else:
                print('Valores digitados incorretos excedem o mínimo ou máximo')
        except ValueError: # Caso o user coloque string ou float
             print('Digite apenas valores inteiros')
             continue # retorna a pergunta
#fim
def opcaoFeijoada():
    print('--------------- Menu 2 de 3 - Opção Feijoada---------------')
    while True:
        opcaoF = input('Selecione a feijoada: \n' +
                     'b- básica \n' +
                     'p- premium \n' +
                     's- suprema  \n' +
                     '>>  ')
        opcaoF = opcaoF.lower()
        opcaoF = opcaoF.strip()
        if opcaoF == 'b':
            return 1.00
        if opcaoF == 's':
            return 1.25
        if opcaoF == 'p':
            return 1.50
        else:
            print('Opção inválida')
            continue #voltará ao incio
#fim
def acompanhamentoFeijoada():
    print('--------------- Menu 2 de 3 - Acompanhamento Feijoada---------------')
    acumulador = 0
    while True:
        acompanhamentoF = input('Deseja incluir algum adicional? \n' +
                     '0- Não, encerre. \n' +
                     '1- 200g de arroz \n' +
                     '2- 150g de farofa  \n' +
                     '3- 100g de couve \n'  +
                     '4- 1 laranja descascada \n' +
                     '>>  ')
        if acompanhamentoF == '0':
            return acumulador #retorna os valores
        if acompanhamentoF == '1':
            acumulador = acumulador + 5 # Adiciona o acompanhamento ao acumulador
            continue # Volta para o wT
        if acompanhamentoF == '2':
            acumulador = acumulador + 6  # Adiciona o acompanhamento ao acumulador
            continue  # Volta para o wT
        if acompanhamentoF == '3':
            acumulador = acumulador + 7  # Adiciona o acompanhamento ao acumulador
            continue  # Volta para o wT
        if acompanhamentoF == '4':
            acumulador = acumulador + 3  # Adiciona o acompanhamento ao acumulador
            continue  # Volta para o wT
        else:
            print('Inválido')
            continue


#fim

# Ínicio do main
print('--------------- Bem Vindo ao programa de Feijoada do Guilherme Abreu do Nascimento ---------------')
volume = volumeFeijoada()
print(volume)
opcao = opcaoFeijoada()
print(opcao)
acompanhamento = acompanhamentoFeijoada()
total = volume * opcao + acompanhamento
print('Total R$ {:.2f} (Volume: R$ {:.2f}) (Opção: R$ {:.2f}) (Acompanhamento: R$ {:.2f})'. format(total, volume, opcao, acompanhamento))