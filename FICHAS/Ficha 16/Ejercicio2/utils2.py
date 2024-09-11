import random
def cant_alumnos():
    n = -1
    while n <= 0:
        n = int(input('Ingrese la cantidad de alumnos: '))
        if n <= 0:
            print('La cantidad de alumnos es invalida.')
    return n
def asignar_legajo(v):
    n = len(v)
    for i in range(n):
        v[i] = random.randint(50000, 55000)
    return v

def ordenar(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
    return v
def buscar_legajo(array, legajo):
    izq, der = 0, len(array) - 1
    while izq <= der:
        x = (izq + der) // 2
        if legajo == array[x]:
            return array[x]
        if legajo < array[x]:
            der = x - 1
        else:
            izq = x + 1
    return -1