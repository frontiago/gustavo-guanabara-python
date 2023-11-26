# Aula 14 - While
# https://youtu.be/LH6OIn2lBaI?si=KXWedsxwjhmBtTcb
# Exercícios 57 até 65

n = 1
par = impar = 0
soma = 0

while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
        soma += n

print(f'Você digitou {par} pares e {impar} ímpares')
print(f'A soma dos números digitados é {soma}')