from funciones import *
def main():
    op = 0

    while op != 3:
        print('1.Cargar sorteo')
        print('2.Mostrar sorteo')
        print('3. Salir')
        op = int(input('Ingrese opcion: '))

        if op == 1:
            opcion_a()
            print('Sorteo cargado!')
        elif op == 2:
            opcion_b()


if __name__ == '__main__':
    main()
