import random
from clase import Empleo


def validar_intervalor(men, may, msj):
    val = int(input(msj))
    while may < val or val < men:
        print('El valor ingresado es invalido, intente nuevamente.')
        val = int(input(msj))
    return val


def validar_may(men, msj):
    val = val = int(input(msj))
    while men >= val:
        print('No puedes ingresar cero como valor, ingrese un valor nuevamente.')
        val = int(input(msj))
    return val


def opcion_a():
    n = validar_may(0, 'Ingrese cantidad de empleos: ')
    v = n * [0]
    descripcion = ['computacional', 'home office', 'medio turno', 'turno completo', 'semanal']
    for i in range(len(v)):
        # id, descripcion, tipo, retribucion
        id = random.randint(1, 30)
        descrip = random.choice(descripcion)
        tipo = random.randint(0, 39)
        retri = random.randint(10000, 20000)
        v[i] = Empleo(id, descrip, tipo, retri)
        print(v[i])
    return v


def ordenar_desc(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].descripcion > v[j].descripcion:
                v[i], v[j] = v[j], v[i]


def opcion_b(v):
    ordenar_desc(v)
    acum_sueldo = 0
    for i in range(len(v)):
        print(v[i])
        acum_sueldo += v[i].retribucion
    return acum_sueldo


def opcion_c(v):
    n = len(v)
    cant_empleos = 40 * [0]
    for i in range(n):
        cant_empleos[v[i].tipo - 1] += 1
    return cant_empleos


def opcion_d(v):
    num = validar_may(0, 'Ingrese un identificador a buscar: ')
    for i in range(len(v)):
        if v[i].id == num:
            r = f'Descripcion: {v[i].descripcion}'
            r += f' Sueldo a pagar: {v[i].retribucion}'
            return r
    return -1
