peso = float(input("peso(kg): "))
altura = float(input("altura(m): "))

imc = round(peso / (altura**2),2)
print("tu imc es: ",imc)
