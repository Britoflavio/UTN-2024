from clase import Pantalon
import random
import pickle
import os.path


def validar_positi(men, msj):
    val = int(input(msj))
    while men >= val:
        print(f'Numero invalido, intente con un numero mayor a {men}')
        val = int(input(msj))
    return val


def opcion_a():
    v = []
    n = validar_positi(0, 'Ingrese cantidad de registros: ')
    nombres = ['juan', 'fla', 'vio', 'sole', 'jazz', 'pepe', 'jan', ]
    for i in range(n):
        # CODIGO, NOMBRE, TALLE, TALLE CIN 3, 50  , TIPO DE TELA 1,3 STOCK
        codigo = random.randint(1, 100)
        nombre = random.choice(nombres)
        talle_largo = random.randint(30, 50)
        talle_cintura = random.randint(30, 50)
        tipo = random.randint(1, 3)
        stock = random.randint(0, 60)
        pant = Pantalon(codigo, nombre, talle_largo, talle_cintura, tipo, stock)
        ordenar_op_a(v, pant)

    return v


def ordenar_op_a(v, pant):
    x = len(v)
    izq, der = 0, x - 1
    while izq <= der:
        prom = (izq + der) // 2
        if v[prom].codigo == pant.codigo:
            x = prom
            break
        else:
            if pant.codigo < v[prom].codigo:
                der = prom - 1
            else:
                izq = prom + 1
    if izq > der:
        x = izq
    v[x:x] = [pant]


def opcion_b(v):
    tipo_tela = ['Jean', 'Gabardina', 'Denim']
    for i in range(len(v)):
        n = v[i].tipo - 1
        v[i].tipo = tipo_tela[n]
        print(v[i])


def opcion_c(v):
    u = int(input('Stock minimo: '))
    fc = [[0] * 21 for _ in range(21)]
    for i in range(len(v)):
        f = v[i].talle - 30
        c = v[i].talle_cin - 30
        fc[f][c] += v[i].stock

    for f in range(21):
        for c in range(21):
            if fc[f][c] > u:
                print(f'Largo: {f + 30}, Cintura: {c + 30}, stock: {fc[f][c]}')

def opcion_d(v, tela, arch_bin):
    m = open(arch_bin, 'wb')
    for i in range(len(v)):
        if v[i].stock > 0 and v[i].tipo == tela:
            pickle.dump(v[i], m)
    m.close()


def opcion_e(arch_bin):
    if not os.path.exists(arch_bin):
        print(f'El archivo {arch_bin} no existe.')
        print()
        return
    sum_stock = cant_produc = 0
    m = open(arch_bin, 'rb')
    size = os.path.getsize(arch_bin)
    while m.tell() < size:
        v = pickle.load(m)
        cant_produc += 1
        sum_stock += v.stock
        print(v)
    prom = 0
    if cant_produc != 0:
        prom = sum_stock / cant_produc
        print(f'El promedio es de : {round(prom, 2)}')
