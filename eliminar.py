import csv
import os
from listar import mostrar


def eliminar_dados(filename, ficheiros, chave=None, quiet=False):
    if chave is None:
        mostrar(filename, ficheiros)
        chave = int(input('Insira o ID do registo que deseja eliminar: '))
    encontrado = False
    with open(filename) as in_file, open(filename + '.tmp', 'w') as out_file:
        reader = csv.reader(in_file)
        writer = csv.writer(out_file)
        for row in reader:
            if str(row[0]) == str(chave):
                encontrado = True
                if not quiet:
                    print(f'Registo eliminado: {row[0]}')
            else:
                writer.writerow(row)
    os.replace(filename + '.tmp', filename)
    if not encontrado:
        if not quiet:
            print(f'Registo com chave {row[0]} não existe.')