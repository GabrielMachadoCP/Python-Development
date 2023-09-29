#RM99880 - Gabriel Machado Carrara Pimentel

print("Digite um ditado popular:")
ditado = input()
conteudo = 'conteudo.txt'

# Armazenando o conteúdo ao arquivo conteudo.txt
arquivo = open(conteudo, "w", encoding="utf-8")
arquivo.write(ditado)
arquivo.close
print()
print(f"O ditado foi salvo em {conteudo}")

arquivo = open(conteudo, "r", encoding='utf-8')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()