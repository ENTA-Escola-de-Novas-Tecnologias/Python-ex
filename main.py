from Control import Control
from menus import main_menu, menu_produtos

if __name__ == '__main__':
    control = Control('dados/control.csv', )
    print(control.ids['idproduto'])
    print(control.ids['idcliente'])
    print(control.ids['idencomenda'])
    print(control.ids['idtransporte'])

    print(control.getset('idproduto'))

