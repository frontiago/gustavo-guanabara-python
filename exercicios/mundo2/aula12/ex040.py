# Exercício 040 - Aquele clássico da média
# https://www.youtube.com/watch?v=QuWDyUeoaJs&t=2s&pp=ygUbZ3VzdGF2byBndWFuYWJhcmEgNDAgcHl0aG9u

# Crie um programa que leia duas notas de um aluno e calcule a sua média
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0, reprovado
# Média entre 5.0 e 6.9 - recuperação
# Média 7.0 ou superior - aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f'APROVADO! Parabéns, sua média foi {media:.1f}')
elif media >= 5:
    print(f'RECUPERAÇÃO! sua média foi {media:.1f}')
elif media < 5:
    print(f'REPROVADO! Sua média foi {media:.1f}')


