import random


class Ticket:
    def __init__(self, codigo, dni):
        self.codigo = codigo
        self.dni = dni
        self.destino = random.randint(1, 20)
        self.asiento = random.randint(1, 70)
        self.valor = random.randint(70, 150)

    def __str__(self):
        r = 'Codigo de vuelo: ' + str(self.codigo)
        r += 'Numero de identificacion pasajero: ' + str(self.dni)
        r += 'Destino vuelo: ' + str(self.destino)
        r += 'Asiento designado: ' + str(self.asiento)
        r += 'Precio del vuelo: ' + str(self.valor)
        return r
