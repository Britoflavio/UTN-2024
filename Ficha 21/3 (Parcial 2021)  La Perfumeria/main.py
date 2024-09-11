from funciones import *


def main():
    op = 0
    vector = []
    while op != 6:
        print('1.Cargar ventas')
        print('2.Mostrar facturas especificas')
        print('3.Importe total de un tipo de perfume')
        print('4.Datos de ventas especifico')
        print('5.Buscar una venta')
        print('6.Salir')
        op = validar_rango(0, 7, 'Ingrese una opcion: ')

        if op == 1:
            vector = opcion_1()
        elif op == 2:
            opcion_2(vector)

        elif op == 3:
            x = int(input('Ingrese el tipo de marca:'))
            acumulado = opcion_3(vector, x)
            if acumulado != 0:
                print('El  total acumulado es: ', acumulado)
            else:
                print('El tipo elegido aun no tiene compras registradas.')
        elif op == 4:
            mostrar(vector)

        elif op == 5:
            op5 = opcion_5(vector)
            if op5 != -1:
                print(op5)
            else:
                print('No existe la factura buscada.')


if __name__ == '__main__':
    main()
