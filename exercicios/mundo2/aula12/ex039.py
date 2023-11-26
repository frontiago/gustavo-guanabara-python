# Exercício 039 - Alistamento militar
# https://www.youtube.com/watch?v=ePwP4gU_waY&t=571s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgMzggcHl0aG9u

# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar no serviço militar
# Se é hora de se alistar
# Se já passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

ano_nascimento = int(input('Qual seu ano de nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade == 18:
    print(f'CHEGOU A HORA! Você tem {idade} anos, vamos para alistamento')
elif idade > 18:
    print(f'JÁ ERA! Você se alistou há {idade - 18} anos atrás')
elif idade < 18:
    print(f'CALMA! Ainda falta {18 - idade} ano(s) para o alistamento')