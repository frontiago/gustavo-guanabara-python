# Exercício 072 - Número por extenso
# https://www.youtube.com/watch?v=ei2Kr3ccfO0&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=2&pp=iAQB

# Crie um programa que que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero, até vinte
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

numeros = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
    'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

numero = int(input('Digite um número entre 0 e 20: '))

for i in range(0, len(numeros)):
    if i == numero:
        print(numeros[i])

if numero < 0 or numero > 20:
    print('É pra digitar um número entre 0 e 20')
