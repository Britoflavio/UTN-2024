import funciones
1
def main():
    archivo = 'envios-tp3.txt'
    formato = 'HC'
    vec = []


    op = 0
    while op != 10:
        print("1. Cargar arreglo desde archivo de texto")
        print("2. Cargar arreglo desde teclado")
        print("3. Listado ordenado")
        print("4. Busqueda por direccion")
        print("5. Busqueda por codigo postal")
        print("6. Cantidad de envios con direccion válida")
        print("7. Importe final acumulado")
        print("8. Envio con mayor importe")
        print("9. Importe final promedio")
        print("10. Salir")
        op = int(input("Ingrese numero de opcion: "))

        if op == 1:
            vec, formato = funciones.punto1(vec, formato, archivo)
        elif op == 2:
            funciones.opcion2(vec)

        elif op == 3:
            if len(vec) != 0:
                funciones.opcion3(vec)
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()
        elif op == 4:
            m = funciones.opcion4(vec)
            if m is None:
                print('No existe registro.')
            else:
                print('Registro encontrado: ', m)
        elif op == 5:
            cp = funciones.opcion5(vec)
            if cp is None:
                print('No existe registro.')
            else:
                print('Registro encontrado, valor de forma de pago cambiado con exito.')
                print('Registro actualizado: ', cp)

        elif op == 6:
            cant = funciones.opcion6(vec, formato)
            print('Formato: ', formato)
            print('Cantidad de envios por tipo(0, 1, 2 ,3 ,4 ,5 ,6): ', cant)
        elif op == 7:
            cant_final = funciones.opcion7(vec, formato)
            print('Formato: ', formato)
            print('Cantidad de envios por tipo(0, 1, 2 ,3 ,4 ,5 ,6): ', cant_final)

        elif op == 8:
            nuev = funciones.opcion7(vec, formato)
            porc, mont_may = funciones.opcion8(nuev)
            print('Porcentaje que representa el monto mayor: ' + str(porc) + '%')
            print('Tipo de envio con mayor importe:', mont_may) #ACA DEBE SALIR DE 0 AL 6, PERO NO SE ME OCURRE (SEGURO HAY QUE HACER ARRAY BIDIMENSIONAL)
        elif op == 9:
            prom = funciones.prom_total(vec)
            print('El promedio total entre todos los envios del arreglo es de: ', prom)
            envios_men = funciones.menor_promedio(vec, prom)
            print('Hay un total de ', envios_men, ' envios que tuvieron un importe menor al promedio.')



if __name__ == '__main__':
    main()