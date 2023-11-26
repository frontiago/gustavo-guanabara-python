# Aula 12 - Condições aninhadas
# https://www.youtube.com/watch?v=j9bYDjaAYzw&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=2&pp=iAQB
# Exercícios do 36 até 45

nome = str(input('Digite seu nome: ')).lower()

if nome == 'thiago':
    print(f'seu nome é maravilhoso, {nome} é o nome mais lindo do mundo')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('é um nome bem comum no Brasil')
elif nome in 'ana claudia jessica juliana':
    print('belo nome feminino')
else:
    print('seu nome é bem comum')

print(f'tenha um bom dia, {nome}')