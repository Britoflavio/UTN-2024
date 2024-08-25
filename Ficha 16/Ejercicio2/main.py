import utils2

def main():

    n = utils2.cant_alumnos()
    v = n * [0]
    asignados = utils2.asignar_legajo(v)
    vector_ordenado = utils2.ordenar(asignados)
    print('Legajos ordenados de menor a mayor: ', vector_ordenado)

    legajo = int(input('Ingrese el legajo a buscar: '))
    buscador_legajo = utils2.buscar_legajo(vector_ordenado, legajo)
    if buscador_legajo == -1:
        print('El legajo no existe.')
    else:
        print('Legajo encontrado existosamente:', buscador_legajo)

if __name__ == '__main__':
    main()