nomes=["da","fa","oi","da"]
index=[]
#index   0    1    2   3
 
def insert(nomesi:list):
    nomesi.append(input("insert um nome"))
 
def listar(listarl:list,tipovalor:str):
    for listal in listarl:
        print(tipovalor, " " , listal)

def delete(nomesd:list):
    nomesd.pop( int(input(" insert posiçao ")))

def procurar(nomesp:list,indexs:list):
    indexs.clear()
    nome=input("insert nome de procura")
    for i in range(len(nomesp)):
        if nomesp[i] == nome:
            indexs.append(i)

while True:
    print ("1 - inserir nome")
    print ("2 - listar nomes")
    print ("3 - delete nome")
    print ("4 - procurar nome")
    print ("5 - sair")
    opt=input("Escolha Opção")
    match opt :
        case "1":
            insert(nomes)
        case "2":
            listar(nomes,"nome")
        case "3":
            procurar(nomes, index)
            listar(index,"posiçao")
            delete(nomes)
        case "4":
            procurar(nomes, index)
            listar(index,"posiçao")
        case "5":
            print("fim do programa")
            break
        case _:
            print("nao escolheu a opçao certa")