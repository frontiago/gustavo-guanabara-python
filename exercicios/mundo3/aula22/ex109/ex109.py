# Exercício 109 -
#

# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108

import moeda

preco = float(input("Digite o preço: R$"))

print()
print(f"O preço aumentado em 20% é: {moeda.aumentar(preco, 20, True)}")
print(f"O preço reduzido em 33% é: {moeda.diminuir(preco, 33, True)}")
print(f"O dobro do preço: {moeda.dobro(preco, True)}")
print(f"A metade do preço: {moeda.metade(preco, True)}")