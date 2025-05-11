a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))

if a and b and c > 0:
    media = (a + b + c) / 4
    print(f'A média dos valores {a}, {b} e {c} é {media}.')
else:
    print('Digite apenas números positivos!')