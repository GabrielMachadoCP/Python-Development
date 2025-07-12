import re
erro = ""
try:
    print("Digite seu nome:")
    nome = input()
    if re.search("\d", nome):
        erro = "nomes não podem conter números"
        raise ValueError
    print("Digite seu CEP (Somente números)")
    cep = input()
    if not re.search("\d{5}-\d{3}", cep) or len(cep) > 9:
        erro = "CEP deve conter 8 dígitos"
        raise ValueError
    print(f"Nome{nome}\nCEP: {cep}")
except ValueError:
    print(erro)
finally:
    print("Fim de programa")