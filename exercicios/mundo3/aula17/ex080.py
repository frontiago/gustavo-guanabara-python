# Exercício 080 - Lista ordenada sem repetição
# https://www.youtube.com/watch?v=QDpwjBYRcVE&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=11&pp=iAQB

# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort())
# No final, mostre a lista ordenada na tela

lista = []

# Read the numbers and add to the list
for i in range(1, 6):
    numero = int(input(f'Digite o {i}º número: '))
    lista.append(numero)

# Read the list and print the numbers unordered and their positions
for p, v in enumerate(lista):
    print(f'O número {v} foi adicionado na posição {p}')

# Print the list ordered
print(sorted(lista))
