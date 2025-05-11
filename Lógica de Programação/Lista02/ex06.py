while True:
    num1 = int(input('Digite um número para ser a base da operação: '))
    num2 = int(input('Digite um número para ser o expoente da operação: '))

    op = num1 ** num2

    print(f'O resultado da sua operação é: {op}')

    sair = str(input('Quer sair? (sim ou não)')).upper()
    sair_01 = sair.startswith('S')
    if sair_01 == True:
        break
    else:
        continue