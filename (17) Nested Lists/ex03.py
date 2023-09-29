matriz = []
qtdelin = 5
qtdecol = 1
for i in range(0,qtdelin,1):
    linha = []
    for j in range(0,qtdecol,1):
        print("Digite o nome:")
        nome = input()
        linha.append(nome)
    for l in range(0,qtdecol,1):
        print(f"Digite o estado de {nome}:")
        estado = input().upper()
        linha.append(estado)
    matriz.append(linha[:])

print("Agora escolha um Estado brasileiro qualquer:")
escolhaEstado = input().upper()

for i in range(0, len(matriz), 1):    
    if escolhaEstado in matriz[i][1]:
        print(f"As pessoas que nasceram no estado {escolhaEstado} são: {matriz[i][0]}")