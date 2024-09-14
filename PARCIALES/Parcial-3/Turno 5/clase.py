class Publicaciones:
    def __init__(self, cod, tit, pub, costo):
        self.codigo = cod
        self.titulo = tit
        self.tipo = pub
        self.costo = costo

    def __str__(self):
        r = f'Codigo de identificacion: {self.codigo}'
        r += f' Titulo: {self.titulo}'
        r += f' Tipo de publicacion: {self.tipo}'
        r += f' Costo de produccion: {self.costo}'
        return r
