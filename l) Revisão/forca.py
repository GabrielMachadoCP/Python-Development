import random


palavra = ["ESQUISITO"]#,"EXCELENTE", "MISERÁVEL"]

sorteio = random.choice(palavra)
if sorteio == "ESQUISITO":
    dica = "Aquilo que é diferente do normal"
elif sorteio == "EXCELENTE":
    dica = "Aquilo que é melhor do que ótimo" 
elif sorteio == "MISERÁVEL":
    dica = "Aquele que está em péssimo estado" 


print(f"""
Dica: {dica}
            
U==============U
|
|
|
|
|
|
| __  __  __  __  __  __  __  __  __""")



l1 = sorteio[:1]
l2 = sorteio[1:2]
l3 = sorteio[2:3]
l4 = sorteio[3:4]
l5 = sorteio[4:5]
l6 = sorteio[5:6]
l7 = sorteio[6:7]
l8 = sorteio[7:8]
l9 = sorteio[8:9]
letras = [l1,l2,l3,l4,l5,l6,l7,l8,l9]
print(letras)

print("Digite sua tentativa:")
tentativa1 = input()
if tentativa1.upper() == l1 or tentativa1.upper() == l2 or tentativa1.upper() == l3 or tentativa1.upper() == l4 or tentativa1.upper() == l5 or tentativa1.upper() == l6 or tentativa1.upper() == l7 or tentativa1.upper() ==l8 or tentativa1.upper() == l9:
    print("acertou")
else:
    print("errou")

print("Digite sua tentativa:")
tentativa2 = input()
if tentativa2.upper() == l1 or tentativa2.upper() == l2 or tentativa2.upper() == l3 or tentativa2.upper() == l4 or tentativa2.upper() == l5 or tentativa2.upper() == l6 or tentativa2.upper() == l7 or tentativa2.upper() ==l8 or tentativa2.upper() == l9:
    print("acertou")
else:
    print("errou")