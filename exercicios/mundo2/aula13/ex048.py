# Exercício 048 - Soma ímpares múltiplos de três
# https://www.youtube.com/watch?v=iHjsUxNA-wo&t=477s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNDggcHl0aG9u

# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500

soma = 0

for i in range(1, 16):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
print(f'A soma é: {soma}')