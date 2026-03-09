# LISTA DE INTEIROS
# As listas permitem guardar vários valores na mesma variável.
# Neste caso temos uma lista de números inteiros.

numeros = [1, 5, 8, 3, 9, 23]

# Índices da lista (posições)
# index:   0  1  2  3  4   5
# valores: 1  5  8  3  9  23

# Percorrer a lista e mostrar todos os números
for numero in numeros:
    print(numero)

# Alterar um valor da lista
# Neste caso vamos alterar o valor da posição 2 (que era 8) para 6
numeros[2] = 6

print("\nLista depois da alteração:")

# Voltar a mostrar os valores da lista
for numero in numeros:
    print(numero)



# ---------------------------------------------------------
# LISTA DE STRINGS
# Uma lista também pode guardar texto (strings)

# Índice da lista
# index:   0       1        2
nomes = ["Joao", "Pedro", "Antonio"]

# Índice dos caracteres dentro de cada string
# Joao    -> 0 1 2 3
# Pedro   -> 0 1 2 3 4
# Antonio -> 0 1 2 3 4 5 6

# Percorrer e mostrar todos os nomes
for nome in nomes:
    print(nome)

# Apenas criar algumas linhas em branco
print("\n\n\n")

# Mostrar o primeiro elemento da lista
print(nomes[0])

# Alterar o primeiro nome da lista
nomes[0] = "Tiago"

# Aceder a um caractere dentro da string
# Tiago -> T i a g o
# índice  0 1 2 3 4
print(nomes[0][2])  # mostra a letra "a"



# ---------------------------------------------------------
# PERGUNTAS IMPORTANTES SOBRE LISTAS

# 1 - Quantas dimensões existem?
# Neste caso temos duas formas de indexação:
# nomes[0] -> posição na lista
# nomes[0][2] -> posição dentro da string

# 2 - Como adicionar elementos?
# usar append()

# 3 - Como remover elementos?
# usar remove() ou pop()

# 4 - Comparação de strings
# == compara o conteúdo completo da string (Unicode)



print("\n\n\n")


# ---------------------------------------------------------
# REMOVER ELEMENTOS DA LISTA

print(nomes)

# remove() remove pelo valor
nomes.remove("Pedro")
print(nomes)

# pop() remove pela posição (index)
nomes.pop(0)
print(nomes)


# ---------------------------------------------------------
# ADICIONAR ELEMENTOS

# append() adiciona um novo elemento no final da lista
nomes.append("Dario")
print(nomes)


# ---------------------------------------------------------
# OUTRAS FUNÇÕES ÚTEIS

# count() conta quantas vezes um valor aparece
print(nomes.count("Dario"))

# len() devolve o número total de elementos na lista
print(nomes)
print(len(nomes))

# index() devolve a posição onde um elemento aparece
print(nomes.index("Antonio"))