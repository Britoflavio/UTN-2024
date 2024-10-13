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