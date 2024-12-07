precio= int(input("Inserte precio: "))
descuento= int(input("Inserte Descuento: "))
if 1 > descuento:
    resultado= precio*(1-descuento)
else:
    resultado= precio*(1-(descuento/100))

print("El descuento es: ",resultado)