# Aula 09 - Manipulando Texto
# https://www.youtube.com/watch?v=a7DH88vk2Sk&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=31&pp=iAQB

frase = 'Curso Em Video Python'

# frase[9] - mostra a letra v que está na 9ªposição
# frase[9:21] - mostra Video Python, da posição 9 até 20
# frase[9:21:2] - do 9 ao 20 indo de 2 em 2
# frase[:5] - do começo até a 4ªposição
# frase[9::3] - a partir da 9ª posição até o final indo de 3 em 3

# len(frase) - mostra o comprimento da variavel em caracteres
# frase.count('o') - conta a quantidade de o na variável
# frase.find('Android') - procura pela palavra 'Android' na string, quando não encontra, retorna -1

# 'Curso" in frase - checa se existe a palavra Curso na string, mostra True
# frase.replace('Python', 'Android') - substitui a palavra Python por Android

# frase.upper() - transforma as letras em miúsculas
# frase.lower() - transforma as letras em minúsculas
# frase.capitalize() - a primeira letra pra maiscula
# frase.title() - a primeira letra de cada palavra pra maiúscula

# frase.strip() - remove espaços do começo e do final da string
# frase.rstrip() - remove somente os espaços da direita
# frase.lstrip() - remove somente os espaços da esquerda

# frase.split() - separa as palavras da string, utiliza o espaço entre elas pra separar
# '-'.join(frase) - coloca caracteres entre os espaços da string, resultado: Curso-Em-Video-Python

print(frase.lower())