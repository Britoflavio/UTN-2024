import soporte

v = soporte.vector_unknown_range(300000)
entrada = [1, 5, 3, 3, 3, 2, 3, 4, 5]

cont = []
num = []

def buscar_secuencial(v, x):

    for i in range(len(v)):
        if v[i] == x:
            return i
    return -1

for i in v:
    nro = buscar_secuencial(num, i)
    if nro == -1:
        num.append(i)
        cont.append(1)
    else:
        cont[nro] += 1
print(len(num))