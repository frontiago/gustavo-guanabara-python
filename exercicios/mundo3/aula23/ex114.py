# Exercício 113 - Site está acessível?
# https://youtu.be/8jAykqxIeqw?si=0FHMVsuI8Z_nCLEF

# Crie um código em python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("ERRO! Não foi localizado o site")
else:
    print("Consegui acessar o site Pudim com sucesso")
    print(site.read())