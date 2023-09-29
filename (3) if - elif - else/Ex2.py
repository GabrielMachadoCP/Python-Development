print("Digite sua idade:")
idade = int(input())
if idade >= 18:
    print("Você é obrigado a votar!")
elif idade < 16:
    print("Você não pode votar!")
else:
    print("Você pode votar se quiser.")