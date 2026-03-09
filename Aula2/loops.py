# loops Foreach  // While  
# [] <----- array ou lista

nomes = ["Joao", "Pedro", "Antonio"]
#index     0       1         2

for nome in nomes:
    print(nome)

# funçao range()

for i in range(len(nomes)):
    print(nomes[i])

for i in range(1,11):
    print(i)


# while    <------- controlado por uma expressao ex: Val1 < val2

ifinal=len(nomes)

# tamanho da lista 3
i=0
while i<ifinal:     # começa em 0 e acaba em 2
    print("controlo de iterador",i)
    print(nomes[i])
    i+=1


#flag=True
while True:
    print("1- bom dia")
    print("1- boa tarde")
    print("3- Sair")
    opc=input("intrud a opc")
    match opc:
        case "1":
            print("bom dia")
        case "2":
            print("boa tarde")
        case "3":
            print("sair")
            break
        case _:
            print("opc errada")