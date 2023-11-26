# Exercício 037 - Conversor de bases numéricas
# https://www.youtube.com/watch?v=B3F0IjH5WAM&t=564s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgMzYgcHl0aG9u

# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

numero = int(input('Digite um número para fazer a conversão: '))

print('''
Para qual base deseja converter
[ 1 ] - BINÁRIO
[ 2 ] - OCTAL 
[ 3 ] - HEXADECIMAL 
''')

opcao = int(input('Digite a opção de sua escolha: '))

if opcao == 1:
    print(f'O número {numero} convertido para binário é: {bin(numero) [2:]}')
elif opcao == 2:
    print(f'O número {numero} convertido para octal é: {oct(numero) [2:]}')
elif opcao == 3:
    print(f'O número {numero} convertido para hexadecimal é: {hex(numero) [2:]}')

