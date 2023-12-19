# Exercício 100 - Função que calcula área
# https://www.youtube.com/watch?v=MEs-41JcuhM&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=101&pp=iAQB

# Faça um programa que tenha uma lista chamada números e duas funções chamada sorteia() e somapar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint
from time import sleep

numeros = []


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    for cont in range(0, 5):
        n = randint(1, 100)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia(numeros)
print('')
somapar(numeros)