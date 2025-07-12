# Ana zerlin       RM 98065
# Bianca Dancs     RM 551645
# Gabriel Pimentel RM 99880
# Hellen Assis     RM 98284

import random
import csv

#Variáveis
num_jogadores = 3
jogadores = []
pontuacoes = []
palavras = [] 
valores = []
letras_palpite = []
letras_restantes = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
letras_palavras = set('ACDGILMNOQRSTUV')
palavras_adivinhadas = []
palavras_chute = []
letras_adivinhadas = set(letras_palpite)
jogador_atual = 0
acabou = False

#Ler as opções da roda do arquivo.txt
with open('d:/valores.txt', 'r') as valores_file:
    for i in range(12):
        linha = valores_file.readline().strip()
        valores.append(linha)

#Ler as palavras do arquivo.csv
with open('d:/palavras.csv', 'r') as palavras_file:
    palavras_csv = csv.reader(palavras_file)
    for row in palavras_csv:
        palavras.append(row[0])
for i in range(num_jogadores):
    nome = input(f"Digite o nome do jogador {i+1}: ")
    jogadores.append(nome)
    pontuacoes.append(0)

#Estrutura de repetição para iniciar o jogo
while acabou == False:
    print()
    print(":"*100)
    print(f"Jogador atual: {jogadores[jogador_atual]}\n")

    #Mostrar o painel com a dica
    print("Dica: PROGRAMAÇÃO")
    for palavra in palavras:
        for letra in palavra:
            if letra in letras_palpite:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print("\n")
    input("Pressione Enter para rodar a roda...")
    valorRoda = random.choice(valores)
    print(f"Opção da roda: {valorRoda}\n")
    
    #Condições para a roda
    if valorRoda == 'PERDE A VEZ':
        print("Você passa a vez!\n")

    elif valorRoda == 'PERDEU TUDO':
        print("Você perdeu todos os seus pontos!")
        pontuacoes[jogador_atual] = 0
        
    else:
        #Verificar se o jogador pode chutar a palavra
        if len(letras_palavras) <= 3:
            chutar = input("Deseja chutar a palavra? (S/N): ").upper()

            #Escolha de chutar as palavras
            if chutar == 'S':
                palavra_chute1 = input("Digite a primeira palavra: ").upper()
                palavras_chute.append(palavra_chute1)

                #Acertando a palavra DICIONARIO
                if palavra_chute1 in palavras:
                    print(f"Parabéns! A palavra '{palavra_chute1}' está correta.")
                    palavra_chute2 = input("Qual a próxima palavra: ").upper()

                    #Acertando a palavra ALGORITMO
                    if palavra_chute2 in palavras:
                        print(f"Parabéns! A palavra '{palavra_chute2}' está correta.")
                        palavras_chute.append(palavra_chute2)
                        palavra_chute3 = input("Qual a última palavra: ").upper()

                        #Acertando a palavra ARQUIVOS
                        if palavra_chute3 in palavras:
                            palavras_chute.append(palavra_chute3)
                            pontuacoes[jogador_atual] += int(valorRoda) * len(palavras_chute)
                            print(f"Parabéns! A palavra '{palavra_chute3}' está correta.")
                            acabou = True
                        else:
                            print("Chute de palavra incorreto. Você perdeu todos os pontos!")
                            pontuacoes[jogador_atual] = 0
                    else:
                        print("Chute de palavra incorreto. Você perdeu todos os pontos!")
                        pontuacoes[jogador_atual] = 0
                else:
                    print("Chute de palavra incorreto. Você perdeu todos os pontos!")
                    pontuacoes[jogador_atual] = 0

            #Escolha de não chutar as palavras
            else:
                print(f"Letras chutadas: {letras_palpite}")
                letra = input("Escolha uma letra: ").upper()
                if letra in letras_restantes:
                    letras_restantes.remove(letra)
                    letras_palpite.append(letra)
                    pontos_rodada = 0
                    for palavra in palavras:
                        if letra in palavra:
                            pontos_rodada += int(valorRoda) * palavra.count(letra)
                    if pontos_rodada > 0:
                        pontuacoes[jogador_atual] += pontos_rodada
                        print(f"Parabéns! A letra '{letra}' está na palavra(s).")
                        print(f"{jogadores[jogador_atual]} ganhou {pontos_rodada} pontos!\n")
                        print(":"*30)
                    else:
                        print(f"A letra {letra} já foi escolhida ou não está na palavra.\n")

        #Jogo funcionando normalmente até faltarem 3 letras
        else:
            print(f"Letras chutadas: {letras_palpite}")
            letra = input("Escolha uma letra: ").upper()
            if letra in letras_restantes:
                letras_restantes.remove(letra)
                letras_palpite.append(letra)
                pontos_rodada = 0
                for palavra in palavras:
                    if letra in palavra:
                        pontos_rodada += int(valorRoda) * palavra.count(letra)
                if pontos_rodada > 0:
                    pontuacoes[jogador_atual] += pontos_rodada
                    print(f"Parabéns! A letra '{letra}' está na palavra(s).")
                    print(f"{jogadores[jogador_atual]} ganhou {pontos_rodada} pontos!\n")
                    print(":"*30)
                else:
                    print(f"A letra {letra} já foi escolhida ou não está na palavra.\n")
        if letra in letras_palavras:
            letras_palavras.remove(letra)
        if letras_adivinhadas == letras_palavras:
            print("Você adivinhou todas as letras das palavras!")
            palavras_adivinhadas = palavras
            letras_palpite = []
        print("Pontuações:")
        for i in range(num_jogadores):
            print(f"{jogadores[i]}: {pontuacoes[i]} pontos")
        if set(palavras_adivinhadas) == set(palavras) or set(palavras_chute) == set(palavras):
            acabou = True
    jogador_atual = (jogador_atual + 1) % num_jogadores

#Fim do jogo
vencedores = []
max_pontuacao = max(pontuacoes)
print("\nFim do jogo!")
print("Palavras adivinhadas:")
for palavra in palavras_adivinhadas:
    print(palavra)
for i in range(num_jogadores):
    if pontuacoes[i] == max_pontuacao:
        vencedores.append(jogadores[i])
for i in vencedores:
    print(f"O vencedor foi {i} com {max_pontuacao} pontos.")