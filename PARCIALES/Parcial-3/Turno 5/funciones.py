from clase import Publicaciones
import random


def val_intervalo(men, may, msj):
    val = int(input(msj))
    while may < val or val < men:
        print(f'Valor invalido ingrese un numero entre {men} y {may}')
        val = int(input(msj))
    return val


def val_may(men, msj):
    val = int(input(msj))
    while val <= men:
        print(f'Valor invalido ingrese un numero mayor a {men}')
        val = int(input(msj))
    return val


def opcion_a():
    n = val_may(0, 'Ingrese cantidad de publicaciones: ')
    v = n * [0]
    codigos = ['CASDAS', 'ASD12CASD', 'XCACSAASDASD', 'ZASDDASD']
    titulo = ['CASDAS123123', 'asdas', 'asdas', 'asdas']
    for i in range(len(v)):
        #cod, tit, pub, costo
        cod = random.choice(codigos)
        tit = random.choice(titulo)
        pub = random.randint(1,30)
        costo = random.randint(1000,2000)
        v[i] = Publicaciones(cod,tit,pub,costo)
        print(v[i])
    return v

def opcion_c(v):
    cant_tipos = 30 * [0]
    for i in range(len(v)):
        cant_tipos[v[i].tipo] += 1
    return cant_tipos
