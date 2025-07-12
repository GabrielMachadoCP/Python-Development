print("Digite 20 números:")

numeros = []
soma = 0
for i in range(1,6,1):
    numeros.append(float(input()))
    

for num in numeros:
    soma += num
    media = soma/5
print(f"A média é: {media}")