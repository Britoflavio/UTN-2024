from funciones import *


def main():
    op = 0
    v = []

    while op != 5:
        print('1.')
        print('2.')
        print('3.')
        print('4.')
        print('5. Finalizar programa.')
        op = validar_intervalo(1, 5, 'Ingrese un valor: ')

        if op == 1:
            v = opcion_a()
        elif op == 2:
            mon = int(input('Ingrese el mononto minimo: '))
            if mon != 0:
                cant = opcion_b(v, mon)
                print('Cantidad de juicios mostrados: ', cant)
            else:
                print('No puede ingresar cero como valor.')
        elif op == 3:
            pass
        elif op == 4:
            pass


if __name__ == '__main__':
    main()
