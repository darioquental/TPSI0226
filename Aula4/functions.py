# =====================================
# FUNÇÕES: PASSAGEM POR VALOR E REFERÊNCIA
# =====================================

# -------------------------------------
# 1) PASSAGEM POR VALOR (TIPOS IMUTÁVEIS)
# -------------------------------------

def troca_numero(num1, num2):
    print("\nDentro da função (antes da troca):", num1, num2)
    
    # Troca os valores (apenas localmente)
    num1, num2 = num2, num1
    
    print("Dentro da função (depois da troca):", num1, num2)
    
    return num1, num2  # precisa retornar para alterar fora


nu1 = 2
nu2 = 3

print("Antes da função:", nu1, nu2)

nu1, nu2 = troca_numero(nu1, nu2)

print("Depois da função:", nu1, nu2)


# -------------------------------------
# 2) PASSAGEM POR REFERÊNCIA (TIPOS MUTÁVEIS)
# -------------------------------------

def adiciona_elemento(lista):
    print("\nDentro da função (antes do append):", lista)
    
    # Modifica diretamente o objeto original
    lista.append(5)
    
    print("Dentro da função (depois do append):", lista)


listas = [1, 2, 3, 4]

print("\nAntes da função:", listas)

adiciona_elemento(listas)

print("Depois da função:", listas)