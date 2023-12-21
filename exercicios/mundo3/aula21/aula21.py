# Aula 21 - Funções - Parte 2
# Exercícios 101 até 106
# https://youtu.be/etjJ_4Eqrk8?si=75PL1Y1wFpznBg6U

def fatorial(num):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número para ver o fatorial: '))
print(f'O fatorial de {n} é {fatorial(n)}')