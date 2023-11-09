#5

# def realce(text):
# foi criado um pamtr recebe texto e após esse texto recebi uma propriedade len que irá ajustar o tam
#     tam = len(text)
#     #só printa se tiver algum caracter
#     if tam:
#         print('+', '-' * tam, '+')
##irá multiplicar dependendo do tamanho do texto inserido
#         print('|', text, '|')
#         print('+', '-' * tam, '+')
# realce('Game of Thrones')
# realce('Game of Thrones Game of Thrones Game of Thrones Game of Thrones Game of Thrones Game of Thrones')

#E L
# def comida():
#     carne = 12
#     print(carne)
#
# carne = 12
# comida()
#--------
# def comida():
#     ovos = 'ceviche'
#     batata()
#     print(ovos)
#
# def batata():
#     salmão = 23
#     print(salmão)
#
# comida()
# batata()

#E G
# def comida():
#     global ovos
#     ovos = 'comida'
#
# ovos = 'global'
# comida()
# print(ovos)

# def val_text(pergunta, min, max):
#     variavel = input(pergunta)
#     tam = len(variavel)
#     print(variavel)
#     while ((tam < min) or (tam > max)):
#         variavel = input(pergunta)
#         tam = len(variavel)
#         return variavel
# x = val_text('Digite uma str: ', 10, 20)
# print('Você digitou a string: {}. \n Dado válido. Encerrando...'.format(x))

#func com parametro de outra func
# def imprimeComCondição(num, fcond):
#     if fcond(num):
#         print(num)
# def par(x):
#     return x % 2 == 0
# def impar(x):
#     return not par(x)
#
# imprimeComCondição(5, par)
#5 não é par ent não vai imprimir se for par ele aparece na saida

# F LAMBDA
# res = lambda x, y: x * y
# print(res(55, 55))
#
# soma = lambda x, y: x + y
# print(soma(55, 55))

# AULA PRATICA 5
# def soma(x=0, y=0, z=0):
#     """
#     Retorna a soma de x + y + z
#     :param x:
#     :param y:
#     :param z:
#     :return: soma inteira
#     """
#     return x+y+z
#
# print(soma(3,2))
# #help(soma)

# def valida_int(pergunta, min, max):
#     x = int(input(pergunta))
#     while ((x < min) or (x > max)):
#          x = int(input(pergunta))
#     return x
#
#
# def fatorial(num):
#     """
#     Calcula a fatorial
#     :param num:
#     :return:
#     """
#     fat = 1
#     if num == 0:
#         return fat
#     for i in range(1, num+1, 1):
#         fat *= i
#     return fat
# #num+1 retorna a função no valor exato pois o for começa em zero
# x = valida_int('Digite um valor para calcular a fatorial: ', 0, 99999)
# print('{}! = {}'.format(x,fatorial(x)))
# help(fatorial)

#2
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
         x = int(input(pergunta))
    return x

def existeArquivos(nomeArquiuvo):
    try:
        a = open(nomeArquiuvo, 'rt')
        a.close()
    except FileNotFoundError:
          return False
    else:
          return True

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Error')
    else:
          print('Arquivo {} criado.\n'.format(nomeArquivo))

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
       a = open(nomeArquivo, 'at')
    except:
        print('Error')
    else:
        a.write('{} ; {}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Error')
    else:
        print(a.read())
    finally:
        a.close()


#main
arquivo = 'games.txt'
if not existeArquivos(arquivo):
    print('Existe')
else:
    print('Inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - CADASTRAR NOVO ITEM')
    print('2 - LISTAR CADASTROS')
    print('3 - SAIR')

    op = valida_int('ESCOLHA A OPÇÃO DESEJADA: ', 1, 3)
    if op == 1:
        print('Opção cadastrar selecionada\n')
        nomeJogo = input('NomeJogo:')
        nomeVideogame = input('NomeVideogame:')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Opção listar selecionada\n')
        listarArquivo(arquivo)
    elif op == 2:
        print('Encerrando programa...')
        break