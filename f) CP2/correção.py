# Gabriel Machado

import random

#Sorteio do funcionário
sorteio = random.randint(1,3)
if sorteio == 1:
    func = "Gabriel"
elif sorteio == 2:
    func = "Bianca"
else:
    func = "Ana"

#Mensagem de Boas Vindas
print(f"Bem-vindo à Vinheria Agnello.\nO funcinário que irá te acompanhar é {func}")

#Requisitando informações do cliente
print("Informe seu nome:")
cliente = input()
print("Informe o CEP da sua residência:")
cep =  input()
print("Informe o ano de seu nascimento:")
anoNasc = int(input())

#Verificando a maioridade
idade = 2023 - anoNasc
if idade < 18:
    print(f"{cliente} não é permitida a venda para menores de 18 anos!")
else:
    #Variáveis para auxiliar nos cálculos
    subtotal = total = 0

    #Preparando a mensagem final
    msgfinal = f"Dados da compra:\nAtendido por: {func}\nCliente: {cliente}\nItens da Compra\t\tValor\t\tQtde\tSubtotal\n"

    #Repetindo a venda de vinhos
    continua = "sim"
    while continua.lower() == "sim":

        #Exibindo opções de vinhos
        print("Escolha um dos vinhos da lista:\n(1)Vinho suave tinto\tR$ 15.00\n(2)Vinho Seco tinto\tR$ 25.00\n(3)Vinho suave branco\tR$ 35.00\n(4)Vinho Seco Branco\tR# 30.00\n(5)Vinho sem álcool\tR$ 40.00\n")

        #Armazenando o vinho escolhido e quantidade
        vinho = int(input())
        print("Em qual quantidade deseja adquirir este vinho?")
        qtde = int(input())
        match vinho:
            case 1:
                subtotal = 15 * qtde
                msgfinal += f"Vinho suave tinto\t R$ 15.00\t{qtde}\tR${subtotal:.2f}\n"
            case 2:
                subtotal = 25 * qtde
                msgfinal += f"Vinho seco tinto\t R$ 25.00\t{qtde}\tR${subtotal:.2f}\n"
            case 3:
                subtotal = 35 * qtde
                msgfinal += f"Vinho suave branco\t R$ 35.00\t{qtde}\tR${subtotal:.2f}\n"
            case 4:
                subtotal = 30 * qtde
                msgfinal += f"Vinho seco branco\t R$ 30.00\t{qtde}\tR${subtotal:.2f}\n"
            case 5:
                subtotal = 40 * qtde
                msgfinal += f"Vinho sem álcool\t R$ 40.00\t{qtde}\tR${subtotal:.2f}\n"
            case _:
                print("Por Favor, escolha uma das opções da lista.")
        
        total += subtotal

        #Continuando ou não a compra
        print("Deseja continuar comprando? (Responda: sim ou não)")
        continua = input()

    #Exibindo informações finais
    print(msgfinal)
    print(f"Total da compra R$ {total:.2f}")

    #Verificando o frete
    if total < 200:
        print("valor do frete R$ 30.00")
    else:
        print("FRETE GRÁTIS!!!\n")
    
#Exibindo mensagem de despedida
print(f"{cliente}, foi um prazer atendê-lo. Volte em breve!")