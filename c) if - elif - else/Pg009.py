import random

print('''Escolha entre: 
Pedra
Papel
Tesoura
''')

jogador = input("Sua Jogada:")

computador = ("pedra", "papel", "tesoura")
print("Jogada do computador:", random.choice(computador))