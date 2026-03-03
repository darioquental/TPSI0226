'''
==========================================
OPERADORES EM PYTHON
Aritméticos | Decisão | Lógicos | IF | MATCH
==========================================
'''

# ---------------------------------
# OPERADORES ARITMÉTICOS
# ---------------------------------

# +  -> soma
# -  -> subtracção
# /  -> divisão
# *  -> multiplicação
# %  -> resto da divisão (módulo)
# ** -> potência

num1 = int(input("Insira o número 1: "))
num2 = int(input("Insira o número 2: "))

print(f"Soma: {num1 + num2}")
print(f"Subtracção: {num1 - num2}")
print(f"Divisão: {num1 / num2}")
print(f"Multiplicação: {num1 * num2}")
print(f"Resto da divisão: {num1 % num2}")
print(f"Potência: {num1 ** num2}")


# ---------------------------------
# OPERADORES DE DECISÃO
# ---------------------------------

# ==  igualdade
# !=  diferente
# >   maior que
# <   menor que
# >=  maior ou igual
# <=  menor ou igual


# ---------------------------------
# OPERADORES LÓGICOS
# ---------------------------------

# and -> E (todas as condições verdadeiras)
# or  -> OU (pelo menos uma verdadeira)
# not -> negação


# ---------------------------------
# IF SIMPLES
# ---------------------------------

val1 = 2
val2 = 3
val3 = 6

if val1 > val2:
    print("val1 é maior que val2")
else:
    print("val2 é maior ou igual a val1")


# ---------------------------------
# EXERCÍCIO: ENCONTRAR O MAIOR E O MENOR
# ---------------------------------
# Forma organizada e correcta

if val1 >= val2 and val1 >= val3:
    maior = val1
elif val2 >= val1 and val2 >= val3:
    maior = val2
else:
    maior = val3

if val1 <= val2 and val1 <= val3:
    menor = val1
elif val2 <= val1 and val2 <= val3:
    menor = val2
else:
    menor = val3

print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")


# ---------------------------------
# MATCH CASE (Python 3.10+)
# ---------------------------------

print("\nMenu:")
print("1 - Bom dia")
print("2 - Boa noite")
print("3 - Sair")

opc = input("Escolha uma opção: ")

match opc:
    case "1":
        print("Bom dia")
    case "2":
        print("Boa noite")
    case "3":
        print("A sair do programa...")
    case _:
        print("Opção inválida")