texto = input('Digite algo: ')

print(f'Numérico?  {texto.isnumeric()}')
print(f'Alfabético? {texto.isalpha()}')
print(f'Alfanumérico? {texto.isalnum()}')
print(f'Minúscula? {texto.islower()}')
print(f'Maiúscula? {texto.isupper()}')
print(f'Capitalizada? {texto.istitle()}')
print(f'Só tem espaços? {texto.isspace()}')

