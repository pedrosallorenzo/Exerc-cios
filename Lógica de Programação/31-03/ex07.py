# Ex.07 - Faça um programa que peça 3 valores e calcula sua média aritmética simples, mostrando esse resultado na tela.


num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite outro número: '))

ma = (num1 + num2 + num3) / 3

print(f'A média aritmética dos números {num1}, {num2} e {num3} é igual a {ma:0.2f}')