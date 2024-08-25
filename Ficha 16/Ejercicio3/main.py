import utils3
def main():

    n = 7
    v = [0] * n

    valores = utils3.puntaje_random(v)
    suma = utils3.promedio(v)
    ordenados = utils3.puntos_ordenados(v)
    print('Mejores tres notas :', ordenados[n - 3:])

    nota = int(input('Buscar nota deseada: '))
    nota_encontrada = utils3.buscador_nota(v, nota)
    if nota_encontrada == -1:
        print('No se registro una nota con el valor deseado.')
    else:
        notas_mayores = []
        for i in v:
            if i > nota_encontrada:
                notas_mayores.append(i)
        print('Notas mayores a la nota registrada:', notas_mayores)

    print('Diferencia entre el mayor y meno puntaje:', ordenados[-1] - ordenados[0])

    puntaje = utils3.total(v)
    prom = utils3.promedio(v[1:6])
    if puntaje < 20:
        print('La pareja esta descalificada:', puntaje)
    else:
        print('Estan clasificados, promedio: ', prom)


if __name__ == '__main__':
    main()