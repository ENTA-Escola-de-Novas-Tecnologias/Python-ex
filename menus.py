import os
from listar import mostrar
from inserir import inserir_dados, inserir_encomenda
from menu_clientes import modificar_cliente, eliminar_cliente, listar_clientes


def main_menu(control, ficheiros):
    opcoes = {
        '0': 'quit()',
        '1': 'menu_clientes(control, ficheiros)',
        '2': 'menu_produtos(control, ficheiros)',
        '3': 'menu_transportes(control, ficheiros)',
        '4': 'menu_encomendas(control, ficheiros)',
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
                print(ficheiros.fields)
                eval(opcoes.get(str(opcao)))
                break


def menu_clientes(control, ficheiros):
    while True:
        opcoes = {
            '0': 'print()',
            '1': 'inserir_dados("dados/clientes.csv", control, ficheiros)',
            '2': 'modificar_cliente(control, ficheiros)',
            '3': 'eliminar_cliente(control, ficheiros)',
            '4': 'mostrar("dados/clientes.csv", ficheiros)',
        }
        #os.system('clear')
        print('MENU CLIENTES')
        print('1. Inserir cliente')
        print('2. Modificar cliente')
        print('3. Eliminar cliente')
        print('4. Listar clientes')
        print('0. Voltar')
        while True:
            opcao = int(input('Insira uma opção válida: '))
            if 0 < opcao <= 4:
                eval(opcoes.get(str(opcao)))
                break
            else:
                return


def menu_produtos(control, ficheiros):
    opcoes = {
        '0': 'print()',
        '1': 'inserir_dados("dados/produtos.csv", control, ficheiros)',
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
        if 0 < opcao <= 4:
            eval(opcoes.get(str(opcao)))
            break
        else:
            return


def menu_transportes(control, ficheiros):
    opcoes = {
        '0': 'print()',
        '1': 'inserir_dados("dados/transportes.csv", control, ficheiros)',
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
        if 0 < opcao <= 4:
            eval(opcoes.get(str(opcao)))
            break
        else:
            return


def menu_encomendas(control, ficheiros):
    opcoes = {
        '0': 'print()',
        '1': 'inserir_encomenda("dados/encomendas.csv", control, ficheiros)',
        '2': 'modificar_detalhe()',
        '3': 'eliminar_detalhe()',
        '4': 'listar_encomendas()'
    }
    os.system('clear')
    print('MENU Detalhes de Encomenda')
    print('1. Inserir encomenda')
    print('2. Modificar Encomenda')
    print('3. Eliminar Encomenda')
    print('4. Listar Encomendas')
    print('0. Voltar')
    while True:
        opcao = int(input('Insira uma opção válida: '))
        if 0 < opcao <= 4:
            eval(opcoes.get(str(opcao)))
            break
        else:
            return


def menu_relatorios(control, ficheiros):
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
        if 0 < opcao <= 4:
            eval(opcoes.get(str(opcao)))
            break
        else:
            return
