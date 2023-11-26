# Exercício 065 - Maior e menor valores
# https://www.youtube.com/watch?v=QNPuPlPM--0&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNjQgcHl0aG9u

# Crie um programa que leia vários números inteiros pelo teclado
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores

numero = 0
media = 0
maior = menor = 0
quantidade_numeros = 0
soma = 0
resposta = ''.lower()

while resposta != 'n':
    numero = int(input('Digite um número: '))
    quantidade_numeros += 1
    soma += numero

    if quantidade_numeros == 1:
        maior = numero
        menor = numero
    else:
        if numero < menor:
            menor = numero
        elif numero > maior:
            maior = numero

    resposta = str(input('Deseja continuar? [sim / nao]: '))

media = soma / quantidade_numeros

print('')
print('=' * 20)
print(f'A média é: {media:.2f} ')
print(f'A quantidade de números é de: {quantidade_numeros} números')
print(f'A soma entre esses números é: {soma}')
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')