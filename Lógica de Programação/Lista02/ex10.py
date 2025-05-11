num = int(input('Digite um número: '))

if num <= 1:
    print(f'{num} não é um número primo.')
else:
    divisor = 2
    e_primo = True
    
    while divisor < num:
        if num % divisor == 0:
            e_primo = False
            break
        divisor += 1
    if e_primo:
        print(f'{num} é um número primo!')
    else:
        print(f'{num} não é um número primo.')