num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

maior = max(num1, num2)
menor = min(num1, num2)

if maior == menor:
    print('Os números digitados são iguais!')
elif maior == num1:
    print('O primeiro número digitado é o maior!')
elif maior == num2:
    print('O segundo número é maior que o primeiro!')
else:
    print('Erro. Tente novamente!')