# Exercício 073 - Tuplas com time de futebol
# https://www.youtube.com/watch?v=RexybLcGewA&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=3&pp=iAQB

# Crie uma tupla preenchida com os primeiros 20 colocados da tabela do campeonato brasileiro de futebol,
# na ordem de colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética
# D) Em que posição da tabela está o time da chapecoense

times = (
    'Botafogo', 'Palmeiras', 'Bragantino', 'Grêmio', 'Flamengo',
    'Atlético-MG', 'Atlético-PR', 'Fluminense', 'Fortaleza', 'Cuiabá',
    'São Paulo', 'Internacional', 'Bahia', 'Cruzeiro', 'Corinthians',
    'Santos', 'Goiás', 'Vasco', 'Curitiba', 'América-MG'
)

# show all teams
def show_all():
    for i in range(0, len(times)):
        print(f'{i + 1}º - {times[i]}')

# the first five teams
def show_five():
    print(times[0:6])

# last four teams
def show_last_four():
    print(times[16:])

# show teams alphabetic
def show_sorted():
    print(sorted(times))

while True:
    print('''
    TABELA E ESTATÍSTICAS DO CAMPEONATO BRASILEIRO
    A - A tabela inteira do campeonato
    B - Apenas os 5 primeiros colocados
    C - Os últimos 4 colocados da tabela
    D - Uma lista com os times em ordem alfabética
    E - Em que posição da tabela está o time do Bahia
    F - SAIR
    ''')

    option = str(input('Opção: ')).lower()

    if option == 'a':
        show_all()
    elif option == 'b':
        show_five()
    elif option == 'c':
        show_last_four()
    elif option == 'd':
        show_sorted()
    elif option == 'e':
        posicao = times.index('Bahia')
        print(f'O Bahia está na {posicao}ª posição')
    elif option == 'f':
        break
    else:
        print('Digite uma opção válida')

print('PROGRAMA FINALIZADO!')