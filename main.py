from Control import Control
from inicializar_tabelas import Tabelas
from menus import main_menu, menu_produtos

INITAPP = True

if __name__ == '__main__':
    control = Control('dados/control.csv', )
    tabelas = Tabelas(INITAPP)
    main_menu(control, tabelas)

