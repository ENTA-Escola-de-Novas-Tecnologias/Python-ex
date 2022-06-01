import os


def main_menu():
    opcoes = {
        '0': 'quit()',
        '1': 'menu_clientes()',
        '2': 'menu_produtos()',
        '3': 'menu_transportes()',
        '4': 'menu_encomendas()',
        '5': 'menu_relatorios()'
    }
    while True:
        os.system('clear')
        print('MENU PRINCIPAL')
        print('1. Clientes')
        print('2. Produtos')
        print('3. Transportes')
        print('4. Encomendas')
        print('5. Relatórios')
        print('0. Sair')
        print()
        while True:
            opcao = int(input('Insira uma opção válida: '))
            if 0 <= opcao <= 5:
                eval(opcoes.get(str(opcao)))
                break


def menu_clientes():
    opcoes = {
        '0': 'print()',
        '1': 'inserir_cliente()',
        '2': 'modificar_cliente()',
        '3': 'eliminar_cliente()',
        '4': 'listar_clientes()'
    }
    os.system('clear')
    print('MENU CLIENTES')
    print('1. Inserir cliente')
    print('2. Modificar cliente')
    print('3. Eliminar cliente')
    print('4. Listar clientes')
    print('0. Voltar')
    while True:
        opcao = int(input('Insira uma opção válida: '))
        if 0 <= opcao <= 4:
            eval(opcoes.get(str(opcao)))
            break



def menu_produtos():
    opcoes = {
        '0': 'print()',
        '1': 'inserir_produto()',
        '2': 'modificar_produto()',
        '3': 'eliminar_produto()',
        '4': 'listar_produtos()'
    }
    os.system('clear')
    print('MENU Produtos')
    print('1. Inserir produto')
    print('2. Modificar produto')
    print('3. Eliminar produto')
    print('4. Listar produtos')
    print('0. Voltar')
    while True:
        opcao = int(input('Insira uma opção válida: '))
        if 0 <= opcao <= 4:
            eval(opcoes.get(str(opcao)))
            break


def menu_transportes():
    opcoes = {
        '0': 'print()',
        '1': 'inserir_transporte()',
        '2': 'modificar_transporte()',
        '3': 'eliminar_transporte()',
        '4': 'listar_transportes()'
    }
    os.system('clear')
    print('MENU Transportes')
    print('1. Inserir transportadora')
    print('2. Modificar transportadora')
    print('3. Eliminar transportadora')
    print('4. Listar transportadoras')
    print('0. Voltar')
    while True:
        opcao = int(input('Insira uma opção válida: '))
        if 0 <= opcao <= 4:
            eval(opcoes.get(str(opcao)))
            break


def menu_encomendas():
    opcoes = {
        '0': 'print()',
        '1': 'manter_encomenda()',
        '2': 'manter_detalhe_encomendas()'
    }
    os.system('clear')
    print('MENU Encomendas')
    print('1. Manter Encomenda')
    print('2. Manter Detalhe da Encomenda')
    print('0. Voltar')
    while True:
        opcao = int(input('Insira uma opção válida: '))
        if 0 <= opcao <= 2:
            eval(opcoes.get(str(opcao)))
            break


def menu_encomendas_detalhe():
    opcoes = {
        '0': 'print()',
        '1': 'inserir_detalhe()',
        '2': 'modificar_detalhe()',
        '3': 'eliminar_detalhe()',
        '4': 'listar_encomendas()'
    }
    os.system('clear')
    print('MENU Detalhes de Encomenda')
    print('1. Inserir detalhe encomenda')
    print('2. Modificar Detalhe Encomenda')
    print('3. Eliminar Detalhe Encomenda')
    print('4. Listar Encomendas')
    print('0. Voltar')
    while True:
        opcao = int(input('Insira uma opção válida: '))
        if 0 <= opcao <= 4:
            eval(opcoes.get(str(opcao)))
            break


def menu_relatorios():
    opcoes = {
        '0': 'print()',
        '1': 'listar_clientes()',
        '2': 'listar_produtos()',
        '3': 'listar_ransportadoras()',
        '4': 'listar_encomendas()'
    }
    os.system('clear')
    print('MENU Relatórios')
    print('1. Listar clientes')
    print('2. Listar produtos')
    print('3. Listar transportadoras')
    print('4. Listar Encomendas')
    print('0. Voltar')
    while True:
        opcao = int(input('Insira uma opção válida: '))
        if 0 <= opcao <= 4:
            eval(opcoes.get(str(opcao)))
            break
