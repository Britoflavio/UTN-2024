from clase import Juico
import random


def validar_intervalo(men, may, msj):
    val = int(input(msj))
    while may < val or val < men:
        print('Valor ingresado invalido, intenta nuevamente.')
        val = int(input(msj))
    return val


def validar_may(men, msj):
    val = int(input(msj))
    while men >= val:
        print('Valor invalido, intente nuevamente.')
        val = int(input(msj))
    return val


def opcion_a():

    cargas = validar_may(1, 'Ingrese un valor: ')
    v = cargas * [0]
    descripcion = ['Robo armado', 'Robo bancario', 'Hacker', 'Asesinato']
    client = ['Jorge', 'Carlos', 'Martin', 'Soledad', 'Sofia', 'Jorgelina', 'Trinidad', 'Agustina']
    for i in range(cargas):
        # expediente, descrip, tipo, cliente, monto
        expe = random.randint(1, 200)
        descrip = random.choice(descripcion)
        tipo = random.randint(1, 15)
        cliente = random.choice(client)
        monto = random.randint(1000, 10000)
        v[i] = Juico(expe, descrip, tipo, cliente, monto)
    return v


def ordenar_descrip(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].descripcion > v[j].descripcion:
                v[i], v[j] = v[j], v[i]


def opcion_b(v, mon):
    cont = 0
    for i in range(v):
        if v[i].monto > mon:
            cont += 1
            ordenar_descrip(v)
            print(v[i])
    return cont
