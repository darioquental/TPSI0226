#operadores aritemeticos

# soma + , sub - , div / , Mult * , mode % (resto da div), ** exponential

total=0
num1=0
num2=0

#input values
num1=int(input("insira num 1"))
num2=int(input("insira num 2"))

total=num1+num2
print(f"soma : {total}")

total=num1-num2
print("sub : ",total," .")

total=num1/num2
print(f"div : {total}")

total=num1*num2
print("Mult : ",total," .")


# operadores de decisão

# == igualdade , != diferente , > maior que , < menor que 
# >= maior ou igual e <=menor ou igual

# expressao
# Val1 == Val2    = True/False

# operadores logicos

# and (&&) e  or (||)

# expressao
# Val1 > Val2 and val2 > Val3  = True/False
#    true     or     false    = True  


# If

val1=2
val2=3

if val1>val2:
    print("val1 é o maior")
else:
    print("val2 é o maior")


#exercicio encontra o maior e o menor
val1=2
val2=3
val3=4

if val1>val2 and val2>val3:
    print("val1 é o maior , Val3 é o menor")
elif val2>val1 and val1>val3:
    print("val2 é o maior , Val3 é o menor")
# continuar o codigo
