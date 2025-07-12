matriz1 = []
matriz2 = []
qtdelin = 3
qtdecol = 2
for i in range(0,qtdelin,1):
    linha = []
    for j in range(0,qtdecol,1):
        print("Digite um numero inteiro para a primeira matriz:")
        numero = float(input())
        linha.append(numero)
    matriz1.append(linha[:])

for i in range(0,qtdelin,1):
    linha = []
    for j in range(0,qtdecol,1):
        print("Digite um numero inteiro para a segunda matriz:")
        numero = float(input())
        linha.append(numero)
    matriz2.append(linha[:])

for h in matriz1:
    print(h)
print()
for k in matriz2:
    print(k)

s00 = matriz1[0][0] + matriz2[0][0]
s01 = matriz1[0][1] + matriz2[0][1]
s10 = matriz1[1][0] + matriz2[1][0]
s11 = matriz1[1][1] + matriz2[1][1]
s20 = matriz1[2][0] + matriz2[2][0]
s21 = matriz1[2][1] + matriz2[2][1]

MatrizSoma = [
    [s00,s01],
    [s10,s11],
    [s20,s21],
]

print()
print(MatrizSoma)