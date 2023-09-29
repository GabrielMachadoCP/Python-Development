soma = gordo = 0
while soma <= 100000:
    print("Digite o peso dos hipopótamos:")
    peso = float(input())
    if peso > gordo:
        gordo = peso
    soma += peso
print(f"O hipopótamo mais gordo tem {gordo} kg")