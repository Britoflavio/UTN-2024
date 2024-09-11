import funciones


def main():
    archivo = 'envios-tp3.txt'
    formato = 'HC'
    vec = []
    cant_final = []
    op = 0
    while op != 10:
        print("1. Cargar arreglo desde archivo de texto")
        print("2. Cargar arreglo desde teclado")
        print("3. Listado ordenado")
        print("4. Busqueda por direccion")
        print("5. Busqueda por codigo postal")
        print("6. Cantidad de envios con direccion válida por tipo")
        print("7. Importe final acumulado")
        print("8. Envio con mayor importe")
        print("9. Importe final promedio")
        print("10. Salir")
        op = funciones.validar_rango(1, 10, "Ingrese numero de opcion: ")

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
            x = input('Ingresar cp: ')
            cp = funciones.opcion5(vec, x)
            if cp == -1:
                print('No existe registro del siguiente cp: ' + str(x))
            else:
                print('Registro encontrado, valor de forma de pago cambiado con exito.')
                print('Registro actualizado: ', cp)

        elif op == 6:
            if len(vec) != 0:
                cant = funciones.opcion6(vec, formato)
                print('Formato: ', formato)
                for i in range(7):
                    print("Direccion valida en el tipo " + str(i) + ":", cant[i])

            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()
        elif op == 7:
            if len(vec) != 0:
                cant_final = funciones.opcion7(vec, formato)
                print('Formato: ', formato)
                for i in range(7):
                    print("Importe acumulado tipo " + str(i) + ":" + "$", cant_final[i])
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()
        elif op == 8:
            if len(cant_final) != 0:
                porc, tipo_may = funciones.opcion8(cant_final)
                print('Porcentaje que representa el monto mayor: ' + str(porc) + '%')
                print('Tipo de envio con mayor importe:', tipo_may)
            else:
                print('Para realizar este procedimiento primero debes seleccionar la opcion 7.')

        elif op == 9:
            if len(vec) != 0:
                prom = funciones.prom_total(vec)
                print('El promedio total entre todos los envios del arreglo es de: ', prom)
                envios_men = funciones.menor_promedio(vec, prom)
                print('Hay un total de ', envios_men, ' envios que tuvieron un importe menor al promedio.')
            else:
                print('No hay datos en el arreglo')


if __name__ == '__main__':
    main()
