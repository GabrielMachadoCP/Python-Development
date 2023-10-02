
#Sorteando a jogada do computador
def jogada_computador(opcoes):
    import random
    return random.choice(opcoes)


def verifica(jogador, pc): 
    if (jogador == "PAPEL") and (pc == "TESOURA"):
        ptopc += 1
        return vencedor == pc
    elif (jogador == "TESOURA") and (pc == "PEDRA"):
        ptopc += 1
        return vencedor == pc
    elif (jogador == "PEDRA") and (pc == "PAPEL"):
        ptopc += 1
        return vencedor == pc
    elif (jogador == pc):
        return print(f"Empate!\nAmbos jogaram {pc}") 
    else:
        ptojogador += 1
        return vencedor == jogador

vencedor = ''
opcoes = ["PEDRA", "PAPEL", "TESOURA"]