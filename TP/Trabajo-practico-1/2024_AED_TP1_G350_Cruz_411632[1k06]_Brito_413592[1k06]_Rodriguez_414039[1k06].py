cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))
precio = int
final = int
provincia = "No aplica"
#Identificacion del CP según el formato
if len(cp) == 8 and cp[0] != "O" and cp[0] != "I" and cp[0].isalpha() and cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[4].isdigit() and cp[5].isalpha() and cp[6].isalpha() and cp[7].isalpha():
    destino = "Argentina"
    if cp[0].upper() == "A":
        provincia = "Salta"
    elif cp[0].upper() == "B":
        provincia = "Provincia de Buenos Aires"
    elif cp[0].upper() == "C":
        provincia = "Ciudad Autónoma de Buenos Aires"
    elif cp[0].upper() == "D":
        provincia = "San Luis"
    elif cp[0].upper() == "E":
        provincia = "Entre Ríos"
    elif cp[0].upper() == "F":
        provincia = "La Rioja"
    elif cp[0].upper() == "G":
        provincia = "Santiago del Estero"
    elif cp[0].upper() == "H":
        provincia = "Chaco"
    elif cp[0].upper() == "J":
        provincia = "San Juan"
    elif cp[0].upper() == "K":
        provincia = "Catamarca"
    elif cp[0].upper() == "L":
        provincia = "La Pampa"
    elif cp[0].upper() == "M":
        provincia = "Mendoza"
    elif cp[0].upper() == "N":
        provincia = "Misiones"
    elif cp[0].upper() == "P":
        provincia = "Formosa"
    elif cp[0].upper() == "Q":
        provincia = "Neuquén"
    elif cp[0].upper() == "R":
        provincia = "Río Negro"
    elif cp[0].upper() == "S":
        provincia = "Santa Fe"
    elif cp[0].upper() == "T":
        provincia = "Tucumán"
    elif cp[0].upper() == "U":
        provincia = "Chubut"
    elif cp[0].upper() == "V":
        provincia = "Tierra del Fuego"
    elif cp[0].upper() == "W":
        provincia = "Corrientes"
    elif cp[0].upper() == "X":
        provincia = "Córdoba"
    elif cp[0].upper() == "Y":
        provincia = "Jujuy"
    elif cp[0].upper() == "Z":
        provincia = "Santa Cruz"
else:
    destino = "Otro"

if (len(cp) == 4 and cp.isdigit()):
    destino = "Bolivia"
elif (len(cp) == 9 and cp[5] == "-" and cp[0].isdigit() and cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[4].isdigit() and cp[6].isdigit() and cp[7].isdigit() and cp[8].isdigit() ):
    destino = "Brasil"
elif (len(cp) == 7 and cp.isdigit()):
    destino = "Chile"
elif (len(cp) == 6 and cp.isdigit()):
    destino = "Paraguay"
elif (len(cp) == 5 and cp.isdigit()):
    destino = "Uruguay"

#Tipo de envío segun la tabla 2
if tipo == 0:
    precio = 1100

elif tipo == 1:
    precio = 1800

elif tipo == 2:
    precio = 2450

elif tipo == 3:
    precio = 8300

elif tipo == 4:
    precio = 10900

elif tipo == 5:
    precio = 14300

elif tipo == 6:
    precio = 17900

#Ajuste de precios segun tabla 3
if ((destino == "Bolivia") or (destino == "Paraguay") or ((destino == "Uruguay") and (cp[0] == "1")) or ((destino == "Brasil") and ((cp[0] == "8") or (cp[0] == "9" )) ) ):
        precio *= 1.2

elif ((destino == "Chile") or ((destino == "Uruguay") and (cp[0] != "1")) or ((destino == "Brasil") and ((cp[0] == "0") or (cp[0] == "1") or (cp[0] == "2") or (cp[0] == "3" )) )):
        precio *= 1.25

elif ((destino == "Brasil") and ((cp[0] == "4") or (cp[0] == "5") or (cp[0] == "6") or (cp[0] == "7" )) ):
        precio *= 1.3

elif (destino == "Argentina"):
    inicial = precio
elif (destino == "Otro"):
    precio *= 1.5
inicial = precio
#Calculo de precio final según el tipo de pago
if pago == 1:
    final = precio * 0.9
else:
    final = precio

print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
inicial = int(inicial)
print("Importe inicial a pagar:", inicial)
final = int(final)
print("Importe final a pagar:", final)
