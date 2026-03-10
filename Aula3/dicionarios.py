# Dicionarios Babys
# {} <--- dicionarios         -> tipo de ficheiro json
# chave - valor

carros={"Marc":"BMW","Modelo":"M3"}
# acesso em Mapping
print(carros)
print(carros["Marc"])
print(carros["Modelo"])
carros.update({"Ano":2000})
print(carros)
carros.update({"Marca":"BMW"})
print(carros)
carros.pop("Marc")
print(carros)
