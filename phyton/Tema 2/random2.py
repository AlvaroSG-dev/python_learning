import random

# Opciones del juego
opciones = ["piedra", "papel", "tijeras"]

# El usuario elige una opción
usuario = input("Elige piedra, papel o tijeras: ").lower()

# La computadora elige una opción al azar
computadora = random.choice(opciones)

print(f"La computadora eligió: {computadora}")

# Determinar el resultado
if usuario == computadora:
    print("¡Es un empate!")
elif (usuario == "piedra" and computadora == "tijeras") or \
     (usuario == "papel" and computadora == "piedra") or \
     (usuario == "tijeras" and computadora == "papel"):
    print("¡Ganaste!")
else:
    print("Perdiste.")
