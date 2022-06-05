import csv


def inserir_dados(filename, control, ficheiros, id=None):
    with open(filename, 'a') as file:
        tab = ficheiros.tabelas.index(filename)
        while True:
            chave = None
            linha = []
            idx = 0
            for texto in ficheiros.fields[1][tab]:
                if chave is None:
                    chave = texto
                    if id is None:
                        linha.append(control.getset(chave))
                    else:
                        linha.append(id)
                else:
                    resposta = input(texto)
                    linha.append(resposta)
                    if len(resposta) > ficheiros.fields[2][tab][idx]:
                        ficheiros.fields[2][tab][idx] = len(resposta)
                idx += 1
            writer = csv.writer(file)
            writer.writerow(linha)
            if input('Continuar (s/n)?') != "s":
                break


def inserir_encomenda(filename, control, tabelas):
    with open(filename, 'a', encoding='utf-8') as file:
        tab = tabelas.tabelas.index(filename)
        chave = None
        linha = []
        idx = 0
        for texto in tabelas.fields[1][tab]:
            if chave is None:
                chave = texto
                idencomenda = control.getset(chave)
                linha.append(idencomenda)
            else:
                resposta = input(texto)
                linha.append(resposta)
                if len(resposta) > tabelas.fields[2][tab][idx]:
                    tabelas.setmax(2, tab, idx, len(resposta))
            idx += 1
        writer = csv.writer(file)
        writer.writerow(linha)
        inserir_dados('dados/encdetalhe.csv', control, tabelas, idencomenda)
