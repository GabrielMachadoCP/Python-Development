print("Digite 15 números inteiros:")

numeros = []
soma = 0
for i in range(1,16,1):
    numeros.append(int(input()))
    

for num in numeros:
    soma += num
print(soma)