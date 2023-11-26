# Exercício 086 - Matriz em Python
# https://www.youtube.com/watch?v=2-fy24bbMJ4&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=17&pp=iAQB

# Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tela, com a formatação correta

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número [{linha}][{coluna}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

