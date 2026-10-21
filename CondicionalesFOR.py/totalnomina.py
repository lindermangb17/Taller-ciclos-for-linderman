"""

Caso. Una empresa tiene N empleados, con 0 ≤ N ≤ 1000. Se recibe el sueldo no negativo de cada empleado y se desea el total de la nómina. Para una empresa sin empleados, el total es cero. Fórmula o relación: Nómina = sueldo1 + sueldo2 + ... + sueldon.

"""

N = int(input("Ingrese el N de empleados: "))

nomina = 0


if N < 0 or N > 1000:
    print("Cantidad de empleados invalida")

else:
    for i in range(1,N+1):
        sueldo= int(input("Ingrese el sueldo "+str(i)+str(": " )))
        nomina=nomina+sueldo

    print("Nomina: ", nomina)

