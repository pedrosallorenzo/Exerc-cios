# Quando mudamos o tipo da variável, chamamos de cast/casting


horario = str(input('Digite um horário do dia:'))
if horario == 'Manhã':
  print('Bom dia!')
elif horario == 'Tarde':
  print('Boa tarde!')
elif horario == 'Noite':
  print('Boa noite!')
else:
  print('Você não digitou algo válido. Tente novamente.')