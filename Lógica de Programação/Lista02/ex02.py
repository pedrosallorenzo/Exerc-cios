i = 1
num = float(input('Digite um número: '))
print(i)
while num != 0:
    num = float(input('Digite um número: '))
    i += 1
    print(i)
    if num == 0:
        print('Você digitou o número proibído!')
        print(f'Você digitou {i - 1} números que foram aceitos.')
        break