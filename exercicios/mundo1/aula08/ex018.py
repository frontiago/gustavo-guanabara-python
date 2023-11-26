# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo

import math

angulo = int(input('Digite o valor do ângulo: '))
radiano = math.radians(angulo)

seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')
print(f'Tangente: {tangente:.2f}')
