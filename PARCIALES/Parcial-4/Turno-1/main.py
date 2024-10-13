from funciones import *


def main():
    op = 0
    v = []
    while op != 6:
        print('1. Cargar lotes')
        print('2. Mostrar lotes')
        print('3. Mostrar superficie total vendida por manzana')
        print('4. Generar archhivo')
        print('5. Mostrar archivo')
        print('6. Salir')
        op = int(input('Ingrese una opcion: '))
        if op == 1:
            v = opcion_a()
        elif op == 2:
            if v:
                opcion_b(v)
            else:
                print('No hay registros.')
                print()
        elif op == 3:
            if v:
                opcion_c(v)
            else:
                print('No hay registros.')
                print()
        elif op == 4:
            pass
        elif op == 5:
            pass


if __name__ == '__main__':
    main()
