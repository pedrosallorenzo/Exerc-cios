id = int(input('Digite sua idade: '))
sx = str(input('Digite seu sexo: ').lower())
ac = int(input('Digite a quantidade de anos de contribuição: '))

if sx == 'homem' and id >= 66 or ac >= 36:
    print('Você pode aposentar!')
elif sx == 'mulher' and id >= 62 or ac >= 33:
    print('Você não pode aposentar!')
else:
    print('Erro, tente novamente!')