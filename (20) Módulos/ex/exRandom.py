import random
frutas = [ 'maçã','banana','kiwi']
# Sorteando um numero
sorteia_numero = random.randint(10,50)
print("Numero sorteado: {}".format(sorteia_numero))
#Sorteando uma fruta
sorteiaFruta = random.choice(frutas)
print(sorteiaFruta)