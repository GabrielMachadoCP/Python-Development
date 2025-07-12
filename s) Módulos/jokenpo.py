# Gabriel Machado Carrara Pimentel
# RM 99880

import funcoesJogo

continuar = "SIM"
ptojogador = ptopc = 0

while continuar == "SIM":
    print("JOKENPÔ")
    print(":" * 30)
    print("PEDRA")
    print("PAPEL")
    print("TESOURA")
    jogador = input("Escolha sua Jogada: ").upper()
    pc = funcoesJogo.jogada_computador(funcoesJogo.opcoes)
    print(f"Jogada do computador: {pc}")
    resultado = funcoesJogo.verifica(jogador, pc, ptojogador, ptopc)
    ptojogador, ptopc = resultado  

    print("Deseja jogar novamente?")
    continuar = input().upper()
print()
print(":" * 30)
print(f"Placar final: \nVocê: {ptojogador}\nPC: {ptopc}")