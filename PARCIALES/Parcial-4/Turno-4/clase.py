class Pieza:
    def __init__(self, cod, descp, tipo, secto, stock):
        self.codigo = cod
        self.descipcion = descp
        self.tipo = tipo
        self.sector = secto
        self.stock = stock

    def __str__(self):
        r = f'Codigo de identificacion: {self.codigo}'
        r += f' -Descripcion: {self.descipcion}'
        r += f' -Tipo de pieza: {self.tipo}'
        r += f' -Sector dentro del edificio: {self.sector}'
        r += f' -Stock en la empresa: {self.stock}'
        return r
