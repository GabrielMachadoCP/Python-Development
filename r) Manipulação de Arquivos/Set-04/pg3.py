#RM99880 - Gabriel Machado Carrara Pimentel

numeros = {9}
numero = 1
pares = {0}

while numero != 0:
    numeros.discard(9)
    print("Digite números inteiros:")
    numero = int(input())
    numeros.add(numero)

for i in numeros:
    if i % 2 == 0:
        pares.add(i)
        pares.discard(0)
numerosPares = "numerosPar.txt"
arquivo = open(numerosPares, "w")

for numero in pares:
    arquivo.write(str(numero) + "\n")

arquivo.close()
print()
print(f"Os números pares foram salvos!")
arquivo = open(numerosPares, "r")
conteudo = arquivo.read()

print(f"Conteúdo do arquivo '{numerosPares}':")
print(conteudo)
arquivo.close()