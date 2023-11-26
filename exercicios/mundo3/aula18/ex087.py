# Exercício 087 - Mais sobre matriz em python
# https://www.youtube.com/watch?v=QhS829x6up4&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=19&pp=iAQB

# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_total = soma_terceira_coluna = maior_segunda = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número: [{linha}][{coluna}]: '))
        soma_total += matriz[linha][coluna]

        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]

        if linha == 1:
            if matriz[1][coluna] > maior_segunda:
                maior_segunda = matriz[1][coluna]

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print()
print(f'A soma total é: {soma_total}')
print(f'A soma da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda}')