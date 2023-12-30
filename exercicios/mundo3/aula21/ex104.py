# Exercício 104 - Validando entrada de dados em python
# https://www.youtube.com/watch?v=VrQmMbPpbf0&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=39&pp=iAQB

# Crie um programa que tenha a função leiaint(), que vai funcionar semelhante a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leinaint('Digite um n')

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print(" \033[0;31mERRO! Digite um número inteiro válido. \033[m")
        if ok:
            break
    return valor


n = leiaint("Digite um número: ")

print(f"Você digitou o número {n}")
