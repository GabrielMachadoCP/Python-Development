try:
    qi = 1
    genios = 0
    while True:
        print("Digite valores de QI de diversas pessoas:")
        qi = int(input())
        if qi < 140:
            continue
        elif qi == 0:
            break
        else:
            genios += 1
except ValueError:
    print("Somente números inteiros são aceitos!")
print(f"A quantidade de gênios digitada foi {genios}")