nome = str(input('Digite seu nome: ')) 
peso = float(input('Digite seu peso: '))
altu = float(input('Digite sua altura (em metros): '))

imc = peso / altu ** 2

if imc >= 40.0:
    print(f'{nome} eu IMC é {imc:0.2f}, você está com obesidade grave! Procure um médico urgente!')
elif imc >= 30 and imc <= 39.9:
    print(f'{nome} seu IMC é {imc:0.2f}, você está com obesidade! Procure um médico!')
elif imc >= 25.0 and imc <= 29.9:
    print(f'{nome} seu IMC é {imc:0.2f}, você está com sobrepeso!')
elif imc >= 18.5 and imc <= 24.9:
    print(f'{nome} seu IMC é {imc:0.2f}, você está normal!')
elif imc < 18.5:
    print(f'{nome} seu IMC é {imc:0.2f}, você está com magreza! Coma muito!')
else:
    print('Erro, tente novamente!')