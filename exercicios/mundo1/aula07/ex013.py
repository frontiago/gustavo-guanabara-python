# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite o salário do funcionário: '))
novo_salario = salario + (salario * 0.15)

print(f'O salário antigo era: R$ {salario:.2f}')
print(f'O novo salário será de: R$ {novo_salario:.2f}')