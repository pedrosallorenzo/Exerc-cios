"""
Estrutura de repetição

for
while
* Não se utiliza for e while juntos
* O for é usado quando se sabe o número de repetições, enquanto o while é usado quando não se sabe
* O while TEM QUE ocorrer um erro, se não, ocorrerá um LOOP INFINITO!
"""

n = -1
while n < 0 or n > 10:
    n = int(input('Digite um inteiro entre 0 e 10: '))

print(f'O número digitado foi: {n}')