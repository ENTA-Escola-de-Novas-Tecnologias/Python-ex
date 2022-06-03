import csv


def inserir_dados(filename, control, tabelas):
    with open(filename, 'a', encoding='utf-8') as file:
        tab = tabelas.tabelas.index(filename)
        while True:
            chave = None
            linha = []
            for textos in tabelas.fields[tab]:
                for texto in textos:
                    if chave is None:
                        chave = texto
                        linha.append(control.getset(chave))
                    else:
                        linha.append(input(texto))
                writer = csv.writer(file)
                writer.writerow(linha)
                if input('Continuar (s/n)?') is not 's':
                    break
