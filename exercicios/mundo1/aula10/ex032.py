# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

ano = 2020

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} NÃO é bissexto')
