# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto

produto = float(input('Digite o preço do produto R$: '))
novo_preco = produto - (produto * 0.05)

print(f'O produto custava R$ {produto:.2f}')
print(f'Com desconto de 5% fica R$ {novo_preco:.2f}')
