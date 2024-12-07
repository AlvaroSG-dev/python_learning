numero = input("Inserte un numero: ")
while int(numero)< 0:
    print("Error Inserte un numero positivo")
    numero = input("Inserte un numero: ")
pares = 0
impares = 0
for i in range (0, len(numero)):
    digito = int(numero[i])
    if digito % 2 == 0:
        pares += digito
    elif digito % 2 != 0:
        impares += digito

solucion= abs(pares - impares)
print(solucion)

