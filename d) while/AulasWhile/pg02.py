soma = 0
comp = 1
while comp != 0:
    print("Digite o comprimento da asa de um pelicano")
    print("Pressione 0 para encerrar")
    comp = float(input())
    soma += comp
print(f"A soma dos comprimentos dos pelicanos é {soma}")