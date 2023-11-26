# Exercício 060 - Cálculo do fatorial
# https://www.youtube.com/watch?v=9dlBZlkvvxY&t=547s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNjAgcHl0aG9u

# Faça um programa que leia um número qualquer e mostre o seu fatorial
# Ex: 5! = 5x4x3x2x1 = 120

numero = int(input('Digite um número: '))
fatorial = 1
count = 1

while count <= numero:
    fatorial *= count
    count += 1
    print(fatorial)