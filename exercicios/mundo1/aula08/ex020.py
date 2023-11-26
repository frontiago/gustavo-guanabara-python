# O mesmo professor do desafio anterior quer sortear a ordem da apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada

import random

aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print(f'A ordem das apresentações será: {lista}')
