#Gabriel Machado Carrara Pimentel 
#RM 99880

numeros = {0}
print("Digite um tipo numérico entre Real ou inteiro:")
tipo = input().lower()

numeros.discard(0)

if tipo == "real":
    while len(numeros) <= 9:
        print("Digite um numero real:")
        numeros.add(float(input()))       
elif tipo == "inteiro":
    while len(numeros) <= 9:
        print("Digite um numero inteiro:")
        numeros.add(int(input()))
else:
    print("Escolha o tipo numérico Real ou Inteiro!")

n1,n2,n3,n4,n5,n6,n7,n8,n9,n10 = numeros
if n1>n2 and n1>n3 and n1>n4 and n1>n5 and n1>n6 and n1>n7 and n1>n8 and n1>n9 and n1>n10:
    maiorValor = n1
elif n2>n1 and n2>n3 and n2>n4 and n2>n5 and n2>n6 and n2>n7 and n2>n8 and n2>n9 and n2>n10:
    maiorValor = n2
elif n3>n1 and n3>n2 and n3>n4 and n3>n5 and n3>n6 and n3>n7 and n3>n8 and n3>n9 and n3>n10:
    maiorValor = n3
elif n4>n1 and n4>n3 and n4>n2 and n4>n5 and n4>n6 and n4>n7 and n4>n8 and n4>n9 and n4>n10:
    maiorValor = n4
elif n5>n1 and n5>n3 and n5>n4 and n5>n2 and n5>n6 and n5>n7 and n5>n8 and n5>n9 and n5>n10:
    maiorValor = n5
elif n6>n1 and n6>n3 and n6>n4 and n6>n5 and n6>n2 and n6>n7 and n6>n8 and n6>n9 and n6>n10:
    maiorValor = n6
elif n7>n1 and n7>n3 and n7>n4 and n7>n5 and n7>n6 and n7>n2 and n7>n8 and n7>n9 and n7>n10:
    maiorValor = n7
elif n8>n1 and n8>n3 and n8>n4 and n8>n5 and n8>n6 and n8>n7 and n8>n2 and n8>n9 and n8>n10:
    maiorValor = n8
elif n9>n1 and n9>n3 and n9>n4 and n9>n5 and n9>n6 and n9>n7 and n9>n8 and n9>n2 and n9>n10:
    maiorValor = n9
else:
    maiorValor = n10

# A função max resolveria o problema de encontrar o maior valor do set
# maiorValor = max(numeros)

#Outro jeito de solucionar seria:
# for i in numeros:
#     if i > maiorValor:
#         maiorValor = i

print(f"O tipo numérico escolhido foi o {tipo}.\nO maior número identificado dentro do set foi {maiorValor}.\nTamanho do set: {len(numeros)}.\nOs valores do set são:")
for i in numeros:
    print(i)