import random
operaciones = int(input("Inserte Numero de operaciones: "))
correctas= 0
for _ in range (operaciones):
    x=random.randint(0,9)
    y=random.randint(0,9)
    w = ["+","*","-"]
    operador = random.choice(w)
    if operador == "+":
        z= x+y
        print(f"{x} + {y}= ")
    elif operador == "*":
        z= x*y
        print(f"{x} * {y}= ")
    elif operador == "-":
        z= x-y
        print(f"{x} - {y}= ")
    solución= int(input("Inserte Resultado:" ))
    if solución == z:
        print("Correcto")
        correctas += 1
    else:
        print ("Incorrecto")
print(f"Has tenido bien: {correctas}/{operaciones}")
