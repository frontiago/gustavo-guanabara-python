# Escreva um programa que pergunta o salário de um funcionário e calcula o valor do seu aumento
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual é o salário do funcionário? '))

if salario > 1250:
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.15)

print(f'Salário antigo: {salario:.2f}')
print(f'Novo salário: {novo_salario:.2f}')