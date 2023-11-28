# Exercício 093 - Cadastro de jogador de futebol
# https://www.youtube.com/watch?v=5yKiud-YNaE&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgOTMgcHl0aG9u

# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
# isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))

for c in range(total):
    partidas.append(int(input(f'Quantos gols na partida {c + 1}: ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print()

print(jogador)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print()

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')