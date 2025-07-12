import random
import re

def sorteianome(nomes) :
    sorteio = random.randint(0,4)
    return nomes[sorteio]


#Tupla dos funcionários
funcionarios = ("Ana", "Bianca", "Gabriel", "Hellen", "João")

#Sorteio do funcionário
nomefunc = sorteianome(funcionarios)

#Dicionário aninhado com os vinhos disponíveis
vinhos = {
    "vinho1" : {"nome" : "Suave Tinto", "valor" : 25.0, "estoque" : 50},
    "vinho2" : {"nome" : "Seco Tinto  ", "valor" : 35.0, "estoque" : 60},
    "vinho3" : {"nome" : "Suave Branco", "valor" : 15.0, "estoque" : 52},
    "vinho4" : {"nome" : "Seco Branco", "valor" : 36.0, "estoque" : 15},
    "vinho5" : {"nome" : "Sem ácool", "valor" : 40.0, "estoque" : 0}
}

#Mensagem de boas vindas
print(f"Bem-vindo à Vinheria Agnello.")
print(f"O funcionário {nomefunc} vai acompanhá-lo.")

#Requisitando informações do usuário
erro = ""

try :
    print("Informe seu nome")
    nome = input()
    if re.search("\d", nome) :
        erro = "Nomes não podem conter dígitos"
        raise ValueError
    
    print("Informe seu CEP")
    cep = input()
    if not re.search("[0-9]{5}-\d{3}", cep) or len(cep) > 9 :
        erro = "CEP inválido (formato: 00000-000)"
        raise ValueError
    
    print("Digite seu ano de nascimento")
    anonasc = int(input())
    if not re.search("\d{4}", str(anonasc)) or len(str(anonasc)) > 4 :
        erro = "Ano de nascimento incorreto"
        raise ValueError
    
    #Armazenando informações do cliente em um Dicionário
    cliente = {
        "nome" : nome,
        "cep" : cep,
        "ano_nasc" : anonasc
    }

    #Verificando a maioridade
    idade = 2023 - cliente["ano_nasc"]
    if idade < 18 :
        print(f"{cliente['nome']} : não é permitida a venda para menores de 18 anos")
    else :
        #Exibindo opções de vinhos (estoque > 0)
        print("Escolha um dos vinhos da lista:")

        for i in range(1, len(vinhos) + 1, 1) :
            if vinhos["vinho" + str(i)]["estoque"] > 0 :
                print(f"({i}) {vinhos['vinho' + str(i)]['nome']} \t R$ {vinhos['vinho' + str(i)]['valor']:.1f}")

        #Escolha da quantidade do vinho pelo usuário
        vinho = int(input())

        print("Quantidade deste vinho?")
        qtde = int(input())

        #Verificando se o cliente escolheu um vinho da lista
        if "vinho" + str(vinho) in vinhos :
            #Verificando se há quantidade suficiente deste vinho
            estoque = vinhos['vinho' + str(vinho)]['estoque']

            if estoque > 0 and qtde <= estoque :
                #Atualizar o estoque
                novo_estoque = estoque - qtde
                vinhos['vinho' + str(vinho)]['estoque'] = novo_estoque

                #Registrando a compra no List
                compra = []
                compra.append(vinhos['vinho' + str(vinho)]['nome'])
                compra.append(vinhos['vinho' + str(vinho)]['valor'])
                compra.append(qtde)
                compra.append(vinhos['vinho' + str(vinho)]['valor'] * qtde)
            else :
                print("Quantidade informada excede estoque")
        else :
            print("Opção inválida da lista de vinhos")

    #Exibindo dados da compra
    print(":" * 70)
    print(f"{nome}, foi um prazer atendê-lo.")
    msg = "Tipo do vinho \t Preço \t Qtde \t Subtotal \n"
    for i in compra :
        msg += str(i) + " \t "

    print(msg)
    print(":" * 70)

    #Exibindo o estoque
    print("Nosso estoque final ficou:")
    for i in range(1, len(vinhos) + 1, 1) :
        vinho = vinhos['vinho' + str(i)]['nome']
        valor = vinhos['vinho' + str(i)]['valor']
        estoque = vinhos['vinho' + str(i)]['estoque']
        print(f"Vinho: {vinho} \t Preço: R${valor} \t Estoque: {estoque}")
    
    print(":" * 70)

except ValueError :
    print(erro)