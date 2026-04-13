# controlo de fluxo "Loop" a uma dimençao

#varaux=1
#varaux=listanum[5] 

#listanum[5]=9
#listanum[5] = listanum[0]

#listanum[0]= 1
#listanum[0] = varaux
listanum=[9,2,4,8,6,1]
#index    0 1 2 3 4 5
flags=True

#bubble sort
while flags:
    flags=False
    print("loooop de fora")
    for i in range(len(listanum)-1):
        print("loop interior")
        print("i: ",i)
        if listanum[i]>listanum[i+1]:
            flags=True
            print("troca aconteceu","posiçao i" ,listanum[i],"posiçao i+1", listanum[i+1])
            listanum[i],listanum[i+1]=listanum[i+1],listanum[i]
    print(listanum)