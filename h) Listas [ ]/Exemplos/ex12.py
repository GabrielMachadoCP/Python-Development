#Ordena a lista
frutas = ["maçã", "uva","tomate","morango", "banana"]
frutas.sort()
for j in frutas:
    print(j)

numeros = [150, 20, 5, 200, 40]
numeros.sort(reverse = True) #Ordena inversamente
print(numeros)

frutas = ["maçã", "Uva","tomate","morango", "banana"]
frutas.sort()
print(frutas)

frutas = ["maçã", "Uva","tomate","morango", "banana"]
frutas.sort(key=str.lower) #Vai desconsiderar a importância da letra maiúscula
print(frutas)