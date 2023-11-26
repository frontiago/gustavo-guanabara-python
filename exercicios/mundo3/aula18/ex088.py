# Exercício 088 - Palpites para a mega sena
# https://www.youtube.com/watch?v=Hd7Ycaj61xE&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=20&pp=iAQB

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = []
jogos = []
quantidade = int(input('Número de jogos: '))
total = 1

while total <= quantidade:
    contador = 0
    while True:
        num = randint(1, 60)

        if num not in lista:
            lista.append(num)
            contador += 1

        if contador >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for indice, lista in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista}')
    sleep(1)