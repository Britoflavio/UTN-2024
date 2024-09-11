import random

def puntaje_random(v):
    n = len(v)
    for i in range(n):
        v[i] = random.randint(1, 10)
    return v
def puntos_ordenados(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i + 1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
    return v
def buscador_nota(array, nota):
    izq, der = 0, len(array) - 1
    while izq <= der:
        x = (izq + der) // 2
        if nota == array[x]:
            return array[x]
        if nota < array[x]:
            der = x - 1
        else:
            izq = x + 1
    return -1
def total(v):

    cont = 0
    for i in v:
        cont += i
    return cont
def promedio(v):

    total = 0
    for i in v:
        total += i
    return total // len(v)