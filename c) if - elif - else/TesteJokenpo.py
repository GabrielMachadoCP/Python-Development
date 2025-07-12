import random

print('''Escolha entre: 
Pedra
Papel
Tesoura
''')

jogador = input("Sua Jogada:")

computador = ("pedra", "papel", "tesoura")
print("Jogada do computador:", random.choice(computador))

if computador == "pedra":
    if jogador == "Pedra":
        print("Empatou!")
    elif jogador == "Papel":
        print("Você Venceu!")
    elif jogador == "Tesoura":
        print("Você Perdeu!")

if computador == "papel":
    if jogador == "Papel":
        print("Empatou!")
    elif jogador == "Tesoura":
        print("Você Venceu!")
    elif jogador == "Pedra":
        print("Você Perdeu!")

if computador == "tesoura":
    if jogador == "Tesoura":
        print("Empatou!")
    elif jogador == "Pedra":
        print("Você Venceu!")
    elif jogador == "Papel":
        print("Você Perdeu!")
