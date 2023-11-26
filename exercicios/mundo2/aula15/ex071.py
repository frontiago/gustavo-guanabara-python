# Exercício 071 - Simulador de caixa eletrônico
# https://www.youtube.com/watch?v=_XGgwltYpYk&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNzAgcHl0aG9u

# Crie um programa que simule o funcionamento de um caixa eletrônico
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10, R$1

print('--- CAIXA 24HRS ---')
print('Esse caixa possui apenas notas de 1, 10, 20 e 50')
print('-' * 20)

valor = int(input('Qual o valor deseja sacar? R$ '))
total = valor
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de {cedula}')
            
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        total_cedula = 0

        if total == 0:
            break
