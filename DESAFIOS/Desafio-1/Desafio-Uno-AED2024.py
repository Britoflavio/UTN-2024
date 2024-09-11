# Primera parte

print('Calculo de horas, minutos y segundos totales desde el evento pasado')

cantidad_segundos = float(input("Ingrese segundos transcurridos desde el evento pasado:"))

hora = int(cantidad_segundos // 3600)
minutos = int((cantidad_segundos % 3600) // 60)
segundos = int((cantidad_segundos % 3600) % 60)

if hora >= 24:
    print('Excedido')
else:
    print('Tiempo transcurrido:', str(hora) + ":" + str(minutos) + ":" + str(segundos))

# Segunda parte

print('Calculo de segundos totales, teniendo en cuenta horas, minutos y segundos totales')

horas_ingresadas = int(input('Ingrese cantidad de hora:'))
minutos_ingresados = int(input('Ingrese cantidad de minutos:'))
segundos_ingresados = int(input('Ingrese cantidad de segundos:'))

segundos_totales = (horas_ingresadas * 3600) + (minutos_ingresados * 60) + segundos_ingresados

print('Total de segundos:', segundos_totales)
