# Exercício 096 - Função que calcula área
# https://www.youtube.com/watch?v=oV1s53YGtvE&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=97&pp=iAQB

# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno

def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'A área de um terreno de {largura}m largura por {comprimento}m de comprimento é {area_terreno}m')
    print()


area(10, 30)