class Pantalon:
    def __init__(self, cd, nom, tal, tal_c, tipo, stock):
        self.codigo = cd
        self.nombre = nom
        self.talle = tal
        self.talle_cin = tal_c
        self.tipo = tipo
        self.stock = stock

    def __str__(self):
        r = f'Codigo de producto: {self.codigo}'
        r += f' -Nombre del modelo: {self.nombre}'
        r += f' -Talle de largo: {self.talle}'
        r += f' -Talle de cintura: {self.talle_cin}'
        r += f' -Tipo de tela: {self.tipo}'
        r += f' -Stock disponible: {self.stock}'
        return r
