# Exercício 058 - Jogo de adivinhação v2.0
# https://www.youtube.com/watch?v=-QkOIHJ1Chw&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNTggcHl0aG9u

# Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10.
# Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer

from random import randint

computer = randint(0, 10)
print('----- GUESS THE NUMBER OF THE COMPUTER -----')
player = int(input('Type a number between 1 and 10: '))

while player != computer:
    player = int(input('Type a number between 1 and 10: '))

print(f'CONGRATULATIONS! YOU WIN! THE COMPUTER SAID {computer}')