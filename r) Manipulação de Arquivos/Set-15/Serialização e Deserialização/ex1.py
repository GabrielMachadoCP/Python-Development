#criando arquivo JSON

import json
usuarios = {
    "astro":{"nome" : "Astrogildo", "login" : "astro", "senha" : "123"},
    "beri":{"nome" : "Berisvaldo", "login" : "beri", "senha" : "456"}
}
try:
    with open('d:/usuarios.json', 'w', encoding="utf-8") as f:
        json.dump(usuarios, f)

except FileNotFoundError:
    print("Caminho inexistente")    