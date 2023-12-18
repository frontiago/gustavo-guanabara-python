# Exercício 099 - Função que calcula área
# https://www.youtube.com/watch?v=vp9UX7wr92o&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=100&pp=iAQB

# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def bigger(*num):
    contador = maior = 0
    print('')
    print('Analisando valores...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1

    print(f'Foram informados {contador} valores ao todo')
    print(f'O maior valor informado foi {maior}')


# Programa principal
bigger(2, 9, 7, 83, 8, 14)
bigger(7, 18, 9)
bigger(1, 2)
bigger()
