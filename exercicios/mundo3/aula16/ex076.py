# Exercício 076 - Lista de preços com tupla
# https://www.youtube.com/watch?v=Qp2cXfCHk2I&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=6&pp=iAQB

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular

produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90
)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30} ', end='')
    else:
        print(f'R$ {produtos[pos]:.2f}')