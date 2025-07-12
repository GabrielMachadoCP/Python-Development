import csv
with open('d:/usuarios.csv', 'r', encoding='utf-8') as f:
    usuarios = csv.reader(f)
    for i in usuarios:
            print(i)