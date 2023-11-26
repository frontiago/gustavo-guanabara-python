# Exercício 072 - Análise de dados em uma tupla
# https://www.youtube.com/watch?v=1u7oA8ckjAc&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=5&pp=iAQB

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares

numeros = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: '))
)

print(f'O número 9 aparece {numeros.count(9)} vez(es)')
print(f'O número 3 aparece no indíce {numeros.index(3)}')

print(f'Os números pares são')

for i in numeros:
    if i % 2 == 0:
        print(i, end=' ')
