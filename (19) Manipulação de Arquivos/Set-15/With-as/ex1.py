try:
    #criando e escrevendo um arquivo
    f = open('d:/mafagafo.txt', 'w', encoding='utf-8')
    f.write('Um ninho de mafagafos,')
    f.write('tinha sete mafagafinhos.\n')
    f.write('Quem desmafagar esses mafagafinhos')
    f.write('bom desmafagador será.')
    f.close()
    #Lendo um arquivo completamente
    f = open('d:/mafagafo.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente!")