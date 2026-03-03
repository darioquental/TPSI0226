'''
==========================================
COMENTÁRIOS E TIPOS DE DADOS EM PYTHON
==========================================
'''

# Comentário de uma linha utiliza o símbolo #

# ---------------------------------
# OUTPUT (SAÍDA) PARA A CONSOLA
# ---------------------------------

print("Hello World TPSI0226")


# ---------------------------------
# INT (Número Inteiro)
# ---------------------------------

tel = 9   # número inteiro (int)
print("\nTipo da variável tel:")
print(type(tel))
print("Valor de tel:")
print(tel)

# Python é uma linguagem de tipagem dinâmica
# A mesma variável pode mudar de tipo automaticamente

tel = "9"   # agora é uma STRING (texto), já não é número

# Atenção:
# "9" NÃO tem valor 57.
# Só teria valor 57 se utilizássemos: ord("9")

print("\nTipo da variável tel após alteração:")
print(type(tel))
print("Novo valor de tel:")
print(tel)


# ---------------------------------
# FLOAT (Número Decimal)
# ---------------------------------

med = 2.3
print("\nTipo da variável med:")
print(type(med))
print("Valor de med:")
print(med)


# ---------------------------------
# STRING (Texto)
# ---------------------------------

nom = "Dario"
print("\nTipo da variável nom:")
print(type(nom))
print("Valor de nom:")
print(nom)


# ---------------------------------
# BOOLEAN (Verdadeiro ou Falso)
# ---------------------------------

flag = True
print("\nTipo da variável flag:")
print(type(flag))
print("Valor de flag:")
print(flag)


# ---------------------------------
# LISTA []
# ---------------------------------
# Pode guardar vários tipos de dados
# É MUTÁVEL (pode ser alterada)

lista = [1, "dario", 4.4, False, 9]

print("\nTipo da variável lista:")
print(type(lista))
print("Conteúdo da lista:")
print(lista)


# ---------------------------------
# TUPLO ()
# ---------------------------------
# Parecido com a lista, mas é IMUTÁVEL
# Não pode ser alterado depois de criado

tuplo = (1, 3, 4, 6)

print("\nTipo da variável tuplo:")
print(type(tuplo))
print("Conteúdo do tuplo:")
print(tuplo)