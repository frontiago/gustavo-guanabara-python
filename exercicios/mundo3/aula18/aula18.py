# Aula 18 - Listas parte 02
# https://youtu.be/YV_JQmZNFsk?si=bXJixcgZzE37Ya6F

galera = list()
dado = list()
totalmaior = totalmenor = 0

for i in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor += 1

print(f'Temos {totalmaior} maior e {totalmenor} menor idade')