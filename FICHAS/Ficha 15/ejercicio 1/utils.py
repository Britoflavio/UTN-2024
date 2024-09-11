def rango_valido(msg='Ingrese un numero:'):
    num = 0
    while 4 < num < 1:
        num = int(input(msg))
        if 4 < num < 1:
            print('El numero ingresado debe estar dentro del intervalo (1,4)')
    return num

def rango_trimestral(t):
    if t == 1:
        return range(3)
    else:
        if t == 2:
            return range(3, 6)
        if t == 3:
            return range(6, 9)
        else:
            return range(9, 12)

def prom_trismetral(lluvia):
    trimestre = rango_valido('Ingrese el trimestre a calcular: ')
    suma = 0
    rango = rango_trimestral(trimestre)
    for i in rango:
        suma += lluvia[i]

    return trimestre, suma / len(rango)

def promedio_anual(lluvia):
    suma = 0
    taman = len(lluvia)

    for i in range(taman):
        suma += lluvia[i]

    return suma / taman
def mes_men_lluvia(lluvia):
    menor = ()
    tam = len(lluvia)

    for m in range(tam):
        if m == 0:
            menor = m, lluvia[m]
        else:
            if menor[1] > lluvia[m]:
                menor = m, lluvia[m]
    return menor[0]

