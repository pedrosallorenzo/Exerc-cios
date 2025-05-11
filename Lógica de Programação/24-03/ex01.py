# Faça um programa que peça a nota e a porcentagem de falta do estudante, se a nota for maior que 7, o estudante sera aprovado, caso contrario, se a nota for maior ou igual a 6 sua presença precisará ser pelo menos de 75% para aprovação, e o estudante estará reprovado nos outros campos.


nota = float(input('Digite sua nota: '))
faltas = float(input('Digite quantas faltas você tem: '))
tda = 200
tdf = 200 - faltas
if nota > 7:
  print('Você foi aprovado')
elif nota >= 6 and tdf >= 150:
  print('Você também foi aprovado!')
elif tdf < 150 or nota < 6:
  print('Você foi reprovado!')
else:
  print('Você não digitou algo válido. Tente novamente.')