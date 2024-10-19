import os.path
import pickle
import random
from clase import Pieza


def validar(men, msj):
    val = int(input(msj))
    while val <= men:
        print(f'Valor invalido intenta con un numero mayor a {men}')
        val = int(input(msj))
    return val


def opcion_a():
    n = validar(0, 'Ingrese cantidad de registros: ')
    v = []
    descripciones = ['tttttssasas', 'gggggasgasdas', 'qqqqqqqasasgasdasd', 'jjjjjasasas', 'aaasgasgasg', 'aesdasfa',
                     '22214124']
    for i in range(n):
        # codigo, descripcion, tipo entre 0 y 19, numero de sector entre 10 y 25, stock
        codigo = random.randint(100, 300)
        descripcion = random.choice(descripciones)
        tipo = random.randint(0, 19)
        sector = random.randint(10, 25)
        stock = random.randint(0, 10)
        piezas = Pieza(codigo, descripcion, tipo, sector, stock)
        ordenar_op_a(v, piezas)
    print('Registros cargados exitosamente.')
    print()
    return v


def ordenar_op_a(v, piezas):
    x = len(v)
    izq, der = 0, x - 1
    while izq <= der:
        prom = (izq + der) // 2
        if piezas.codigo == v[prom].codigo:
            x = prom
            break
        else:
            if izq < der:
                der = prom - 1
            else:
                izq = prom + 1
    if izq > der:
        x = izq
    v[x:x] = [piezas]


def opcion_b(v):
    x = int(input('Ingrese un valor: '))
    for i in range(len(v)):
        if x > v[i].stock:
            print(v[i])
            print('Stock reducido')
            print()
        else:
            print(v[i])
            print()


def opcion_c(v):
    fc = [[0] * 16 for _ in range(20)]

    for i in range(len(v)):
        f = v[i].tipo
        c = v[i].sector - 10
        fc[f][c] += v[i].stock

    for f in range(20):
        for c in range(16):
            if fc[f][c] > 0:
                print(f'Tipo: {f}, Sector: {c}, Stock: {fc[f][c]}')


def opcion_d(v, arch_bin):
    m = open(arch_bin, 'wb')
    for i in range(len(v)):
        if v[i].sector > 15:
            pickle.dump(v[i], m)
    m.close()


def opcion_e(arch_bin):
    if not os.path.exists(arch_bin):
        print(f'El archivo {arch_bin} no existe.')
        print()
        return
    cant_piezas = suma_stock = 0
    m = open(arch_bin, 'rb')
    size = os.path.getsize(arch_bin)
    while m.tell() < size:
        piezas = pickle.load(m)
        cant_piezas += 1
        suma_stock += piezas.stock
        print(piezas)
    prom = 0
    if cant_piezas != 0:
        prom = suma_stock / cant_piezas
        print(f'Cantidad promedio de stock : {round(prom, 2)}')
