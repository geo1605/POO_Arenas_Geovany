lista = [10,9,10,18,29,10,81,72,43,12,7,29,32,19,15]
infancia = []
adolescentes = []
jovenes = []
adultos = []
for i in lista:
    if i >= 6 and i<=11:
        infancia.append(i)
    elif i>=12 and i<=17:
        adolescentes.append(i)
    elif i>=18 and i<=26:
        jovenes.append(i)
    elif i>28:
        adultos.append(i)

print("infancia: ",infancia)
print("adolescentes: ",adolescentes)
print("jovenes: ",jovenes)
print("adultos: ",adultos)

