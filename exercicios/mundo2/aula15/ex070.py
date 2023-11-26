# Exercício 070 - Estatísticas em produtos
# https://www.youtube.com/watch?v=hS8QdW-1HTo&t=810s&pp=ygUkZ3VzdGF2byBndWFuYWJhcmEgZXhlcmljaW8gNzAgcHl0aG9u

# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# a) Qual o total gasto na compra
# b) Quantos produtos custam mais de R$ 1000
# c) Qual é o nome do produto mais barato

total = total_produto_1000 = menor = contador = 0
produto_barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço R$: '))
    contador += 1
    total += preco

    resposta = str(input('Quer continuar? [S / N]: ')).strip().upper()[0]

    if contador == 1:
        menor = preco
        produto_barato = produto
    else:
        if preco < menor:
            menor = preco
            produto_barato = produto

    if resposta == 'N':
        break
    if preco > 1000:
        total_produto_1000 += 1

print('-' * 20)
print('--- FIM DO PROGRAMA ---')
print(f'O total gasto foi R$: {total:.2f}')

if total_produto_1000 >= 2:
    print(f'Há {total_produto_1000} produtos acima de R$ 1.000,00')
elif total_produto_1000 == 1:
    print(f'Há apenas {total_produto_1000} produto acima de R$ 1.000,00')
else:
    print('NÃO há nenhum produto acima de R$ 1.000,00')

print(f'O produto mais barato é {produto_barato} que custa R$ {menor:.2f}')