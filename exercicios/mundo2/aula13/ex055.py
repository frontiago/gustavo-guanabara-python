# Exercício 055 - Maior e menor da sequência
# https://www.youtube.com/watch?v=Kjpb_IAOKRQ&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNTQgcHl0aG9u

# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
# https://www.youtube.com/watch?v=Kjpb_IAOKRQ&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=23&ab_channel=CursoemV%C3%ADdeo

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é {maior:.2f}kg ')
print(f'O menor peso é {menor:.2f}kg ')