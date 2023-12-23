# Código 3 Verificação de Notas para Aprovação:
nota1 = float(input('digite a nota da 1 matéria: '))
nota2 = float(input('digite a nota da 2 matéria: '))
nota3 = float(input('digite a nota da 3 matéria: '))
minimo = 7
if nota1 >= minimo and nota2 >= minimo and nota3 >= minimo:
    print('passou')
else:
    print('reprovado')
