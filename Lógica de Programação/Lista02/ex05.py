while True:
    nome = str(input('Digite seu nome (maior que 3 caracteres): ')).capitalize()
    idade = int(input('Digite sua idade (0 - 150): '))
    salario = float(input('Digite seu salário (maior que R$0,00): '))
    sexo = str(input('Digite seu gênero (F ou M): ')).upper()
    estado_civil = str(input('Digite seu estado civil (solteiro, casado, viúvo, divorciado): ')).upper()

    sexo_01 = sexo.startswith('F') or sexo.startswith('M')

    estado_civil_01 = estado_civil.startswith('S') or estado_civil.startswith('C') or estado_civil.startswith('V') or estado_civil.startswith('D')

    while len(nome) < 3:
        print('Seu nome é menor que 3 caracteres. Escreva-o novamente!')
        nome = str(input('Digite seu nome (maior que 3 caracteres): ')).capitalize()
        continue
    while idade < 0 or idade > 150:
        print('Você digitou uma idade incompatível! Escreva-a novamente!')
        idade = int(input('Digite sua idade (0 - 150): '))
        continue
    while salario < 0:
        print('Você digitou um salário incompatível! Escreva-o novamente!')
        salario = float(input('Digite seu salário (maior que R$0,00): '))
        continue
    while sexo_01 == False:
        print('Você digitou um sexo incompatível! Escreva-o novamente!')
        sexo = str(input('Digite seu gênero (F ou M): ')).upper()
        continue
    while estado_civil_01 == False:
        print('Você digitou um estado civil incompatível! Escreva-o novamente!')
        estado_civil = str(input('Digite seu estado civil (solteiro, casado, viúvo, divorciado): ')).upper()
        continue
    
    sexo_02 = sexo.lower().capitalize()
    estado_civil_02 = estado_civil.lower().capitalize()

    print(f'Nome: {nome}\nIdade: {idade}\nSalário: R${salario:.02f}\nSexo: {sexo_02}\nEstado civil: {estado_civil_02}')
    break