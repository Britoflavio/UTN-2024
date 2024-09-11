def num_impar(num):
    if num % 2 != 0:
        numerito = 3 * num + 1
        return int(numerito)

def num_par(num):
    if num % 2 == 0:
        numer = num // 2
        return int(numer)
def prom(suma, cantidad):
    if cantidad == 0:
        promedio = 0
    else:
        promedio = suma / cantidad
    return promedio

def main():

    num = int(input('Ingrese numero entero positivo:'))
    numeros = [num]
    cant_num = 1
    long_orbita = 0

    while num != 1:
        cant_num += num
        if num_impar(numeros[-1]):
            resultado_del_impar = num_impar(num)
            numeros.append(resultado_del_impar)

        if num_par(num):

            resultado_del_par = num_par(num)
            numeros.append(resultado_del_par)

        long_orbita = len(numeros)
        promedio = prom(cant_num, long_orbita)
        mayor = max(numeros)
        num = numeros[-1]

    print('N =', numeros[0])
    print('Orbita de N = ', numeros)
    print('Longuitud de orbita:', long_orbita)
    print('Promedio de los valores de la orbita:', promedio)
    print('Mayor de los numeros de la orbita:', mayor)
main()