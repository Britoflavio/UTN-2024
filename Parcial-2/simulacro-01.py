ARCHIVO_TXT = 'entrada.txt'

def es_impar(letra):
    if letra.isdigit():
        parse = int(letra)
        if parse % 2 != 0:
            return True
        else:
            return False

def mayus(letra):
    if letra.isupper():
        return True
    else:
        return False
def es_vocal(letra):
    vocales = 'aeiouáéíóú'
    return letra in vocales
def may_long(letra):
    may = None
    if may is None:
        may = letra
    elif may < letra:
        may = letra
    return may

def main():

    TEXTO = open(ARCHIVO_TXT)
    PALABRAS = TEXTO.read()

    palabra = letras = palabras_validas = r2 = 0
    esta_impar = empieza_vocal = tiene_b = False
    impar_en_palabra = 0

    for letra in PALABRAS:

        #Manejamos la parte donde finaliza la palabra, que deberia contar cuando aparezca el digito .  y espacio
        #Por ejemplo contar palabras, si algo esta en True al finalizar la palabra y debemos contar , etc
        if letra == '.' or letra == ' ':
            #Si la bandera llega en TRUE al final de la palabra contamos que es una palabra valida para el punto 1
            if esta_impar:
                palabras_validas += 1
            if letras > 0:
                palabra += 1
            if empieza_vocal and tiene_b:
                r2 = may_long(letras)

            esta_impar = empieza_vocal = tiene_b = False
            impar_en_palabra = letras = 0

        else:

            letras += 1

            if letras == 1 and es_vocal(letra.lower()):
                empieza_vocal = True
            else:
                if empieza_vocal and letra.lower() == 'b':
                    tiene_b = True

            #Si el digito es impar,pasamos la bandera a TRUE y contamos las veces que se encontro un numero impar
            if letras == 1 and es_impar(letra):
                impar_en_palabra += 1
                esta_impar = True
                #Si hay mas de 1 impar en la palabra activamos la bandera a FALSE, por motivo de doble numero
                if impar_en_palabra > 1:
                    esta_impar = False
            #Si encontramos una mayuscula y tambien tenemos un impar detectado, significa que no es valida la palabra
            if letra.isupper() or es_impar(letra) is False and impar_en_palabra == 1:
                esta_impar = False

    print('Palabras con este formato 1asys:', palabras_validas)
    print("Segundo resultado:", r2)
main()

'''

print("Primer resultado:", r1)
print("Segundo resultado:", r2)
print("Tercer resultado:", r3)
print("Cuarto resultado:", r4)

'''