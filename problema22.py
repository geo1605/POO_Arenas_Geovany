def suma(a,b):
    c= a + b
    return c
def resta(a,b):
    c= a - b
    return c
def div(a,b):
    c= a / b
    return c
def mult(a,b):
    c= a * b
    return c

a = float(input("primer numero: "))
b = float(input("segundo numero: "))


print("1. suma")
print("2. resta")
print("3. divicion")
print("4. multiplicacion")
x = int(input("elije: "))

if x == 1:
    print(suma(a,b))
if x == 2:
    print(resta(a,b))
if x == 3:
    print(div(a,b))
if x == 4:
    print(mult(a,b))