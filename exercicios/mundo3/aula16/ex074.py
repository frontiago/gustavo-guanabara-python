# Exercício 074 - Maior e menor valores em tupla
# https://www.youtube.com/watch?v=mlwt2CRQkTQ&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=4&pp=iAQB

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from math import trunc
from random import randint

numeros = (randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000))

print(numeros)
