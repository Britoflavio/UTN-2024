class Servicio:
    def __init__(self, iden, nom, serv, imp):
        self.identificador = iden
        self.nombre = nom
        self.tipo = serv
        self.importe = imp

    def __str__(self):
        r = f'Codigo identificatorio: {self.identificador} ;'
        r += f' Nombre del cliente: {self.nombre} ;'
        r += f' Tipo de servicio prestado: {self.tipo} ;'
        r += f' Importe a pagar: {self.importe}'
        return r
