import random

class Ronda:
    def __init__(self,nombre):
        self.nombre = nombre
        self.numero = random.randint(1,12)
        self.palo = random.choice(('Basto', 'Copa', 'Oro', 'Espada'))
    def __str__(self):
        r = 'Nombre del jugador: ' + self.nombre
        r += ' CARTA = ' + str(self.numero)
        r += self.palo
        return r