print('|' + '-' * 68 + '|')
print("|Bem-vindo ao Gerenciamento de Livros - Guilherme Abreu do Nascimento|")
print('|' + '-' * 68 + '|')

# Lista para armazenar os livros cadastrados
lista_livro = []

# Variável global para rastrear o próximo ID disponível
id_global = 0

# Função para cadastrar um livro
def cadastrar_livro(id):
    nome = input("Nome do livro: ")
    autor = input("Autor do livro: ")
    editora = input("Editora do livro: ")

    # Cria um dicionário representando um livro e o adiciona à lista de livros
    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }
    lista_livro.append(livro)

# Função para consultar livros
def consultar_livro():
    while True:
        print("Opções:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print('-' * 68)
            print("Livros Cadastrados:")
            for livro in lista_livro:
                print('-' * 68)
                print("ID:", livro["id"])
                print("Nome:", livro["nome"])
                print("Autor:", livro["autor"])
                print("Editora:", livro["editora"])
        elif opcao == "2":
            print('-' * 68)
            id_busca = int(input("Digite o ID do livro a ser consultado: "))
            for livro in lista_livro:
                if livro["id"] == id_busca:
                    print('-' * 68)
                    print("ID:", livro["id"])
                    print("Nome:", livro["nome"])
                    print("Autor:", livro["autor"])
                    print("Editora:", livro["editora"])
                    break
            else:
                print("Livro não encontrado.")
        elif opcao == "3":
            print('-' * 68)
            autor_busca = input("Digite o autor a ser pesquisado: ")
            for livro in lista_livro:
                if livro["autor"] == autor_busca:
                    print("ID:", livro["id"])
                    print("Nome:", livro["nome"])
                    print("Autor:", livro["autor"])
                    print("Editora:", livro["editora"])
        elif opcao == "4":
            break
        else:
            print("Opção inválida")

# Função para remover um livro
def remover_livro():
    print('-' * 68)
    id_remover = int(input("Digite o ID do livro a ser removido: "))
    for livro in lista_livro:
        if livro["id"] == id_remover:
            lista_livro.remove(livro)
            print("Livro removido com sucesso.")
            break
    else:
        print("Livro não encontrado.")

# Loop principal do programa
while True:
    print("\nOpções:")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")
    print('-' * 68)

    opcao_menu = input("Escolha uma opção: ")

    if opcao_menu == "1":
        id_global += 1  # Incrementa o ID global antes de cadastrar o livro
        cadastrar_livro(id_global)
    elif opcao_menu == "2":
        consultar_livro()
    elif opcao_menu == "3":
        remover_livro()
    elif opcao_menu == "4":
        break
    else:
        print("Opção inválida")
