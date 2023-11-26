# Exercício 068 - Jogo do par ou ímpar
# https://www.youtube.com/watch?v=4Ca6iRJo3M0&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNjggcHl0aG9u

# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo

from random import randint
resultado = 0
vitorias = 0
derrota = False

while not derrota:
    pc_numero = randint(1, 10)

    print('''
    Digite P ou I para escolher Par ou Ímpar
    ''')

    escolha = str(input('Sua escolha: ')).lower()
    player_numero = int(input('Digite um número entre 1 e 10: '))
    print('')

    if 1 <= player_numero <= 10:
        resultado = pc_numero + player_numero

        # Checar vitórias
        if resultado % 2 == 0 and escolha == 'p':
            print(f'VOCÊ GANHOU, DEU PAR!')
            print(f'Você escolheu {player_numero} e o pc {pc_numero} o resultado é {player_numero + pc_numero}')
            vitorias += 1
        if resultado % 2 != 0 and escolha == 'i':
            print(f'VOCÊ GANHOU, DEU ÍMPAR!')
            print(f'Você escolheu {player_numero} e o pc {pc_numero} o resultado é {player_numero + pc_numero}')
            vitorias += 1

        # Checar derrotas
        if resultado % 2 == 0 and escolha == 'i':
            print('VOCÊ PERDEU! DEU PAR')
            print(f'Você escolheu {player_numero} e o pc {pc_numero} o resultado é {player_numero + pc_numero}')
            derrota = True
        if resultado % 2 != 0 and escolha == 'p':
            print('VOCÊ PERDEU! DEU ÍMPAR')
            print(f'Você escolheu {player_numero} e o pc {pc_numero} o resultado é {player_numero + pc_numero}')
            derrota = True
    else:
        print('Digite um número válido entre 1 e 10: ')

print('')
print('JOGO ENCERRADO!')
print(f'Vitórias consecutivas: {vitorias}')





