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
nomes = [input("Digite o nome do primeiro jogador:"),
         input("Digite o nome do segundo jogador:"),
         input("Digite o nome do terceiro jogador:")]

#Exibindo a dica e o painel de palavras
print("\nDica: Programação")
painel1 = []
for i in range(len(palavra1)):
    painel1.append("_ ")
painel2 = []
for i in range(len(palavra2)):
    painel2.append("_ ")
painel3 = []
for i in range(len(palavra1)):
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
    if sorteioRoda != 'PASSA_A_VEZ' and sorteioRoda != 'PERDEU_TUDO':
        ponto_roda = int(sorteioRoda)
    
    #Verificando opções da roda
    if sorteioRoda == "PASSA_A_VEZ":
        print(f"\nJogador: {nomes[jogador_atual].upper()}. PASSOU A VEZ!")
        jogador_atual += 1
    elif sorteioRoda == "PERDEU_TUDO":
        print(f"\nJogador: {nomes[jogador_atual].upper()}. PERDEU TUDO!")
        pontos[jogador_atual] = 0
        jogador_atual += 1
    else:
        print()