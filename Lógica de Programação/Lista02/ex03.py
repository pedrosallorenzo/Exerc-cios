i = 0

while i >= 0:
    nota = float(input('Digite sua nota (entre 0 e 10): '))
    if nota >= 0 and nota <= 10:
        print(f'Sua nota, {nota}, é válida.')
        break

    if nota < 0 or nota > 10:
        print('Nota inválida!')
        continue