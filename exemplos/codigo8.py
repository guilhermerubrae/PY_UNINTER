# Código 8 Classificação de Triângulos:
A = int(input('Digite o 1 lado: '))
B = int(input('Digite o 2 lado: '))
C = int(input('Digite o 3 lado: '))

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
