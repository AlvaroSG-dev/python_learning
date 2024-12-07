import random


saldo = int(input("Inserte saldo inicial: "))
saldo_inicial = saldo
colores = {0: "verde"}
for i in range(1, 37):
    colores[i] = "negro" if i % 2 == 0 else "rojo" 

print("¡Bienvenido al juego de la ruleta!")
print(f"Tu saldo inicial es de {saldo}€.")

while saldo > 0:
    print(f"\nTu saldo actual es de {saldo}€.")
    try:
        apuesta = int(input("¿Cuánto deseas apostar? "))
        if apuesta > saldo or apuesta <= 0:
            print("Apuesta inválida. No puedes apostar más de tu saldo o un valor negativo.")
            continue
    except ValueError:
        print("Entrada no válida. Ingresa un número entero.")
        continue
    tipo_apuesta = input("¿Deseas apostar a un color (rojo, negro, verde) o a un número (0-36)? ").lower()
    if tipo_apuesta in ["rojo", "negro", "verde"]:
        eleccion = tipo_apuesta
    elif tipo_apuesta.isdigit() and 0 <= int(tipo_apuesta) <= 36:
        eleccion = int(tipo_apuesta)
    else:
        print("Apuesta no válida. Ingresa 'rojo', 'negro', 'verde' o un número entre 0 y 36.")
        continue
    numero = random.randint(0, 36)
    color_ganador = colores[numero]
    print(f"\nLa ruleta gira... ¡Ha salido el número {numero} ({color_ganador})!")
    if eleccion == numero:  
        saldo += apuesta * 35
        print(f"¡Felicidades! Has acertado el número exacto. Ganaste {apuesta * 35}€. Tu saldo ahora es de {saldo}€.")
    elif eleccion == color_ganador:  
        if color_ganador == "verde":
            saldo += apuesta * 14
            print(f"¡Acertaste al verde! Ganaste {apuesta * 14}€. Tu saldo ahora es de {saldo}€.")
        else:
            saldo += apuesta
            print(f"¡Felicidades! Has acertado el color. Ganaste {apuesta}€. Tu saldo ahora es de {saldo}€.")
    else:  
        saldo -= apuesta
        print(f"Lo siento, has perdido. Tu saldo ahora es de {saldo}€.")
    if saldo > 0:
        seguir = input("¿Deseas seguir jugando? (si/no): ").lower()
        if seguir != "si":
            saldo_final= saldo - saldo_inicial
            print("¡Gracias por jugar! Te retiras con un saldo de {}€.".format(saldo))
            if saldo_inicial> saldo:
                print("Tus perdidas fueron de {}€.".format(saldo_final))
            else:
                print("Tus ganancias fueron de {}€.".format(saldo_final))
            break
    else:
        print("Te has quedado sin saldo. Fin del juego.")
        break



