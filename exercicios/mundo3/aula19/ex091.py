# Exercício 091 - Jogo de dados
# https://www.youtube.com/watch?v=cwrqIztaAwk&pp=ygUMZ3VhbmFiYXJhIDkw

# Crie um programa onde quatro jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# Sabendo que o vencedor tirou o maior número do dado

from random import randint
from time import sleep
from operator import itemgetter

jogadas = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

ranking = []

print('Valores sorteados: ')

for k, v in jogadas.items():
    print(f'O {k} jogou {v}')
    sleep(1)

print()
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print('*** RANKING ***')
for i, v in enumerate(ranking):
    print(f'{i+1}ºlugar, o {v[0]} tirou {v[1]}')
    sleep(1)
