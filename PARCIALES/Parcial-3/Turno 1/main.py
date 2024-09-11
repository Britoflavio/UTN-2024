from funciones import *


def main():
    op = 0
    v = []

    while op != 5:
        print('1.')
        print('2.')
        print('3.')
        print('4.')
        print('5. Finalizar programa')
        op = validar_intervalor(1, 5, 'Ingrese una opcion: ')

        if op == 1:
            v = opcion_a()
        elif op == 2:
            if len(v) != 0:
                op2 = opcion_b(v)
                print('Valor acumulado de los empleados mostrados: ', op2)
            else:
                print('Primero debes cargar el vector con la opcion 1.')

        elif op == 3:
            pass
        elif op == 4:
            pass



if __name__ == '__main__':
    main()
