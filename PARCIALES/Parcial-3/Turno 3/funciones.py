from clase import Servicio
import random


def val_intervalo(men, may, msj):
    val = int(input(msj))
    while may < val or val < men:
        print(f'Valor invalido, intente nuevamente entre {men} y {may}')
        val = int(input(msj))
    return val


def val_may(men, msj):
    val = int(input(msj))
    while val <= men:
        print(f'Valor invalido, el valor ingresado debe ser mayor a {men}')
        val = int(input(msj))
    return val


def opcion_a():
    n = val_may(0, 'Ingrese cantidad de servicios a cargar: ')
    v = n * [0]
    nombres = ['Jorge', 'Pedro', 'Soeldad', 'Agustina', 'Luciano', 'Ruben', 'Tinita', 'Lucho']
    for i in range(len(v)):
        # iden, nom, serv, imp
        iden = random.randint(1, 50)
        nom = random.choice(nombres)
        serv = random.randint(1, 10)
        imp = random.randint(2000, 6000)
        v[i] = Servicio(iden, nom, serv, imp)
        print(v[i])
    print('Servicios cargados exitosamente.')

    return v


def ordenar_b(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].identificador > v[j].identificador:
                v[i], v[j] = v[j], v[i]


def opcion_b(v):
    i1 = val_may(0, 'Ingrese el primer valor siendo el menor: ')
    i2 = val_may(i1, 'Ingrese el segundo valor siendo el mayor: ')
    cont = 0
    for i in range(len(v)):
        if i1 <= v[i].importe <= i2:
            ordenar_b(v)
            cont += 1
            print(v[i])
    print('Ningun servicio cumple con esta condicion.')

