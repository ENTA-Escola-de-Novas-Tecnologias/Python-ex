import csv


def mostrar(filename, ficheiros, id=None):
    imprimiu_header = False
    tab = ficheiros.tabelas.index(filename)
    with open(filename, encoding='utf-8') as file:
        lines = csv.reader(file)
        for line in lines:
            space = 0
            minus = 0
            idx = 0
            for campo in line:
                if imprimiu_header and id is not None and id != line[0]:
                    continue
                imprimiu_header = True
                space += ficheiros.getmax(2, tab, idx) - minus + 1
                minus = ficheiros.getmax(2, tab, idx)
                print(f'{campo:<{space}}', end='')
                idx += 1
            if idx > 0:
                print()


def mostrar_encomendas(filename, ficheiros):
    tab = ficheiros.tabelas.index(filename)
    with open(filename, encoding='utf-8') as file:
        lines = csv.reader(file)
        header = None
        for line in lines:
            if header is None:
                header = line
            else:
                print_header('dados/encdetalhe.csv', header, ficheiros)
                space = 0
                minus = 0
                idx = 0
                for campo in line:
                    space += ficheiros.getmax(2, tab, idx) - minus + 1
                    minus = ficheiros.getmax(2, tab, idx)
                    print(f'{campo:<{space}}', end='')
                    idx += 1
                print()
                if idx > 1:
                    mostrar('dados/encdetalhe.csv', ficheiros, line[0])


def print_header(filename, header, ficheiros):
    tab = ficheiros.tabelas.index(filename)
    space = 0
    minus = 0
    idx = 0
    for campo in header:
        space += ficheiros.getmax(2, tab, idx) - minus + 1
        minus = ficheiros.getmax(2, tab, idx)
        print(f'{campo:<{space}}', end='')
        idx += 1
    print()
