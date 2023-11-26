# Exercício 049 - Tabuada v.2.0
# https://www.youtube.com/watch?v=QtElJDa9ICM&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNDggcHl0aG9u

# Refaça o desafio 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando laço for

numero = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')