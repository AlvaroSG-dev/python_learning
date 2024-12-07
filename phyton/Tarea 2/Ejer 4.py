total= 0
contador=0
while total<10000:
    num= float(input("Inserte N:"))
    contador= contador+1
    total=total+num
media= total/contador
print("media: ", media)
print("Contador", contador)
print("Total", total)