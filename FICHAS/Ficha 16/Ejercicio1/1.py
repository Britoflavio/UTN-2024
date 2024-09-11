import utils1
def main():

    n = int(input('Ingrese la cantidad de valores que deseas ingresar, entre 1 y 100: '))
    if 1 <= n <= 100:

        v = [0] * n
        new = utils1.cargar_valores(v)
        new_order = utils1.ordenar(new)
        m = int(input('Ingrese numero que desea buscar:'))
        numero_buscado = utils1.busqueda_binaria(new, m)

        if numero_buscado == -1:
            print('El numero no existe')
        else:
            valores_may = utils1.impares(new_order, m)
            print('cantindad de impares:', valores_may)

        print('Vector ordenado ascendetemente: ', new_order)
    else:
        print('La cantidad de valores debe ser del 1 al 100, sin excepcion.')





if __name__ == '__main__':
    main()