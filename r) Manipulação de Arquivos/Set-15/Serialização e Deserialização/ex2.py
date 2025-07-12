#Lendo arquivo JSON

import json
import os
try:
    usuarios = {}
    if os.path.exists('d:/usuarios.json'):
        with open('d:/usuarios.json', 'r', encoding='utf-8') as f:
            usuarios = json.loads(f.read())
        print(usuarios)
except FileNotFoundError:
    print("Arquivo não encontrado")