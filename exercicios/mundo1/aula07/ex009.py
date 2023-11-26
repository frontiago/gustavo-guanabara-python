# Faça um programa que leia um número inteiro qualquer
# e mostra na tela a sua tabuada

num = int(input('Digite um número para ver sua tabuada: '))

for x in range(1, 11):
    print(f'{num} x {x} = {num * x}')

