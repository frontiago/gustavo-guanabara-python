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


def linha(tamanho=42):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m {c} \033[m - \033[34m {item} \033[m")
        c += 1
    print(linha())
    opc = leiaint("\033[32m Sua opção: \033[m")
    return opc

