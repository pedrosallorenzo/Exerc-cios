# Ex.05 - Sua tarefa é criar um programa em Python que pede o preço original de um produto e dá 20% de desconto.


prod = float(input('Digite o valor original do produto: '))

op = prod * 0.2
desc = prod - op

print(f'O valor R${prod:0.2f}, com um disconto de 20% fica R${desc:0.2f}. Descontando um total de R${op:0.2f}')