# Exercício 056 - Analisador completo
# https://www.youtube.com/watch?v=fokDF4th0IY&t=691s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNTYgcHl0aG9u

# https://youtu.be/fokDF4th0IY?si=rnV_t3QI3HnAqfbe
# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
# O final do programa, mostre:

# A média de idade do grupo
# Qual é o nome do mais velho
# Quantas mulheres tem menos de 20 anos

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulheres = 0

for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo: [M / F]: ')).strip().lower()
    soma_idade += idade

    if i == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome

    if sexo in 'Ff' and idade < 20:
        total_mulheres += 1

media_idade = soma_idade / 4

print(f'A média de idade é de {media_idade:.0f} anos')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho}')
print(f'O total de mulheres é de {total_mulheres}')