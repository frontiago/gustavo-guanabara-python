# Exercício 103 - Ficha do jogador
# https://www.youtube.com/watch?v=FbOvilKfHMI&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=38&pp=iAQB

# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não teha sido informado corretamente.


def ficha(jogador='Desconhecido', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


# Programa principal
nome_jogador = str(input("Nome do jogador: "))
gols_jogador = str(input("Número de gols: "))

if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0

if nome_jogador.strip() == '':
    ficha(gols=gols_jogador)
else:
    ficha(nome_jogador, gols_jogador)