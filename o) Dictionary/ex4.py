#Nested Dictionary (Dicionário Aninhado)
clientes = {
    "cliente1":{"nome":"Astrogildo","ano":1998},
    "cliente2":{"nome":"Berisvaldo","ano":2003},
    "cliente3":{"nome":"Gumercindo","ano":2010},
}

print(clientes)
print()

print(clientes.get("cliente1").get("nome"))
print(clientes["cliente2"]["ano"])
