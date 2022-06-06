import csv

from eliminar import eliminar_dados
from inserir import inserir_dados
from listar import mostrar


def modificar_dados(filename, control, ficheiros):
    mostrar(filename, ficheiros)
    opcao = int(input('Insira o ID do registo que deseja modificar: '))
    eliminar_dados(filename, opcao, True)
    inserir_dados(filename, control, ficheiros, opcao, True)

