num = float(input('Digite um número: '))

op = num % 2

if op == 0:
    print('O número digitado é par!')
elif op == 1:
    print('O número digitado é ímpar!')
else:
    print('Erro, tente novamente!')