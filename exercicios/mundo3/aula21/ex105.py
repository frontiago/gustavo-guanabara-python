# Exercício 105 - Analisando e gerando dicionários
# https://www.youtube.com/watch?v=Kbs97l38vVQ&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=40&pp=iAQB

# Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# A) A quantidade de notas
# B) A maior nota
# C) A menor nota
# D) A média da turma
# E) A situação (opcional)

# Adicione também as docstrings da função

def notas(* nota, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos
    param n: uma ou mais notas dos alunos (aceita várias)
    param situacao: valor opcional, indicando se deve ou não adicionar a situação
    param return: dicionário com várias informações sobre a situação da turma
    """
    resultado = dict()
    resultado["total"] = len(nota)
    resultado["maior"] = max(nota)
    resultado["menor"] = min(nota)
    resultado["media"] = sum(nota)/len(nota)

    if situacao:
        if resultado["media"] >= 7:
            resultado["situacao"] = "BOA"
        elif resultado["media"] >= 5:
            resultado["situacao"] = "RAZOAVEL"
        elif resultado["media"] < 5:
            resultado["situacao"] = "RUIM"

    return resultado


# Programa principal
resposta = notas(5.5, 3.7, 4.9, 3.8, situacao=True)
print(resposta)
help(notas)