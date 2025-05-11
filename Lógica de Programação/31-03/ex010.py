# Ex.10 - Faça um programa que, dados 3 números inteiros, mostre na tela o maior deles.


num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite outro número: '))

maior = max(num1, num2, num3)

print(f'O maior número é o {maior}')