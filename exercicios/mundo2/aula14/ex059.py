# Exercício 059 - Criando um menu de opções
# https://www.youtube.com/watch?v=OBJL5vPj4-E&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNTggcHl0aG9u

# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso

option = 0
soma = 0
maior = 0

while option != 5:
    print(' ')
    print('=' * 20)
    print(' ')
    number1 = int(input('Digite o primeiro número: '))
    number2 = int(input('Digite o segundo número: '))

    print('''
    Escolha a operação
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números 
    [ 5 ] Sair do programa
    ''')

    option = int(input('Digite o número da operação: '))
    print(' ')

    if option == 1:
        soma = number1 + number2
        print(f'Você escolheu somar, a soma deu: {soma} ')
    elif option == 2:
        multiplicacao = number1 * number2
        print(f'Você escolheu multiplicar e o resultado é {multiplicacao}')
    elif option == 3:
        if number1 > number2:
            maior = number1
            print(f'O primeiro númbero é maior, {number1} é maior que {number2}')
        else:
            maior = number2
            print(f'O segundo númbero é maior, {number2} é maior que {number1}')

    elif option == 4:
        number3 = int(input('Digite o terceiro e novo número para a operação: '))

        print('''
            Escolha a operação
            [ 1 ] Somar
            [ 2 ] Multiplicar
            [ 3 ] Maior
            [ 5 ] Sair do programa
            ''')

        option = int(input('Digite o número da operação: '))
        print(' ')

        if option == 1:
            soma = number1 + number2 + number3
            print(f'A soma entre os três números é: {soma}')
        elif option == 2:
            multiplicar = number1 * number2 * number3
            print(f'A multiplicação entre os três números é: {multiplicar}')
        elif option == 3:
            if number1 > number2 and number1 > number3:
                maior = number1
            elif number2 > number1 and number2 > number3:
                maior = number2
            elif number3 > number1 and number3 > number2:
                maior = number3
            print(f'O maior entre {number1}, {number2} e {number3} é -> {maior}')

print('VOCÊ SAIU DO PROGRAMA! REINICIE E TENTE NOVAMENTE')