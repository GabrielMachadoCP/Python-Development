dicionario = {
    "montadora" : "Ford",
    "modelo" : "Mustang",
    "ano" : 2000
}

dicionario["ano"] = 1964
print(dicionario)

dicionario.update({"montadora" : "VW", "modelo" : "Ferrari", "cor":"vermelho"})
print(dicionario)

dicionario.pop("montadora")

dicionario.popitem()
print(dicionario)