# Exercício 051 - Progressão aritmética
# https://www.youtube.com/watch?v=-OnqSGh0u4g&t=453s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNTAgcHl0aG9u

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

numero = int(input('Digite um número para calcular o seu fatorial: '))
count = numero
fatorial = 1

while count > 0:
    print(f'{count}', end=' ')
    print(f'x' if count > 1 else ' = ', end=' ')
    fatorial *= count
    count -= 1
print(fatorial)