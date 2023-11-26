# Exercício 069 - Análise de dados do grupo
# https://www.youtube.com/watch?v=4Ca6iRJo3M0&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNjggcHl0aG9u

# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar.
# No final mostre:
# a) Quantas pessoas tem mais de 18 anos
# b) Quantos homens foram cadastrados
# c) Quantas mulheres tem menos de 20 anos

pessoas = 0
homens = 0
mulheres = 0
resposta = ''

while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo dessa pessoa [M / F]: ')).strip().lower()
    pessoas += 1
    resposta = str(input('Deseja continuar? [S / N]: ')).lower()

    if resposta == 'n':
        break

    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres += 1
    if idade > 18:
        pessoas += 1

print('')
print(f'{pessoas} pessoas tem mais de 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{mulheres} mulheres tem menos de 20 anos')

