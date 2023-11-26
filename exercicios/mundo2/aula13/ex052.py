# Exercício 052 - Números primos
# https://www.youtube.com/watch?v=Er5Hyd4LyVw&t=579s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNTIgcHl0aG9u

# Faça um programa que leia um número inteiro e diga
# se ele é ou não um número primo

numero = int(input('Digite um número: '))
multiplos = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'\033[34m', end=' ')
        multiplos += 1
    else:
        print(f'\033[31m', end=' ')
    print(c, end=' ')

if numero > 1:
    print(f'\n\033[m O número {numero} tem {multiplos} múltiplos')

if numero == 1:
    print('Não pode ser UM')
elif numero == 0:
    print('Zero não tem divisor nem primo')
elif numero < 0:
    print('O número é negativo')

if multiplos == 2:
    print('É PRIMO')
elif multiplos > 2:
    print('NÃO É PRIMO!')
