import random
from clase import Lote
import os.path
import pickle
def validar_mayor(men, msj):
    val = int(input(msj))
    while men > val:
        print(f'Valor invalido debe ser mayor a {men}')
        val = int(input(msj))
    return val


def opcion_a():
    n = validar_mayor(0, 'Ingrese cantidad de lotes a cargar: ')
    v = []
    nombres = ['flavio', 'jorge', 'pedro', 'juan', 'lucas']
    apellidos = ['brito', 'ridoni', 'santos', 'cruz', 'moreno']
    for i in range(n):
        nombre = random.choice(nombres) + ' ' + random.choice(apellidos)
        manzana = random.randint(1, 35)
        lote = random.randint(1, 20)
        orientacion = random.randint(1, 4)
        terreno = round(random.uniform(200, 1000), 2)
        valor = round(random.uniform(10000, 20000), 2)
        lotes = Lote(nombre, manzana, lote, orientacion, terreno, valor)
        ordenar_archivo(v, lotes)
    return v


def ordenar_archivo(v, lote):
    n = len(v)
    x = n
    izq, der = 0, n - 1
    while izq <= der:  # mientras 0 sea menor al tama;o del arreglo
        c = (izq + der) // 2
        if lote.nombre == v[c].nombre:
            x = c
            break
        else:
            if lote.nombre < v[c].nombre:
                der = c - 1
            else:
                izq = c + 1
    if izq > der:
        x = izq
    v[x:x] = [lote]


def opcion_b(v):
    ubic = ['Norte', 'Sur', 'Este', 'Oeste']
    for i in range(len(v)):
        n = v[i].orientacion
        v[i].orientacion = ubic[n - 1]
        print(v[i])

def opcion_c(v):
    fc = [[0] * 4 for f in range(35)]
    for i in range(len(v)):
        f = v[i].manzana - 1
        c = v[i].orientacion - 1
        fc[f][c] += v[i].terreno

    for f in range(35):
        for c in range(4):
            if fc[f][c] != 0:
                print(f'Manzana: {f+1} -Orientacion: {c+1}, -Superficie: {round(fc[f][c], 2)}')

    print()
    manz = int(input('Ingrese manzana para mostrar superficie vendida: '))
    total = 0
    f = manz - 1
    for c in range(4):
        total += fc[f][c]
    print(f'La superficie para la manzana {manz}: {total}')
    print()

def opcion_d(arch_bin, v):
    l1 = int(input('Primer valor: '))
    l2 = int(input('Segundo valor: '))
    m = open(arch_bin, 'wb')
    for i in range(len(v)):
        if l1 <= v[i].lote <= l2:
            pickle.dump(v[i], m)
    m.close()
    print('Archivo generado.')
    print()

def opcion_e(arch_bin):
    if not os.path.exists(arch_bin):
        print('El archivo no existe.')
        print()
        return
    valor_total = cant_lotes = 0
    m = open(arch_bin, 'rb')
    size = os.path.getsize(arch_bin)
    while m.tell() < size:
        lines = pickle.load(m)
        cant_lotes += 1
        valor_total += lines.valor
        print(lines)
    m.close()
    prom = 0
    if cant_lotes != 0:
        prom = valor_total / cant_lotes
    print(f'Valor promedio de ventas entre los lotes del archivo: {round(prom, 2)}')

