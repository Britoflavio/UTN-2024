class Registro:
    def __init__(self, dni, mon, tipo):
        self.dni = dni
        self.monto = mon
        self.tipo = tipo

    def __str__(self):
        r = f'Reserva por documento: {self.dni}'
        r += f' Monto a agar: {self.monto}'
        r += f' Tipo de casa: {self.tipo}'
        return r

