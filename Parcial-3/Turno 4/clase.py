class Juico:
    def __init__(self, expediente, descrip, tipo, cliente, monto):
        self.expediente = expediente
        self.descripcion = descrip
        self.tipo = tipo
        self.cliente = cliente
        self.monto = monto

    def __str__(self):
        r = 'Codigo de expediente: ' + str(self.expediente)
        r += ' Descripcion del juicio: ' + self.descripcion
        r += ' Tipo de juicio: ' + str(self.tipo)
        r += ' Nombre del cliente: ' + self.cliente
        r += ' Monto  a cobrar: ' + str(self.monto)
        return r
