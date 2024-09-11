class Venta:
    def __init__(self, num, importe, tipo, apellido, marca):
        self.factura = num
        self.importe = importe
        self.tipo = tipo
        self.apellido = apellido
        self.marca = marca

    def __str__(self):
        r = 'Numero: ' + str(self.factura)
        r += ' Importe: ' + str(self.importe)
        r += ' Tipo: ' + self.tipo
        r += ' Apellido: ' + self.apellido
        r += ' Marca: ' + str(self.marca)
        return r
