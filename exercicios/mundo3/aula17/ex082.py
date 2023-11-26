# Exercício 082 - Dividindo valores em várias listas
# https://www.youtube.com/watch?v=uk0gDFQEo_I&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=13&pp=iAQB

# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente.
# Ao final, mostre conteúdo das três listas geradas

lista = []
lista_pares = []
lista_impares = []

while True:
    numero = int(input('Digite um número: '))

    if numero == 999:
        break

    lista.append(numero)

    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'Números digitados {lista}')
print(f'Pares: {lista_pares}')
print(f'Ímpares: {lista_impares}')
