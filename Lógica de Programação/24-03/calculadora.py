num1 = float(input("Digite um número"))

print("Escolha a operação desejada:")
print("Adição        --> 1")
print("Subtração     --> 2")
print("Multiplicação --> 3")
print("Divisão       --> 4")
print("Potenciação   --> 5")

op = int(input("Operação (Número): "))

if op == 5:
  num2 = int(input("Digite o número para fazer a potenciação: "))
  res = num1 ** num2
  print("O resultado da sua operação é: {}" .format(res))
elif op == 1:
  num2 = float(input("Digite um número para somar com o anterior: "))
  res = num1 + num2
  print("O resultado da sua operação é: {}" .format(res))
elif op == 2:
  num2 = float(input("Digite um número para subtrair com o outro: "))
  res = num1 - num2
  print("O resultado da sua operação é: {}" .format(res))
elif op == 3:
  num2 = float(input("Digite um número para multiplicar com o outro: "))
  res = num1 * num2
  print("O resultado da sua operação é: {}" .format(res))
elif op == 4:
  num2 = float(input("Digite um número para dividir o anterior: "))
  res = num1 / num2
  print("O resultado da sua operação é: {}" .format(res))
else:
  print("Você não digitou um número válido ou não digitou um número. Tente novamente.")