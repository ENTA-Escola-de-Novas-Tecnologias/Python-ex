import os
import pickle
from Control import Control
from inicializar_tabelas import Tabelas
from menus import main_menu, menu_produtos

INITAPP = True

if __name__ == '__main__':
    if INITAPP:
        ficheiros = Tabelas(INITAPP)
        control = Control('dados/control.csv')
    else:
        with open("dados/inicializar.dat", "rb") as infile:
            ficheiros = pickle.load(infile)
        with open("dados/control.dat", "rb") as infile:
            control = pickle.load(infile)

    main_menu(control, ficheiros)

    with open("dados/inicializar.dat", "wb") as output:
        pickle.dump(ficheiros, output)
    with open("dados/control.dat", "wb") as output:
        pickle.dump(control, output)
