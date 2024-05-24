promedio1 = float(input("pon el promedio1: "))
promedio2 = float(input("pon el promedio2: "))
promedio3 = float(input("pon el promedio3: "))

if promedio1 > promedio2:
    if promedio1 > promedio3:
        print("promedio 1 es mayor")
    else:
        print("promedio 3 es mayor")
else:
    if promedio2 > promedio3:
        print("promedio 2 es mayor")
    else:
        print("promedio 3 es mayor")

