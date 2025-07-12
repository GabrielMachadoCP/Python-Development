# RM 99880 - Gabriel Machado Carrara Pimentel
try:
    cadastrar = "sim"
    while cadastrar == "sim":
        print("Digite seu nome:")
        nome = input()
        print("Digite seu login:")
        login = input()
        print("Digite sua senha:")
        senha = input()

        conteudo = f'd:/{login}.txt'

        f = open(conteudo, "w", encoding='utf-8')
        f.write(f"{nome}\n{login}\n{senha}")
        f.close()

        f = open(conteudo, "r", encoding='utf-8')
        print(f.read())
        f.close()

        print()
        print("Deseja fazer um novo cadastro?")
        cadastrar = input().lower()
except FileNotFoundError:
    print("Arquivo não existe!")