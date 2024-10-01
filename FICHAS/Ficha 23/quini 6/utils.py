def val_intervalo(men, may, msj):
    val = int(input(msj))
    while val < men or val > may:
        print(f'Valor ingresado es invalido intente entre {men} y {may}')
        val = int(input(msj))
    return val


def orden_ascendente(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
