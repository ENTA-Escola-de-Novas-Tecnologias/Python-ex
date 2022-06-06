import csv
import os


def eliminar_dados(filename, chave=None):
    if chave is None:
        chave = int(input('Insira o ID do registo que deseja eliminar: '))
    encontrado = False
    with open(filename) as in_file, open(filename + '.tmp', 'w') as out_file:
        reader = csv.reader(in_file)
        writer = csv.writer(out_file)
        for row in reader:
            print(f'row[0]={row[0]} chave={chave}')
            if str(row[0]) == str(chave):
                encontrado = True
                print(f'Registo eliminado: {row}')
            else:
                writer.writerow(row)
    os.replace(filename + '.tmp', filename)
    if not encontrado:
        print(f'Registo com chave {row[0]} não existe.')