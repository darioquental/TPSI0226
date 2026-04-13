# Lista de nomes
lista_nomes = ["Dario Quental", "Joao Alves"]

# Aceder a caracteres específicos
print("Letra 5 do primeiro nome:", lista_nomes[0][4])
print("Letra 5 do segundo nome:", lista_nomes[1][4])

print("\n--- Loop pelos nomes ---")

# Loop pelos nomes (forma simples)
for nome in lista_nomes:
    print("Nome completo:", nome)
    print("Primeira letra:", nome[0])
    print("Última letra:", nome[-1])
    print("---")