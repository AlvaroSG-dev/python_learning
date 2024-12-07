Tamaño = ["PEQUEÑA", "MEDIANA", "GRANDE", "FAMILIAR"]
Grande = False
TamañoElegido=input("inserte el tamaño de la pizza (PEQUEÑA/MEDIANA/GRANDE/FAMILIAR)").upper().strip()
while TamañoElegido != "PEQUEÑA" and TamañoElegido != "MEDIANA" and TamañoElegido != "GRANDE" and TamañoElegido != "FAMILIAR":
    print("Error elije un tamaño que aparezca")
    TamañoElegido=input("inserte el tamaño de la pizza (PEQUEÑA/MEDIANA/GRANDE/FAMILIAR)").upper().strip()
if TamañoElegido != "PEQUEÑA" and TamañoElegido != "MEDIANA":
    Grande = True
Borde = False
queso = 0
Adicionales = input("¿Quiere añadirle extras? (s/n)").upper().strip()
while Adicionales != "S" and Adicionales !="N":
    print("Error elije si o no")
    Adicionales = input("¿Quiere añadirle extras? (s/n)").upper().strip()
if Adicionales == "S":
    queso = int(input("cuanto queso extra quiere añadirle costando 1.5 más: "))
    Borde = input("quiere relleno de borde (s/n) ").upper().strip()
    if Borde == "S":
        Borde = True
Descuento = False
Recogida = input("Quiere recogerlo en el local (s/n)").upper().strip()
while Recogida != "S" and Recogida != "N":
    print("Error elije si o no")
    Recogida = input("Quiere recogerlo en el local (s/n)").upper().strip()
if Recogida == "S":
    Descuento = True
PTamaño= 0
PrecioBase = 8
if Grande == True:
    PTamaño = 4
else:
    PTamaño = 0
if Borde == True:
    PAdicionales = 1.5 * queso + 2.5
else: 
    PAdicionales = 1.5 * queso
if Descuento == True:
    Recoger = 0.9
else:
    Recoger = 1
Total = (PrecioBase + PTamaño + PAdicionales)*Recoger
print(f"Desglose de su pedido: ")
print(f"Coste de la pizza: {PrecioBase}$")
print(f"Usted ha elegido el tamaño: {TamañoElegido} que le costará: {PTamaño}$")
print(f"Por los adicionales que ha elegido: queso({queso}) y si queria o no borde sería: {PAdicionales}$")
print(f"Que dependiendode si recogio o no en el local el precio sería de: {Total} $ ")