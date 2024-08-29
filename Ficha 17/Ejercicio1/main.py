def datos(n):
    temp = n * [0]
    region = n * [0]
    dia = n * [0]
    for i in range(len(temp)):
        temp[i] = int(input('Ingrese temperatura registrada: '))
        region[i] = int(input('Ingrese la region, identificandolas de 1-20: '))
        dia[i] = int(input('Ingrese dia que la temperatura fue registrada: '))
    return temp, region, dia
def prom_temp(temp):
    cont_temp = 0
    n = len(temp)
    for i in range(n):
        cont_temp += temp[i]
    return cont_temp // n

def temperatura_region(dias, regiones, temp, region):
    for i in range(len(regiones)):
        if regiones[i] == region:
            print(dias[i], temp[i])

def order(temp, reg, dias):
    n = len(dias)
    for i in range(n-1):
        for j in range(i+1, n):
            if dias[i] > dias[j]:
                dias[i], dias[j] = dias[j], dias[i]
                reg[i], reg[j] = reg[j], reg[i]
                temp[i], temp[j] = temp[j], temp[i]



def main():
    temp = region = dia = None
    temp, region, dia = datos(5)
    pro = prom_temp(temp)
    order(temp, region, dia)
    x = int(input('Ingresar region del 1-20:'))
    temperatura_region(dia, region, temp, x)
    print(temp)


if __name__ == '__main__':
    main()