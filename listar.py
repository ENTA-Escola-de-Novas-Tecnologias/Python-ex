import csv


def mostrar(filename, ficheiros):
    tab = ficheiros.tabelas.index(filename)
    with open(filename, encoding='utf-8') as file:
        lines = csv.reader(file)
        for line in lines:
            space = 0
            minus = 0
            idx = 0
            for campo in line:
                space += ficheiros.getmax(2, tab, idx) - minus + 1
                minus = ficheiros.getmax(2, tab, idx)
                print(f'{campo:<{space}}', end='')
                idx += 1
            print()

