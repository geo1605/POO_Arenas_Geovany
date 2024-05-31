tienda = dict(lavadora=340.5, microondas=100, foco=34, coso=300)
descuentos = dict()

for clave, valor in tienda.items():
    valor = float(valor)
    descuento = valor - (valor * 0.10) 
    descuentos[clave] = descuento  

print("Precios originales:", tienda)
print("Precios con descuento:", descuentos)
