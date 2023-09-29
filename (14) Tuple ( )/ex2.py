frutas = ("maçã", "uva", "tomate")
(a,b,c) = frutas
print(f"{a}\n{b}\n{c}")
(x,*y) = frutas
frutas = ("maçã", "uva", "tomate", "uva", "kiwi")
(k, *w, z) = frutas
print(f"{k}\n{w}\n{z}")