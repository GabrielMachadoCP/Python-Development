import re
erro = ""

try:
    print("digite seu nome:")
    nome = input()
    if re.search("\d", nome):
        erro = "Nomes não podem conter dígitos"
        raise ValueError
    print("Digite a placa:")
    placa = input()
    if not re.search("[A-Z]{3}\d{1}[A-Z]{1}\d{2}", placa) or len(placa) > 7:
        erro = "não é uma placa da mercosul Válida"
        raise ValueError
    mercosul = placa[0:3] + " " + placa[3:]
    print(f"Nome: {nome}\tPlaca Mercosul: {mercosul}")
except ValueError:
    print(erro)
finally:
    print("Fim do Programa!")