# Aula 19 - Dicionários
# https://youtu.be/ZWj8o692qGY?si=MnlEnlkZGQZxgMWA

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(v, end=' ')
    print()

