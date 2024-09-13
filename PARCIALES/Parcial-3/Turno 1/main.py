from funciones import *


def main():
    op = 0
    v = []

    while op != 5:
        print('1.Cargar empleos')
        print('2.Mostrar empleos')
        print('3.Cantidad de empleos por tipo')
        print('4.Buscar empleo especifico')
        print('5. Finalizar programa')
        op = validar_intervalor(1, 5, 'Ingrese una opcion: ')

        if op == 1:
            v = opcion_a()
        elif op == 2:
            if len(v) != 0:
                op2 = opcion_b(v)
                print('Valor acumulado de los empleados mostrados: ', op2)
            else:
                print('No existen empleos registrados.')
        elif op == 3:
            if len(v) != 0:
                acum = opcion_c(v)
                for i in range(len(acum)):
                    if acum[i] > 0:
                        print('Cantidad de empleos de tipo ' + str(i) + ':', acum[i])
            else:
                print('No existen empleos registrados.')

        elif op == 4:
            if len(v) != 0:
                rest = opcion_d(v)
                if rest is not None:
                    print(rest)
                else:
                    print('No se encontro identificador.')
            else:
                print('No hay registros de empleos')


if __name__ == '__main__':
    main()
