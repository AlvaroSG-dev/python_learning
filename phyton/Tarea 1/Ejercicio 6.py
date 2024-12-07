X= int(input("Insrte Base: "))
Y = int(input("Inserte Exponente: "))
if X >= 0:
    Solucion = X**Y
    if Y>= 0:
        print("Solución: ", Solucion)
    else:
        print("Error Inserte Exponente Positivo")
else:
    print("Error Inserte base positiva")