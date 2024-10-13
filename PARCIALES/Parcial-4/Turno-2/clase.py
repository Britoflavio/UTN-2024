class Libro:
    def __init__(self, isbn, tit, autor, idioma, precio):
        self.isbn = isbn
        self.titulo = tit
        self.autor = autor
        self.idioma = idioma
        self.precio = precio

    def __str__(self):
        r = f'Numero de ISBN: {self.isbn}'
        r += f' -Titulo: {self.titulo}'
        r += f' -Autor: {self.autor}'
        r += f' -Idioma: {self.idioma}'
        r += f' -Precio: {self.precio}'
        return r