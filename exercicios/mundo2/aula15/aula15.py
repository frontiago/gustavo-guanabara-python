# Aula 15 - Interrompendo repetições while
# https://www.youtube.com/watch?v=1OFp_-R2B2A&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=35&t=2s&pp=iAQB
# Exercícios 66 até 71

numero = 0
soma = 0
quantidade_numeros = 0

while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    quantidade_numeros += 1
    soma += numero

print(f'Quantidade de números: {quantidade_numeros}')
print(f'Soma: {soma}')
