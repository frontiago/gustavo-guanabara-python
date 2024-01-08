# Exercício 111 -
#

# Crie um pacote chamado utilidadesCev que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote
# e mantenha tudo funcionando.

from utilidadescev import moeda

preco = float(input("Digite o preco: R$"))
moeda.resumo(preco, 20, 22)