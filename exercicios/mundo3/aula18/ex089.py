# Exercício 089 - Boletim com listas compostas
# https://www.youtube.com/watch?v=7xrCJnniqMw&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=21&pp=iAQB

# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um que permita que o usuário possa mostrar
# notas de cada aluno individualmente

lista = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2

    lista.append([nome, [nota1, nota2], media])
    resposta = str(input('Deseja continuar? '))

    if resposta in 'Nn':
        break

print('-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

for i, v in enumerate(lista):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')

while True:
    print('-' * 35)
    option = int(input('Mostrar notas de qual aluno? 999 interrompe: '))
    if option == 999:
        print('FINALIZANDO...')
        break
    if option <= len(lista) - 1:
        print(f'Notas de {lista[option][0]} são {lista[option][1]}')
print('<<< VOLTE SEMPRE >>>')