from funciones import *


def main():
    op = 0
    v = []

    while op != 5:
        print('1.')
        print('1.')
        print('1.')
        print('1.')
        print('1.')
        op = val_intervalo(1,5, 'Ingrese una opcion: ')

        if op == 1:
            v = opcion_a()
        elif op == 2:
            pass
        elif op == 3:
            x = val_may(0, 'Ingrese cantidad de publicaciones de un tipo a buscar: ')
            contador = opcion_c(v)
            for i in range(len(contador)):
                if x < contador[i]:
                    print(f'Cantidad de publicaciones en el tipo {i}: {contador[i]}')
        elif op == 4:
            pass


if __name__ == '__main__':
    main()
