import os as fsos
import json

filename="./Aula7/Dados/data2.txt"
dicionario={}


if fsos.path.exists(filename):
    with open(filename,"r",  encoding="utf-8") as manipfile:
        dicionario=json.load(manipfile)
   
#edit 1  menu
objeto=[{"nomes":{"nomepatrao":"dario","nomeempregado":"Marieta"},"tel":[2,1]},{"nome":"joao","tel":3},{"nome":"Pedro","tel":4},{"nomes":{"nomepatrao":"dario","nomeempregado":"Marieta"},"tel":[2,1]},{"nome":"joao","tel":3},{"nome":"Pedro","tel":4}]

print(objeto[0]["nomes"])
print(objeto[1]["nome"])
with open(filename,"w", encoding="utf-8") as manipfile:
    json.dump(dicionario,manipfile,  ensure_ascii=True , indent=4)