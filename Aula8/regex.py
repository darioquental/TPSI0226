import re as reg

# Padrões 
# "ABC"   -----------> procura o padrão ABC no texto
# [A-L]   -----------> procura o padrão A a L no texto
#  *.mp3

#funções

#reg.search()   ------ procura em qualquer parte do texto
#reg.match()    ------ procura no inicio da string
#reg.findall()  ------ devolve todas as ocurrencias na string
#reg.split()    ------ divide a string em partes por padrão

email= "sdasdas@gmail.com"
padrao=r"^[\w\.]+@[\w]+\.\w+$"

resultado=reg.match(padrao,email)

print (resultado)
print (resultado.group())
print (resultado.start())
print (resultado.end())
print (resultado.span())

#[] lista
#{
# nome: Pedro
# } dicionario /objeto

#https://regex101.com/
#https://overthewire.org/wargames/