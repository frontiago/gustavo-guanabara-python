# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7,00 por cada km acima do limite

velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print(f'VOCÊ FOI MULTADO! Ultrapassou {excesso} kms acima do permitido ')
    print(f'Deverá pagar R$ {multa},00 de multa')
else:
    print(f'PARABÉNS, VOCÊ ESTÁ DENTRO DO LIMITE DE VELOCIDADE PERMITIDO')