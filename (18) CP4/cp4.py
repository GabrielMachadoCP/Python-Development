# Ana zerlin       rm 98065
# Bianca Dancs     rm 551645
# Gabriel Pimentel rm 99880
# Hellen Assis     rm 98284
# João Gava        rm 550595

import random
import re

#Função que fará o sorteio do funcionário
def funcionario() :
    func = ("Ana", "Bianca", "Gabriel", "Hellen", "João")
    sorteio = random.choice(func)
    return sorteio


#Criação da função para verificação do CEP
def digitos(cep):
    if not re.search  == ("\d{5}-\d{3}", cep) or len(cep) > 9:
        print("CEP deve conter 8 dígitos mais um traço entre o 5º e 6º dígito")


#Criação do Nested Dictionary com os vinhos
vinhos = {
    "vinho1" : {"nome" : "(1) Suave Tinto", "valor" : 25, "estoque" : 50},
    "vinho2" : {"nome" : "(2) Seco Tinto", "valor" : 35, "estoque" : 60},
    "vinho3" : {"nome" : "(3) Suave Branco", "valor" : 15, "estoque" : 52},
    "vinho4" : {"nome" : "(4) Seco Branco", "valor" : 36, "estoque" : 15},
    "vinho5" : {"nome" : "(5) Sem ácool", "valor" : 40, "estoque" : 0}
}
erro = ""
funci = funcionario()

try:
    #Mensagem de Boas Vindas
    print(f"Bem-vindo à Vinheria Agnello.\nO funcinário que irá te acompanhar é {funci}")

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

    informacoes = {
        "nome" : cliente,
        "cep" : cep,
        "anoNasc" : anoNasc
    }

    #Verificando a maioridade
    if anoNasc > "2005":
        print(f"{cliente} não é permitida a venda para menores de 18 anos!")
    else:
        #Variáveis para auxiliar nos cálculos
        subtotal = total = 0

        #Preparando a mensagem final
        msgfinal = f"\nDados da compra:\nAtendido por: {funci}\nCliente: {cliente}\nItens da Compra\t\tValor\t\tQtde\tSubtotal\n"

        #Imprimindo o dicionario de vinhos
        print(":"*70)
        print("Escolha um tipo de vinho:")
        for i in range(1, len(vinhos) +1, 1):
            vin = "vinho" + str(i)
            nomeVin = vinhos[vin]["nome"]
            valorVin = vinhos[vin]["valor"]
            estoqueVin = vinhos[vin]["estoque"]
        
            if estoqueVin > 0:
                print(f"Vinho:{nomeVin} \tPreço: R${valorVin:.2f}")

        #Armazenando o vinho escolhido e quantidade
        vinho = int(input())
        print("Em qual quantidade deseja adquirir este vinho?")
        qtde = int(input())

        print(estoqueVin)
        # if qtde > estoqueVin:
        #     print("Não temos estoque suficiente")
        # else:
        match vinho:
            case 1:
                subtotal = 25 * qtde
                msgfinal += f"Vinho suave tinto\t R$ 25.00\t{qtde}\tR${subtotal:.2f}\n"
            case 2:
                subtotal = 35 * qtde
                msgfinal += f"Vinho seco tinto\t R$ 35.00\t{qtde}\tR${subtotal:.2f}\n"
            case 3:
                subtotal = 15 * qtde
                msgfinal += f"Vinho suave branco\t R$ 15.00\t{qtde}\tR${subtotal:.2f}\n"
            case 4:
                subtotal = 36 * qtde
                msgfinal += f"Vinho seco branco\t R$ 36.00\t{qtde}\tR${subtotal:.2f}\n"
            case 5:
                subtotal = 40 * qtde
                msgfinal += f"Vinho sem álcool\t R$ 40.00\t{qtde}\tR${subtotal:.2f}\n"
            case _:
                print("Por Favor, escolha uma das opções da lista.")
            
        estoqueFinal = estoqueVin - qtde
        total += subtotal
        compra = [nomeVin, valorVin, qtde, subtotal]

        estoqueFin = f"Vinho: {nomeVin} \tPreço: R${valorVin:.2f} \tEstoque: {estoqueFinal}"

        #Exibindo informações finais
        print(msgfinal)
        print(f"Total da compra R$ {total:.2f}")
        
        print(estoqueFin)
        #Exibindo mensagem de despedida
        print(f"{cliente}, foi um prazer atendê-lo. Volte em breve!")

#Exibindo a mensagem de erro
except ValueError:
    print(erro)
finally:
    print("Fim de programa")