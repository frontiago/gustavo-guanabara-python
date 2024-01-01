# Exercício 107 -
#

# Crie um módulo chamado moeda.py que tenha funções incorporadas aumentar(), diminuir(), dobro(), metade()
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

preco = float(input("Digite o preço: R$"))

print(f"A metade de {preco} é R${moeda.metade(preco)}")
print(f"O dobro de {preco} é R${moeda.dobro(preco)}")
print(f"Aumentando 10%, temos R${moeda.aumentar(preco, 10)}")
print(f"Diminuindo 13%, temos R${moeda.diminuir(preco, 13)}")

