# Exercício 101 - Funções para votação
# https://www.youtube.com/watch?v=czDcimdc3GU&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=36&pp=iAQB

# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import date


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Você tem {idade} anos, você NÃO vota'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Você tem {idade} anos, seu voto é OPCIONAL'
    else:
        return f'Você tem {idade} anos, o voto é OBRIGATÓRIO'


nascimento = int(input('Seu ano de nascimento: '))
print(voto(nascimento))