import random
import pickle
import os.path
from clase import Cobros


def opcion_a(dat):
    dia = str(random.randint(1, 31))
    tipo = str(random.randint(1, 15))
    monto = str(random.randint(2000, 10000))
    cuenta = '300'
    nuev = Cobros(dia, tipo, monto, cuenta)

    archivo = open(dat, 'ab')  # ab modo append y binario
    pickle.dump(nuev, archivo)  # Para grabar datos en el archivo : pickle.dump()
    archivo.close()


def opcion_b(num_cuenta, dat):
    total = 0

    size = os.path.getsize(dat)
    if size <= 0:
        return False, total

    archivo = open(dat, 'rb')  # rb modo lecutra y binario
    while archivo.tell() < size:
        cobro = pickle.load(archivo) # lee los datos del archivo
        if cobro.cuenta == num_cuenta:
            total += cobro.monto
    archivo.close()
    return True, total
