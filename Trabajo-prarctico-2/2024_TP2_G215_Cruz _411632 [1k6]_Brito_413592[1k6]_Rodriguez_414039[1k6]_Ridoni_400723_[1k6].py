NOMBRE_ARCHIVO = "envios-tp3.txt"
def hc_validacion(direccion):
    anterior = ''
    for letra in direccion:
        if letra in " ." or letra in ' ':
            pass
        else:
            if anterior.isupper() and letra.isupper():
                return False
            if not letra.isalnum():
                return False
        anterior = letra
    return True
def tipos_id(tipo):

    if tipo == 0 or tipo == 1 or tipo == 2:
        return 'Carta Simple'
    if tipo == 3 or tipo == 4:
        return 'Carta Certificada'
    if tipo == 5 or tipo == 6:
        return 'Carta Expresas'
def mayor_cant(r5, r6, r7):

    if r5 > r6 and r5 > r7:
        return 'Carta Simple'
    elif r6 > r5 and r6 > r7:
        return 'Carta Certificada'
    else:
        return 'Carta Expresa'
def importes_id(tipo):
    if tipo == 0:
        return 1100
    elif tipo == 1:
        return 1800
    elif tipo == 2:
        return 2450
    elif tipo == 3:
        return 8300
    elif tipo == 4:
        return 10900
    elif tipo == 5:
        return 14300
    elif tipo == 6:
        return 17900
