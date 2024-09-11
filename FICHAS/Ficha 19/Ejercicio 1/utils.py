import clases
def ordenar(v):
    for i in range(len(v)):
        for j in range(len(v)):
            if v[i].promedio < v[j].promedio:
                v[i], v[j] = v[j], v[i]

def datos(vec):
    for i in range(len(vec)):
        nombre = input('Ingrese el nombre del atleta ' + str(i + 1) + ': ')
        vec[i] = clases.Atletas(nombre)
def podio(v):
    for i in range(len(v)):
        print('El puesto' + str(i + 1) + ' es para: ' + str(v[i].nombre) + ' con promedio de ' + str(v[i].promedio))