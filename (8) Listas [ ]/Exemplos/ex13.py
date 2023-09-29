frutas = ["maçã", "uva","tomate","morango", "banana"]
copiafrutas = frutas #Está igualando, logo o que acontece em uma lista ocorre na outra
frutas.append("kiwi")
print(frutas)
print(copiafrutas)

#Por isso usa-se a função copy

frutas = ["maçã", "uva","tomate","morango", "banana"]
copiafrutas = frutas.copy()
frutas.append("kiwi")
print(frutas)
print(copiafrutas)

#Podemos usar a função list, que tem a mesma lógica
frutas = ["maçã", "uva","tomate","morango", "banana"]
copiafrutas = list(frutas)
frutas.append("kiwi")
print(frutas)
print(copiafrutas)