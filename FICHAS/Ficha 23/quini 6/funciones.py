import random
from utils import *
import pickle


def opcion_a():
    v = [0] * 6

    for i in range(len(v)):
        v[i] = val_intervalo(0, 36, f'{i + 1}° numero sorteado: ')
    orden_ascendente(v)
    m = open('extracto.dat', 'wb')  # SOLO ESCRITO “wb”
    pickle.dump(v, m)  # Para grabar datos en el archivo : pickle.dump()
    m.close()


def opcion_b():
    archivo = 'extracto.dat'
    m = open(archivo, 'rb')  # rb Solo Lectura
    v = pickle.load(m)  # Para leer datos desde un archivo
    print(v)
    m.close()
