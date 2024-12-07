import random

# Generar 5 dígitos aleatorios y unirlos en un número de lotería
numero_lotería = "".join(str(random.randint(0, 9)) for _ in range(5))

print(f"El número de la lotería es: {numero_lotería}")
