def valida1(n1, x):
    soma = digito = resto = 0
    cont = x
    for i in n1:
        soma += i * cont
        cont -= 1
    resto = soma % 11
    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto
        return digito



#Programa Principal
cpfnum = []
cpfval = ""
d1 = 0
d2 = 0
digiuno = digiduo = 0
print("Digite seu cpf (Somente números)")
cpf = input()
for i in range(0,9,1):
    cpfnum.append(int(cpf[i:i+1]))
digiuno = valida1(cpfnum, 10)
cpfnum.append(digiuno)
digiduo = valida1(cpfnum, 11)
cpfnum.append(digiduo)
for i in cpfnum:
    cpfval += str(i)
d1 = (cpf[9:10])
d2 = (cpf[10:11])
if digiuno == d1 and digiduo == d2:
    print(f"O cpf de número {cpf} é válido")
else:
    print(f"O cpf de número {cpf} é inválido")
    print(f"O correto seria {cpfval}")
