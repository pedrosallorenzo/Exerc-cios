cl = str(input('Digite a sua classe: ').lower())
nv = int(input('Dgite o seu nível: '))
ie = int(input('Digite 1 caso possua algum ítem especial e digite 2 caso não possua nenhum ítem especial: '))

if ie == 1:
    if nv >= 30 and cl == 'guerreiro':
        print('Seu título é de GUERREIRO MAIOR!')
    if nv >= 30 and cl == 'ladino':
        print('Seu título é de LADINO MAIOR!')
    if nv < 30 and cl == 'guerreiro':
        print('Seu título é de GUERREIRO MENOR!')
    if nv <30 and cl == 'ladino':
        print('Seu título é de LADINO MENOR!')
elif ie == 2:
    print('Jogador sem título')