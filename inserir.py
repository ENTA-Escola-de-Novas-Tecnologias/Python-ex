import csv


def inserir_dados(filename, control, tabelas, idencomenda=None):
    with open(filename, 'a', encoding='utf-8') as file:
        tab = tabelas.tabelas.index(filename)
        while True:
            chave = None
            linha = []
            print(f'tabelas.fields[tab]={tabelas.fields[1][tab]}')
            for texto in tabelas.fields[1][tab]:
                if chave is None:
                    chave = texto
                    if idencomenda is None:
                        linha.append(control.getset(chave))
                    else:
                        linha.append(idencomenda)
                else:
                    linha.append(input(texto))
            writer = csv.writer(file)
            writer.writerow(linha)
            if input('Continuar (s/n)?') != "s":
                break


def inserir_encomenda(filename, control, tabelas):
    with open(filename, 'a', encoding='utf-8') as file:
        tab = tabelas.tabelas.index(filename)
        chave = None
        linha = []
        print(f'tabelas.fields[tab]={tabelas.fields[1][tab]}')
        for texto in tabelas.fields[1][tab]:
            if chave is None:
                chave = texto
                idencomenda = control.getset(chave)
                linha.append(idencomenda)
            else:
                linha.append(input(texto))
        writer = csv.writer(file)
        writer.writerow(linha)
        inserir_dados('dados/encdetalhe.csv', control, tabelas, idencomenda)
