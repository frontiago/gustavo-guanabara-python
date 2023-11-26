# Crie um programa que leia quanto dinheiro a pessoa tem na carteira
# e mostre quantos dólares ela pode comprar
# Considere U$D 1.00 = R$ 4.94 (valor do dólar em 25/09/2023)

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.94

print(f'Com R$ {real} você consegue comprar USD {dolar:.2f}')

