from funciones import *
def main():
    v = []
    op = 0
    ARCHIVO_BIN = 'libros.dat'
    while op != 6:
        print('1.')
        print('2.')
        print('3.')
        print('4.')
        print('5. ')
        print('6. Salir')
        op = val_interval(1,6, 'Ingrese opcion: ')
        if op == 1:
            v = opcion_a(v)
        elif op == 2:
            if v:
                opcion_b(v)
            else:
                print('No hay registros.')
                print()
        elif op == 3:
            if v:
                n = val_minimo(1000000000000, 'Ingrese ISBN: ')
                pos = bsucar_isbn(v, n)
                if pos != -1:
                    opcion_c(v,pos)
                else:
                    print(f'No encontramos el libro {n}')
            else:
                print('No hay registros cargados.')
        elif op == 4:
            if v:
                a = input('Nombre del autor: ')
                p = int(input('Precio maximo deseado: '))
                opcion_d(v, ARCHIVO_BIN, a, p)
            else:
                print('No existen registros.')
        elif op == 5:
            opcion_e(ARCHIVO_BIN)
if __name__ == '__main__':
    main()