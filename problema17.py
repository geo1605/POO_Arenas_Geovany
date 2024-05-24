
i= 0
while i <1 :
    print("elije: ")
    print("1.  Celsius a Fahrenheit")
    print("2.   Fahrenheit a Celsius")
    print("oprime un numero mayor para terminar")
    x = int(input())
    if x <= 2:
        if x == 1:
            c = float(input("Celsius: "))
            f = (c* 9/5)+32
            print("Fahrenheit: ",f)
        else:
            f = float(input("Fahrenheit: "))
            c = ((f) - 32) * 5/9
            print("Celsius: ",c)
    else:
        break


