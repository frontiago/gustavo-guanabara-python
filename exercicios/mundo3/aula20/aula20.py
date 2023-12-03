# Aula 20 - Funções
# https://youtu.be/ezfr9d7wd_k?si=n5Gl87bncc0GO8D8

valores = [7, 2, 5, 0, 4, 9, 8, 3, 2, 6]
lista_pares = []


def contar(lista):
    tamanho = len(lista)
    print(f'Possui {tamanho} elementos')


def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


def pares(lista):
    for valor in lista:
        if valor % 2 == 0:
            lista_pares.append(valor)
    print(f'Os números pares são: {lista_pares}')


print()
print('-' * 30)
print(valores)
contar(valores)
dobra(valores)
pares(valores)