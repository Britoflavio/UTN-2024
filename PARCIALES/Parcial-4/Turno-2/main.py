from funciones import *
def main():
    v = []
    op = 0
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
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass
if __name__ == '__main__':
    main()