from funciones import *


def main():
    op = 0
    ARCHIVO_DAT = 'cobros.dat'
    while op != 6:
        print('1.')
        print('2.')
        print('3.')
        print('4.')
        print('5.')
        print('6. Salir')
        op = int(input('Ingrese opcion a realizar: '))
        if op == 1:
            opcion_a(ARCHIVO_DAT)
        elif op == 2:
            cuenta_buscada = int(input('Ingrese cuenta a buscar:'))
            encontrada, total = opcion_b(cuenta_buscada, ARCHIVO_DAT)
            if encontrada:
                print(f'El total de la cuenta {cuenta_buscada} es de : ${total}')
            else:
                print(f'No se encontro la cuenta {cuenta_buscada}')
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass


if __name__ == '__main__':
    main()
