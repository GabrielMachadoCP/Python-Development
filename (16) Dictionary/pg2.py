pokemons = {
    "pokemon1" : {"nome":"bulbassauro", "tipo":"planta"},
    "pokemon2" : {"nome":"gloom", "tipo":"planta"},
    "pokemon3" : {"nome":"squirtle", "tipo":"água"},
    "pokemon4" : {"nome":"blastoise", "tipo":"água"},
    "pokemon5" : {"nome":"wartortle", "tipo":"água"},
    "pokemon6" : {"nome":"charizard", "tipo":"fogo"},
    "pokemon7" : {"nome":"charmander", "tipo":"fogo"},
    "pokemon8" : {"nome":"pikachu", "tipo":"elétrico"},
    "pokemon9" : {"nome":"luxio", "tipo":"elétrico"},
    "pokemon10": {"nome":"Elekid", "tipo":"elétrico"}
}

print("Escolha um tipo de pokemon:")
escolha = input().lower()

nomesP = pokemons["pokemon1"]['nome'], pokemons["pokemon2"]['nome']
nomesF = pokemons["pokemon6"]['nome'], pokemons["pokemon7"]['nome']
nomesA = pokemons["pokemon3"]['nome'], pokemons["pokemon4"]['nome'], pokemons["pokemon5"]['nome']
nomesE = pokemons["pokemon8"]['nome'], pokemons["pokemon9"]['nome'], pokemons["pokemon10"]['nome']

qntdP = len(nomesP)
qntdF = len(nomesF)
qntdA = len(nomesA)
qntdE = len(nomesE)

if escolha == "planta":
    print(f"Existem {qntdP} pokemons do tipo {escolha} são estes: {nomesP}")
elif escolha == "fogo":
    print(f"Existem {qntdF} pokemons do tipo {escolha} são estes: {nomesF}")
elif escolha == "água":
    print(f"Existem {qntdA} pokemons do tipo {escolha} são estes: {nomesA}")
elif escolha == "elétrico":
    print(f"Existem {qntdE} pokemons do tipo {escolha} são estes: {nomesE}")
else:
    print("Escolha um dos tipos citados acima!")