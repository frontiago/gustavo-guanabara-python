# Exercício 063 - Sequência de fibonacci v1.0
# https://www.youtube.com/watch?v=w7yn1_Mfu0E&t=548s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNjIgcHl0aG9u

# Escreva um programa que leia um número n inteiro qualquer e mostre na tela
# os n primeiros elementos de uma sequência de fibonacci
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> -> 5 -> 8

terms = int(input('How many terms? '))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if terms <= 0:
    print('Please, enter a positive integer')
elif terms == 1:
    print(f'Fibonnaci sequence upto {terms}:')
    print(n1)
# generate fibonacci sequence
else:
    print('Fibonacci sequence:')
    while count < terms:
        print(n1)
        nt = n1 + n2
        # update values
        n1 = n2
        n2 = nt
        count += 1