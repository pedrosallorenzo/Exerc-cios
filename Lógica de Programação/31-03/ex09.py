# Ex.09 - Faça um programa que peça 4 números reais e calcula: a. A média aritmética simples. b. A variância desses dados. c. O desvio padrão desses dados.


num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite outro número: '))
num4 = float(input('Digite outro número: '))

op = int(input('Escolha uma dessas operações para fazer:\n1 - Média Aritmética\n2 - Variância\n3 - Desvio Padrão\n'))

if op == 1:
    ma = (num1 + num2 + num3 + num4) / 4
    print(f'A média aritmética dos números {num1}, {num2}, {num3} e {num4} é igual a {ma:0.2f}.')
elif op == 2:
    va = sum((x - sum([num1, num2, num3, num4]) / 4) ** 2 for x in [num1, num2, num3, num4]) / 4 
    print(f'A variância dos números {num1}, {num2}, {num3} e {num4} é igual a {va:0.2f}.')
elif op == 3:
    va = sum((x - sum([num1, num2, num3, num4]) / 4) ** 2 for x in [num1, num2, num3, num4]) / 4 
    dp = va ** 0.5
    print(f'O desvio padrão dos números {num1}, {num2}, {num3} e {num4} é igual a {dp:0.2f}.')
else:
    print('Você não escolheu uma opção válida. Tente novamente.')