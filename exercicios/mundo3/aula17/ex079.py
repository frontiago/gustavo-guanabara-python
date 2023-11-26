# Exercício 079 - Valores únicos em uma lista
# https://www.youtube.com/watch?v=LkAzRnc_GPk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=10&pp=iAQB

# Crie um programa aonde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
# Caso o numéro já exista lá dentro, ele não será adicionado
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    numero = int(input('Digite um número: '))

    if numero == 999:
        break

    if numero not in lista:
        lista.append(numero)

print(sorted(lista))