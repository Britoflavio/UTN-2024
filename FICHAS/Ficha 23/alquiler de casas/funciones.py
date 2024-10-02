from clase import *


def crear_alquiler(linea):
    tokens = linea.split(',')
    documento = tokens[0]
    monto = float(tokens[1])
    tipo = int(tokens[2])
    return Registro(documento, monto, tipo)
