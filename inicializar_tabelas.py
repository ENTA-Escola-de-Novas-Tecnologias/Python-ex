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
            'dados/control.csv'
        ]
        self.fields = [
            [
                ['IDCLIENTE', 'NOME', 'MORADA', 'CPOSTAL', 'LOCALIDADE', 'TELEFONE'],
                ['IDPRODUTO', 'NOME', 'CUSTO', 'STOCK', 'ENCOMENDAS', 'MINIMO'],
                ['IDENCOMENDA', 'IDCLIENTE', 'DATA', 'IDTRANSPORTE'],
                ['IDENCOMENDA', 'IDPRODUTO', 'QUANTIDADE', 'PRECO'],
                ['IDPRODUTO', 'IDCLIENTE', 'IDENCOMENDA', 'IDTRANSPORTE']
            ],
            [
                ['IDCLIENTE', 'Nome do cliente: ', 'Morada do cliente: ', 'Código postal: ', 'Localidade: ',
                 'Telefone: '],
                ['IDPRODUTO', 'Nome do produto: ', 'Custo: ', 'Unidades em stock: ', 'Unidades encomendadas: ',
                 'Mínimo disponível: '],
                ['IDENCOMENDA', 'ID do cliente: ', 'Data da encomenta: ', 'ID da transportadora: '],
                ['IDENCOMENDA', 'ID do produto: ', 'Quantidade: ', 'Preço: '],
                ['IDPRODUTO', 'IDCLIENTE', 'IDENCOMENDA', 'IDTRANSPORTE']
            ]
        ]
        if self.limpar:
            idx = 0
            for tabela in self.tabelas:
                with open(tabela, 'w', encoding='utf-8') as output:
                    writer = csv.writer(output)
                    writer.writerow(self.fields[0][idx])
                idx += 1
