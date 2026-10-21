"""

Caso. Se conoce el primer término A, la diferencia D y la cantidad N de términos de una
progresión. A y D son enteros entre -100 y 100, y N está entre 0 y 1000. Determine la suma de
los N términos; si N es cero, el total es cero.
Fórmula o relación: t1 = A; tk+1 = tk + D; S = t1 + t2 + ... + tn.s

"""

A = int(input("Ingrese el termino A: "))
D = int(input("Ingrese la diferencia D: "))
N = int(input("Cantidad de terminos N: "))

if -100 <= A <= 100 and -100 <= D <= 100 and 0 <= N <= 1000:
    t = A
    suma = 0
    for K in range(N):
        suma = suma + t
        t = t + D
    print(suma)
else:
    print("Valores inválidos")