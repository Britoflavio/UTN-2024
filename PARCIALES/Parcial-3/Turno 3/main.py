from funciones import *


def main():
    op = 0
    v = []

    while op != 5:
        print('1. Cargar servicios')
        print('2. Mostrar servicios mediante un importe intermedio')
        print('3. Mostrar la cantidad de servicios del mismo tipo')
        print('4.')
        print('5. Salir')
        op = val_intervalo(1,5, 'Ingrese una opcion: ')
        if op == 1:
            v = opcion_a()
        elif op == 2:
            if len(v) != 0:
                opcion_b(v)
                print()
            else:
                print('Primero debe cargar como minimo un servicio')
                print()
        elif op == 3:
            if len(v) != 0:
                acum = opcion_c(v)
                for i in range(len(acum)):
                    if acum[i] > 0:
                        print(f'Cantidad de serivicios de tipo {i + 1}: {acum[i]}')
            else:
                print('No hay registros de serivios, cargue al menos uno.')
        elif op == 4:
            if len(v) != 0:
                opcion_d(v)
            else:
                print('No hay registros de servicios, cargue servicios antes de continuar.')


if __name__ == '__main__':
    main()
