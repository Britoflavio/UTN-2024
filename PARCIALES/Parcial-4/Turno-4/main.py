from funciones import *
def main():
    op = 0
    v = []
    ARCHIVO_BIN = 'piezas.dat'
    while op != 6:
        print('1.')
        print('2.')
        print('3.')
        print('4.')
        print('5.')
        print('6. Salir')
        op = int(input('Ingrese una opcion: '))
        if op == 1:
            v = opcion_a()
        elif op == 2:
            if v:
                opcion_b(v)
            else:
                print('No hay registros existentes.')
                print()
        elif op == 3:
            if v:
                opcion_c(v)
            else:
                print('No hay registros existentes.')
                print()
        elif op == 4:
            if v:
                opcion_d(v, ARCHIVO_BIN)
            else:
                print('No existen registros.')
                print()
        elif op == 5:
            opcion_e(ARCHIVO_BIN)


if __name__ == '__main__':
    main()
