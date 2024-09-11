from clases import Venta
import random


def validar_rango(men, may, msj):
    valor = int(input(msj))
    while may < valor or valor < men:
        print('Valor ingresado incorrectamente. Ingrese un valor valido...')
        valor = int(input(msj))
    return valor


def validar_may(may, msj):
    valor = int(input(msj))
    while may >= valor:
        print('Valor ingresado incorrectamente. Ingrese un valor valido...')
        valor = int(input(msj))
    return valor


def opcion_1():
    n = validar_may(0, 'Cuantas ventas quieres ingresar(minima 1 venta)? ')
    v = n * [0]
    tipos = ['A', 'B', 'C', 'E']
    apellidos = ['Robert', 'Jorgeal', 'Brito', 'Santos', 'Robertes', 'EsJorgeal', 'AsBrito', 'OsSantos']
    for i in range(n):
        # num, importe, tipo, apellido, marca
        num = random.randint(0, 200000)
        importe = random.randint(22000, 30000)
        tipo = random.choice(tipos)
        apellido = random.choice(apellidos)
        marca = random.randint(1, 17)

        v[i] = Venta(num, importe, tipo, apellido, marca)

    return v


def mostrar(v):
    for i in range(len(v)):
        print(v[i])


def ordenar(vec):
    n = len(vec)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vec[i].apellido > vec[j].apellido:
                vec[i], vec[j] = vec[j], vec[i]


def opcion_2(vec):
    x = int(input('Buscar importes mayores a: '))
    t = input('Tipo de factura distinto a: ')
    for i in range(len(vec)):
        if vec[i].importe > x and vec[i].tipo != t.isupper():
            ordenar(vec)
            print(vec[i])


def opcion_3(vec, x):
    n = len(vec)
    tipos = 17 * [0]
    for i in range(n):
        marca = vec[i].marca
        tipos[marca] += vec[i].importe

    return tipos[x - 1]


def opcion_4(vec):
    n = len(vec)

    for i in range(n):
        if 5 < vec[i].marca < 12 and vec[i].tipo != 'C':
            r = 'Numero de factura: ' + str(vec[i].factura)
            r += ' Comprador: ' + vec[i].apellido
            r += ' Importe: ' + '$' + str(vec[i].importe)
            print(r)


def opcion_5(vec):
    n = int(input('Ingrese un numero de factura: '))
    p = int(input('Cargar importe para buscar importes menores: '))
    for i in range(len(vec)):
        if vec[i].factura == n and vec[i].importe < p:
            return vec[i]
    return -1

