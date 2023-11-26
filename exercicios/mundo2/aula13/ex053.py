# Exercício 053 - Detector de palínsdromo
# https://www.youtube.com/watch?v=5VBWe6BXzRo&t=604s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNTIgcHl0aG9u

# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços

# Exemplos:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO

frase = str(input('Digite uma frase: ')).strip()
frase_fatiada = frase.split()
frase_junta = ''.join(frase_fatiada)
inverso = ''

for letra in range(len(frase_junta) - 1, -1, -1):
    inverso += frase_junta[letra]

print(f'{frase_junta} ao contrário é {inverso}')

if frase_junta == inverso:
    print('Temos um palíndromo')
else:
    print('NÃO temos um palíndromo')