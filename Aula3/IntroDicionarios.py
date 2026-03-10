# DICIONÁRIOS EM PYTHON
# {} -> estrutura usada para criar um dicionário
# Um dicionário guarda dados em pares: chave -> valor
# Muito usado para representar dados tipo JSON

# Exemplo inicial
carros = {"Marca": "BMW", "Modelo": "M3"}

# ----------------------------------------------------
# Mostrar o dicionário completo
print(carros)

# Aceder a valores através da chave
print(carros["Marca"])
print(carros["Modelo"])


# ----------------------------------------------------
# ADICIONAR OU ALTERAR VALORES

# Método update() adiciona nova chave ou altera se já existir
carros.update({"Ano": 2000})
print(carros)

# Outra forma de adicionar
carros["Cor"] = "Preto"
print(carros)


# ----------------------------------------------------
# OBTER VALORES

# get() devolve o valor da chave (evita erro se não existir)
print(carros.get("Marca"))

# get() com valor default
print(carros.get("Pais", "Não definido"))


# ----------------------------------------------------
# LISTAR CHAVES E VALORES

# keys() -> devolve todas as chaves
print(carros.keys())

# values() -> devolve todos os valores
print(carros.values())

# items() -> devolve chave e valor
print(carros.items())


# ----------------------------------------------------
# PERCORRER DICIONÁRIO

# Percorrer apenas chaves
for chave in carros.keys():
    print(chave)

# Percorrer valores
for valor in carros.values():
    print(valor)

# Percorrer chave e valor
for chave, valor in carros.items():
    print(chave, "->", valor)


# ----------------------------------------------------
# REMOVER ELEMENTOS

# pop() remove usando a chave
carros.pop("Modelo")
print(carros)

# popitem() remove o último elemento inserido
carros.popitem()
print(carros)


# ----------------------------------------------------
# TAMANHO DO DICIONÁRIO

print(len(carros))


# ----------------------------------------------------
# VERIFICAR SE EXISTE UMA CHAVE

if "Marca" in carros:
    print("Existe a chave Marca")


# ----------------------------------------------------
# COPIAR DICIONÁRIO

carros2 = carros.copy()
print(carros2)


# ----------------------------------------------------
# LIMPAR DICIONÁRIO

carros.clear()
print(carros)
