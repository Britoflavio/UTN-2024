import clases
import os.path

def validar_rango(menor, mayor, mensaje):

    valor = int(input(mensaje))
    while mayor < valor or valor < menor:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(mensaje))
    return valor

def validar_mayor(menor, mensaje):

    valor = int(input(mensaje))
    while valor <= menor:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(mensaje))
    return valor

def ordenar(v):

    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].cp > v[j].cp:
                v[i], v[j] = v[j], v[i]
def cargar(vec, formato, archivo):

    if not os.path.exists(archivo):
        print('El archivo', archivo, 'no existe')
        return

    pr = True
    m = open(archivo, "rt")
    for line in m:

        if pr is True:
            if "SC" in line:
                formato = "SC"
            pr = False
        else:
            cp = line[0:9].strip().upper()
            direccion = line[9:29].strip()
            tipo = int(line[29])
            pago = int(line[30])
            env = clases.Envio(cp, direccion, tipo, pago)
            vec.append(env)

    m.close()
    return formato

def punto1(vec, formato, archivo):
    if len(vec) != 0:
        r = int(input("Quieres borrar los datos previos? 1: Si / 2: No (volver al menu): "))
        if r == 1:
            vec = []
            formato = cargar(vec, formato, archivo)
            print("Carga terminada")
        else:
            print("Carga cancelada")
    else:
        formato = cargar(vec, formato, archivo)
        print("Carga terminada")

    print()
    return vec, formato
def opcion2(v):

    m = validar_mayor(0, "Cuantos registros quiere agregar al arreglo (al menos 1)?: ")

    for i in range(m):
        cp = input("Codigo postal: ")
        destino = input("Direccion envio: ")
        tipo = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
        pago = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")
        envio = clases.Envio(cp, destino, tipo, pago)
        v.append(envio)

    print("Carga terminada")
    print()

def opcion3(v):

    n = len(v)
    ordenar(v)
    print("Hay", n, "registros en el arreglo")
    m = validar_rango(1, n, "Cantidad a mostrar (al menos 1 y no mas de " + str(n) + ")?: ")
    print("Listado de envios ordenados por codigo postal...")

    for i in range(m):
        print(v[i], 'Pais:', clases.Envio.cp(v[i]))

def opcion4(vec):

    n = len(vec)
    destino = input("Ingrese direccion de destino: ")
    tipo = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")

    for i in range(n):
        if vec[i].destino == destino and vec[i].tipo == tipo:
            return vec[i]

def opcion5(vec):

    n = len(vec)
    x = input('Ingresar cp: ')

    for i in range(n):
        if vec[i].cp == x:
            if vec[i].pago == 1:
                vec[i].pago = 2
            else:
                vec[i].pago = 1
            return vec[i]

def opcion6(vec, formato):
    n = len(vec)
    vec_conteo = 7 * [0]

    for i in range(n):

        if formato == 'HC':
            destino = clases.Envio.vali_direc(vec[i].destino)
            if destino is True:
                num = vec[i].tipo
                vec_conteo[num] += 1

        else:
            num = vec[i].tipo
            vec_conteo[num] += 1
    return vec_conteo
def opcion7(vec, formato):
    n = len(vec)
    vec_finales = 7 * [0]

    for i in range(n):
        final = clases.Envio.final_amount(vec[i])
        if formato == 'HC':
            destino = clases.Envio.vali_direc(vec[i].destino)
            if destino is True:
                num = vec[i].tipo
                vec_finales[num] += final
        else:
            num = vec[i].tipo
            vec_finales[num] += final
    return vec_finales
def ordenar_monto(vec):
    n = len(vec)
    for i in range(n - 1):
        for j in range(i+1, n):
            if vec[i] > vec[j]:
                vec[i], vec[j] = vec[j], vec[i]
    return vec[-1]
def buscar_monto(vec, x):
    for i in range(len(vec)):
        if x == vec[i]:
            return i
    return -1

#PUNTO 8
def opcion8(vec):

    n = len(vec)
    monto_total = 0


    ordenar_monto(vec)
    monto_mayor = vec[-1]

    for i in range(n-1):
        monto_total += vec[i]
    porc = (monto_mayor * 100) // monto_total
    return porc, monto_mayor


#PUNTO 9
def prom_total(vec):
    importe_final = 0
    envios_total = len(vec)

    for i in range(envios_total):
        importe_envio = clases.Envio.final_amount(vec[i])
        importe_final += importe_envio
    return importe_final // envios_total

def menor_promedio(vec, prom):

    cont_menor = 0
    envios = len(vec)
    for i in range(envios):
        importe_envio = clases.Envio.final_amount(vec[i])
        if prom > importe_envio:
            cont_menor += 1
            print(importe_envio)
    return cont_menor