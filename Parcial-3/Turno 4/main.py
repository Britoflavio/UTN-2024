from funciones import *


def main():
    op = 0
    v = []

    while op != 5:
        print('1.Cargar juicios')
        print('2.Mostrar datos de juicios especificos')
        print('3.Mostrar cantidad de juicios')
        print('4.')
        print('5. Finalizar programa.')
        op = validar_intervalo(1, 5, 'Ingrese un opcion del programa: ')

        if op == 1:
            v = opcion_a()
        elif op == 2:
            mon = int(input('Ingrese el monto minimo: '))
            if mon != 0:
                cant = opcion_b(v, mon)
                print('Cantidad de juicios mostrados: ', cant)
            else:
                print('No puede ingresar cero como valor.')
        elif op == 3:
            x = validar_may(0, 'Ingrese el minimo de cantidad de juicios para filtrar: ')
            tipos = opcion_c(v)
            for i in range(len(tipos)):
                if x < tipos[i]:
                    print("Direccion valida en el tipo " + str(i) + ":", tipos[i])
        elif op == 4:
            pass


if __name__ == '__main__':
    main()
