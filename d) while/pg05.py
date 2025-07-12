valor = float(input())
dinheiro = float(input())

troco = dinheiro - valor

notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
moedas1 = 0

while troco>= 50:
    notas50 += 1
    troco -= 50

while troco>= 20:
    notas50 += 1
    troco -= 20

while troco>= 10:
    notas50 += 1
    troco -= 10

while troco>= 5:
    notas50 += 1
    troco -= 5

while troco>= 1:
    notas50 += 1
    troco -= 1

print("Notas de 50:", notas50)
print("Notas de 20:",  notas20)
print("Notas de 10", notas10)
print("Notas de 5:", notas5)
print("Moedas de 1:", moedas1)