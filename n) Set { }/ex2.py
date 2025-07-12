#Para navegar nos elementos do set não usamos for in range por não ter indice
#Usamos portanto, o for-each

frutas = {"uva", "maçã", "tomate"}
for i in frutas:
    print(i)

#Para verificar  aexistência de certo valor:
frutas = {"uva", "maçã", "tomate"}
print("banana" in frutas)