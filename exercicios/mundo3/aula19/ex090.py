# Exercício 090 - Dicionário em python
# https://www.youtube.com/watch?v=HipQYUk4koA&pp=ygUMZ3VhbmFiYXJhIDkw

# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário
# No final, mostre o conteúdo da estrutura na tela

turma = []
aluno = {}

for i in range(0, 3):
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input('Média: '))
    aluno['situacao'] = str(input('Situação: '))
    turma.append(aluno.copy())
    print()

for result in turma:
    for key, value in result.items():
        print(value)
    print()

