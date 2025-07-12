import re

print("Digite números:")

numeros = []
n = 0
soma_dos_negativos = 0

while numeros != 0:
    numeros.append(int(input()))
    if 0 in numeros:
        break

lista = numeros[:-1]
lista.sort()
for n in lista:
    if n < 0:
        soma_dos_negativos += n
print(f"Tamanho da lista: {len(lista)}")
print(f"Lista em ordem Crescente: {lista}")
print(f"A soma dos números negativos é: {soma_dos_negativos}")
