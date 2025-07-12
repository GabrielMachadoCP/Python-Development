#import statistics
numeros = []
num = media = 0.0
soma = 0.0
for i in range(0,20,1):
    print("Digite um número real:")
    num = float(input())
    numeros.append(num)
#media = statistics.mean(numeros)
for i in numeros:
    soma += i
media = soma / len(numeros)
print(f"Média dos valores é {media}")