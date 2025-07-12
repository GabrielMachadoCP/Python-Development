#RM99880 - Gabriel Machado Carrara Pimentel
import random

def somaInferiores(matriz):
    soma = 0
    soma += sum(matriz[i][0] for i in range(1, 5))
    soma += sum(matriz[i][1] for i in range(2, 5))
    soma += sum(matriz[i][2] for i in range(3, 5))
    soma += matriz[4][3]
    return soma


matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(round(random.uniform(10.0, 20.0),2))
    matriz.append(linha)

print("Matriz:")
for i in matriz:
    print(i)

total = sum(sum(linha) for linha in matriz)
Inferiores = somaInferiores(matriz)
somaDiagPrin = sum(matriz[i][i] for i in range(5))
Superiores = total - Inferiores - somaDiagPrin

print(f"\nResultado da soma dos valores da parte superior em relação à diagonal principal:{Superiores:.2f} ")
print(f"Resultado da soma dos valores da parte inferior em relação à diagonal principal: {Inferiores:.2f}")