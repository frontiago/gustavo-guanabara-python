# Exercício 067 - Tabuada v3.0
# https://www.youtube.com/watch?v=X0a5aZg93Uc&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNjYgcHl0aG9u

# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo

while True:
    numero = int(input('Digite um número para ver sua tabuada: '))
    if numero < 0:
        break
    print('')
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
    print('')