# Exercício 042 - Analisando triângulos
# https://www.youtube.com/watch?v=ZX7sCPjcHA0&t=1s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNDAgcHl0aG9u

# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados são iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

reta1 = float(input('Digite o primeiro segmento da reta: '))
reta2 = float(input('Digite o primeiro segmento da reta: '))
reta3 = float(input('Digite o primeiro segmento da reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('Forma um triângulo')
    if reta1 == reta2 and reta1 == reta3:
        print('O triângulo é do tipo Equilátero')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('O triângulo é do tipo Isósceles')
    elif reta1 != reta2 and reta1 != reta3:
        print('O triângulo é do tipo Escaleno')
else:
    print("NÃO forma um triângulo")

