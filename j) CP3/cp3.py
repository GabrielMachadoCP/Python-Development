# Ana zerlin      rm 98065
# Bianca Dancs    rm 551645
# Gabriel Machado rm 99880
# Hellen Assis    rm 98284

import random
import re

erro = ""

try:

    #Criação da função para verificação do CEP
    def digitos(cep):
        if not re.search  == ("\d{5}-\d{3}", cep) or len(cep) > 9:
            print("CEP deve conter 8 dígitos mais um traço entre o 5º e 6º dígito")


    #Sorteio do funcionário com uma lista
    func = ["Ana", "Bianca", "Gabriel", "Hellen"]
    sorteio = random.choice(func)

    #Mensagem de Boas Vindas
    print(f"Bem-vindo à Vinheria Agnello.\nO funcinário que irá te acompanhar é {sorteio}")

    #Requisitando informações do cliente
    print("Informe seu nome:")
    cliente = input()
    #Validação de informações dos dados
    if re.search("\d", cliente):
        erro = "Nomes não podem conter números"
        raise ValueError
    print("Informe o CEP da sua residência:")
    cep =  input()
    if not re.search("\d{5}-\d{3}", cep) or len(cep) > 9:
        digitos(cep)
        raise ValueError
    print("Informe o ano de seu nascimento:")
    anoNasc = input()
    if not re.search("\d{4}", anoNasc) or len(anoNasc) > 4:
        erro = "Anos devem conter 4 dígitos"
        raise ValueError

    #Verificando a maioridade
    if anoNasc > "2005":
        print(f"{cliente} não é permitida a venda para menores de 18 anos!")
    else:
        #Variáveis para auxiliar nos cálculos
        subtotal = total = 0

        #Preparando a mensagem final
        msgfinal = f"Dados da compra:\nAtendido por: {sorteio}\nCliente: {cliente}\nItens da Compra\t\tValor\t\tQtde\tSubtotal\n"

        #Repetindo a venda de vinhos
        continua = "sim"
        while continua.lower() == "sim":

            #Exibindo opções de vinhos
            vinhos = ["(1)Vinho suave tinto\tR$ 15.00","\n(2)Vinho Seco tinto\tR$ 25.00","\n(3)Vinho suave branco\tR$ 35.00","\n(4)Vinho Seco Branco\tR$ 30.00","\n(5)Vinho sem álcool\tR$ 40.00\n"]

            print("Escolha um dos vinhos da lista:\n")
            for i in vinhos:
                print(i)

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
    
#Exibindo a mensagem de erro
except ValueError:
    print(erro)
finally:
    print("Fim de programa")