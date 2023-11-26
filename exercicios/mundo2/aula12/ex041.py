# Exercício 041 - Classificando atletas
# https://www.youtube.com/watch?v=ZiC5NgSGJXU&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNDEgcHl0aG9u

# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade
# até 9 anos: mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 20 anos: sênior
# acima: master

from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
categoria = ''

if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade == 20:
    categoria = 'Sênior'
else:
    categoria = 'Master'

print('')
print(f'Você tem {idade} anos, sua categoria é {categoria}')


