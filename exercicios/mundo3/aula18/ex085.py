# Exercício 085 - Lista com pares e ímpares
# https://www.youtube.com/watch?v=2-fy24bbMJ4&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=17&pp=iAQB

# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

numero = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)

numero[0].sort()
numero[1].sort()

print(f'Os pares {numero[0]}')
print(f'Os ímpares {numero[1]}')

