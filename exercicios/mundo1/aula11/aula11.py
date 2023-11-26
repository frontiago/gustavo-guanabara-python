# Aula 11 - Cores no Terminal
# https://www.youtube.com/watch?v=0hBIhkcA8O8&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=47&ab_channel=CursoemV%C3%ADdeo

# \033[m  - escape sequence, padrão ANSI
# \033[0:33:44m
# 0 - text
# 33 - color
# 44 - background

# 0 - none , 1 - bold , 4 - underline , 7 - negative
# 30 - white         40 - bg white
# 31 - red           41 - bg red
# 32 - green         42 - bg green
# 33 - yellow        43 - bg yellow
# 34 - blue          44 - bg blue
# 35 - purple        45 - bg purple
# 36 - light blue    46 - bg light blue
# 37 - gray          47 - bg gray

nome = 'Thiago'
cores = {
    'close': '\033[m',
    'red': '\033[0:31m',
    'blue': '\033[34m',
    'yellow': '\033[33m',
    'whiteblack': '\033[3:30m'
}

print(f'Olá, muito prazer em te conhecer {cores["red"]} {nome} {cores["close"]}')