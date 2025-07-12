print("Digite o seu salário:")
salario = float(input())
print("Digite o anos de trabalho:")
tempo = float(input())
if tempo < 5:
    print("Seu novo salário é:", salario * 0.05 + salario)
elif tempo >= 5 and tempo <= 10:
    print("Seu novo salário é:", salario * 0.10 + salario)
elif tempo >= 11 and tempo <= 15:
    print("Seu novo salário é:", salario * 0.15 + salario)
else:
    print("Seu novo salário é:", salario * 0.20 + salario)