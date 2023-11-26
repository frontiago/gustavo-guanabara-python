# Exercício 078 - Maior e menor valor da lista
# https://www.youtube.com/watch?v=q8Z1cRdJnfk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=9&pp=iAQB

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista

lista = []
menor = maior = posicaoMaior = posicaoMenor = 0

for i in range(1, 6):
    valor = int(input(f'Digite o {i}º valor: '))
    lista.append(valor)

for p, v in enumerate(lista):
    # print(f'O valor {v} está na posição {p} ')
    if p == 0:
        menor = v
        maior = v
    else:
        if v < menor:
            menor = v
            posicaoMenor = p
        elif v > maior:
            maior = v
            posicaoMaior = p

print(f'O maior valor é {maior} e sua posição é {posicaoMaior}')
print(f'O menor valor é {menor} e sua posição é {posicaoMenor}')
