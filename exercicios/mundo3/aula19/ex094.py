# Exercício 094 - Unindo dicionários e listas
# https://www.youtube.com/watch?v=ETnExBCFeps&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgOTMgcHl0aG9u

# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em uma dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média

galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERROR, por favor, digite apenas M ou F')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO, responda apenas S ou N')
    if resposta == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')

media = soma / len(galera)
print(f'B) A média de idade é de {media:.0f} anos')

print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ', end='')
print()

print('D) A lista de pessoas acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('<<< ENCERRADO >>>')