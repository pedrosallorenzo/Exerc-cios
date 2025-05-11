# Ex.06 - Generalize o problema anterior, perguntando a porcentagem de desconto e mostrando os mesmos dados acima.


prod = float(input('Digite o preço do produto: '))
desc = int(input('Digite a porcentagem (%) do desconto: '))

op = (desc * prod) / 100

nvalor = prod - op

print(f'O produto no valor de R${prod:0.2f}, com um desconto de {desc}%, ficará custando ao final R${nvalor:0.2f}. Economizando R${op:0.2f}!')