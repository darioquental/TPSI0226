#Lista em inteiros trocas sao mais faceis

numeros=[1,5,8,3,9,23]
#index   0,1,2,3,4,5

for numero in numeros:
    print(numero)
numeros[2]=6

for numero in numeros:
    print(numero)

#Lista de Strings

#ind D1   0       1        2
nomes= ["Joao","Pedro","Antonio" ]
#ind D2  0123   01234   0123456 

for nome in nomes:
    print(nome)

#print("ola","mundo",end="\t",sep="        ")
print("",end="\n\n\n\n")
print(nomes[0])

nomes[0]="Tiago"
print(nomes[0][2])

# 1 -  quantas dimençoes realmente tem? 2 Dimençoes 
# 2 -  como adicionar mais elementos?
# 3 -  como remover elementos?
# 4 -  == compara unicode da string completa 

print("",end="\n\n\n\n")


#remover da lista
print(nomes)
nomes.remove("Pedro")
print(nomes)
nomes.pop(0)
print(nomes)

nomes.append("Dario")
print(nomes)
print(nomes.count("Dario"))

print(nomes)
print(len(nomes))
print(nomes.index('Antonio'))
