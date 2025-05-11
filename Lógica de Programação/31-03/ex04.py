# Ex.04 - Faça um programa que pede o dia e mês de aniversário e diz quantos dias faltam para o aniversário, quantos dias se passaram do aniversário ou se hoje é o aniversário do usuário. (obs.: não utilize bibliotecas)


def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def dias_no_mes(mes, ano):
    if mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if eh_bissexto(ano) else 28
    else:
        return 31

def dias_desde_inicio_ano(dia, mes, ano):
    dias = 0
    for m in range(1, mes):
        dias += dias_no_mes(m, ano)
    dias += dia
    return dias

def calcular_diferenca(dia_aniv, mes_aniv, dia_atual, mes_atual):
    ano_atual = 2025
    dias_ano = 366 if eh_bissexto(ano_atual) else 365

    dias_aniversario = dias_desde_inicio_ano(dia_aniv, mes_aniv, ano_atual)
    dias_hoje = dias_desde_inicio_ano(dia_atual, mes_atual, ano_atual)

    if dias_aniversario == dias_hoje:
        return "Parabéns, hoje é o seu aniversário!!"
    elif dias_aniversario > dias_hoje:
        return f"Faltam {dias_aniversario - dias_hoje} dias para o seu aniversário."
    else:
        return f"Já se passaram {dias_hoje - dias_aniversario} dias desde o seu aniversário."

dia_aniv = int(input('Digite o dia do seu aniversário: '))
mes_aniv = int(input('Digite o mes do seu aniversário: '))
dia_atual = int(input('Digite o dia de hoje: '))
mes_atual = int(input('Digite o mês atual: '))

resultado = calcular_diferenca(dia_aniv, mes_aniv, dia_atual, mes_atual)
print(resultado)