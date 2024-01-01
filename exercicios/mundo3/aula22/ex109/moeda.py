def aumentar(preco=0, taxa=0, formatado=False):
    resultado = preco + (preco * taxa / 100)
    return resultado if formatado is False else moeda(resultado)


def diminuir(preco=0, taxa=0, formatado=False):
    resultado = preco - (preco * taxa / 100)
    return resultado if formatado is False else moeda(resultado)


def dobro(preco=0, formatado=False):
    resultado = preco * 2
    return resultado if not formatado else moeda(resultado)


def metade(preco=0, formatado=False):
    resultado = preco / 2
    return resultado if not formatado else moeda(resultado)


def moeda(preco=0, pais_moeda="R$"):
    return f"{pais_moeda}{preco:>.2f}".replace(".", ",")