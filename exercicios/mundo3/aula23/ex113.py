# Exercício 113 -
#

# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade de digitação
# de um número inválido. Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31m POR FAVOR, digite um número inteiro válido \033[m")
            continue
        except KeyboardInterrupt:
            print()
            print("\033[33m PROGRAMA INTERROMPIDO PELO USUÁRIO \033[m ")
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31m POR FAVOR, Digite um número float válido \033[m ")
        except KeyboardInterrupt:
            print()
            print("\033[33m PROGRAMA INTERROMPIDO PELO USUÁRIO \033[m")
            return 0
        else:
            return n


n1 = leiaint("Digite um número inteiro: ")
n2 = leiafloat("Digite um número float: ")
print(f"O valor inteiro foi {n1} e o real foi {n2}")