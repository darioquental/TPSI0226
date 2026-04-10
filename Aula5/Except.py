# ==========================================
# AULA – EXCEÇÕES EM PYTHON 
# ==========================================

# Exceções são erros que ocorrem em runtime (durante a execução do programa)
# Devem ser tratadas para evitar que o programa "crashe"

# Exemplos de exceções comuns:
# FileNotFoundError → ficheiro não existe
# ZeroDivisionError → divisão por zero
# ValueError → valor inválido
# IndexError → índice fora da lista

# ------------------------------------------
# Exemplo 1: Conversões e ASCII
# ------------------------------------------

char = str(1)
print("String:", char)
print("ASCII de '1':", ord("1"))
print("Letra correspondente ao código 65:", chr(65))


# ------------------------------------------
# Exemplo 2: ZeroDivisionError
# ------------------------------------------

n1 = 0

try:
    total = 10 / n1
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero!")


# ------------------------------------------
# Exemplo 3: ValueError (input inválido)
# ------------------------------------------

string = input("\nIntroduz um número inteiro: ")

try:
    resultado = int(string)
except ValueError as erro:
    print("Erro: valor inválido ->", erro)
else:
    print("Conversão realizada com sucesso:", resultado)


# ------------------------------------------
# Exemplo 4: Raise (lançar exceção manual)
# ------------------------------------------

idade = -1

try:
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    print("Idade válida")
except ValueError as erro:
    print("Erro:", erro)


# ------------------------------------------
# Exemplo 5: finally (executa sempre)
# ------------------------------------------

try:
    numero = int(string)
except ValueError:
    print("Erro na conversão")
finally:
    print("Fim do programa (executa sempre)")


# ------------------------------------------
# Exemplo 6: Múltiplas exceções (ValueError + IndexError)
# ------------------------------------------

lista = [1, 2, 3, 4]

try:
    valor = int("abc")   # ValueError
    print(lista[10])     # IndexError
except ValueError as erro_valor:
    print("Erro de valor:", erro_valor)
except IndexError as erro_index:
    print("Erro de índice:", erro_index)