# Gabriel Machado Carrara Pimentel
# Rm 99880
import csv

catalogo = []
continuar = 'sim'
while continuar == 'sim':
    titulo = input("Digite o titulo do filme:")
    genero = input("Digite o gênero do filme:") 
    duracao = input("Digite a duração do filme:") 
    clas = input("Digite a classificação indicativa do filme:") 
    diret = input("Digite o diretor do filme:")         
    filmes = [titulo, genero,duracao,clas,diret]
    catalogo.append(filmes)
    print("Deseja inserir mais um filme ao catálogo?")
    continuar = input()
with open('d:/filmes.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Título', 'Gênero', 'Duração', 'Classificação Inidicativa', 'Diretor'])
    writer.writerows(catalogo)