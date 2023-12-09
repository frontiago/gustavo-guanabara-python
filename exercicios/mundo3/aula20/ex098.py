# Exercício 098 - Função que calcula área
# https://www.youtube.com/watch?v=DCBlt_z2UOE&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=99&pp=iAQB

# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
# e realize a contagem.

# Seu programa tem que realizar três contagens através da função criada:
# A) de 1 até 10, de 1 em 1
# B) de 10 até 0, de 2 em 2
# C) Uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
        print()
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')


print()
# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print('Agora é a sua vez de personalizar')
initial = int(input('Início: '))
final = int(input('Fim: '))
step = int(input('Passo: '))
contador(initial, final, step)
