class Empleo:
    def __init__(self, id, descripcion, tipo, retribucion):
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.retribucion = retribucion

    def __str__(self):
        r = f'Numero de identificacion del empleo: {self.id}'
        r += f' Descripcion del empleo: {self.descripcion}'
        r += f' Tipo de empleo: {self.tipo}'
        r += f' Retribucion: {self.retribucion}'
        return r
