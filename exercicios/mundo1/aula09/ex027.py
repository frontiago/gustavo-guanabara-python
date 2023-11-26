# Faça um programa que leia o nome completo de uma pessoa,
# mostrando o primeiro e último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Digite seu nome: ')).lower().strip()
nomes = nome.title().split()

print(f'Primeiro nome: {nomes[0]}')
print(f'Último nome: {nomes[len(nomes) - 1]}')