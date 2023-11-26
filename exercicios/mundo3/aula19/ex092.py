# Exercício 092 - Cadastro de trabalhador
# https://www.youtube.com/watch?v=Vsqemzdrj78&t=621s&pp=ygUMZ3VhbmFiYXJhIDky

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
# dicionário se por acaso a CPTS for diferente de zero, o dicionário receberá também o ano de contratação
# e salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime

dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Nº Carteira de trabalho (0 não tem) '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print()

for k, v in dados.items():
    print(f'{v}')