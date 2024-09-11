class Envio:
    def __init__(self, cp, destino, tipo, pago):
        self.cp = cp
        self.destino = destino
        self.tipo = tipo
        self.pago = pago

    def cp(self):
        n = len(self.cp)
        if n < 4 or n > 9:
            return 'Otro'
        # Argentina
        if n == 8:
            if self.cp[0].isalpha() and self.cp[0] not in 'IO' and self.cp[1:5].isdigit() and self.cp[5:8].isalpha():
                return 'Argentina'
            else:
                return 'Otro'
        # Brasil
        if n == 9:
            if self.cp[0:5].isdigit() and self.cp[5] == '-' and self.cp[6:9].isdigit():
                return 'Brasil'
            else:
                return 'Otro'
        if self.cp.isdigit():
            # Bolivia
            if n == 4:
                return 'Bolivia'
            # Chile
            if n == 7:
                return 'Chile'
            # Paraguay
            if n == 6:
                return 'Paraguay'
            # Uruguay
            if n == 5:
                return 'Uruguay'
        return 'Otro'

    def final_amount(self, cp):

        importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
        monto = importes[self.tipo]
        if cp == 'Argentina':
            inicial = monto
        else:
            if cp == 'Bolivia' or cp == 'Paraguay' or (cp == 'Uruguay' and self.cp[0] == '1'):
                inicial = int(monto * 1.20)
            elif cp == 'Chile' or (cp == 'Uruguay' and self.cp[0] != '1'):
                inicial = int(monto * 1.25)
            elif cp == 'Brasil':
                if self.cp[0] == '8' or self.cp[0] == '9':
                    inicial = int(monto * 1.20)
                else:
                    if self.cp[0] == '0' or self.cp[0] == '1' or self.cp[0] == '2' or self.cp[0] == '3':
                        inicial = int(monto * 1.25)
                    else:
                        inicial = int(monto * 1.30)
            else:
                inicial = int(monto * 1.50)

        final = inicial
        if self.pago == 1:
            final = int(0.9 * inicial)

        return final

    def vali_direc(self):
        cant_caracter = cant_dig = 0
        todo_digito = False
        anterior = " "
        v = self
        for letra in v:
            if letra in " .":
                if cant_caracter == cant_dig:
                    todo_digito = True
                cant_caracter = cant_dig = 0
                anterior = " "
            else:
                cant_caracter += 1
                if not letra.isdigit() and not letra.isalpha():
                    return False
                if anterior.isupper() and letra.isupper():
                    return False
                if letra.isdigit():
                    cant_dig += 1
                anterior = letra
        return todo_digito

    def __str__(self):
        r = 'Codigo Postal: ' + str(self.cp)
        r += ' Direccion: ' + str(self.destino)
        r += ' Tipo de envio: ' + str(self.tipo)
        r += ' Forma de pago: ' + str(self.pago)
        return r
