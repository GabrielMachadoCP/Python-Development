# add() - adiciona novos valore
#update() - adiciona um conjunto de valores

#remove() - se não existir ocasiona erro
#discard() - se não existir não ocasiona erro
#pop() - remove aleatoriamente
#clear() - esvazia o set
#del() - Elimina o set completamente

frutas = {"uva", "maçã"}
frutas.add("tomate")
print(frutas)

frutas2 = {"pêra", "kiwi"}
frutas3 = {"amora", "cajú"}
frutas.update(frutas2)
frutas.update(frutas3)
print(frutas)

frutas.remove("tomate")
frutas.discard("tangerina")
frutas.pop()
print(frutas)

frutas.clear()
print(frutas)

del(frutas)
# print(frutas) ==> ocasiona erro por ter sido deletado