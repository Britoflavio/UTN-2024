import clases
def cartas(v):
    for i in range(len(v)):
        nombre = input('Nombre del jugador ' + str(i + 1) + ': ')
        v[i] = clases.Ronda(nombre)

def mostrar(v):
    for i in range(len(v)):
        print('La carta de ' + v[i].nombre + ' es: ' + str(v[i].numero) + ' ' + v[i].palo)
def ganador(v, j1, j2):

    if v[0].numero > v[1].numero:
        j1 += (v[0].numero + v[1].numero)
    elif v[0].numero < v[1].numero:
        j2 += (v[0].numero + v[1].numero)
    else:
        if v[0].palo == 'Oro':
            j1 += (v[0].numero + v[1].numero)
        elif v[1].palo == 'Oro':
            j2 += (v[0].numero + v[1].numero)
        else:
            j1 += v[0].numero
            j2 += v[1].numero
    return j1, j2