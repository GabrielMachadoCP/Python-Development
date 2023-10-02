import funcoesJogo

continuar = "SIM"
ptojogador = ptopc = 0

while continuar == "SIM":
    print("JOKENPÔ")
    print(":"*30)
    print("PEDRA")
    print("PAPEL")
    print("TESOURA")
    jogador = input("Escolha sua Jogada: ").upper()
    pc = funcoesJogo.jogada_computador(funcoesJogo.opcoes)
    print(f"Jogada do computador: {pc}")

    funcoesJogo.verifica(jogador, pc)
    if funcoesJogo.vencedor == "Computador":
        print(f"Derrota! \nVocê escolheu: {jogador} \nO computador escolheu: {pc}")
        ptopc += 1
    elif funcoesJogo.vencedor == "Jogador":
        print(f"Vitória!\nVocê escolheu: {jogador} \nO computador escolheu: {pc}")
        ptojogador += 1
    print("Deseja jogar novamente?")
    continuar = input().upper()
print(f"Placar final: \n Você {ptojogador}\n Pc {ptopc}")