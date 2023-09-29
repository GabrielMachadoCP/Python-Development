#Gabriel Machado Carrara Pimentel 
#RM 99880

pokemons = ("bulbassauro", "planta", "gloom", "planta", "squirtle", "água", "blastoise", "água", "wartortle", "água", "charizard", "fogo", "charmander", "fogo", "pikachu", "elétrico", "luxio", "elétrico", "Elekid", "elétrico")
planta = pokemons [0], pokemons[2]
água = pokemons[4], pokemons[6], pokemons[8]
fogo = pokemons[10], pokemons[12]
elétrico = pokemons[14], pokemons[16], pokemons[18]

print("Escolha um tipo de pokemon (Planta, Água, Fogo, Elétrico):")
escolha = input()

if escolha.lower() == "planta":
    print("Quantidade de pokemons de planta:",len(planta))
    for i in planta:
        print("Nome:", i)
elif escolha.lower() == "água":
    print("Quantidade de pokemons de água:",len(água))
    for j in água:
        print("Nome:", j)
elif escolha.lower() == "fogo":
    print("Quantidade de pokemons de fogo:",len(fogo))
    for k in fogo:
        print("Nome:", k)
elif escolha.lower() == "elétrico":
    print("Quantidade de pokemons elétricos:",len(elétrico))
    for h in elétrico:
        print("Nome:", h)
else:
    print("Escolha um dos tipos citados acima!")