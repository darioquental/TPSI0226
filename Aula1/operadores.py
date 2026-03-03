'''
==========================================
OPERADORES EM PYTHON
Aritméticos | Decisão | Lógicos | IF
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
# ** -> potência (exponencial)

total = 0
num1 = 0
num2 = 0

# INPUT DE VALORES
num1 = int(input("Insira o número 1: "))
num2 = int(input("Insira o número 2: "))

# Soma
total = num1 + num2
print(f"Soma: {total}")

# Subtracção
total = num1 - num2
print(f"Subtracção: {total}")

# Divisão
total = num1 / num2
print(f"Divisão: {total}")

# Multiplicação
total = num1 * num2
print(f"Multiplicação: {total}")

# Resto da divisão
total = num1 % num2
print(f"Resto da divisão: {total}")

# Potência
total = num1 ** num2
print(f"Potência: {total}")


# ---------------------------------
# OPERADORES DE DECISÃO (COMPARAÇÃO)
# ---------------------------------

# ==  igualdade
# !=  diferente
# >   maior que
# <   menor que
# >=  maior ou igual
# <=  menor ou igual

# Uma expressão devolve sempre True ou False
# Exemplo:
# val1 == val2  -> True ou False


# ---------------------------------
# OPERADORES LÓGICOS
# ---------------------------------

# and -> E (ambas as condições têm de ser verdadeiras)
# or  -> OU (apenas uma precisa de ser verdadeira)
# not -> negação

# Exemplo lógico:
# True and False  -> False
# True or False   -> True


# ---------------------------------
# IF SIMPLES
# ---------------------------------

val1 = 2
val2 = 3

if val1 > val2:
    print("val1 é o maior")
else:
    print("val2 é o maior")


# ---------------------------------
# EXERCÍCIO: ENCONTRAR O MAIOR E O MENOR
# ---------------------------------