# Aula 10 - Condições Parte 1
# https://www.youtube.com/watch?v=K10u3XIf1-Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=38&t=1126s&pp=iAQB

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 6:
    print(f'APROVADO! Você passou com média {media}')
else:
    print(f'REPROVADO! Sua média foi {media}, estude mais ')