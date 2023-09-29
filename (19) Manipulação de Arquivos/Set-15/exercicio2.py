# RM 99880 - Gabriel Machado Carrara Pimentel

import json
import os

print("Digite seu login")
loginUser = input()
try :
    if os.path.exists('d:/usuarios.json') :
        with open('d:/usuarios.json', 'r', encoding="utf-8") as f :
            usuarios = json.loads(f.read())

    if loginUser in usuarios.keys():
        print("Digite sua senha")
        senhaUser = input()
        while usuarios[loginUser]["senha"] != senhaUser :
            print("Senha inválida, tente novamente")
            senhaUser = input()
        print(":" * 100)
        print("Seja bem-vindo!\n")
        print("Nome: ", usuarios[loginUser]["nome"])
        print("Login: ", usuarios[loginUser]["login"])
        print("Senha: ", usuarios[loginUser]["senha"])
    else:
        print("Usuário não cadastrado e/ou login incorreto")
except FileNotFoundError:
    print("Arquivo inexistente")