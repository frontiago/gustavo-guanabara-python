# Exercício 081 - Extraindo dados de uma lista
# https://www.youtube.com/watch?v=SXJKAVVlvGA&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=12&pp=iAQB

# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista

lista = []
total_numeros = 0

while True:
    numero = int(input('Digite um número: '))

    if numero == 999:
        break

    lista.append(numero)
    total_numeros += 1

print(f'Foram digitados {total_numeros} números')
print(sorted(lista, reverse=True))

if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('NÃO há o valor 5 na lista')

