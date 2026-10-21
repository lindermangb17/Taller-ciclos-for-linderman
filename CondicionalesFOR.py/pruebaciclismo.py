"""

Caso. Se reciben los tiempos de N ciclistas, con 1 ≤ N ≤ 20, sobre una vuelta de 250 metros. Cada registro contiene identificador entero positivo único, minutos enteros no negativos,segundos entre 0 y 59 y centésimas entre 0 y 99. Cada tiempo total es positivo. Informe la velocidad media de cada ciclista en kilómetros por hora y el identificador del ganador. En empate de tiempo gana el primero recibido.

Fórmula o relación: Tiempo en segundos T = 60 * minutos + segundos + centésimas/100; velocidad = 900/T. Menor T determina el ganador.

"""

r=0
mins=0

N = int(input("Ingrese el N de ciclistas: "))

if 1 <= N <= 20:
    for r in range(1,N+1):
        id = int(input("identificador ciclista "))
        mins= int(input("minutos ciclista "+str(id)+str(": ")))
        segundos = int(input("segundos ciclista "+str(id)+str(": ")))
        centesimas = int(input("centesimas ciclista "+str(id)+str(": ")))
        if id > 0 and 
        


