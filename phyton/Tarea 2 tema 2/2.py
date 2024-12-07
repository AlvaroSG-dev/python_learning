import random
print("Tienes 15 rondas para este Reto")
Dificultad= input("Escoge  dificultad (Facil/Intermedio/Dificil/Extremo): ")
rondas_maximas = 15
array = []
if Dificultad == "Facil":
    tamaño_array= 5
    array.extend([False]*5)
elif Dificultad == "Intermedio":
    tamaño_array = 8
    array.extend([False]*8)
elif Dificultad == "Dificil":
    tamaño_array = 11
    array.extend([False]*11)
elif Dificultad == "Extremo":
    tamaño_array = 15
    array.extend([False]*15)
posicion_mosca = random.randint(0, tamaño_array - 1)
array[posicion_mosca]= True

rondas = 0
juego_terminado = False

print("¡Bienvenido al juego de cazar la mosca!")
print(f"Tienes un array de {tamaño_array} posiciones, desde 0 hasta {tamaño_array - 1}.")
print(f"Intenta atrapar la mosca antes de {rondas_maximas} rondas.")
while rondas < rondas_maximas and not juego_terminado:
    posicion_jugador = int(input(f"Ronda {rondas + 1}. Elige una posición (0 a {tamaño_array - 1}): "))

    if posicion_jugador < 0 or posicion_jugador >= tamaño_array:
        print(f"Posición no válida. Elige un número entre 0 y {tamaño_array - 1}.")
        continue
    rondas += 1

    if posicion_jugador == posicion_mosca:
        print(f"¡Enhorabuena! Has cazado la mosca en la posición {posicion_mosca} en {rondas} rondas.")
        juego_terminado = True
        print(array)
    elif abs(posicion_jugador - posicion_mosca) == 1:
        print("¡La mosca revolotea! Se mueve a otra posición aleatoria.")
        x= posicion_mosca
        array[x] = False
        while x==posicion_mosca:
            posicion_mosca = random.randint(0, tamaño_array - 1)
        array[posicion_mosca]= True
    else:
        print("La mosca sigue en su posición. Prueba de nuevo.")
if not juego_terminado:
    print(f"Se acabaron las rondas. No lograste cazar la mosca. Estaba en la posición {posicion_mosca}.")
    print(array)