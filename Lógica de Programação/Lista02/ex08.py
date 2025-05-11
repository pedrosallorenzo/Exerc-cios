num = int(input('Digite um número: '))

if num <= 0:
    print('Por favor, digite um número inteiro positivo!')
else:

    a = 0
    b = 1
    contador = 0

    while contador < num:
        print(a, end=' ')
        proximo = a + b
        a = b
        b = proximo
        contador += 1