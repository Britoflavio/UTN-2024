ARCHIVO_TXT = 'entrada.txt'

def digitos(letra):

    numeros = '01234569'
    return letra in numeros

def es_vocal(letra):

    vocales = 'aeiouáéíóúAEIOU'
    return letra in vocales

def promed(suma, total):
    if total == 0:
        promedio = 0
    else:
        promedio = round(suma / total, 2)
    return promedio

def main():

    texto = open(ARCHIVO_TXT)
    letras = texto.read()

    #VARIABLES
    cont_letras = cont_palabras = cont_vocales_palabra = palabras_validas = 0
    digito_palabra = cont_r = cont_e = existe_r_e = cantidad_suma = 0
    anterior = primera_vocal = None
    palabra_valida = hay_r = hay_e = False
    existe_fi = False
    r3 = r4 = 0

    for letra in letras:

        if letra == ' ' or letra == '.':

            #Contar  PALABRAS
            if cont_letras > 0:
                cont_palabras += 1

            #Verificamos la condicion del punto1, sea palabra con 2 vocales y 6 caracteres
            if palabra_valida and cont_letras == 6 and digito_palabra >= 1:
                palabras_validas += 1

            #Verificamos validacion del punto2, palabra que tenga R y 2>=E
            if hay_e and hay_r:
                cantidad_suma += cont_letras
                existe_r_e += 1
            #Valuamos si la palabra anterior es vocal, si lo es valuamos que sean ambas minuscula o mayuscula, y si son distintas sumamos 1
            if es_vocal(anterior):
                if primera_vocal.islower() and anterior.islower():
                    if primera_vocal != anterior:
                        r3 += 1
                else:
                    if primera_vocal.isupper() and anterior.isupper():
                        if primera_vocal != anterior:
                            r3 += 1

            #Reseteo de palabras para poder analizar una NUEVA PALABRA
            cont_letras = 0
            cont_vocales_palabra = 0
            cont_e = cont_r = 0
            palabra_valida = hay_r = hay_e = False
            existe_fi = False
            anterior = primera_vocal = ''

        else:
            #Contar letra por vuelta
            cont_letras += 1

            #R4
            #Detectamos que la variable anterior sea F y la nueva letra sea I, para formar FI
            if anterior == 'f' and letra == 'i':
                existe_fi = True

            #Si existe FI valuamos que tengamos una N o una T en el resto de la palabra
            if existe_fi:
                if letra == 'n' or letra == 't':
                    r4 += 1
            #R3
            #Si es vocal y se es la primera letra asignamos la letra a variable vocal
            if es_vocal(letra) and cont_letras < 2:
                primera_vocal = letra

            if existe_fi:
                print(letra)
                if letra == 'n' or letra == 't':
                    r4 += 1
            #R2
            #Verificar cuantas R o E tiene la palabra
            if letra.lower() == 'r':
                cont_r += 1
            if letra.lower() == 'e':
                cont_e += 1
            #Si la palabra tiene unicamente 1 r y 2 o mas e, bandera en truue
            if cont_r == 1:
                hay_r = True
            if cont_e >= 2:
                hay_e = True

            #R1
            #Contar cuantos digitos hay en la palabra
            if digitos(letra):
                digito_palabra += 1
            #Verificar vocales usando lower para identificarlas aunque sean mayuscula
            if es_vocal(letra.lower()):
                cont_vocales_palabra += 1
            #Si el contador dde vocales en palabra es menor a 3 entonces detectamos una palabra valida
            if cont_vocales_palabra < 3:
                palabra_valida = True
                
            #Guardamos la anterior letra
            anterior = letra
    r2 = promed(cantidad_suma, existe_r_e)

    print("Primer resultado:", palabras_validas)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


main()