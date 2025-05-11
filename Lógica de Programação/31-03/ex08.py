# Ex.08 - Faça um programa que peça 4 valores positivos e calcula: a. A média aritmética simples. b. A média geométrica. c. A média harmônica


num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite outro número: '))
num4 = float(input('Digite outro número: '))

op = int(input('Escolha uma dessas operações para fazer:\n1 - Média Aritmética\n2 - Média Geométrica\n3 - Média Harmônica\n'))

if op == 1:
    ma = (num1 + num2 + num3 + num4) / 4
    print(f'A média aritmética dos números {num1}, {num2}, {num3} e {num4} é igual a {ma:0.2f}.')    
elif op == 2:
    mg = (num1 * num2 * num3 * num4) ** (1/4)
    print(f'A média geométrica dos números {num1}, {num2}, {num3} e {num4} é igual a {mg:0.2f}.')
elif op == 3:
    mh = 4 / (1/num1 + 1/num2 + 1/num3 + 1/num4)
    print(f'A média harmônica dos números {num1}, {num2}, {num3} e {num4} é igual a {mh:0.2f}.')
else:
    print('Você não escolheu uma opção válida. Tente novamente.')