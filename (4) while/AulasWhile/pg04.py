import random 
escolha = "sim"
ptojogador = ptopc = 0

while escolha == "sim":
    print("Escolha: \npedra\npapel\ntesoura")
    jogador = input()
    sorteio = random.randint(1,3)
    if sorteio == 1:
        pc = "pedra"
    else:
        if sorteio == 2:
            pc = "papel"
        else:
            pc = "tesoura"
    d1 = (jogador == "papel") and (pc == "tesoura")
    d2 = (jogador == "tesoura") and (pc == "pedra")
    d3 = (jogador == "pedra") and (pc == "papel")
    df = d1 or d2 or d3

    if escolha == pc:
        print(f"Empate! \nVocê escolheu: {jogador} \nO computador escolheu: {pc}")
    elif df:
        print(f"Derrota! \nVocê escolheu: {jogador} \nO computador escolheu: {pc}")
        ptopc += 1
    else:
        print(f"Vitória!\nVocê escolheu: {jogador} \nO computador escolheu: {pc}")
        ptojogador += 1
    print("Deseja continuar? Sim ou Não")
    escolha = input().lower()
print(f"Placar final: \n Você {ptojogador}\n Pc {ptopc}")