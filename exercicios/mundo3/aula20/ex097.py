# Exercício 097 - Função que calcula área
# https://www.youtube.com/watch?v=Q6basnSo7r0&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=98&pp=iAQB

# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
# como parâmetro e mostre uma mensagem com tamanho adaptável.

# Ex: escreva('Olá Mundo')
# Saída
# ---------
# Olá Mundo
# ---------

def escreva(msg):
    print('-' * len(msg))
    print(f'{msg}')
    print('-' * len(msg))


escreva('MEU NOME É THIAGO FERREIRA DA SILVA')