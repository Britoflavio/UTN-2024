import csv
import os

ARCHIVO_CSV = 'envios-tp4.csv'
ARCHIVO_BIN = 'envios-tp4.bin'


def csv_a_binario(archivo_bin, archivo_csv):
    if os.path.exists(ARCHIVO_BIN):
        sobre_escibir = input(f'El archivo  binario {ARCHIVO_BIN} ya  existe. Desea sobrescrbirlo? (SI/NO): ')
        if sobre_escibir.upper() != 'SI':
            print('Operacion cancelada')
            return
    bin_archivo = open(archivo_bin, 'wb')
    csv_archivo = open(archivo_csv,  encoding='utf-8')

    lector_csv = csv.reader(csv_archivo)

    encabezado = next(lector_csv)

    for fila in lector_csv:
        codigo_postal = int(fila[0])
        direccion_fisica = fila[1].encode('utf-8')  # Convertimos la cadena a bytes
        tipo_envio = fila[2].encode('utf-8')
        forma_pago = fila[3].encode('utf-8')
