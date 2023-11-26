# Exercício 061 - Progressão aritmética v2.0
# https://www.youtube.com/watch?v=vu5ehetQGe8&t=344s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNjAgcHl0aG9u

# Refaça o desafio 051, lendo o primeiro termo e a razão de uma P.A
# mostrando os 10 primeiros termos da progressão usando a estrutura while

first = int(input('Digite o primeiro número da P.A: '))
razao = int(input('Digite a razão: '))
quantidade = int(input('Digite a quantidade de termos: '))
termo = first
count = 1

while count <= quantidade:
    print(f'{termo}', end=' ')
    termo += razao
    count += 1

