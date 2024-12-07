N= int(input("Inserte N:"))
Contador= 0
Factorial= 1
while Contador < N :
    Factorial=Factorial*(N-Contador)
    Contador= Contador +1
print("Solución del Factorial: ",Factorial)