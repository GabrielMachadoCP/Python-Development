def resto(n1, n2):
    result = n1 % n2
    return result


print("Digite 2 números inteiros")
num1 = int(input())
num2 = int(input())
resultado = resto(num1, num2)
print(f"O resto da divisão é: {resultado}")