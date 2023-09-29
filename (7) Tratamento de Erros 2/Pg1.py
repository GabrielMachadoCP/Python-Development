import re
erro = ""
try:
    print("Digite seu nome:")
    nome = input()
    if re.search("\d", nome):
        erro = "nomes não podem conter números"
        raise ValueError
    print("Digite seu telefone")
    tel = input()
    if not re.search("\d{10,11}", tel) or len(tel) > 11:
        erro = "O telefone deve conter 11 ou 10 dígitos"
        raise ValueError
    if len(tel) == 10:
        tel = "(" + tel[0:2] + ")" + tel[2:6] + "-" + tel[6:]
    else:
        tel = "(" + tel[0:2] + ")" + tel[2:7] + "-" + tel[7:]
    print(f"Nome: {nome}\tTelefone: {tel}")
except ValueError:
    print(erro)
finally:
    print("Fim de programa")