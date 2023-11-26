# Crie um programa que leia o nome de uma cidade e
# diga se ela começa ou não com o nome 'SANTO'

cidade = input('Digite uma cidade: ').strip().lower()
print(f'{cidade[:5] == "santo"}')