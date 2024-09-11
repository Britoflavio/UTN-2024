import random
class Atletas:
    def __init__(this, nombre):
        this.nombre = nombre
        this.tiempo_nado = random.randint(10, 20)
        this.tiempo_ciclismo = random.randint(10, 40)
        this.tiempo_corriendo = random.randint(10, 25)
        this.promedio = round((this.tiempo_nado + this.tiempo_ciclismo + this.tiempo_corriendo) / 3, 2)
    def __str__(this):
        nombre = 'Nombre del Atleta: ' + this.nombre
        tiempo_n = ' Tiempo total de nado en minutos: ' + str(this.tiempo_nado)
        tiempo_c = ' Tiempo total de ciclismo en minutos: ' + str(this.tiempo_ciclismo)
        tiempo_co = ' Tiempo total corriendo en minutos: ' + str(this.tiempo_corriendo)
        prom = ' Tiempo promedio: ' + str(this.promedio)
        return nombre + tiempo_n + tiempo_c + tiempo_co + prom