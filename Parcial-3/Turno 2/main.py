import funciones

def main():
    op = 0
    v = []
    while op != 5:
        print('GESTION DE INFORMACION DE LOS TICKETS VENDIDOS')
        print('1.Cargar datos de n tickets')
        print('2.Mostrar los datos de todos los tickets cuyo número de asiento sea mayor al numero ingresado')
        print('3.Buscar importes mayores')
        print('4.')
        op = funciones.validacion_rango(0, 6, 'Ingrese numero de opcion: ')

        if op == 1:
            v = funciones.punto_a()
            print()
        elif op == 2:
            if len(v) != 0:
                funciones.punto_b(v)
                print()
            else:
                print('No hay registro de tickets.')
        elif op == 3:
            funciones.punto_c(v)
if __name__ == '__main__':
    main()
