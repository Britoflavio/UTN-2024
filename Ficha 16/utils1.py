def cargar_valores(v):
    n = len(v)
    for i in range(n):
        v[i] = int(input('Ingrese numeros: '))

    return v
def ordenar(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i + 1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
    return v

def busqueda_binaria(array, numero):
    izq, der = 0, len(array)-1
    while izq <= der:
        c = (izq + der) // 2
        if numero == array[c]:
            return c
        if numero < array[c]:
            der = c - 1
        else:
            izq = c + 1
    return -1
def impares(array, numero):
    cont = 0
    for i in array:
        if i > numero:
            cont += 1
    return cont