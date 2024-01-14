from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = "cursoemvideo.txt"

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar novas pessoas", "Sair do sistema"])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho("NOVO CADASTRO")
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do sistema...até logo")
        break
    else:
        print("\033[31m ERRO! Digite uma opção válida \033[m")
    sleep(2)
