senha = ""
frase = "Acesso concedido!"
cont = 0

while senha != "p4ssw0rd":
    print("Digite sua senha:")
    senha = input()
    cont += 1
    if cont >= 5:
        frase = "Conta bloqueada"
        break
print(frase)