import random
# Generar un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)
intento = None

print("¡Adivina el número entre 1 y 100!")

# Bucle para continuar hasta que el usuario adivine el número
while intento != numero_aleatorio:
    intento = int(input("Introduce tu intento: "))
    
    if intento < numero_aleatorio:
        print("El número es mayor.")
    elif intento > numero_aleatorio:
        print("El número es menor.")
    else:
        print("¡Felicidades! Has adivinado el número.")