import math
try:
    print("Digite valores inteiros para A, B e C:")
    A = int(input())
    B = int(input())
    C = int(input())
    delta = B**2 - 4 * A * C
    try:
        x1 = (-B + math.sqrt(delta)) / 2 * A
        x2 = (-B - math.sqrt(delta)) / 2 * A
        print(f"Delta é {delta}")
        print(f"x1 é {x1}")
        print(f"x2 é {x2}")
    except ValueError:
        print("Erro! Delta Negativo")
except ValueError:
    print("Os valores de A, B e C devem ser inteiros!")
