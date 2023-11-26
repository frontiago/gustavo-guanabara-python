# Exercício 084 - Lista composta e análise de dados
# https://www.youtube.com/watch?v=zPtvuLiEdKk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=16&pp=iAQB

# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

temporaria = []
principal = []
maior = menor = 0

while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))

    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]

    principal.append(temporaria[:])
    temporaria.clear()

    resposta = str(input('Quer continuar? [S / N]: '))

    if resposta in 'Nn':
        break

print(f'Foram cadastras {len(principal)} pessoas')

print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end='')

print()

print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}', end='')