class Lote:
    def __init__(self, iden, manz, lote, terr, superf, val):
        self.nombre = iden
        self.manzana = manz
        self.lote = lote
        self.orientacion = terr
        self.terreno = superf
        self.valor = val

    def __str__(self):
        r = f'Nombre del propetario: {self.nombre}'
        r += f' -Numero de la manzana: {self.manzana}'
        r += f' -Numero de lote: {self.lote}'
        r += f' -Orientacion del terreno: {self.orientacion}'
        r += f' -Superficie del terreno en metro cuadrado: {self.terreno}'
        r += f' -Monto de venta del lote: {self.valor}'
        return r