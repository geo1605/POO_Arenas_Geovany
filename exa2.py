import math
def cRect(a,b):
    r = a*b 
    return r
def cCuad(a):
    r = a*a
    return r
def cTri(a):
    r = (a*a)/2
    return r
i = 1
while i > 0:
    print("hola que quieres calcular?")
    print("1. triangulo")
    print("2. cuadrado")
    print("3. rectangulo")
    print("otro para salir")
    o = int(input("elije: "))
    if o == 1:
        r = float(input("coloca el lado:"))
        result = cTri(r)
        print(result)
    elif o == 2:
        r = float(input("coloca el lado:"))
        result = cCuad(r)
        print(result)
    elif o == 3:
        b = float(input("coloca base:"))
        a = float(input("coloca altura"))
        result = cRect(a,b)
        print(result)
    else:
        i = -1
