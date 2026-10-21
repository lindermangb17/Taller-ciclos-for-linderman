"""

Una pantalla debe presentar todos los enteros comprendidos entre dos limites A y B,
ambos incluidos, empezando por A y terminando en B. Los limites son enteros entre -100 y
100. Si coinciden, presente ese unico valor.

"""
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))

if -100> A or A >100 :
    print("Numero A invalido")

if -100> B or B >100:
    print("Numero B invalido")

else:
    if -100<= A <=100 and -100<= B<=100:
        for R in range(A,B+1): 
            print(R)
