# Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo

print('=' * 20)
print('Analisador de Triângulos')
print('=' * 20)
reta1 = float(input('Digite o primeiro segmento: '))
reta2 = float(input('Digite o segundo segmento: '))
reta3 = float(input('Digite o terceiro segmento: '))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print('Sim, é possível formar um triângulo')
else:
    print('NÃO é possível formar um triângulo')