# Exercício 057 - Validação de dados
# https://www.youtube.com/watch?v=JGztEBLGj5E&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNTYgcHl0aG9u

# Faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''

while sexo in 'Mm' or sexo in 'Ff':
    sexo = str(input('Digite o sexo [M / F]: '))
print('Acabou')