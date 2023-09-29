dicionario = {
    "montadora" : "Ford",
    "modelo" : "Mustang",
    "ano" : 1964,
    "ano" : 2000
}

print(dicionario)
print(dicionario["modelo"])
print(dicionario.get("montadora"))
print(len(dicionario))
print(dicionario.keys())
print(dicionario.values())

novoDicionario = dict(montadora = "Audi",
                      modelo = "Malibu",
                      ano = 2005)

print(novoDicionario)
print(novoDicionario.get("montadora"))