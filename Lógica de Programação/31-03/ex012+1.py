#Ex.12+1 - Faça um programa que peça a informação se o usuário é homem ou mulher, o peso, a altura e a idade e mostre na tela o TMB em calorias. A Taxa Metabólica Basal (TMB) é a quantidade mínima de energia que o corpo precisa para manter as funções vitais, como respiração, circulação e temperatura corporal, em repouso. A TMB representa cerca de 60% a 70% do gasto energético total diário de uma pessoa e varia de acordo com o sexo, a idade, o peso e a altura. Para homens: TMB = 66,47 + (13,75 x peso em kg) + (5,003 x altura em cm) - (6,755 x idade em anos) Para mulheres: TMB = 655,09 + (9,563 x peso em kg) + (1,85 x altura em cm) - (4,676 x idade em anos)


gen = int(input('Escolha seu gênero\n1 - Homem\n2 - Mulher\n'))
peso = float(input('Digite o seu peso (em quilogramas): '))
alt = float(input('Digite a sua altura (em centímetros): '))
idade = int(input('Digite a sua idade: '))

if gen == 1:
    htmb = 66.47 + (13.75 * peso) + (5.003 * alt) - (6.755 * idade)
    print(f'A sua taxa metabólica basal (TMB) é igual a: {htmb:0.2f}. Ou seja, você gasta em média, sem fazer nenhum exercício extra, {htmb:0.2f}cal/dia')
elif gen == 2:
    mtmb = 665.09 + (9.563 * peso) + (1.85 * alt) - (4.676 * idade)        
    print(f'A sua taxa metabólica basal (TMB) é igual a: {mtmb:0.2f}. Ou seja, você gasta em média, sem fazer nenhum exercício extra, {mtmb:0.2f}cal/dia')