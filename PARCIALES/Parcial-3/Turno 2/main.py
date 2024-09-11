from funciones import *


def main():
    op = 0
    v = []
    while op != 5:
        print('GESTION DE INFORMACION DE LOS TICKETS VENDIDOS')
        print('1.Cargar datos de n tickets')
        print('2.Mostrar los datos de todos los tickets cuyo número de asiento sea mayor al numero ingresado')
        print('3.Buscar importes mayores')
        print('4.')
        op = validacion_rango(1, 5, 'Ingrese numero de opcion: ')

        if op == 1:
            v = punto_a()
            print()
        elif op == 2:
            if len(v) != 0:
                punto_b(v)
                print()
            else:
                print('No hay registro de tickets.')
        elif op == 3:
            punto_c(v)
        elif op == 4:
            op4 = opcion_d(v)
            if op4 != -1:
                print(op4)
            else:
                print('No existe. ')


if __name__ == '__main__':
    main()
