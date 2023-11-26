# Exercício 043 - Índice de massa corporal
# https://www.youtube.com/watch?v=b7r34za963I&t=5s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNDMgcHl0aG9u

# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida

peso = float(input('Qual o seu peso, em kg: '))
altura = float(input('Qual a sua altura, em metros: '))
imc = float(peso / (altura * 2) * 100)

print('=' * 20)
print('IMC - RESULTADO')
print('=' * 20)
print(f'IMC: {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está no seu peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está em sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade')
elif imc >= 40:
    print('Você está com obesidade mórbida')
else:
    print('Digite números válidos')