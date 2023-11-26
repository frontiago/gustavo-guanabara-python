# Escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado e a quantidade de dias pelos
# quais ele alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$ 60 por dia e R$ 0,15 por km rodado

distancia = float(input('O carro percorreu quantos km? '))
dias_alugado = int(input('O carro foi alugado por quantos dias? '))
custo = (60 * dias_alugado) + (distancia * 0.15)

print(f'O custo total do aluguel do carro é de R$ {custo:.2f}')
