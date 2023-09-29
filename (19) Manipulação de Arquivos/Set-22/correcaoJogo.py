import csv
import random

#Lendo o arquivo de texto com os valores da roda
with open('d:/valores.txt', 'r') as arquivo:
    roda = arquivo.read().split()

palavras = []

#Lendo o arquivo csv com as três palavras
with open('d:/palavras.csv', 'r') as file:
    arquivo_csv = csv.reader(file)
    for item in arquivo_csv:
        palavras.append(item)

#Palavra 1
palavra = palavras[0][0]
palavra1 = []
for i in range(len(palavra)):
    palavra1.append(palavra[i])

#Palavra 2
palavra = palavras[0][1]
palavra2 = []
for i in range(len(palavra)):
    palavra2.append(palavra[i])

#Palavra 3
palavra = palavras[0][2]
palavra3 = []
for i in range(len(palavra)):
    palavra3.append(palavra[i])

#Armazenando os nomes dos jogadores
nomes = [input("Digite o nome do primeiro jogador: "),
         input("Digite o nome do segundo jogador: "),
         input("Digite o nome do terceiro jogador: ")]

#Exibindo a dica e o painel de palavras
print("\nDica: Programação")
painel1 = []
for i in range(len(palavra1)):
    painel1.append("_ ")
painel2 = []
for i in range(len(palavra2)):
    painel2.append("_ ")
painel3 = []
for i in range(len(palavra3)):
    painel3.append("_ ")
print(*painel1)
print(*painel2)
print(*painel3)

#List da pontuação e variavel do jogador atual
pontos = [0, 0, 0]
jogador_atual = 0

#Armazenando o total de letras do jogo
total_letras = len(palavra1) + len(palavra2) + len(palavra3)
acertos = 0
ponto_roda = 0
palpites = {""}
palpites.pop()

#Jogando enquanto total de acertos menor que do que total de letras
while (acertos < total_letras):
    input(f"\nJogador: {nomes[jogador_atual].upper()}. Pressione Enter para rodar a roda...")
    sorteioRoda = random.choice(roda)
    print(f"\nA roda parou em: {sorteioRoda}")

    #Convertendo os valores da roda (se for numero)
    if sorteioRoda != 'PERDE_A_VEZ' and sorteioRoda != 'PERDEU_TUDO':
        ponto_roda = int(sorteioRoda)
    
    #Verificando opções da roda
    if sorteioRoda == "PERDE_A_VEZ":
        print(f"\nJogador: {nomes[jogador_atual].upper()}. PASSOU A VEZ!")
        jogador_atual += 1
    elif sorteioRoda == "PERDEU_TUDO":
        print(f"\nJogador: {nomes[jogador_atual].upper()}. PERDEU TUDO!")
        pontos[jogador_atual] = 0
        jogador_atual += 1
    else:
        #Verificando se faltam 3 letras ou menos
        if acertos < total_letras - 3:
            #Pedindo para digitar uma letra
            letra = input("Digite uma letra:").upper()
            #Verificando se a letra já foi um palpite utilizado
            if letra in palpites:
                print("\nEssa letra já foi utilizada!")
                jogador_atual += 1
            else:
                palpites.add(letra)
                #Verificando se a letra está contida nas palavras
                if letra in palavra1 or letra in palavra2 or letra in palavra3:
                    #Substituindo a letra correta  atualizando acertos
                    for i in range(len(palavra1)):
                        if letra == palavra1[i]:
                            painel1[i] = letra
                            acertos += 1
                            pontos[jogador_atual] += ponto_roda
                    for i in range(len(palavra2)):
                        if letra == palavra2[i]:
                            painel2[i] = letra
                            acertos += 1
                            pontos[jogador_atual] += ponto_roda
                    for i in range(len(palavra3)):
                        if letra == palavra3[i]:
                            painel3[i] = letra
                            acertos += 1
                            pontos[jogador_atual] += ponto_roda
                else:
                    print(f"\nA letra {letra} não está nas palavras!")
                    jogador_atual += 1
        else:
            #Quando faltar 3 letras pedir digitação
            print(f"\nJogador: {nomes[jogador_atual].upper()}. Você já sabe quais são as palavras?")
            print("Gostaria de digitar quais são? (SIM OU NÃO)?")
            escolha = input("Escolha: ").upper()
            if escolha == "SIM":
                print(f"\nJogador: {nomes[jogador_atual].upper()}. Digite quais são as palavras:")
                resposta1 = input("Palavra1: ").upper()
                resposta2 = input("Palavra2: ").upper()
                resposta3 = input("Palavra3: ").upper()
                if resposta1 == palavras[0][0] and resposta2 == palavras[0][1] and resposta3 == palavras[0][2]:
                    painel1 = palavra1
                    painel2 = palavra2
                    painel3 = palavra3
                    pontos[jogador_atual] += ponto_roda * (total_letras - acertos)
                    acertos = total_letras
                else:
                    print("\nQue pena, você errou e PERDEU TUDO!")
                    pontos[jogador_atual] = 0
                    jogador_atual += 1  
            else:
                print("\nNeste caso passamos a vez para o próximo jogador")
                jogador_atual += 1
    #Mostrando o painel e pontuação
    print("\nDica: Programação")
    print(*painel1)
    print(*painel2)
    print(*painel3)
    print("-"*40)
    print("Palpites: ", *palpites)
    print("-"*40)
    print("Pontuação Geral:")
    print(f"Nome: {nomes[0].upper()} : {pontos[0]} pontos")
    print(f"Nome: {nomes[1].upper()} : {pontos[1]} pontos")
    print(f"Nome: {nomes[2].upper()} : {pontos[2]} pontos")
    #Ajustando o jogador atual
    if jogador_atual >= 3:
        jogador_atual = 0
print("Fim de Jogo!")