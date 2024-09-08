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
    for i in range(n):
        # num, importe, tipo, apellido, marca
        num = random.randint(0, 200000)
        importe = random.randint(22000, 30000)
        tipo = random.choice(tipos)
        apellido = input('Apellido del cliente: ')
        marca = random.randint(1, 17)
        v[i] = Venta(num, importe, tipo, apellido, marca)
    print(v)
    return v

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
        if vec[i].importe > x and vec[i].tipo != t:
            ordenar(vec)

        print(vec[i])
