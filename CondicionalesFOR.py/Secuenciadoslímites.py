"""

Una pantalla debe presentar todos los enteros comprendidos entre dos limites A y B,
ambos incluidos, empezando por A y terminando en B. Los limites son enteros entre -100 y
100. Si coinciden, presente ese unico valor.

"""
A = int(input("Ingrese el primer limite A: "))
B = int(input("Ingrese el segundo limite B: "))

if A < -100 or A > 100:
    print("numero A invalido")
elif B > 100 or B < -100:
    print("numero B invalido")
else:
    for valor in range(A,B+1,1):
        print(valor)