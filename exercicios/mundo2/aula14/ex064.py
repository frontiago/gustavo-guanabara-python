# Exercício 064 - Tratando vários valores v1.0
# https://www.youtube.com/watch?v=mYlbttiLHM0&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNjQgcHl0aG9u

# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag)

valor = 0
soma = 0
qtd_numeros = 0

while valor != 999:
    valor = int(input('Digite um valor: '))
    if valor != 999:
        soma += valor
        qtd_numeros += 1

print(f'Foram gerados {qtd_numeros} números')
print(f'A soma entre eles é: {soma}')

