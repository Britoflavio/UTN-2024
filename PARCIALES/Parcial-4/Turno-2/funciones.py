from clase import Libro
import random
import pickle
import os.path

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
    autores = ['fla', 'sole', 'carlo', 'carla', 'pedrin']

    for i in range(n):
        isbn = random.randint(1000000000000,9999999999999)
        titulo = random.choice(titulos)
        autor = random.choice(autores)
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
    print()

def bsucar_isbn(v, n):

    m = len(v)
    izq, der = 0, m - 1
    while izq <= der:
        prom = (izq + der) // 2
        if n == v[prom].isbn:
            return prom
        else:
            if n < v[prom].isbn:
                der = prom - 1
            else:
                izq = prom + 1

    return -1

def opcion_c(v,pos):
    print(v[pos])
    print()
    if v[pos].idioma == 'frances':
        v[pos].precio = round(v[pos].precio * 0.78, 2)
        print('Precio con 22% descuento')
        print(v[pos])
        print()

def opcion_d(v, arch_bin, a , p):
    m = open(arch_bin, 'wb')
    for i in range(len(v)):
        if v[i].autor == a:
            if p > v[i].precio:
                pickle.dump(v[i],m)
    m.close()

def opcion_e(arch_bin):
    if not os.path.exists(arch_bin):
        print(f'No existe el archivo {arch_bin}.')
        print()
        return

    size = os.path.getsize(arch_bin)
    m = open(arch_bin, 'rb')
    cant_lib = 0
    while m.tell() < size:
        cant_lib += 1
        libs = pickle.load(m)
        print(libs)
    print(f'Hay {cant_lib} libros en el archivo')
    print()
    m.close()
