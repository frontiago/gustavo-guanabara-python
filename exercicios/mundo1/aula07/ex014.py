# Escreva um programa que converta uma temperatura
# digitada em Cº e converta para Fº

celsius = float(input('Quantos graus em Celsius deseja converter? '))
fahrenheit = celsius * (9/5) + 32

print(f'{celsius:.1f} Cº são {fahrenheit:.1f} Fº')
