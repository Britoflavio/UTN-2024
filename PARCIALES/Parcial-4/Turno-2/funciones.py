from clase import Libro
import random
def val_interval(men,may,msj):
    val = int(input(msj))
    while men > val or val > may:
        print(f'Valor invalido, intentar entre {men } y {may }')
        val = int(input(msj))
    return val

def val_minimo(men, msj):
    val = int(input(msj))
    while men > val:
        print(f'Valor invalido, debe ser mayor a {men}')
        val = int(input(msj))
    return val

def opcion_a(v):
    v = []
    n = val_minimo(0, 'Ingrese cantidad de libros: ')
    titulos = ['ASDFD', 'SDFSDF', 'SDFER', 'GSDG', 'SDFDFR', 'DSFGDS']
    autor = ['fla', 'sole', 'carlo', 'carla', 'pedrin']

    for i in range(n):
        isbn = random.randint(1000000000000,9999999999999)
        titulo = random.choice(titulos)
        autor = random.choice(autor)
        idioma = random.randint(1,5)
        precio = random.randint(10000,200000)
        libro = Libro(isbn, titulo, autor, idioma, precio)
        ordenar_op_a(v,libro)
    print('Arreglo cargado.')
    print()
    return v
def ordenar_op_a(v, libro):
    n = len(v)
    x = n
    izq, der = 0, n - 1

    while izq <= der:
        prom = (izq + der) // 2
        if libro.isbn == v[prom].isbn:
            x = prom
            break
        else:
            if libro.isbn < v[prom].isbn:
                der = prom - 1
            else:
                izq = prom + 1
    if izq > der:
        x = izq
    v[x:x] = [libro]

def opcion_b(v):
    idiomas = ['esp', 'ingles', 'port', 'frances', 'italiano']
    for i in range(len(v)):
        n = v[i].idioma
        v[i].idioma = idiomas[n - 1]
        print(v[i])
