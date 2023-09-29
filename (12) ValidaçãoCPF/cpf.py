import re

def verificar(cpf):
    if not re.search("\d{3}.\d{3}.\d{3}-\d{2}", cpf) or len(cpf) > 14:
        print("O cpf precisa conter 11 dígitos, contendo também os pontos e traço\nExemplo:\t000.000.000-00")

pesosDig1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
pesosDig2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
listaCpf = []
resultado = []
resultado2 = []
soma1 = 0
soma2 = 0

print("Digite o seu cpf:")
cpf = input() 
verificar(cpf)

d1 = int(cpf[:1])
d2 = int(cpf[1:2])
d3 = int(cpf[2:3])
d4 = int(cpf[4:5])
d5 = int(cpf[5:6])
d6 = int(cpf[6:7])
d7 = int(cpf[8:9])
d8 = int(cpf[9:10])
d9 = int(cpf[10:11])
d10 = int(cpf[12:13])
d11 = int(cpf[13:14])

listaCpf.append(d1)
listaCpf.append(d2)
listaCpf.append(d3)
listaCpf.append(d4)
listaCpf.append(d5)
listaCpf.append(d6)
listaCpf.append(d7)
listaCpf.append(d8)
listaCpf.append(d9)
listaCpf.append(d10)
listaCpf.append(d11)

copiaListaCpf = listaCpf.copy()

mult1 = (pesosDig1[0]) * (copiaListaCpf[0])
mult2 = (pesosDig1[1]) * (copiaListaCpf[1])
mult3 = (pesosDig1[2]) * (copiaListaCpf[2])
mult4 = (pesosDig1[3]) * (copiaListaCpf[3])
mult5 = (pesosDig1[4]) * (copiaListaCpf[4])
mult6 = (pesosDig1[5]) * (copiaListaCpf[5])
mult7 = (pesosDig1[6]) * (copiaListaCpf[6])
mult8 = (pesosDig1[7]) * (copiaListaCpf[7])
mult9 = (pesosDig1[8]) * (copiaListaCpf[8])

resultado.append(mult1)
resultado.append(mult2)
resultado.append(mult3)
resultado.append(mult4)
resultado.append(mult5)
resultado.append(mult6)
resultado.append(mult7)
resultado.append(mult8)
resultado.append(mult9)

copiaListaCpf.pop(-2)
copiaListaCpf.pop(-1)

for i in resultado:
    soma1 += i

resto1 = soma1 % 11

if resto1 > 2:
    digito1 = 11 - resto1
else:
    digito1 = 0

copiaListaCpf.append(digito1)

mul1 = (pesosDig2[0]) * (copiaListaCpf[0])
mul2 = (pesosDig2[1]) * (copiaListaCpf[1])
mul3 = (pesosDig2[2]) * (copiaListaCpf[2])
mul4 = (pesosDig2[3]) * (copiaListaCpf[3])
mul5 = (pesosDig2[4]) * (copiaListaCpf[4])
mul6 = (pesosDig2[5]) * (copiaListaCpf[5])
mul7 = (pesosDig2[6]) * (copiaListaCpf[6])
mul8 = (pesosDig2[7]) * (copiaListaCpf[7])
mul9 = (pesosDig2[8]) * (copiaListaCpf[8])
mul10 = (pesosDig2[9]) * (copiaListaCpf[9])

resultado2.append(mul1)
resultado2.append(mul2)
resultado2.append(mul3)
resultado2.append(mul4)
resultado2.append(mul5)
resultado2.append(mul6)
resultado2.append(mul7)
resultado2.append(mul8)
resultado2.append(mul9)
resultado2.append(mul10)

for i in resultado2:
    soma2 += i

resto2 = soma2 % 11

if resto2 > 2:
    digito2 = 11 - resto2
else:
    digito2 = 0

copiaListaCpf.append(digito2)

if listaCpf == copiaListaCpf:
    print("\nO CPF digitado é válido!\n")
else:
    print("\nCPF inválido!\n")
    print("O CPF digitado foi: ", cpf)
    print("O CPF verificado corretamente é: ", cpf[0:11] + "-" + str(digito1) + str(digito2))