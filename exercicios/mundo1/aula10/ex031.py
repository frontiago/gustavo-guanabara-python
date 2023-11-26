# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km
# e R$ 0,45 para viagens mais longas

distancia = int(input('Qual a distância que irá viajar? '))

if distancia <= 200:
    passagem = float(distancia * 0.50)
else:
    passagem = float(distancia * 0.45)

print(f'Para uma viagem de {distancia}km você irá pagar R$ {passagem:.2f}')