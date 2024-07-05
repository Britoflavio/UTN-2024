ARCHIVO_TXT = 'entrada.txt'
def es_vocal(letras):
    vocales = 'AEIOUaeiou'
    return letras in vocales
def prom(suma, total):
    if total == 0:
        promedio = 0
    else:
        promedio = int(suma / total)
    return promedio
def main():


    cont_letras = cont_vocales = cont_cons = r1 = digitos = tiene_s = palabra_valida_s = suma_s = r4 = 0
    r2 = None
    leer = open(ARCHIVO_TXT)
    texto = leer.read()
    digito = no_p = tiene_vocal_adelante = False
    tiene_ra = False
    anterior = ''

    for letras in texto:

        if letras == ' ' or letras == '.':
            #R1
            #DETECTAMOS QUE SEA PAR Y QUE LAS CONSONANTES SEAN IGUAL A LAS VOCALES
            if cont_letras > 0 and cont_letras % 2 == 0:
                if cont_vocales == cont_cons:
                    r1 += 1
            #R2
            #ACA REALIZAMOS QUE SEA DIGITO QUE NO CONTENGA P Y QUE AL MENOS TENGA 1 DIGITO
            if digito and not no_p and digitos >= 1:
                #CON ESTO DETERMINAMOS LA MAYOR LONGUITUUD DE LAS PALABRAS QUE CUMPLEN LA ANTERIOR CONDICION
                if r2 is None:
                    r2 = cont_letras
                elif r2 < cont_letras:
                    r2 = cont_letras
            #R4
            #SI TIENE RA Y TIENE VOCALES ADELANTE DE LA MITAD DE LA PALABRA SUMAMOS 1 A LAS VALIDAS
            if tiene_ra and tiene_vocal_adelante:
                r4 += 1
            #R3
            #DETECTAMOS EL PROMEDIO, TENEMOS QUE REALIZAR UNA SUMA DE TODAS LAS LETRAS QUE ENTRAN A LA CONDICION Y ADEMAS SUMAR 1 A LA PALABRAS VALIDAS
            if cont_letras > 2:
                if tiene_s >= 1:
                    suma_s += cont_letras
                    palabra_valida_s += 1

            #VARIABLES PARA RESETEAR SU ESTADO
            cont_letras = cont_vocales = cont_cons = tiene_s = 0
            no_p = digito = False
            tiene_vocal_adelante = tiene_ra = False
        else:
            cont_letras += 1
            #R4 BUSCAMOS QUE LA LETRA ANTERIOR SEA R Y LA ACTUAL SEA A
            if anterior.lower() == 'r' and letras.lower() == 'a':
                tiene_ra = True
            #R4 EN ESTE CONDICIONAL CONTAMOS QUE TENGA UNA VOCAL EN SUS PRIMEROS DOS CARACTERES
            if cont_letras <= 2:
                if es_vocal(letras):
                    tiene_vocal_adelante = True
            #R3 BUSCAMOS PALABRAS QUE CONTENGAN S PARA SUMARLA, DESPUES RESETEAMOS CUANDO TERMINA LA PALABRA
            if letras.lower() == 's':
                tiene_s += 1
            #R2 CONTAMOS LOS DIGITOS Y ACTIVAMOS LA BANDERA
            if letras.isdigit():
                digitos += 1
                digito = True
            #R2 ACA TAMBIEN DECTAMOS SI LA PALABRA TIENE P ENTONCES ACTIVAMOS BANDERA
            if letras.lower() == 'p':
                no_p = True
            #R1 CONTAMOS LA CANTIDAD DE VOCALES
            if es_vocal(letras):
                cont_vocales += 1
            else:
                cont_cons += 1
            #ASIGNAMOS VALOR PARA GUARDAR NUESTRA ANTERIOR LETRA
            anterior = letras
    #REALIZAMOS PROMEDIO UTILIZANDO LA FUNCION
    r3 = prom(suma_s, palabra_valida_s)
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)




if __name__ == '__main__':
    main()