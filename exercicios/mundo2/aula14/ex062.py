# Exercício 062 - Super progressão aritmética v3.0
# https://www.youtube.com/watch?v=BWAWq7n6PCk&t=445s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNjIgcHl0aG9u

# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos
# O programa encerra quando ele disser que quer mostrar 0 termos

first = int(input('Digite o primeiro número da P.A: '))
razao = int(input('Digite a razão: '))
quantidade = int(input('Digite a quantidade de termos: '))
termo = first
count = 1

while count <= quantidade:
    print(f'{termo}', end=' ')
    termo += razao
    count += 1