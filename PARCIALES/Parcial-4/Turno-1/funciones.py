import random
from clase import Lote


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
