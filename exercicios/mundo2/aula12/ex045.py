# Exercício 045 - Classificando atletas
# https://www.youtube.com/watch?v=ZiC5NgSGJXU&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNDEgcHl0aG9u

# Crie um programa que faça o computador jogar jokenpô com você

from random import randint
jogada_pc = int(randint(1,3))

print('=' * 20)
print('JOKENPO - ESCOLHA SUA JOGADA')
print('=' * 20)

print('''
[ 1 ] - PEDRA
[ 2 ] - PAPEL
[ 3 ] - TESOURA 
''')

jogada_player = int(input('Sua jogada: '))

if jogada_player == jogada_pc:
    print(f'DEU EMPATE')
elif jogada_player == 1 and jogada_pc == 2:
    print('PERDEU! você jogou pedra e o pc jogou papel')
elif jogada_player == 1 and jogada_pc == 3:
    print('GANHOU! você jogou pedra e o pc jogou tesoura')
elif jogada_player == 2 and jogada_pc == 1:
    print('GANHOU! você jogou papel e o pc jogou pedra')
elif jogada_player == 2 and jogada_pc == 3:
    print('PERDEU! você jogou papel e o pc jogou tesoura')
elif jogada_player == 3 and jogada_pc == 1:
    print('PERDEU! você jogou tesoura e o pc jogou pedra')
elif jogada_player == 3 and jogada_pc == 2:
    print('GANHOU! você jogou tesoura e o pc jogou papel')
