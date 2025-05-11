# Ex.11 - Faça um programa que, dados 3 números inteiros, mostre na tela esses números em ordem crescente.


num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite outro número: '))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
meio = num1 + num2 + num3 - maior - menor

print(f'A ordem crescente dos números escolhidos é: {menor}, {meio} e {maior}')