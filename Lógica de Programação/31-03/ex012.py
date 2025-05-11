# Ex.12 - Faça um programa que, dados 3 strings, mostra essas strings em ordem alfabética.


s1 = str(input("Digite a primeira string: "))
s2 = str(input("Digite a segunda string: "))
s3 = str(input("Digite a terceira string: "))

so = sorted([s1, s2, s3])

print(f'As strings em ordem alfabética fica: {so[0]}, {so[1]}, {so[2]}')