# Exercício 102 - Função para fatorial
# https://www.youtube.com/watch?v=84jUX96cs7Q&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=37&pp=iAQB

# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' x ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)