#RM99880 - Gabriel Machado Carrara Pimentel

print("Digite um ditado popular:")
ditado = input()
conteudo = 'conteudo.txt'

arquivo = open(conteudo, "w", encoding="utf-8")
arquivo.write(ditado)
arquivo.close
print(f"ditado salvo em {conteudo}")

print("Digite mais um ditado:")
novoDit = input()
conteudo = 'conteudo.txt'

arquivo = open(conteudo, "a", encoding='utf-8')
arquivo.write("\n" + novoDit)
arquivo.close
print(f"ditado adicionado a '{conteudo}'")

arquivo = open(conteudo, "r", encoding='utf-8')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()