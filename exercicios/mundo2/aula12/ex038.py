# Exercício 038 - Comparando números
# https://www.youtube.com/watch?v=iuPbB9uHczM&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgMzggcHl0aG9u

# Escreva um programa que leia dois números inteiros e compare-os
# mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

primeiro = float(input('Digite um número: '))
segundo = float(input('Digite outro número: '))

if primeiro > segundo:
    print('O primeiro é maior')
elif segundo > primeiro:
    print('O segundo é maior')
elif primeiro == segundo:
    print('Não existe valor maior, os dois são iguais')
else:
    print('Digite um número válido')