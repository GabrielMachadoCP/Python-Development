cell = {
    "ki": 7400,
    "técnicas":6000,
    "velocidade":66,
    "transformações":3
}

print("Digite uma nova característica para a carta Cell:")
caract = input().lower()
print(f"Qual o valor do(a) {caract}")
valor = int(input())

cell.update({caract:valor})
print("Escolha uma das características:")
for i in cell.keys():
        print(i)
escolha = input().lower()
if escolha == "ki":
    print(f"A característica escolhida foi {escolha} e o valor é {cell['ki']}")
elif escolha == "técnicas":
    print(f"A característica escolhida foi {escolha} e o valor é {cell['técnicas']}")
elif escolha == "velocidade":
    print(f"A característica escolhida foi {escolha} e o valor é {cell['velocidade']}")
elif escolha == "transformações":
    print(f"A característica escolhida foi {escolha} e o valor é {cell['transformações']}")
elif escolha == caract:
    print(f"A característica escolhida foi {escolha} e o valor é {cell[caract]}")
else:
     print("A característica digitada não existe!")