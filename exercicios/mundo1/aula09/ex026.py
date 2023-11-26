# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece pela última vez

frase = 'arara azul'.strip().lower()

print(f'A letra A aparece {frase.count("a")} vezes')
print(f'A letra A aparece pela primeira vez na posição: {frase.find("a")}')
print(f'A última letra A aparece pela última vez na posição: {frase.rfind("a")}')
