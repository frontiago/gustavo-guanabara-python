# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input('Digite um nome: ')
nomeSeparado = nome.split()
nomeJunto = ''.join(nomeSeparado)

print(f'Nome maiúsculo: {nome.upper()}')
print(f'Nome minúsculo: {nome.lower()}')
print(f'Quantidade de letras: {len(nomeJunto)}')
print(f'Letras primeiro nome: {nomeSeparado[0]}')

