from funciones import *


def main():
    ARCHIVO_CSV = 'alquileres.csv'
    ARCHIVO_DAT = 'reservas.dat'

    op = 0
    vec = []
    while op != 4:
        print('1.Cargar reservas')
        print('2.Grabar archivo por montos')
        print('3.Mostrar archivo')
        print('4.Salir')
        op = int(input('Ingrese una opcion: '))

        if op == 1:
            vec = opcion_a(ARCHIVO_CSV)
        elif op == 2:
            val = int(input('Ingrese valor minimo base a guardar: '))
            opcion_b(val, ARCHIVO_DAT, vec)
        elif op == 3:
            lista = opcion_c(ARCHIVO_DAT)
            if lista is not None:
                for i in range(len(lista)):
                    print(f'Tipo de casa {i} recaudo ${round(lista[i], 2)}')
            else:
                print('El archivo no tiene registros')


if __name__ == '__main__':
    main()
