import random
from clases import Ticket


def validacion_rango(men, may, msj):
    n = int(input(msj))
    while may < n or n < men:
        print('El valor ingresado no es correcto. Ingrese otro valor.')
        n = int(input(msj))
    return n


def validar_n(n, mensaje):
    valor = int(input(mensaje))
    while valor <= n:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(mensaje))
    return valor


def punto_a():
    n = int(input('Cantidad ticket a cargar(minimo 1).'))
    v = n * [0]
    codigo_vuelo = ['AA25', 'AB52', 'CB23', 'CC2']
    for i in range(n):
        codigo = random.choice(codigo_vuelo)
        id = i
        destino = random.randint(0, 20)
        asiento = random.randint(1, 100)
        valor = random.randint(200, 20000)
        v[i] = Ticket(codigo, id, destino, asiento, valor)

    return v


def mostrar(v):
    for i in range(len(v)):
        print(v[i])


def ordenar(v):
    m = len(v)
    for i in range(m - 1):
        for j in range(i + 1, m):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]


def punto_b(v):
    m = len(v)
    n = validar_n(0, 'Ingrese numero: ')
    for i in range(m):
        if v[i].asiento > n:
            ordenar(v)
            print(v[i])


def punto_c(v):
    m = validar_n(0, 'Ingrese un valor: ')
    may = []
    d = destinos_array(v)
    for i in range(len(d)):
        if d[i] > m:
            may.append(d[i])
    print(may)


def destinos_array(v):
    n = len(v)
    destinos = 21 * [0]
    for i in range(n):
        num = v[i].destino
        destinos[num] += v[i].valor
    return destinos


