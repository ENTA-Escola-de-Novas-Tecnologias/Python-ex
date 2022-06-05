import csv


class Tabelas:
    def __init__(self, limpar):
        self.limpar = limpar
        self.tabelas = None
        self.fields = None
        self.inicializar_tabelas()

    def inicializar_tabelas(self):
        self.tabelas = [
            'dados/clientes.csv', 'dados/produtos.csv', 'dados/encomendas.csv', 'dados/encdetalhe.csv',
            'dados/transportes.csv', 'dados/control.csv'
        ]
        self.fields = [
            [
                ['IDCLIENTE', 'NOME', 'MORADA', 'CPOSTAL', 'LOCALIDADE', 'TELEFONE'],
                ['IDPRODUTO', 'NOME', 'CUSTO', 'STOCK', 'ENCOMENDAS', 'MINIMO'],
                ['IDENCOMENDA', 'IDCLIENTE', 'DATA', 'IDTRANSPORTE'],
                ['IDENCOMENDA', 'IDPRODUTO', 'QUANTIDADE', 'PRECO'],
                ['IDTRANSPORTE', 'NOME'],
                ['IDPRODUTO', 'IDCLIENTE', 'IDENCOMENDA', 'IDTRANSPORTE']
            ],
            [
                ['IDCLIENTE', 'Nome do cliente: ', 'Morada do cliente: ', 'Código postal: ', 'Localidade: ',
                 'Telefone: '],
                ['IDPRODUTO', 'Nome do produto: ', 'Custo: ', 'Unidades em stock: ', 'Unidades encomendadas: ',
                 'Mínimo disponível: '],
                ['IDENCOMENDA', 'ID do cliente: ', 'Data da encomenta: ', 'ID da transportadora: '],
                ['IDENCOMENDA', 'ID do produto: ', 'Quantidade: ', 'Preço: '],
                ['IDTRANSPORTE', 'Nome da transportadora: '],
                ['IDPRODUTO', 'IDCLIENTE', 'IDENCOMENDA', 'IDTRANSPORTE']
            ],
            [
                [len('IDCLIENTE'), len('NOME'), len('MORADA'), len('CPOSTAL'), len('LOCALIDADE'), len('TELEFONE')],
                [len('IDPRODUTO'), len('NOME'), len('CUSTO'), len('STOCK'), len('ENCOMENDAS'), len('MINIMO')],
                [len('IDENCOMENDA'), len('IDCLIENTE'), len('DATA'), len('IDTRANSPORTE')],
                [len('IDENCOMENDA'), len('IDPRODUTO'), len('QUANTIDADE'), len('PRECO')],
                [len('IDTRANSPORTE'), len('NOME')],
                [len('IDPRODUTO'), len('IDCLIENTE'), len('IDENCOMENDA'), len('IDTRANSPORTE')]
            ]
        ]
        if self.limpar:
            idx = 0
            for tabela in self.tabelas:
                with open(tabela, 'w', encoding='utf-8') as output:
                    writer = csv.writer(output)
                    writer.writerow(self.fields[0][idx])
                idx += 1

    def setmax(self, d1, d2, d3, comprimento):
        self.fields[d1][d2][d3] = comprimento

    def getmax(self, d1, d2, d3):
        return self.fields[d1][d2][d3]
