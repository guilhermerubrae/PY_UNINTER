# Função para exibir o menu de serviços e custos
def exibir_menu():
    # Imprime uma linha de separação para melhorar a legibilidade
    print('|' + '-' * 80 + '|')
    # Imprime uma mensagem de boas-vindas
    print("|Bem-vindo a prestadora de serviçõs de impressão do Guilherme Abreu do Nascimento|")
    # Imprime outra linha de separação
    print('|' + '-' * 80 + '|')
    # Imprime os serviços disponíveis e seus custos
    print("\nAqui estão nossos serviços e seus respectivos custos por página:")
    print("1. Impressão Digital (DIG) - R$ 1.10")
    print("2. Impressão Colorida (ICO) - R$ 1.00")
    print("3. Impressão em Branco e Preto (IBO) - R$ 0.40")
    print("4. Impressão de Fotos (FOT) - R$ 0.20")
    # Imprime os serviços adicionais disponíveis e seus custos
    print("\nTambém oferecemos serviços adicionais de encadernação:")
    print("1. Encadernação Simples - R$ 10.00")
    print("2. Encadernação com Capa Dura - R$ 25.00")
    print("3. Sem Encadernação - R$ 0.00")


# Função para escolher o serviço desejado e retorna o custo do serviço escolhido.
def escolha_servico():
    # Dicionário com os custos por página de cada serviço
    # As chaves são as abreviações dos serviços e os valores são os custos.
    custo_por_pagina = {'DIG': 1.10, 'ICO': 1.00, 'IBO': 0.40, 'FOT': 0.20}

    # Loop infinito para continuar perguntando até receber uma resposta válida
    while True:
        # Pergunta o serviço desejado ao usuário
        servico = input("\nQual serviço você deseja? DIG/ICO/IBO/FOT: ").upper()

        # Verifica se o serviço escolhido está no dicionário
        if servico in custo_por_pagina:
            # Retorna o custo do serviço escolhido
            return custo_por_pagina[servico]

        else:
            # Informa ao usuário que a opção escolhida é inválida e repete a pergunta
            print("Opção inválida. Digite novamente.")

# Função para perguntar o número de páginas ao usuário e retorna o número de páginas com desconto aplicado.
def num_pagina():
    # Loop infinito para continuar perguntando até receber uma resposta válida
    while True:

        try:
            # Pergunta o número de páginas ao usuário
            num_pagina = int(input("\nQuantas páginas você quer? "))

            # Verifica se o número de páginas está dentro do limite aceitável
            if num_pagina < 10000:

                # Aplica um desconto com base no número de páginas
                if num_pagina < 10:
                    desconto = 0
                elif num_pagina < 100:
                    desconto = 0.10
                elif num_pagina < 1000:
                    desconto = 0.15
                else:
                    desconto = 0.20

                # Retorna o número de páginas com desconto aplicado
                return num_pagina * (1 - desconto)

            else:
                # Informa ao usuário que não são aceitos pedidos com mais de 10000 páginas e repete a pergunta
                print("Não são aceitos pedidos com mais de 10000 páginas.")

        except ValueError:
            # Informa ao usuário que o valor digitado é inválido e repete a pergunta
            print("Valor inválido. Digite um número inteiro.")


# Função para perguntar pelo serviço adicional ao usuário
# Esta função não recebe nenhum argumento, mas retorna o custo adicional do tipo de encadernação escolhido.
def servico_extra():
    # Dicionário com os custos adicionais de cada tipo de encadernação
    # As chaves são os números das opções e os valores são os custos.
    custo_adicional = {1: 10.00, 2: 25.00, 0: 0.00}

    # Loop infinito para continuar perguntando até receber uma resposta válida
    while True:

        try:
            # Pergunta pelo serviço adicional ao usuário
            tipo_encadernacao = int(
                input("\nQual tipo de encadernação você quer? Simples (1) / Capa dura (2) / Nenhuma (0): "))

            # Verifica se o tipo de encadernação escolhido está no dicionário
            if tipo_encadernacao in custo_adicional:
                # Retorna o custo adicional do tipo de encadernação escolhido
                return custo_adicional[tipo_encadernacao]

            else:
                # Informa ao usuário que a opção escolhida é inválida e repete a pergunta
                print("Opção inválida. Digite novamente.")

        except ValueError:
            # Informa ao usuário que o valor digitado é inválido e repete a pergunta
            print("Valor inválido. Digite um número inteiro.")


# Exibe o menu de serviços e custos
exibir_menu()

# Pergunta o serviço desejado ao usuário e armazena o custo do serviço escolhido na variável 'servico'
servico = escolha_servico()

# Pergunta o número de páginas ao usuário e armazena o número de páginas com desconto aplicado na variável 'num_paginas'
num_paginas = num_pagina()

# Pergunta pelo serviço adicional ao usuário e armazena o custo adicional do tipo de encadernação escolhido na variável 'extra'
extra = servico_extra()

# Calcula o total a pagar multiplicando o custo do serviço pelo número de páginas e adicionando o custo adicional
total = servico * num_paginas + extra

# Imprime o total a pagar na saída do console
print("\nO valor total da sua conta é R$ {:.2f}".format(total))

