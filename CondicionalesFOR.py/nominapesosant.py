"""

Caso. Se reciben N empleados, con 1 ≤ N ≤ 40. Cada registro contiene, en este orden, identificador entero positivo único, edad entera no negativa en años y años enteros de antigüedad entre 1 y 50. El sueldo ficticio es la suma de una base de 100 unidades monetarias, el valor numérico de la edad y la suma de los enteros desde 1 hasta la antigüedad; toda esa suma se divide entre los años de antigüedad. La edad y la suma de años se consideran aportes numéricos en unidades monetarias dentro de este modelo ficticio. Informe el sueldo de cada empleado, el total de la nómina y los identificadores con mayor y menor sueldo. En empate conserve el primero recibido.

Fórmula o relación: Sueldo = (100 + edad + (1 + 2 + ... + antigüedad))/antigüedad.

"""

N = int(input("Ingrese el N de empleados: "))

if 1 <= N <= 40:
    nomina = 0

    for i in range(N):
        id = int(input("Identificador empleado: "))
        edad = int(input("Edad del empleado: "))
        antig = int(input("Años de antigüedad: "))

        if edad >= 0 and 1 <= antig <= 50:
            suma = (antig * (antig + 1)) / 2
            sueldo = (100 + edad + suma) / antig

            nomina = nomina + sueldo

            print("Empleado", id, ":", sueldo)

            if i == 0:
                mayor = sueldo
                menor = sueldo
                id_mayor = id
                id_menor = id

            elif sueldo > mayor:
                mayor = sueldo
                id_mayor = id

            if sueldo < menor:
                menor = sueldo
                id_menor = id

    print("Nómina:", nomina)
    print("Mayor: Empleado", id_mayor, ":", mayor)
    print("Menor: Empleado", id_menor, ":", menor)

else:
    print("Número de empleados no válido")