def identidicar_pais(cp):

    if len(cp) == 8 and cp[0] != "I" and cp[0] != "O" and cp[0].isalpha() and cp[
        1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[4].isdigit() and cp[
        5].isalpha() and cp[6].isalpha() and cp[7].isalpha():
        return "Arg"
    elif len(cp) == 4 and cp.isdigit():
        return "Bol"
    elif (len(cp) == 9 and cp[5] == "-" and cp[
        0].isdigit() and cp[1].isdigit() and cp[2].isdigit() and cp[
              3].isdigit() and cp[4].isdigit() and cp[6].isdigit() and cp[7].isdigit() and cp[
              8].isdigit()):
        return "Br"
    elif len(cp) == 7 and cp.isdigit():
        return "Ch"
    elif len(cp) == 6 and cp.isdigit():
        return "Par"
    elif len(cp) == 5 and cp.isdigit():
        return "Ur"
    else:
        return "otro"
def menor_br(cp, tipo, pago):

    if identidicar_pais(cp) == "Br" and (cp[0] == "9" or cp[0] == "8"):
        cp_menor = cp
        importe = int(importes_id(tipo) * 1.20)
        if pago == 1:
            return int(importe - importe * 0.1), cp_menor
        else:
            return importe, cp_menor
    elif identidicar_pais(cp) == "Br" and (cp[0] == "0") or (cp[0] == "1") or (cp[0] == "2") or (cp[0] == "3"):
        cp_menor = cp
        importe = int(importes_id(tipo) * 1.25)
        if pago == 1:
            return int(importe - importe * 0.1), cp_menor
        else:
            return importe, cp_menor
    elif identidicar_pais(cp) == "Br" and (cp[0] == "4") or (cp[0] == "5") or (cp[0] == "6") or (cp[0] == "7"):
        cp_menor = cp
        importe = int(importes_id(tipo) * 1.30)
        if pago == 1:
            return int(importe - importe * 0.1), cp_menor
        else:
            return importe, cp_menor
def importe_cp(cp, tipo, pago):

    if identidicar_pais(cp) == "Arg":
        monto = importes_id(tipo)
        if pago == 1:
            return int(monto * 0.90)
        else:
            return int(monto)
    elif identidicar_pais(cp) == "Bol" or identidicar_pais(cp) == "Par" or (
            (identidicar_pais(cp) == "Ur" and cp[
                0] == "1")) or (identidicar_pais(cp) == "Br" and (cp[0] == "9" or cp[0] == "8")):
        monto = int(importes_id(tipo) * 1.20)
        if pago == 1:
            return int(monto * 0.90)
        else:
            return int(monto)
    elif identidicar_pais(cp) == "Ch" or (identidicar_pais(cp) == "Ur" and cp[
        0] != 1) or ((identidicar_pais(cp) == "Br") and (
            (cp[0] == "0") or (cp[0] == "1") or (cp[0] == "2") or (cp[0] == "3"))):
        monto = int(importes_id(tipo) * 1.25)
        if pago == 1:
            return int(monto * 0.90)
        else:
            return int(monto)
    elif (identidicar_pais(cp) == "Br") and (
            (cp[0] == "4") or (cp[0] == "5") or (cp[0] == "6") or (cp[0] == "7")):
        monto = int(importes_id(tipo) * 1.30)
        if pago == 1:
            return int(monto * 0.90)
        else:
            return int(monto)
    elif identidicar_pais(cp) == "otro":
        monto = int(importes_id(tipo) * 1.50)
        if pago == 1:
            return int(monto * 0.90)
        else:
            return int(monto)
def envios_exterior(cp):
    if identidicar_pais(cp) != "Arg":
        return True
    else:
        return False
def envios_buenos_aires(cp):
    if identidicar_pais(cp) == "Arg" and cp[0] == "B" or cp[0] == "b":
        return True
    else:
        return False
def main():

    hc_no_validas = dir_validas = suma_importe = suma_exterior = suma_importe_bsas = envios = imp_acu_total = 0
    porc = prom = 0
    cart_simple = cart_certificadas = cart_expresas = cant_primer_cp = envios_bsas = 0
    tipo_mayor = primer_cp = menor = None

    m = open(NOMBRE_ARCHIVO,  "rt")
    lineas = m.readline()

    # PUNTO NUMERO UNO

    if "HC" in lineas:
        es_tipo = "Hard Control"
    else:
        es_tipo = "Soft Control"

    while True:
        envios += 1
        lineas = m.readline()
        if lineas == "":
            break

        #FORMATO DE LINEA
        cp = lineas[0:9].strip().upper()
        direccion = lineas[9:29].strip()
        tipo = int(lineas[29])
        pago = int(lineas[30])

        #PR 11 Y PR 12
        if identidicar_pais(cp) == 'Br':
            valor = menor_br(cp, tipo, pago)
            if menor is None:
                menor = valor
            elif menor > valor:
                menor = valor

        #CP Y VUELTAS
        if primer_cp is None:
            primer_cp = cp
        if primer_cp == cp:
            cant_primer_cp += 1
        cartas = tipos_id(tipo)

        #BLOQUE PARA MANEJAR HC
        if es_tipo == 'Hard Control':
            if hc_validacion(direccion):
                suma_importe += int(importe_cp(cp, tipo, pago))
                dir_validas += 1
                #CARTA MAS ENVIADA R8
                if cartas == 'Carta Simple':
                    cart_simple += 1
                elif cartas == 'Carta Certificada':
                    cart_certificadas += 1
                else:
                    cart_expresas += 1
                #R13 ENVIOS AL EXTERIOR
                if envios_exterior(cp):
                    suma_exterior += 1
                #R14 ENVIOS A BSAS
                if envios_buenos_aires(cp):
                    envios_bsas += 1
                    suma_importe_bsas += int(importe_cp(cp, tipo, pago))
            else:
                hc_no_validas += 1
        else:

            #BLOQUE MANEJO DE SC
            dir_validas += 1
            suma_importe += int(importe_cp(cp, tipo, pago))
            # R13 ENVIOS AL EXTERIOR
            if envios_exterior(cp):
                suma_exterior += 1
            # R14 ENVIOS A BSAS
            if envios_buenos_aires(cp):
                envios_bsas += 1
                suma_importe_bsas += int(importe_cp(cp, tipo, pago))
            #CARTA MAS ENVIADAS R8 SC
            if cartas == 'Carta Simple':
                cart_simple += 1
            elif cartas == 'Carta Certificada':
                cart_certificadas += 1
            else:
                cart_expresas += 1


        #r4
        imp_acu_total = int(suma_importe)
        tipo_mayor = mayor_cant(cart_simple, cart_certificadas, cart_expresas)

        #r13 (chequeo una posible division por 0)
        if envios == 0:
            porc = 0
        else:
            porc = int((suma_exterior * 100) / envios)

        # r14 (chequeo una posible division por 0)
        if envios_bsas == 0:
            prom = 0
        else:
            prom = int(suma_importe_bsas / envios_bsas)

    m.close()
    print(' (r1) - Tipo de control de direcciones:', es_tipo)
    print(' (r2) - Cantidad de envios con direccion valida:', dir_validas)
    print(' (r3) - Cantidad de envios con direccion no valida:', hc_no_validas)
    print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
    print(' (r5) - Cantidad de cartas simples:', cart_simple)
    print(' (r6) - Cantidad de cartas certificadas:', cart_certificadas)
    print(' (r7) - Cantidad de cartas expresas:', cart_expresas)
    print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
    print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
    print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
    print('(r11) - Importe menor pagado por envios a Brasil:', menor[0])
    print('(r12) - Codigo postal del envio a Brasil con importe menor:', menor[1])
    print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
    print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom)

main()
