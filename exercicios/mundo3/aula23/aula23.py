# Aula 23 - Tratamento de erros e exceções

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados")
except ZeroDivisionError:
    print("Não é possível dividir por zero")
except KeyboardInterrupt:
    print(" O usuário preferiu não informar os dados  ")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(f'O resultado da divisão é: {r}')
finally:
    print("Volte sempre, muito obrigado")