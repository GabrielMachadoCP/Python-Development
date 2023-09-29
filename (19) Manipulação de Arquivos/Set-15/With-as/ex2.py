try:
    #criando e escrevendo um arquivo com with/as
    with open('d:/mafagafo.txt', 'w', encoding='utf-8') as f:
        f.write('Um ninho de mafagafos,')
        f.write('tinha sete mafagafinhos.\n')
        f.write('Quem desmafagar esses mafagafinhos')
        f.write('bom desmafagador será.')
    #Lendo um arquivo completamente
    with open('d:/mafagafo.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente!")