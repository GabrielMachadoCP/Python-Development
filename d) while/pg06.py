# leitura dos valores I, A, B e C
I = int(input("Digite um número inteiro e positivo: "))
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

# exibição dos valores lidos
print("Valores lidos: I =", I, ", A =", A, ", B =", B, ", C =", C)

# verificação do valor de I
if I == 1:
    # ordenação crescente
    while True:
        ordenado = False
        if A > B:
            A, B = B, A
            ordenado = True
        if B > C:
            B, C = C, B
            ordenado = True
        if not ordenado:
            break
    print("Valores em ordem crescente:", A, B, C)

elif I == 2:
    # ordenação decrescente
    while True:
        ordenado = False
        if A < B:
            A, B = B, A
            ordenado = True
        if B < C:
            B, C = C, B
            ordenado = True
        if not ordenado:
            break
    print("Valores em ordem decrescente:", A, B, C)

elif I == 3:
    # colocando o maior entre os outros dois
    if A > B and A > C:
        if B > C:
            maior, meio, menor = A, B, C
        else:
            maior, meio, menor = A, C, B
    elif B > A and B > C:
        if A > C:
            maior, meio, menor = B, A, C
        else:
            maior, meio, menor = B, C, A
    else:
        if A > B:
            maior, meio, menor = C, A, B
        else:
            maior, meio, menor = C, B, A
    print("Valores com o maior entre os outros dois:", meio, maior, menor)

else:
    # mensagem de erro
    print("Valor de I inválido!")