# Solicita o valor total do orçamento (deve ser no mínimo 100 reais)
while True:
    orçamento = float(input('Digite o valor total do orçamento (mínimo R$100,00): R$'))
    if orçamento >= 100:
        break
    else:
        print('Valor inválido. O orçamento deve ser de no mínimo R$100,00.')

serviços = []
valor_gasto = 0

while True:
    serviço = float(input('Digite o valor do serviço: R$'))

    if valor_gasto + serviço > orçamento:
        print('Este serviço ultrapassa o orçamento! Nenhum outro serviço poderá ser pedido.')
        break
    else:
        serviços.append(serviço)
        valor_gasto += serviço

    if valor_gasto == orçamento:
        print('Orçamento totalmente utilizado!')
        break

print('\nServiços que serão executados:')
for i, valor in enumerate(serviços, start=1):
    print(f'Serviço {i}: R${valor:.2f}')

print(f'\nTotal utilizado: R${valor_gasto:.2f}')
print(f'Total disponível do orçamento: R${orçamento - valor_gasto:.2f}')