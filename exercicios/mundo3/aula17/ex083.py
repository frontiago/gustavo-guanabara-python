# Exercício 083 - Validando expressões matemáticas
# https://www.youtube.com/watch?v=dvhP41Z7TLk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=14&pp=iAQB

# Crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
# Seu aplicativo deverá analisar se a expressão passada está com parenteses abertos e fechados na ordem correta

expressao = str(input('Digite uma expressão: '))
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha) > 0:
    print('Essa expressão NÃO é válida')
else:
    print('Essa expressão É válida, PARABÉNS!')



