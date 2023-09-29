#RM99880 - Gabriel Machado Carrara Pimentel
import random

matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(random.randint(10, 30))
    matriz.append(linha)
print("Matriz:")
for linha in matriz:
    print(linha)

linha4 = sum(matriz[3])
coluna2 = (matriz[0][1] + matriz[1][1] + matriz[2][1] + matriz[3][1] + matriz[4][1])
principal = sum(matriz[i][i] for i in range(5))
secundaria = sum(matriz[i][4 - i] for i in range(5))
total = sum(sum(linha) for linha in matriz)

print("\nResultados das somas:")
print(f"Soma da linha 4: {linha4}")
print(f"Soma da coluna 2: {coluna2}")
print(f"Soma da Diagonal Principal: {principal}")
print(f"Soma da Diagonal Secundária: {secundaria}")
print(f"Soma de todos os valores: {total}")