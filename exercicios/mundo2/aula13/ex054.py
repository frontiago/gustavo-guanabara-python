# Exercício 054 - Grupo da maioridade
# https://www.youtube.com/watch?v=IL5iBWoKRIs&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNTQgcHl0aG9u

# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores

menor_idade = 0
maior_idade = 0

for i in range(1, 8):
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

if maior_idade == 0:
    print(f'Nenhuma pessoa atingiu a maior idade')
else:
    print(f'{maior_idade} pessoas atingiram a maior idade')

if menor_idade == 0:
    print(f'Nenhuma pessoa é menor de idade')
else:
    print(f'{menor_idade} pessoas são menor de idade')
