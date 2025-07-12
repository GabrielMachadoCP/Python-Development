# Gabriel Machado Carrara Pimentel
# RM 99880

# Sorteando a jogada do computador
def jogada_computador(opcoes):
    import random
    return random.choice(opcoes)


# Verificando o vencedor da rodada
def verifica(jogador, pc, ptojogador, ptopc):
    if (jogador == "PAPEL") and (pc == "TESOURA"):
        ptopc += 1
        print(f"Derrota! \nPontuação:\nJogador: {ptojogador}\tPC: {ptopc}")
    elif (jogador == "TESOURA") and (pc == "PEDRA"):
        ptopc += 1
        print(f"Derrota! \nPontuação:\nJogador: {ptojogador}\tPC: {ptopc}")
    elif (jogador == "PEDRA") and (pc == "PAPEL"):
        ptopc += 1
        print(f"Derrota! \nPontuação:\nJogador: {ptojogador}\tPC: {ptopc}")
    elif (jogador == pc):
        print(f"Empate!\nAmbos jogaram {pc}")
    else:
        ptojogador += 1
        print(f"Vitória!\nPontuação:\nJogador: {ptojogador}\tPC: {ptopc}")
    return ptojogador, ptopc

opcoes = ["PEDRA", "PAPEL", "TESOURA"]