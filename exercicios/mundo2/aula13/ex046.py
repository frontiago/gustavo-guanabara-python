# Exercício 046 - Contagem regressiva
# https://www.youtube.com/watch?v=NR1RKt6NT8s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNDYgcHl0aG9u

# Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artíficio, indo de 10 até 0, com
# uma pausa de 1 segundo entre eles.

from time import sleep

for x in range(10, 0, -1):
    print(x)
    sleep(1)
print('FIM')