# Exercício 036 - Aprovando empréstimo
# https://www.youtube.com/watch?v=IV13X0QOMU8&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgMzYgcHl0aG9u

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado

casa = float(input('Digite o valor da casa: '))
salario = float(input('Qual o seu salário: '))
anos = int(input('Por quantos anos deseja financiar: '))

prestacao = casa / (anos * 12)
limite = salario * 0.3

print('')
if prestacao > limite:
    print(f'EMPRÉSTIMO NEGADO!')
    print(f'As prestações saíriam a R$ {prestacao:.2f}')
    print(f'O limite para ser aprovado com base no seu salário seria de R$ {limite:.2f}')
elif prestacao <= limite:
    print(f'EMPRÉSTIMO APROVADO!')
    print(f'As prestações serão de  R$ {prestacao:.2f}')
    print(f'Seu salário está dentro do limite de {limite:.2f}')
