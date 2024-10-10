class Cobros:
    def __init__(self, dia, tipo, monto, cuenta):
        self.dia = dia
        self.tipo = tipo
        self.monto = monto
        self.cuenta = cuenta

    def __str__(self):
        r = f' Dia del cobro: {self.dia}'
        r += f' Tipo de servicio: {self.tipo}'
        r += f' Monto cobrado: {self.monto}'
        r += f' Numero de cuenta asocidada al pago: {self.cuenta}'
        return r
