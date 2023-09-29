import math
print("Digite o valor de A:")
a = int(input())
print("Digite o valor de B:")
b = int(input())
print("Digite o valor de c:")
c = int(input())
delta = b * b - 4 * a * c
x1 = (- b + math.sqrt(delta))/(2 * a)
x2 = (- b - math.sqrt(delta))/(2 * a)
print("O valor de x1 é:", x1)
print("O valor de x2 é:", x2)