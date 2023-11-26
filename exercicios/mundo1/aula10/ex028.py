# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador
# o programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

pc = int(randint(1, 5))
usuario = int(input('Digite um número entre 1 a 5: '))

if pc == usuario:
    print(f'PARABÉNS! Você acertou, o PC disse {pc}')
else:
    print(f'ERROU! TENTE NOVAMENTE')