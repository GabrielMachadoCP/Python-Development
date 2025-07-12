# RM 99880 - Gabriel Machado Carrara Pimentel
print("Digite o seu login:")
loginUser = input()
try:
    #Verificando a existência do login
    arquivo = f'd:/{loginUser}.txt'
    f = open(arquivo, "r", encoding='utf-8')
    nome = f.readline()
    login = f.readline()
    senha = f.readline()
    #Verificando a senha
    print("Digite a sua senha:")
    senhaUser = input()
    while senhaUser != senha:
        print("Senha incorreta, tente novamente:")
        senhaUser = input()
    # Exibindo o acesso permitido
    print(f"Seja bem-vindo!\n")
    print(":" * 80)
    print(f"\nInformações da conta:\n")
    print(f"Nome do usuário: {nome}")
    print(f"Login do usuário: {login}")
    print(f"Senha do usuário: {senha}")
except FileNotFoundError:
    print("O usuário digitado não está cadastrado!")