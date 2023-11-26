# Exercício 044 - Gerenciador de pagamentos
# https://www.youtube.com/watch?v=I-SH3QchuZ4&t=2s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNDMgcHl0aG9u

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
# à vista em dinheiro / cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco_produto = float(input('Qual o preço do produto? R$ '))
preco_final = ''
msg = ''

print('=' * 20)
print('ESCOLHA A FORMA DE PAGAMENTO')
print('=' * 20)

print('''
[ 1 ] - DINHEIRO OU CHEQUE
[ 2 ] - À VISTA NO CARTÃO
[ 3 ] - 2X NO CARTÃO
[ 4 ] - 3X OU MAIS NO CARTÃO
''')

forma_de_pagamento = int(input('Digite a forma de pagamento: '))

if forma_de_pagamento == 1:
    msg = 'Você pagou em dinheiro ou cheque'
    preco_final = preco_produto - (preco_produto * 0.10)
elif forma_de_pagamento == 2:
    msg = 'O pagamento foi feito à vista no cartão'
    preco_final = preco_produto - (preco_produto * 0.05)
elif forma_de_pagamento == 3:
    msg = 'Pagamento feito em 2x no cartão'
    preco_final = preco_produto
elif forma_de_pagamento == 4:
    msg = 'O pagamento foi feito em 3x ou mais no cartão'
    preco_final = preco_produto + (preco_produto * 0.2)

print('')
print('=' * 20)
print('RESULTADOS')
print('=' * 20)
print(f'{msg}')
print(f'Total pago: R$ {preco_final:.2f}')
