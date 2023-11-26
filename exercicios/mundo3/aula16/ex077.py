# Exercício 077 - Contando vogais em tupla
# https://www.youtube.com/watch?v=8BgSqrOpKvU&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=7&pp=iAQB

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

palavras = (
    'aprender', 'programar', 'linguagem', 'python',
    'curso', 'gratis', 'estudar', 'praticar',
    'trabalhar', 'mercado', 'programador', 'futuro'
)

for p in palavras:
    print(f'\n Na palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')