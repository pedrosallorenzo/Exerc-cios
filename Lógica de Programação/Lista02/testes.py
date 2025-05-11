# Pede a base e o expoente
base = int(input('Digite a base (inteiro positivo): '))
expoente = int(input('Digite o expoente (inteiro positivo): '))

# Garante que os números sejam positivos
if base < 0 or expoente < 0:
    print('Erro: os números devem ser positivos!')
else:
    resultado = 1  # Começa com 1, pois qualquer número elevado a 0 é 1
    contador = 0

    while contador < expoente:
        resultado *= base  # Multiplica o resultado pela base
        contador += 1      # Aumenta o contador

    # Mostra o resultado final
    print(f'{base} elevado a {expoente} é {resultado}')