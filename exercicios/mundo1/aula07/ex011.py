# Faça um programa que leia a altura e largura de uma parede em metros,
# calcule a área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
area = largura * altura
tinta = area / 2

print(f'Para pintar uma parede de {largura}x{altura} serão necessário {tinta:.1f}L litros de tinta')