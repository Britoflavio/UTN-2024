from clase import *
import os
import pickle
import random


def crear_alquiler(linea):
    tokens = linea.split(',')
    documento = tokens[0]
    monto = float(tokens[1])
    tipo = int(tokens[2])
    return Registro(documento, monto, tipo)


def opcion_a(csv):
    if not os.path.exists(csv):
        print(f'No existe el achivo {csv}')
        return

    v = []
    alquileres = open(csv, 'rt')  # SOLO LECTURA o r, tambien podemos llamarlo como open(csv) sin pasarle nada

    cabecera = True
    for linea in alquileres:
        if cabecera:
            cabecera = False
            continue
        alquiler = crear_alquiler(linea)
        v.append(alquiler)
    alquileres.close()
    return v


def opcion_b(val, dat, v):
    archivo = open(dat, 'wb')  # SOLO ESCRITURA
    for casa in v:
        if casa.monto > val:
            pickle.dump(casa, archivo)  # Para grabar datos en el archivo : pickle.dump()
    archivo.flush()  # baja el buffer
    archivo.close()


def opcion_c(csv):
    size = os.path.getsize(csv)
    if size < 0:
        return None

    archivo = open(csv, 'rb')
    monto_total_tipo = [0] * 10
    while archivo.tell() < size:
        casa = pickle.load(archivo)  # Para leer datos desde un archivo: pickle.load()
        monto_total_tipo[casa.tipo] += casa.monto
    archivo.close()
    return monto_total_tipo
