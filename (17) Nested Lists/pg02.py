matriz = []
qtdelin = 5
qtdecol = 3
menor = 100000
for i in range(0,qtdelin,1):
    linha = []
    for j in range(0,qtdecol,1):
        print("Digite numeros inteiros")
        numero = int(input())
        linha.append(numero)
    matriz.append(linha[:])

for k in range(0, len(matriz), 1):
    if k < menor:
        menor = k

print(f"O menor valor da matriz é {menor}")