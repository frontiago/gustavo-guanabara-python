# Exercício 066 - Vários números com flag
# https://www.youtube.com/watch?v=d2ug6quC1bk&t=218s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNjYgcHl0aG9u

# Crie um programa que leia vários números inteiros pelo teclado
# O programa só vai parar quando o usuário digitar 999, que é a condição de parada
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# ( desconsiderando o flag )

numero = 0
quantidade = 0
soma = 0

while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
    quantidade += 1

print(f'Foram digitados {quantidade} números')
print(f'A soma vale {soma}')