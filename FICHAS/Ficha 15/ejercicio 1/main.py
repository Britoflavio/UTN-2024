import utils
import random
def principal():

    menu = 'Menu de Opciones \n' \
           '=================================== \n' \
           '1 \t Determinar el promedio anual de lluvias \n' \
           '2 \t Determinar el promedio de lluvias para un determinado trimestre \n' \
           '3 \t Determinar el mes más seco del mes \n' \
           '0 \t Salir \n '\
           'Ingrese su opcion: '
    opcion = -1

    lluvias = list()
    for i in range(12):
        lluvias.append(random.uniform(45.8, 160.1))

    while opcion != 0:
        opcion = int(input(menu))
        if opcion == 1:
            prom = utils.promedio_anual(lluvias)
            print('El promedio anual de lluvias en el pais fue', prom, 'mm')
        elif opcion == 2:
            trimestre = utils.prom_trismetral(lluvias)
            print('El promedio de lluvias del trimestre', trimestre[0], 'fue de', trimestre[1], 'mm')
        elif opcion == 3:
            menor = utils.mes_men_lluvia(lluvias)
            print('El mes con menor lluvia registrada fue', menor + 1)


if __name__ == '__main__':
    principal()