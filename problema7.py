p = int(input("mete el peso: "))
if p<1:
    print("costo $50")
elif p>1 and p<5:
    print("costo $100")
elif p>5 and p<10:
    print("costo $200")
elif p>10:
    print("costo $500")