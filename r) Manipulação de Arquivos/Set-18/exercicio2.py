# Gabriel Machado Carrara Pimentel
# RM 99880

import csv

# Lendo o arquivo csv fora do loop
print("O que deseja fazer:\nProcurar por:\tTítulo (1)\tGênero (2)\tDiretor (3)\tSair (4)")
escolha = int(input())
while escolha != 4:
    if escolha == 1:
        print("Digite o título que procura:")
        titulo = input()
        with open('d:/filmes.csv', 'r', encoding='utf-8') as f:
            filmes = csv.reader(f)
            next(filmes)
            for i in filmes:
                if titulo in i:
                    print(i)
    elif escolha == 2:
        print("Digite o gênero que procura:")
        genero = input()
        with open('d:/filmes.csv', 'r', encoding='utf-8') as f:
            filmes = csv.reader(f)
            next(filmes)
            for i in filmes:
                if genero in i:
                    print(i)
    elif escolha == 3:
        print("Digite o diretor que procura:")
        diretor = input()
        with open('d:/filmes.csv', 'r', encoding='utf-8') as f:
            filmes = csv.reader(f)
            next(filmes)
            for i in filmes:
                if diretor in i:
                    print(i)
    else:
        print("Escolha entre 1, 2, 3 ou 4")
    
    print("O que deseja fazer:\nProcurar por:\tTítulo (1)\tGênero (2)\tDiretor (3)\tSair (4)")
    escolha = int(input())
print("Obrigado por acessar o nosso catálogo de filmes")