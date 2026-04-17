# qualquer açao com ficheiros 
# read, write , append , binario
# 1 - open file
# 2 - acção
# 3 - close file

import os as fsos
filename="./Aula7/Dados/data.txt"
Texto=""
opc=0

if fsos.path.exists(filename):
    with open(filename,"r",  encoding="utf-8") as manipfile:
        texto=manipfile.read()

while True:

    print("1 - para intrud no texto")
    print("2 - para listar o texto")
    print("3 - para gravar no file")
    print("4 - sair do programa")
    opc=input("Escolha a opc")
    
    match opc:
        case "1":
            texto=input("intrud uma frase")
        case "2":
            print(texto)
        case "3":
            with open(filename,"w", encoding="utf-8") as manipfile:
                manipfile.write(texto)
        case "4":
            guarda=input("guardar o texto s/n")
            if guarda=="s" or  guarda=="S":
                with open(filename,"w", encoding="utf-8") as manipfile:
                    manipfile.write(texto)
            break
        case _:
            print("opc errada")