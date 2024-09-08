from funciones import *


def main():
    op = 0
    vector = []
    while op != 6:
        print('1.Cargar ventas')
        print('2.')
        print('3.')
        print('4.')
        print('5.')
        print('6.Salir')
        op = validar_rango(0, 7, 'Ingrese una opcion: ')

        if op == 1:
            vector = opcion_1()
        elif op == 2:
            opcion_2(vector)

        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass


if __name__ == '__main__':
    main()
