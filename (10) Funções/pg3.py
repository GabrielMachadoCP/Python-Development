def numeros(num):
    if num % 2 == 0:
        print("Número Par")
    else:
        print("Número Ímpar")


print("Digite números inteiros")
num = int(input())
numeros(num)

while num != 0:
    print("Digite números inteiros")
    num = int(input())
    numeros(num)