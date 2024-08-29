import utils
def main():


    jugador1 = jugador2 = 0

    jugadores = 2 * [None]

    for i in range(3):
        utils.cartas(jugadores)
        utils.mostrar(jugadores)
        jugador1, jugador2 = utils.ganador(jugadores, jugador1, jugador2)

    if jugador1 > jugador2:
        print('El ganador es: ' + jugadores[0].nombre + ' con ' + str(jugador1) + ' puntos')
    elif jugador1 < jugador2:
        print('El ganador es: ' + jugadores[1].nombre + ' con ' + str(jugador2) + ' puntos')
    else:
        print('Empate! ambos jugadores consiguieron' + str(jugador1))

if __name__ == '__main__':
    main()