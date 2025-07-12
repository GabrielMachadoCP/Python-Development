# RM 99880 - Gabriel Machado Carrara Pimentel

import json

usuarios = {}
try:
    cadastrar = "sim"
    while cadastrar == "sim":
        print("Digite seu nome:")
        nome = input()
        print("Digite seu login:")
        login = input()
        print("Digite sua senha:")
        senha = input()
        usuarios.update({login : {"nome":nome, "login":login, "senha":senha}})
        conteudo = f'd:/usuarios.json'

        with open(conteudo, "w", encoding='utf-8') as f:
            json.dump(usuarios,f)
        print()
        print("Deseja fazer um novo cadastro?")
        cadastrar = input().lower()
except FileNotFoundError:
    print("Arquivo não existe!")