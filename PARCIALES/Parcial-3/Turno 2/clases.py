class Ticket:
    def __init__(self, codigo, id, destino, asiento, valor):
        self.codigo = codigo
        self.id = id
        self.destino = destino
        self.asiento = asiento
        self.valor = valor

    def __str__(self):
        r = 'Codigo de vuelo: ' + self.codigo
        r += ' Numero de identificacion pasajero: ' + str(self.id)
        r += ' Destino vuelo: ' + str(self.destino)
        r += ' Asiento designado: ' + str(self.asiento)
        r += ' Precio del vuelo: ' + str(self.valor)
        return r
